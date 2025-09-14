# 🐍 Instalação e Execução - Python

## 📋 Pré-requisitos

- **Python**: Versão 3.8 ou superior
- **Sistema**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Memória**: Mínimo 4GB RAM recomendado
- **Espaço**: ~500MB para dependências

## 🚀 Instalação Rápida

### 1. Clone o Repositório
```bash
git clone https://github.com/MagnaSoluto/projeto-pokemon-elite-4-new-py.git
cd projeto-pokemon-elite-4-new-py
```

### 2. Crie Ambiente Virtual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

### 3. Instale Dependências
```bash
# Atualizar pip
pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt
```

### 4. Execute o Projeto
```bash
# Demonstração (recomendado para primeiro uso)
python3 main.py --mode demo

# Otimização (encontra o melhor sexteto - 93% vitórias!)
python3 main.py --mode optimize --generations 20 --population 30

# Análise de equipe (testa performance)
python3 main.py --mode analyze --simulations 50

# Simulação de batalhas (testa contra Elite Four)
python3 main.py --mode simulate --simulations 50
```

## 🔧 Modos de Execução

### 🎮 Demonstração
```bash
python main.py --mode demo
```
- Executa uma demonstração completa
- Mostra funcionalidades básicas
- Ideal para primeiro contato

### 🧬 Otimização
```bash
python3 main.py --mode optimize --generations 20 --population 30
```
- Encontra o melhor sexteto usando algoritmos genéticos
- **Resultado**: 93% de taxa de vitória contra Elite Four!
- `--generations`: Número de gerações (padrão: 20)
- `--population`: Tamanho da população (padrão: 30)

### 📊 Análise
```bash
python3 main.py --mode analyze --simulations 50
```
- Analisa performance de uma equipe
- **Resultado**: Taxa de vitória de 82.4% para equipe demo
- `--simulations`: Número de simulações (padrão: 50)

### ⚔️ Simulação
```bash
python3 main.py --mode simulate --simulations 50
```
- Simula batalhas contra Elite Four
- **Resultado**: Performance detalhada por membro
- `--simulations`: Número de simulações (padrão: 50)

## 📁 Estrutura de Saída

Após execução, os resultados são salvos em:

```
output/
├── best_team.txt              # Melhor equipe encontrada
├── team_performance.txt       # Performance da equipe
├── battle_analysis_*.csv      # Análises detalhadas
├── plots/                     # Gráficos e visualizações
├── models/                    # Modelos salvos
└── reports/                   # Relatórios gerados
```

## 🐛 Solução de Problemas

### Erro de Importação
```bash
# Se houver erro de módulos não encontrados
pip install -r requirements.txt --force-reinstall
```

### Erro de Permissão
```bash
# No macOS/Linux, se necessário
sudo pip install -r requirements.txt
```

### Ambiente Virtual
```bash
# Se o ambiente virtual não ativar
python3 -m venv venv --clear
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

### Dados Não Encontrados
```bash
# Verificar se os arquivos de dados existem
ls data/
# Deve conter: pokemon_data.csv e elite_four_data.csv
```

## 🚀 Execução Avançada

### Personalizar Configurações
```python
# Editar pokemon_elite_four/utils/config.py
# Para alterar parâmetros padrão
```

### Usar como Módulo
```python
from pokemon_elite_four import Pokemon, PokemonTeam, BattleSystem

# Criar Pokémon
charizard = Pokemon("Charizard", 6, PokemonType.FIRE, PokemonType.FLYING)

# Criar equipe
team = PokemonTeam([charizard, blastoise, venusaur])

# Sistema de batalhas
battle_system = BattleSystem()
```

## 📊 Exemplos de Uso

### Análise Rápida
```bash
python main.py --mode demo
```

### Otimização Completa
```bash
python main.py --mode optimize --generations 200 --population 100
```

### Análise Detalhada
```bash
python main.py --mode analyze --simulations 500
```

## 🔍 Verificação de Instalação

```bash
# Testar importação
python -c "import pokemon_elite_four; print('✅ Instalação OK')"

# Testar funcionalidades básicas
python -c "
from pokemon_elite_four import Pokemon, PokemonType
p = Pokemon('Pikachu', 25, PokemonType.ELECTRIC)
print(f'✅ {p.name} criado com sucesso!')
"
```

## 📞 Suporte

- **Issues**: [GitHub Issues](../../issues)
- **Documentação**: [README_PYTHON.md](README_PYTHON.md)
- **Código**: [pokemon_elite_four/](pokemon_elite_four/)

---

*Instalação testada em Python 3.8+ em Windows, macOS e Ubuntu*
