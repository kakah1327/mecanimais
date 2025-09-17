# 🔧 Guia de Instalação e Configuração
## Braço Robótico LEGO EV3

---

## 📋 Índice
1. [Pré-requisitos](#pré-requisitos)
2. [Instalação do Software](#instalação-do-software)
3. [Configuração do Hardware](#configuração-do-hardware)
4. [Configuração do EV3](#configuração-do-ev3)
5. [Instalação do Projeto](#instalação-do-projeto)
6. [Verificação da Instalação](#verificação-da-instalação)
7. [Configurações Avançadas](#configurações-avançadas)
8. [Solução de Problemas de Instalação](#solução-de-problemas-de-instalação)

---

## 🔍 Pré-requisitos

### Sistema Operacional Suportado:
- ✅ **Windows 10/11** (recomendado)
- ✅ **macOS 10.14+**
- ✅ **Linux Ubuntu 18.04+**

### Hardware Necessário:
- 🤖 **LEGO Mindstorms EV3** (45544 ou 31313)
- 🔌 **Cabo USB** (incluído no kit EV3)
- 💾 **Cartão microSD** (8GB+, Classe 10)
- 💻 **Computador** com porta USB disponível

### Conhecimentos Básicos:
- Familiaridade com linha de comando
- Conceitos básicos de programação Python
- Experiência básica com LEGO Mindstorms

---

## 💻 Instalação do Software

### Passo 1: Instalar Python

#### Windows:
```bash
# Baixe Python 3.8+ de: https://www.python.org/downloads/
# Durante a instalação, marque "Add Python to PATH"

# Verifique a instalação
python --version
pip --version
```

#### macOS:
```bash
# Instalar via Homebrew (recomendado)
brew install python3

# Ou baixar de: https://www.python.org/downloads/

# Verifique a instalação
python3 --version
pip3 --version
```

#### Linux (Ubuntu/Debian):
```bash
# Atualizar repositórios
sudo apt update

# Instalar Python e pip
sudo apt install python3 python3-pip

# Verifique a instalação
python3 --version
pip3 --version
```

### Passo 2: Instalar Dependências Python

```bash
# Criar ambiente virtual (recomendado)
python -m venv ev3_env

# Ativar ambiente virtual
# Windows:
ev3_env\Scripts\activate
# macOS/Linux:
source ev3_env/bin/activate

# Instalar pybricks
pip install pybricks

# Instalar dependências adicionais
pip install pyusb
pip install bluetooth-python  # Para conexão Bluetooth (opcional)
```

### Passo 3: Instalar Visual Studio Code (Recomendado)

```bash
# Baixe de: https://code.visualstudio.com/

# Extensões recomendadas:
# - Python
# - LEGO Education EV3 MicroPython
# - Python Docstring Generator
```

---

## 🔧 Configuração do Hardware

### Montagem do Braço Robótico:

#### Componentes Necessários:
- **3x Motores Large EV3** (L-Motor)
- **1x Sensor de Toque EV3**
- **1x Sensor de Cor EV3**
- **Peças estruturais LEGO** (vigas, conectores, engrenagens)

#### Esquema de Montagem:

```
        [Garra]
           |
      [Motor C - Garra]
           |
        [Cotovelo]
           |
    [Motor B - Cotovelo]
           |
         [Base]
           |
     [Motor A - Base]
           |
      [EV3 Brick]
```

#### Conexões dos Cabos:

| Componente | Porta | Cabo |
|------------|-------|------|
| Motor da Base | A | Cabo do Motor |
| Motor do Cotovelo | B | Cabo do Motor |
| Motor da Garra | C | Cabo do Motor |
| Sensor de Toque | S1 | Cabo do Sensor |
| Sensor de Cor | S4 | Cabo do Sensor |

### Verificação da Montagem:

1. **Estabilidade**: Certifique-se de que a base está firme
2. **Movimento Livre**: Todos os motores devem girar livremente
3. **Cabos Seguros**: Todos os cabos devem estar bem conectados
4. **Alcance**: Verifique se o braço alcança todas as posições

---

## 🤖 Configuração do EV3

### Passo 1: Preparar o Cartão microSD

```bash
# Baixar imagem do EV3dev ou Pybricks
# EV3dev: https://www.ev3dev.org/downloads/
# Pybricks: https://pybricks.com/ev3-micropython/startinstall.html

# Gravar imagem no cartão SD usando:
# - Balena Etcher (recomendado)
# - Raspberry Pi Imager
# - dd (Linux/macOS)
```

#### Usando Balena Etcher:
1. Baixe e instale o Balena Etcher
2. Insira o cartão microSD no computador
3. Selecione a imagem baixada
4. Selecione o cartão SD
5. Clique em "Flash"

### Passo 2: Configurar o EV3

1. **Inserir cartão SD** no EV3
2. **Ligar o EV3** (pressione o botão central)
3. **Aguardar inicialização** (pode levar alguns minutos)
4. **Configurar rede** (se necessário)

### Passo 3: Conectar ao Computador

#### Conexão USB (Recomendada):
```bash
# Conecte o cabo USB entre EV3 e computador
# O EV3 deve aparecer como dispositivo de rede

# Windows: Verificar em "Dispositivos e Impressoras"
# macOS: Verificar em "Preferências do Sistema > Rede"
# Linux: Verificar com "lsusb"
```

#### Conexão Bluetooth (Alternativa):
```bash
# No EV3, vá para: Wireless and Networks > Bluetooth
# Ative o Bluetooth e torne o dispositivo visível
# No computador, pareie com o EV3
```

---

## 📁 Instalação do Projeto

### Passo 1: Baixar o Código

```bash
# Criar pasta do projeto
mkdir lego_ev3_arm
cd lego_ev3_arm

# Baixar arquivos do projeto
# (substitua pelos comandos específicos do seu repositório)
git clone [URL_DO_REPOSITORIO]
# ou
# Baixar e extrair arquivo ZIP
```

### Passo 2: Estrutura de Arquivos

```
lego_ev3_arm/
├── main.py              # Código principal
├── README.md            # Manual do usuário
├── INSTALACAO.md        # Este arquivo
├── TROUBLESHOOTING.md   # Solução de problemas
├── FAQ.md               # Perguntas frequentes
└── config/              # Configurações (opcional)
    ├── settings.py
    └── calibration.json
```

### Passo 3: Configurar Permissões (Linux/macOS)

```bash
# Dar permissão de execução
chmod +x main.py

# Adicionar usuário ao grupo dialout (Linux)
sudo usermod -a -G dialout $USER
# Fazer logout e login novamente
```

---

## ✅ Verificação da Instalação

### Teste 1: Verificar Python e Dependências

```bash
# Ativar ambiente virtual
source ev3_env/bin/activate  # Linux/macOS
# ou
ev3_env\Scripts\activate     # Windows

# Testar importações
python -c "import pybricks; print('Pybricks OK')"
python -c "from pybricks.ev3devices import Motor; print('EV3 Devices OK')"
```

### Teste 2: Verificar Conexão com EV3

```bash
# Testar conexão
python -c "
from pybricks.hubs import EV3Brick
ev3 = EV3Brick()
ev3.speaker.beep()
print('Conexão EV3 OK')
"
```

### Teste 3: Verificar Motores e Sensores

```bash
# Executar teste básico
python -c "
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port

# Testar motores
base_motor = Motor(Port.A)
elbow_motor = Motor(Port.B)
gripper_motor = Motor(Port.C)

# Testar sensores
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)

print('Hardware OK')
"
```

### Teste 4: Executar Programa Principal

```bash
# Executar o programa completo
python main.py

# Deve ouvir:
# - 3 bipes curtos (inicialização)
# - Movimentos do braço
# - 2 bipes longos (finalização)
```

---

## ⚙️ Configurações Avançadas

### Configuração de Rede (EV3dev)

```bash
# Conectar via SSH
ssh robot@ev3dev.local
# Senha padrão: maker

# Configurar WiFi
sudo connmanctl
> enable wifi
> scan wifi
> services
> connect wifi_[NETWORK_ID]
```

### Configuração de Desenvolvimento

#### VS Code com EV3:
1. Instalar extensão "LEGO Education EV3 MicroPython"
2. Conectar ao EV3 via USB
3. Abrir pasta do projeto
4. Configurar device EV3 na extensão

#### Configurações do Python:
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./ev3_env/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true
}
```

### Otimizações de Performance

```python
# config/settings.py
MOTOR_SETTINGS = {
    'max_speed': 720,      # graus/segundo
    'acceleration': 720,   # graus/segundo²
}

SAFETY_SETTINGS = {
    'duty_limit': 50,      # % da força máxima
    'timeout': 5000,       # ms para timeout
}

POSITIONS = {
    'LEFT': 160,
    'MIDDLE': 100,
    'RIGHT': 40,
}
```

---

## 🚨 Solução de Problemas de Instalação

### Problema: Python não encontrado

**Sintomas**: `'python' is not recognized as an internal or external command`

**Solução**:
```bash
# Windows: Reinstalar Python marcando "Add to PATH"
# Ou adicionar manualmente ao PATH:
# C:\Python39\
# C:\Python39\Scripts\

# Verificar:
python --version
```

### Problema: Pybricks não instala

**Sintomas**: `ERROR: Could not find a version that satisfies the requirement pybricks`

**Solução**:
```bash
# Atualizar pip
python -m pip install --upgrade pip

# Instalar pybricks
pip install pybricks

# Se persistir, usar:
pip install --upgrade --force-reinstall pybricks
```

### Problema: EV3 não conecta

**Sintomas**: `ConnectionError` ou `Device not found`

**Solução**:
```bash
# Verificar drivers USB
# Windows: Instalar drivers EV3 da LEGO
# Linux: Verificar permissões USB

# Testar conexão:
lsusb | grep LEGO  # Linux
# ou verificar Device Manager (Windows)

# Reiniciar EV3 e tentar novamente
```

### Problema: Motores não respondem

**Sintomas**: `OSError: [Errno 19] No such device`

**Solução**:
1. Verificar conexões dos cabos
2. Confirmar portas corretas (A, B, C)
3. Testar motores individualmente
4. Verificar se o firmware está atualizado

### Problema: Permissões no Linux

**Sintomas**: `Permission denied` ao acessar USB

**Solução**:
```bash
# Adicionar usuário ao grupo dialout
sudo usermod -a -G dialout $USER

# Criar regra udev para EV3
sudo nano /etc/udev/rules.d/99-ev3.rules

# Adicionar linha:
SUBSYSTEM=="usb", ATTRS{idVendor}=="0694", ATTRS{idProduct}=="0005", MODE="0666"

# Recarregar regras
sudo udevadm control --reload-rules
sudo udevadm trigger

# Fazer logout e login
```

---

## 📞 Suporte de Instalação

### Logs de Diagnóstico:

```bash
# Gerar relatório de sistema
python -c "
import sys
import platform
print(f'Python: {sys.version}')
print(f'Platform: {platform.platform()}')
print(f'Architecture: {platform.architecture()}')

try:
    import pybricks
    print(f'Pybricks: {pybricks.__version__}')
except ImportError:
    print('Pybricks: NOT INSTALLED')
"
```

### Recursos de Ajuda:
- 📖 [Documentação Pybricks](https://pybricks.com/ev3-micropython/)
- 🌐 [Fórum EV3dev](https://github.com/ev3dev/ev3dev/discussions)
- 💬 [Comunidade LEGO](https://www.eurobricks.com/forum/)
- 📧 **Suporte Técnico**: [seu-email@exemplo.com]

---

## ✅ Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] Pybricks instalado
- [ ] EV3 com firmware atualizado
- [ ] Hardware montado corretamente
- [ ] Cabos conectados nas portas certas
- [ ] Conexão USB/Bluetooth funcionando
- [ ] Código do projeto baixado
- [ ] Teste básico executado com sucesso
- [ ] Programa principal funcionando

---

*Instalação concluída com sucesso! Consulte o README.md para instruções de uso.*