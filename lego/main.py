#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

# Inicializa o tijolo EV3
ev3 = EV3Brick()

# Configura o motor da garra
gripper_motor = Motor(Port.A)

# Configura o motor do cotovelo
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [7, 40])

# Configura o motor da base
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

# Limita aceleração
elbow_motor.control.limits(speed=100, acceleration=120)
base_motor.control.limits(speed=100, acceleration=120)

# Sensores
base_switch = TouchSensor(Port.S1)
elbow_sensor = ColorSensor(Port.S3)

# Inicializa o cotovelo
elbow_motor.run_time(-30, 1000)
elbow_motor.run(15)
while elbow_sensor.reflection() < 32:
    wait(10)
elbow_motor.reset_angle(0)
elbow_motor.hold()

# Inicializa a base
base_motor.run(-60)
while not base_switch.pressed():
    wait(10)
base_motor.reset_angle(0)
base_motor.hold()

# Inicializa a garra
gripper_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
gripper_motor.reset_angle(0)
gripper_motor.run_target(200, -90)

# Funções de pegar e soltar


def robot_pick(position):
    """
    Função para pegar um objeto em uma posição específica.
    
    PARÂMETROS:
    - position (int): Ângulo da posição onde o objeto está localizado
                     (valores típicos: LEFT=160, MIDDLE=100, RIGHT=40)
    
    SEQUÊNCIA DE OPERAÇÕES:
    1. Rotaciona a base para a posição especificada
    2. Abaixa o cotovelo para alcançar o objeto
    3. Fecha a garra para segurar o objeto
    4. Levanta o cotovelo para elevar o objeto
    
    RETORNO: Nenhum
    """
    # 1. Rotaciona a base para a posição de coleta
    # Velocidade: 60 graus/segundo para movimento preciso
    base_motor.run_target(60, position)
    
    # 2. Abaixa o cotovelo para -40 graus (posição de coleta)
    # Esta posição permite que a garra alcance objetos no chão
    elbow_motor.run_target(60, -40)
    
    # 3. Fecha a garra até travar, indicando que segurou o objeto
    # duty_limit=50 evita aplicar força excessiva
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    
    # 4. Levanta o cotovelo para a posição neutra (0 graus)
    # Isso eleva o objeto do chão para transporte seguro
    elbow_motor.run_target(60, 0)


def robot_release(position):
    """
    Função para soltar um objeto em uma posição específica.
    
    PARÂMETROS:
    - position (int): Ângulo da posição onde o objeto deve ser colocado
                     (valores típicos: LEFT=160, MIDDLE=100, RIGHT=40)
    
    SEQUÊNCIA DE OPERAÇÕES:
    1. Rotaciona a base para a posição especificada
    2. Abaixa o cotovelo para colocar o objeto no chão
    3. Abre a garra para soltar o objeto
    4. Levanta o cotovelo para a posição neutra
    
    RETORNO: Nenhum
    """
    # 1. Rotaciona a base para a posição de entrega
    # Velocidade: 60 graus/segundo para movimento preciso
    base_motor.run_target(60, position)
    
    # 2. Abaixa o cotovelo para -40 graus (posição de entrega)
    # Esta posição coloca o objeto suavemente no chão
    elbow_motor.run_target(60, -40)
    
    # 3. Abre a garra para -90 graus (posição totalmente aberta)
    # Isso libera o objeto completamente
    gripper_motor.run_target(200, -90)
    
    # 4. Levanta o cotovelo para a posição neutra (0 graus)
    # Prepara o braço para a próxima operação
    elbow_motor.run_target(60, 0)


# ============================================================================
# SEQUÊNCIA DE INICIALIZAÇÃO COMPLETA
# ============================================================================

# Emite 3 bipes curtos para indicar que a inicialização foi concluída
# e o robô está pronto para operar
for i in range(3):
    ev3.speaker.beep()    # Bipe padrão (frequência e duração automáticas)
    wait(100)             # Pausa de 100ms entre os bipes

# ============================================================================
# DEFINIÇÃO DAS POSIÇÕES DE TRABALHO
# ============================================================================

# Define as três posições de trabalho em graus de rotação da base
# Estes valores foram calibrados para o modelo específico do braço robótico
LEFT = 160      # Posição esquerda (160 graus da posição inicial)
MIDDLE = 100    # Posição central (100 graus da posição inicial)  
RIGHT = 40      # Posição direita (40 graus da posição inicial)

# ============================================================================
# CONFIGURAÇÃO DO PROGRAMA PRINCIPAL
# ============================================================================

# Define o número de ciclos que o robô executará
# Altere este valor para controlar quantas vezes o padrão será repetido
ciclos = 1

# ============================================================================
# PROGRAMA PRINCIPAL - SEQUÊNCIA DE MOVIMENTAÇÃO
# ============================================================================

# Executa o número especificado de ciclos
for i in range(ciclos):
    """
    PADRÃO DE MOVIMENTAÇÃO:
    Este padrão move objetos de forma sistemática entre as três posições,
    criando um efeito de "troca de lugares" entre os objetos.
    
    Estado inicial esperado: objetos nas posições LEFT e RIGHT
    Estado final: objetos trocaram de posição (LEFT ↔ RIGHT)
    """
    
    # MOVIMENTO 1: Esquerda → Meio
    # Move um objeto da posição esquerda para a posição central
    # Isso libera a posição esquerda para receber outro objeto
    robot_pick(LEFT)      # Pega o objeto na posição esquerda
    robot_release(MIDDLE) # Coloca o objeto na posição central

    # MOVIMENTO 2: Direita → Esquerda  
    # Move um objeto da posição direita para a posição esquerda
    # Agora a posição direita está livre
    robot_pick(RIGHT)     # Pega o objeto na posição direita
    robot_release(LEFT)   # Coloca o objeto na posição esquerda

    # MOVIMENTO 3: Meio → Direita
    # Move o objeto que estava temporariamente no meio para a direita
    # Completa a troca de posições entre os objetos originais
    robot_pick(MIDDLE)    # Pega o objeto na posição central
    robot_release(RIGHT)  # Coloca o objeto na posição direita

# ============================================================================
# FINALIZAÇÃO DO PROGRAMA
# ============================================================================

# Emite 2 bipes longos para indicar que todos os ciclos foram concluídos
# e o programa terminou com sucesso
for i in range(2):
    ev3.speaker.beep()    # Bipe de finalização
    wait(500)             # Pausa de 500ms entre os bipes (mais longa que a inicialização)
