# 🐍 Guia de Instalação - Pokémon Elite Four Python

Este guia fornece instruções detalhadas para instalar e configurar o sistema Pokémon Elite Four em Python.

## 📋 Pré-requisitos

### Sistema Operacional
- **Windows**: 10 ou superior
- **macOS**: 10.14 (Mojave) ou superior  
- **Linux**: Ubuntu 18.04+ ou distribuição equivalente

### Software Necessário
- **Python**: 3.8, 3.9, 3.10 ou 3.11
- **pip**: Gerenciador de pacotes Python (incluído com Python 3.4+)
- **Git**: Para clonar o repositório

### Verificar Instalações

```bash
# Verificar Python
python3 --version
# Deve retornar: Python 3.8.x ou superior

# Verificar pip
pip3 --version
# Deve retornar: pip 21.x.x ou superior

# Verificar Git
git --version
# Deve retornar: git version 2.x.x ou superior
```

## 🚀 Instalação Passo a Passo

### 1. Clonar o Repositório

```bash
# Clonar o repositório
git clone https://github.com/MagnaSoluto/projeto-pokemon-elite-4-new-py.git

# Navegar para o diretório
cd projeto-pokemon-elite-4-new-py
```

### 2. Criar Ambiente Virtual

**Recomendado**: Sempre use um ambiente virtual para isolar as dependências.

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate

# Verificar ativação (deve mostrar (venv) no prompt)
which python
# Deve retornar: .../projeto-pokemon-elite-4-new-py/venv/bin/python
```

### 3. Atualizar pip (Recomendado)

```bash
# Atualizar pip para versão mais recente
python -m pip install --upgrade pip
```

### 4. Instalar Dependências

```bash
# Instalar todas as dependências
pip install -r requirements.txt

# Verificar instalação
pip list
```

### 5. Verificar Instalação

```bash
# Testar importação das bibliotecas principais
python3 -c "
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from deap import base, creator, tools
import xgboost as xgb
print('✅ Todas as dependências instaladas com sucesso!')
"
```

## 🔧 Configuração Avançada

### Configuração de Desenvolvimento

Para desenvolvimento e contribuição:

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Instalar pre-commit hooks (opcional)
pre-commit install
```

### Configuração de Jupyter Notebook

Para usar o notebook das 41 perguntas:

```bash
# Instalar Jupyter
pip install jupyter notebook

# Iniciar Jupyter
jupyter notebook

# Ou usar JupyterLab
pip install jupyterlab
jupyter lab
```

### Configuração de IDE

#### Visual Studio Code
1. Instalar extensão Python
2. Selecionar interpretador: `./venv/bin/python`
3. Configurar linting com flake8

#### PyCharm
1. Abrir projeto
2. Configurar interpretador: `./venv/bin/python`
3. Ativar inspeção de código

## 🧪 Testes de Instalação

### Teste Básico

```bash
# Executar teste básico
python3 main.py --mode demo

# Saída esperada:
# 🎮 DEMONSTRAÇÃO
# ==============================
# [Resultados da demonstração...]
```

### Teste de Otimização

```bash
# Executar otimização rápida
python3 main.py --mode optimize --generations 10 --population 50

# Saída esperada:
# 🧬 OTIMIZAÇÃO DE EQUIPE
# ==============================
# [Resultados da otimização...]
```

### Teste de Análise

```bash
# Executar análise
python3 main.py --mode analyze --simulations 100

# Saída esperada:
# 📊 ANÁLISE DE EQUIPE
# ==============================
# [Resultados da análise...]
```

## 🐛 Solução de Problemas

### Problema: Python não encontrado

```bash
# Windows
py -3 --version

# macOS/Linux
python3 --version
# ou
python --version
```

**Solução**: Instalar Python 3.8+ do site oficial ou usar gerenciador de pacotes.

### Problema: pip não encontrado

```bash
# Instalar pip manualmente
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

### Problema: Erro de permissão

```bash
# Usar --user flag
pip install --user -r requirements.txt

# Ou usar ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Problema: Dependências conflitantes

