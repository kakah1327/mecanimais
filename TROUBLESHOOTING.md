# 🔧 Guia de Solução de Problemas
## Braço Robótico LEGO EV3

---

## 📋 Índice
1. [Problemas de Conexão](#problemas-de-conexão)
2. [Problemas de Hardware](#problemas-de-hardware)
3. [Problemas de Software](#problemas-de-software)
4. [Problemas de Movimento](#problemas-de-movimento)
5. [Problemas de Calibração](#problemas-de-calibração)
6. [Problemas de Performance](#problemas-de-performance)
7. [Códigos de Erro](#códigos-de-erro)
8. [Diagnóstico Avançado](#diagnóstico-avançado)
9. [Manutenção Preventiva](#manutenção-preventiva)

---

## 🔌 Problemas de Conexão

### ❌ EV3 não conecta ao computador

**Sintomas:**
- Erro "Device not found"
- EV3 não aparece na lista de dispositivos
- Timeout de conexão

**Soluções:**

#### 1. Verificar Conexão USB
```bash
# Windows - Verificar Device Manager
# Procurar por "LEGO EV3" em "Portas (COM & LPT)"

# Linux - Verificar dispositivos USB
lsusb | grep LEGO

# macOS - Verificar System Information
system_profiler SPUSBDataType | grep -i lego
```

#### 2. Reinstalar Drivers
```bash
# Windows:
# 1. Baixar drivers EV3 do site da LEGO
# 2. Desinstalar driver atual no Device Manager
# 3. Reinstalar driver baixado

# Linux:
sudo apt install ev3dev-tools
```

#### 3. Testar Cabo USB
- Usar cabo USB original do EV3
- Testar com outro cabo USB conhecido
- Verificar se o cabo não está danificado

#### 4. Reiniciar Dispositivos
```bash
# Reiniciar EV3
# Pressionar e segurar botão BACK + CENTER + DOWN por 10s

# Reiniciar computador
# Especialmente importante no Windows
```

### ❌ Conexão Bluetooth instável

**Sintomas:**
- Desconexões frequentes
- Latência alta
- Comandos perdidos

**Soluções:**

#### 1. Verificar Distância
- Manter EV3 a menos de 10 metros do computador
- Remover obstáculos entre os dispositivos
- Evitar interferência de outros dispositivos Bluetooth

#### 2. Reconfigurar Pareamento
```bash
# No EV3:
# Settings > Bluetooth > Remove all devices
# Settings > Bluetooth > Make visible

# No computador:
# Remover EV3 da lista de dispositivos
# Parear novamente
```

#### 3. Usar Conexão USB
- Para operações críticas, preferir USB
- Bluetooth apenas para testes e desenvolvimento

---

## 🔧 Problemas de Hardware

### ❌ Motores não respondem

**Sintomas:**
- Motor não gira
- Erro "OSError: [Errno 19] No such device"
- Movimento irregular

**Diagnóstico:**
```python
# Teste individual de motores
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

try:
    motor_a = Motor(Port.A)
    motor_a.run_angle(100, 90)  # Girar 90 graus
    print("Motor A: OK")
except Exception as e:
    print(f"Motor A: ERRO - {e}")
```

**Soluções:**

#### 1. Verificar Conexões
- Cabos bem conectados nas portas corretas
- Verificar se cabos não estão danificados
- Limpar contatos das portas

#### 2. Testar Portas
```python
# Testar todas as portas
ports = [Port.A, Port.B, Port.C, Port.D]
for port in ports:
    try:
        motor = Motor(port)
        print(f"Porta {port}: Motor detectado")
    except:
        print(f"Porta {port}: Nenhum motor")
```

#### 3. Verificar Alimentação
- Bateria do EV3 carregada (>7V)
- LED do EV3 verde (não laranja/vermelho)
- Substituir baterias se necessário

### ❌ Sensores não funcionam

**Sintomas:**
- Valores incorretos dos sensores
- Sensor não detectado
- Leituras inconsistentes

**Diagnóstico:**
```python
# Teste de sensores
from pybricks.ev3devices import TouchSensor, ColorSensor
from pybricks.parameters import Port

# Sensor de toque
try:
    touch = TouchSensor(Port.S1)
    print(f"Touch Sensor: {touch.pressed()}")
except Exception as e:
    print(f"Touch Sensor ERRO: {e}")

# Sensor de cor
try:
    color = ColorSensor(Port.S4)
    print(f"Color Sensor: {color.color()}")
except Exception as e:
    print(f"Color Sensor ERRO: {e}")
```

**Soluções:**

#### 1. Limpeza dos Sensores
- Limpar lentes com pano seco
- Remover poeira dos contatos
- Verificar se não há obstruções

#### 2. Verificar Configuração
```python
# Configuração correta do sensor de cor
color_sensor = ColorSensor(Port.S4)
# Aguardar estabilização
wait(1000)
# Testar leitura
print(color_sensor.ambient())
```

---

## 💻 Problemas de Software

### ❌ Erro de importação do Pybricks

**Sintomas:**
```
ImportError: No module named 'pybricks'
ModuleNotFoundError: No module named 'pybricks.ev3devices'
```

**Soluções:**

#### 1. Verificar Instalação
```bash
# Verificar se pybricks está instalado
pip list | grep pybricks

# Reinstalar se necessário
pip uninstall pybricks
pip install pybricks
```

#### 2. Verificar Ambiente Virtual
```bash
# Ativar ambiente virtual correto
source ev3_env/bin/activate  # Linux/macOS
ev3_env\Scripts\activate     # Windows

# Verificar Python
which python
python --version
```

#### 3. Verificar Versão Python
```bash
# Pybricks requer Python 3.6+
python --version

# Se versão antiga, atualizar Python
```

### ❌ Programa trava ou não responde

**Sintomas:**
- Programa para de executar
- EV3 não responde
- Processo Python consome 100% CPU

**Soluções:**

#### 1. Adicionar Timeouts
```python
# Adicionar timeout em operações
motor.run_target(speed=100, target_angle=90, wait=True)
# Substituir por:
motor.run_target(speed=100, target_angle=90, wait=False)
wait(2000)  # Timeout de 2 segundos
motor.stop()
```

#### 2. Tratamento de Exceções
```python
try:
    robot_pick(LEFT)
except Exception as e:
    print(f"Erro em robot_pick: {e}")
    # Parar todos os motores
    base_motor.stop()
    elbow_motor.stop()
    gripper_motor.stop()
```

#### 3. Monitoramento de Recursos
```python
# Adicionar delays entre operações
def robot_pick(position):
    base_motor.run_target(60, position)
    wait(100)  # Pequena pausa
    elbow_motor.run_target(60, -40)
    wait(100)
    # ... resto da função
```

---

## 🤖 Problemas de Movimento

### ❌ Movimentos imprecisos

**Sintomas:**
- Robô não para na posição correta
- Deriva nas posições ao longo do tempo
- Movimentos inconsistentes

**Soluções:**

#### 1. Recalibrar Motores
```python
# Função de calibração manual
def calibrate_all_motors():
    print("Calibrando motores...")
    
    # Calibrar base
    base_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=50)
    base_motor.reset_angle(0)
    
    # Calibrar cotovelo
    elbow_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
    elbow_motor.reset_angle(0)
    
    # Calibrar garra
    gripper_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=50)
    gripper_motor.reset_angle(0)
    
    print("Calibração concluída!")
```

#### 2. Ajustar Configurações de Motor
```python
# Configurações mais precisas
base_motor.settings(max_speed=360, acceleration=180)
elbow_motor.settings(max_speed=360, acceleration=180)
gripper_motor.settings(max_speed=720, acceleration=360)
```

#### 3. Verificar Folgas Mecânicas
- Apertar todas as conexões LEGO
- Verificar se engrenagens não estão soltas
- Substituir peças desgastadas

### ❌ Garra não segura objetos

**Sintomas:**
- Objetos caem da garra
- Garra não fecha completamente
- Força insuficiente

**Soluções:**

#### 1. Ajustar Força da Garra
```python
# Aumentar duty_limit gradualmente
gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=70)
# Testar com valores: 50, 60, 70, 80 (máximo)
```

#### 2. Verificar Posição de Coleta
```python
# Ajustar altura do cotovelo
elbow_motor.run_target(60, -45)  # Mais baixo
# ou
elbow_motor.run_target(60, -35)  # Mais alto
```

#### 3. Modificar Sequência de Coleta
```python
def robot_pick_improved(position):
    base_motor.run_target(60, position)
    elbow_motor.run_target(60, -40)
    wait(500)  # Pausa para estabilizar
    
    # Abrir garra antes de fechar
    gripper_motor.run_target(200, -90)
    wait(200)
    
    # Fechar com mais força
    gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=75)
    wait(300)  # Aguardar firmar
    
    elbow_motor.run_target(60, 0)
```

---

## ⚖️ Problemas de Calibração

### ❌ Calibração falha

**Sintomas:**
- Motores não encontram posição inicial
- Erro "Stall detection failed"
- Posições inconsistentes após calibração

**Soluções:**

#### 1. Calibração Manual Passo a Passo
```python
def manual_calibration():
    print("Iniciando calibração manual...")
    
    # Calibrar base
    print("Calibrando base... Pressione ENTER quando estiver na posição inicial")
    input()
    base_motor.reset_angle(0)
    
    # Calibrar cotovelo
    print("Calibrando cotovelo... Mova para posição horizontal e pressione ENTER")
    input()
    elbow_motor.reset_angle(0)
    
    # Calibrar garra
    print("Calibrando garra... Abra completamente e pressione ENTER")
    input()
    gripper_motor.reset_angle(0)
    
    print("Calibração manual concluída!")
```

#### 2. Calibração com Sensores
```python
def sensor_calibration():
    # Usar sensor de toque para calibração
    while not touch_sensor.pressed():
        base_motor.run(-100)  # Mover até tocar
    base_motor.stop()
    base_motor.reset_angle(0)
```

#### 3. Verificar Obstruções
- Remover objetos que impedem movimento
- Verificar se estrutura não está travada
- Lubrificar engrenagens se necessário

---

## ⚡ Problemas de Performance

### ❌ Movimentos muito lentos

**Sintomas:**
- Operação demora muito para completar
- Movimentos em câmera lenta
- Timeout em operações

**Soluções:**

#### 1. Aumentar Velocidades
```python
# Velocidades otimizadas
base_motor.run_target(120, position)    # Era 60
elbow_motor.run_target(120, -40)        # Era 60
gripper_motor.run_target(400, -90)      # Era 200
```

#### 2. Configurações de Aceleração
```python
# Aumentar aceleração
base_motor.settings(max_speed=720, acceleration=1440)
elbow_motor.settings(max_speed=720, acceleration=1440)
gripper_motor.settings(max_speed=720, acceleration=1440)
```

#### 3. Otimizar Sequências
```python
# Executar movimentos em paralelo quando possível
def robot_pick_fast(position):
    # Iniciar movimento da base
    base_motor.run_target(120, position, wait=False)
    
    # Enquanto base move, preparar garra
    gripper_motor.run_target(400, -90, wait=False)
    
    # Aguardar base terminar
    while base_motor.control.done() == False:
        wait(10)
    
    # Continuar sequência...
```

### ❌ Bateria descarrega rapidamente

**Sintomas:**
- LED laranja/vermelho frequente
- Desligamento inesperado
- Performance degradada

**Soluções:**

#### 1. Otimizar Uso de Energia
```python
# Usar Stop.COAST em vez de Stop.HOLD quando possível
motor.run_target(100, 90, then=Stop.COAST)

# Desligar motores quando não em uso
motor.stop()
```

#### 2. Verificar Bateria
- Usar baterias recarregáveis de qualidade
- Verificar voltagem (deve ser >7V)
- Substituir baterias antigas

#### 3. Reduzir Força Desnecessária
```python
# Reduzir duty_limit quando possível
gripper_motor.run_until_stalled(200, duty_limit=40)  # Era 50
```

---

## 🚨 Códigos de Erro

### Erros Comuns e Soluções:

#### `OSError: [Errno 19] No such device`
**Causa:** Motor ou sensor não conectado na porta especificada
**Solução:** Verificar conexões e portas

#### `OSError: [Errno 5] Input/output error`
**Causa:** Problema de comunicação com EV3
**Solução:** Reiniciar EV3 e reconectar

#### `RuntimeError: The motor stopped because it was stalled`
**Causa:** Motor travou durante movimento
**Solução:** Verificar obstruções mecânicas

#### `ValueError: speed must be between -1000 and 1000`
**Causa:** Velocidade fora do range permitido
**Solução:** Ajustar valores de velocidade

#### `ConnectionError: Could not connect to EV3`
**Causa:** EV3 não encontrado ou não conectado
**Solução:** Verificar conexão USB/Bluetooth

---

## 🔍 Diagnóstico Avançado

### Script de Diagnóstico Completo:

```python
#!/usr/bin/env python3
"""
Script de diagnóstico completo para braço robótico EV3
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port
import sys

def diagnostic_test():
    print("=== DIAGNÓSTICO DO SISTEMA EV3 ===\n")
    
    # Teste 1: Conexão EV3
    try:
        ev3 = EV3Brick()
        ev3.speaker.beep()
        print("✅ EV3 Brick: Conectado")
    except Exception as e:
        print(f"❌ EV3 Brick: ERRO - {e}")
        return
    
    # Teste 2: Motores
    motors = {'A': Port.A, 'B': Port.B, 'C': Port.C}
    for name, port in motors.items():
        try:
            motor = Motor(port)
            motor.run_angle(100, 45)
            motor.run_angle(100, -45)
            print(f"✅ Motor {name}: OK")
        except Exception as e:
            print(f"❌ Motor {name}: ERRO - {e}")
    
    # Teste 3: Sensores
    try:
        touch = TouchSensor(Port.S1)
        print(f"✅ Touch Sensor: {touch.pressed()}")
    except Exception as e:
        print(f"❌ Touch Sensor: ERRO - {e}")
    
    try:
        color = ColorSensor(Port.S4)
        print(f"✅ Color Sensor: {color.color()}")
    except Exception as e:
        print(f"❌ Color Sensor: ERRO - {e}")
    
    # Teste 4: Bateria
    try:
        voltage = ev3.battery.voltage()
        if voltage > 7000:
            print(f"✅ Bateria: {voltage/1000:.1f}V (OK)")
        else:
            print(f"⚠️ Bateria: {voltage/1000:.1f}V (BAIXA)")
    except Exception as e:
        print(f"❌ Bateria: ERRO - {e}")
    
    print("\n=== DIAGNÓSTICO CONCLUÍDO ===")

if __name__ == "__main__":
    diagnostic_test()
```

### Logs de Sistema:

```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ev3_debug.log'),
        logging.StreamHandler()
    ]
)

def robot_pick_with_logging(position):
    logging.info(f"Iniciando robot_pick para posição {position}")
    try:
        base_motor.run_target(60, position)
        logging.debug("Base movida com sucesso")
        
        elbow_motor.run_target(60, -40)
        logging.debug("Cotovelo abaixado")
        
        gripper_motor.run_until_stalled(200, then=Stop.HOLD, duty_limit=50)
        logging.debug("Garra fechada")
        
        elbow_motor.run_target(60, 0)
        logging.debug("Cotovelo levantado")
        
        logging.info("robot_pick concluído com sucesso")
    except Exception as e:
        logging.error(f"Erro em robot_pick: {e}")
        raise
```

---

## 🛠️ Manutenção Preventiva

### Checklist Diário:
- [ ] Verificar nível da bateria
- [ ] Limpar sensores
- [ ] Verificar conexões dos cabos
- [ ] Testar movimentos básicos

### Checklist Semanal:
- [ ] Calibrar todos os motores
- [ ] Verificar folgas mecânicas
- [ ] Limpar contatos elétricos
- [ ] Executar diagnóstico completo

### Checklist Mensal:
- [ ] Atualizar firmware se disponível
- [ ] Verificar desgaste das peças
- [ ] Backup das configurações
- [ ] Revisar e otimizar código

---

## 📞 Suporte Técnico

### Quando Contactar Suporte:
- Problemas persistem após seguir este guia
- Erros de hardware não resolvidos
- Necessidade de peças de reposição
- Dúvidas sobre modificações avançadas

### Informações para Suporte:
```bash
# Executar antes de contactar suporte
python diagnostic_test.py > diagnostic_report.txt
```

### Contatos:
- **Email**: suporte@exemplo.com
- **Fórum**: [Link do fórum]
- **Documentação**: README.md, FAQ.md

---

*Este guia cobre os problemas mais comuns. Para situações específicas, consulte a documentação adicional ou entre em contato com o suporte técnico.*