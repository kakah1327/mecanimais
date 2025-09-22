# Mecanimais - Braço Robótico LEGO EV3

## 👥 Equipe de Desenvolvimento

**Alunos:**
- **Kauã Ribeiro Santos** - RA 2301838
- **Guilherme Nunes Joanna** - RA 2300794  
- **Lucas Fernandes de Melo** - RA 2301264
- **Cintia Marques Castanho Sae** - RA 2300255

---

## 📋 Índice
1. [Visão Geral](#visão-geral)
2. [Funcionalidades Principais](#funcionalidades-principais)
3. [Requisitos do Sistema](#requisitos-do-sistema)
4. [Hardware Necessário](#hardware-necessário)
5. [Instalação e Configuração](#instalação-e-configuração)
6. [Como Usar](#como-usar)
7. [Configurações Avançadas](#configurações-avançadas)
8. [Manutenção](#manutenção)
9. [Solução de Problemas](#solução-de-problemas)
10. [Suporte](#suporte)

## 🤖 Visão Geral

O **Mecanimais** é um projeto de braço robótico automatizado desenvolvido usando o kit LEGO Mindstorms EV3. O robô é capaz de pegar e mover objetos entre três posições predefinidas (esquerda, centro e direita) de forma autônoma e precisa.

### Características Principais:
- **Movimentação precisa**: Sistema de 3 graus de liberdade (base, cotovelo, garra)
- **Operação autônoma**: Executa sequências programadas sem intervenção
- **Calibração automática**: Auto-calibra todos os motores na inicialização
- **Feedback sensorial**: Utiliza sensores de toque e cor para operação segura
- **Interface amigável**: Sinais sonoros indicam status de operação

## ⚙️ Funcionalidades Principais

### 1. **Movimentação de Objetos**
- Pega objetos em posições específicas
- Move objetos entre três posições predefinidas
- Executa padrão de troca sistemática entre posições

### 2. **Calibração Automática**
- Calibra automaticamente todos os motores na inicialização
- Define posições de referência para operação precisa
- Configura limites de velocidade e aceleração

### 3. **Controle de Segurança**
- Limita força aplicada pela garra (duty_limit=50)
- Velocidades controladas para movimentos suaves
- Sequência de inicialização padronizada

### 4. **Feedback do Sistema**
- Bipes de inicialização (3 bipes curtos)
- Bipes de finalização (2 bipes longos)
- Indicação sonora de status de operação

## 💻 Requisitos do Sistema

### Software:
- **Python 3.x** (versão 3.6 ou superior)
- **Biblioteca pybricks** (para controle do EV3)
- **Sistema operacional**: Windows, macOS ou Linux
- **IDE recomendado**: Visual Studio Code com extensão LEGO Education

### Conexão:
- Cabo USB ou conexão Bluetooth com o EV3
- Cartão microSD (se usando micropython no EV3)

## 🔧 Hardware Necessário

### Componentes LEGO EV3:
1. **EV3 Brick** (unidade de controle principal)
2. **3 Motores Large** (para base, cotovelo e garra)
3. **1 Sensor de Toque** (para calibração)
4. **1 Sensor de Cor** (para detecção de objetos)
5. **Peças estruturais** para montagem do braço

### Configuração de Portas:
- **Motor da Base**: Porta A
- **Motor do Cotovelo**: Porta B  
- **Motor da Garra**: Porta C
- **Sensor de Toque**: Porta S1
- **Sensor de Cor**: Porta S4

## 🚀 Instalação e Configuração

### Passo 1: Preparação do Ambiente
```bash
# Instalar Python (se não estiver instalado)
# Baixar de: https://www.python.org/downloads/

# Instalar pybricks
pip install pybricks
```

### Passo 2: Configuração do EV3
1. Conecte o EV3 ao computador via USB
2. Certifique-se de que o firmware pybricks está instalado no EV3
3. Verifique se todos os motores e sensores estão conectados corretamente

### Passo 3: Download do Código
1. Baixe o arquivo `main.py` para seu computador
2. Coloque o arquivo na pasta do projeto EV3

### Passo 4: Montagem do Hardware
1. Monte o braço robótico seguindo as especificações
2. Conecte os motores e sensores nas portas corretas
3. Verifique se a estrutura está estável e segura

## 📖 Como Usar

### Uso Básico:

1. **Preparação**:
   - Ligue o EV3 Brick
   - Conecte ao computador
   - Coloque objetos nas posições LEFT e RIGHT

2. **Execução**:
   ```bash
   # Navegue até a pasta do projeto
   cd caminho/para/o/projeto
   
   # Execute o programa
   python main.py
   ```

3. **Operação**:
   - O robô emitirá 3 bipes curtos (inicialização)
   - Executará a sequência de movimentação
   - Emitirá 2 bipes longos (finalização)

### Sequência de Operação:
1. **Inicialização**: Calibração automática de todos os motores
2. **Movimento 1**: Objeto da esquerda → centro
3. **Movimento 2**: Objeto da direita → esquerda  
4. **Movimento 3**: Objeto do centro → direita
5. **Finalização**: Sinalização sonora de conclusão

### Posições de Trabalho:
- **LEFT (Esquerda)**: 160° da posição inicial
- **MIDDLE (Centro)**: 100° da posição inicial
- **RIGHT (Direita)**: 40° da posição inicial

## ⚙️ Configurações Avançadas

### Alterando o Número de Ciclos:
```python
# No arquivo main.py, linha ~140
ciclos = 1  # Altere este valor para mais repetições
```

### Ajustando Velocidades:
```python
# Velocidade dos motores (graus/segundo)
base_motor.run_target(60, position)    # 60°/s para base
elbow_motor.run_target(60, -40)        # 60°/s para cotovelo
gripper_motor.run_target(200, -90)     # 200°/s para garra
```

### Modificando Posições:
```python
# Ajuste as posições conforme necessário
LEFT = 160    # Posição esquerda
MIDDLE = 100  # Posição central
RIGHT = 40    # Posição direita
```

### Configurações de Segurança:
```python
# Limite de força da garra (0-100)
duty_limit=50  # 50% da força máxima

# Configurações de aceleração
base_motor.settings(max_speed=720, acceleration=720)
elbow_motor.settings(max_speed=720, acceleration=720)
gripper_motor.settings(max_speed=720, acceleration=720)
```

## 🔧 Manutenção

### Manutenção Regular:
- **Verificar conexões**: Certifique-se de que todos os cabos estão bem conectados
- **Limpeza**: Mantenha os sensores limpos e livres de poeira
- **Lubrificação**: Verifique se as engrenagens estão funcionando suavemente
- **Calibração**: Execute a calibração regularmente para manter a precisão

### Verificações de Segurança:
- Inspecione a estrutura antes de cada uso
- Verifique se não há objetos obstruindo o movimento
- Certifique-se de que a área de trabalho está livre
- Monitore a operação durante a execução

### Cuidados com a Bateria:
- Mantenha a bateria do EV3 carregada
- Desligue o EV3 quando não estiver em uso
- Substitua baterias fracas imediatamente

## 🆘 Solução de Problemas

### Problemas Comuns:

**1. Robô não responde**
- Verifique se o EV3 está ligado
- Confirme a conexão USB/Bluetooth
- Reinicie o EV3 se necessário

**2. Movimentos imprecisos**
- Execute a calibração novamente
- Verifique se não há obstruções mecânicas
- Ajuste as configurações de velocidade

**3. Garra não segura objetos**
- Verifique o limite de força (duty_limit)
- Confirme se o motor da garra está funcionando
- Ajuste a posição de coleta (-40°)

**4. Erro de conexão**
- Reinstale os drivers do EV3
- Verifique o cabo USB
- Tente conexão Bluetooth alternativa

### Códigos de Erro:
- **Bipes contínuos**: Erro de calibração
- **Sem resposta**: Problema de conexão
- **Movimentos erráticos**: Interferência ou obstrução

## 📞 Suporte

### Documentação Adicional:
- `INSTALACAO.md` - Instruções detalhadas de instalação
- `TROUBLESHOOTING.md` - Guia completo de solução de problemas

### Recursos Online:
- [Documentação Pybricks](https://pybricks.com/ev3-micropython/)
- [LEGO Education](https://education.lego.com/en-us/support)
- [Comunidade EV3](https://www.eurobricks.com/forum/index.php?/forums/forum/212-mindstorms/)

### Contato:
- **Projeto**: Mecanimais
- **Equipe**: Kauã Ribeiro Santos, Guilherme Nunes Joanna, Lucas Fernandes de Melo, Cintia Marques Castanho Sae
- **Data**: Setembro 2025

---