```bash
# Limpar cache do pip
pip cache purge

# Reinstalar em ambiente limpo
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Problema: Erro de compilação (Windows)

```bash
# Instalar Visual Studio Build Tools
# Ou usar conda
conda create -n pokemon python=3.9
conda activate pokemon
pip install -r requirements.txt
```

## 📊 Verificação de Performance

### Teste de Performance Básico

```bash
# Executar benchmark
python3 -c "
import time
import sys
sys.path.append('.')

from pokemon_elite_four.core.pokemon import Pokemon, PokemonType, PokemonStats
from pokemon_elite_four.core.battle_system import BattleSystem

# Criar Pokémon de teste
charizard = Pokemon('Charizard', 6, PokemonType.FIRE, PokemonType.FLYING, 
                   PokemonStats(78, 84, 78, 109, 85, 100), 60)
blastoise = Pokemon('Blastoise', 9, PokemonType.WATER, None,
                   PokemonStats(79, 83, 100, 85, 105, 78), 60)

# Teste de batalha
battle_system = BattleSystem()
start_time = time.time()

for i in range(100):
    charizard.restore_full_health()
    blastoise.restore_full_health()
    battle_log = battle_system.battle_pokemon(charizard, blastoise)

end_time = time.time()
print(f'✅ 100 batalhas executadas em {end_time - start_time:.2f} segundos')
print(f'📊 Performance: {(end_time - start_time)/100*1000:.1f}ms por batalha')
"
```

### Teste de Memória

```bash
# Verificar uso de memória
python3 -c "
import psutil
import os
import sys
sys.path.append('.')

# Monitorar memória durante execução
process = psutil.Process(os.getpid())
memory_before = process.memory_info().rss / 1024 / 1024

# Executar otimização
from pokemon_elite_four.analysis.team_optimizer import TeamOptimizer
optimizer = TeamOptimizer()
best_team = optimizer.optimize_team(generations=5, population_size=20)

memory_after = process.memory_info().rss / 1024 / 1024
print(f'✅ Uso de memória: {memory_after - memory_before:.1f} MB')
print(f'📊 Memória total: {memory_after:.1f} MB')
"
```

## 🔄 Atualizações

### Atualizar Dependências

```bash
# Atualizar pip
python -m pip install --upgrade pip

# Atualizar dependências
pip install --upgrade -r requirements.txt
```

### Atualizar Código

```bash
# Atualizar repositório
git pull origin main

# Reinstalar dependências (se necessário)
pip install -r requirements.txt
```

## 📁 Estrutura de Arquivos Após Instalação

```
projeto-pokemon-elite-4-new-py/
├── 📁 venv/                        # Ambiente virtual Python
├── 📁 pokemon_elite_four/          # Código fonte
├── 📁 data/                        # Dados dos Pokémon
├── 📁 output/                      # Resultados (criado após execução)
├── 📁 docs/                        # Documentação
├── main.py                         # Script principal
├── requirements.txt                # Dependências
├── INSTALACAO_PYTHON.md           # Este arquivo
└── README.md                       # Documentação principal
```

## ✅ Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] Git instalado
- [ ] Repositório clonado
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas
- [ ] Teste básico executado com sucesso
- [ ] Teste de otimização executado
- [ ] Teste de análise executado
- [ ] Performance verificada

## 🆘 Suporte

Se encontrar problemas durante a instalação:

1. **Verificar logs**: Os logs são salvos em `output/pokemon_elite_four.log`
2. **Verificar versões**: `python3 --version` e `pip --version`
3. **Verificar ambiente**: `which python` deve apontar para venv
4. **Verificar dependências**: `pip list` deve mostrar todas as bibliotecas
5. **Abrir issue**: [GitHub Issues](https://github.com/MagnaSoluto/projeto-pokemon-elite-4-new-py/issues)

## 🎯 Próximos Passos

Após a instalação bem-sucedida:

1. **Ler README.md**: Entender o projeto
2. **Executar demonstração**: `python3 main.py --mode demo`
3. **Executar otimização**: `python3 main.py --mode optimize`
4. **Explorar resultados**: Verificar pasta `output/`
5. **Usar notebook**: Abrir `docs/CASE_TECNICO_41_PERGUNTAS_PYTHON.ipynb`

---

**Status da Instalação**: ✅ Pronto para uso | **Ambiente**: 🐍 Python 3.8+ | **Performance**: 🚀 Otimizada