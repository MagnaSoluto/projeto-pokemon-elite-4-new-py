# 🏗️ Estrutura do Projeto - Pokémon Elite Four

## 📋 Visão Geral

Este documento apresenta a estrutura completa do projeto Pokémon Elite Four, detalhando a organização de arquivos, módulos, classes e suas responsabilidades. A arquitetura segue princípios de **modularidade**, **extensibilidade** e **manutenibilidade**.

## 🎯 Princípios Arquiteturais

### 1. **Separação de Responsabilidades**
- **Core**: Lógica fundamental do sistema
- **Analysis**: Algoritmos de otimização e análise
- **Utils**: Utilitários e funções auxiliares
- **Data**: Dados e configurações

### 2. **Modularidade**
- **Módulos Independentes**: Baixo acoplamento
- **Interfaces Claras**: Alto coesão
- **Reutilização**: Código compartilhado
- **Testabilidade**: Módulos isolados

### 3. **Extensibilidade**
- **Design Patterns**: Padrões de projeto
- **Interfaces Abstratas**: Contratos claros
- **Plugin Architecture**: Extensões futuras
- **Configuration-Driven**: Configuração externa

## 📁 Estrutura de Diretórios

```
projeto-pokemon-elite-4-new-py/
├── 📁 pokemon_elite_four/          # Pacote principal
│   ├── __init__.py                 # Inicialização do pacote
│   ├── 📁 core/                    # Módulo core (classes fundamentais)
│   │   ├── __init__.py
│   │   ├── pokemon.py              # Classes Pokémon e equipe
│   │   ├── battle_system.py        # Sistema de batalhas
│   │   ├── moves.py                # Movimentos e movesets
│   │   └── config.py               # Configurações do sistema
│   ├── 📁 analysis/                # Módulo de análise
│   │   ├── __init__.py
│   │   ├── team_optimizer.py       # Algoritmo genético
│   │   ├── battle_analyzer.py      # Análise de batalhas
│   │   └── data_processor.py       # Processamento de dados
│   ├── 📁 utils/                   # Módulo de utilitários
│   │   ├── __init__.py
│   │   ├── functions.py            # Funções auxiliares
│   │   ├── install_packages.py     # Instalação de dependências
│   │   └── logging_config.py       # Configuração de logging
│   └── 📁 visualization/           # Módulo de visualização
│       ├── __init__.py
│       ├── plots.py                # Geração de gráficos
│       └── reports.py              # Geração de relatórios
├── 📁 data/                        # Dados do projeto
│   ├── pokemon_data.csv            # Dataset principal de Pokémon
│   ├── elite_four_data.csv         # Dados da Elite dos 4
│   ├── pokemon_moves.csv           # Movimentos disponíveis
│   └── pokemon_movesets.csv        # Movesets dos Pokémon
├── 📁 output/                      # Resultados e saídas
│   ├── 📁 models/                  # Modelos salvos
│   │   ├── best_model.rds          # Melhor modelo encontrado
│   │   ├── all_models.rds          # Todos os modelos
│   │   └── optimization_result.rds # Resultado da otimização
│   ├── 📁 plots/                   # Gráficos gerados
│   │   ├── elite_four_types.png    # Tipos da Elite dos 4
│   │   ├── pokemon_performance.png # Performance dos Pokémon
│   │   ├── team_radar.png          # Radar da equipe
│   │   └── type_efficiency.png     # Efetividade de tipos
│   ├── 📁 reports/                 # Relatórios gerados
│   │   └── relatorio_final.md      # Relatório final
│   ├── 📁 tables/                  # Tabelas de resultados
│   │   ├── best_team.csv           # Melhor equipe
│   │   ├── battle_summary.csv      # Resumo de batalhas
│   │   └── pokemon_performance.csv # Performance individual
│   └── pokemon_elite_four.log      # Log de execução
├── 📁 docs/                        # Documentação
│   ├── CASE_TECNICO_41_PERGUNTAS_PYTHON.ipynb
│   ├── IMPLEMENTACAO_TECNICA.md    # Implementação técnica
│   ├── ANALISE_RESULTADOS.md       # Análise de resultados
│   ├── DECISOES_CIENTIFICAS.md     # Decisões científicas
│   ├── METODOLOGIA_CIENTIFICA.md   # Metodologia científica
│   ├── ESTRUTURA_PROJETO.md        # Este arquivo
│   └── REFERENCIAS_CIENTIFICAS.md  # Referências científicas
├── 📁 tests/                       # Testes automatizados
│   ├── __init__.py
│   ├── test_pokemon.py             # Testes da classe Pokémon
│   ├── test_battle_system.py       # Testes do sistema de batalhas
│   ├── test_optimizer.py           # Testes do otimizador
│   └── test_integration.py         # Testes de integração
├── 📁 scripts/                     # Scripts auxiliares
│   ├── generate_plots.py           # Geração de gráficos
│   ├── generate_reports.py         # Geração de relatórios
│   └── cleanup_output.py           # Limpeza de saídas
├── main.py                         # Script principal
├── requirements.txt                # Dependências Python
├── requirements-dev.txt            # Dependências de desenvolvimento
├── setup.py                        # Configuração do pacote
├── pyproject.toml                  # Configuração do projeto
├── .gitignore                      # Arquivos ignorados pelo Git
├── .github/                        # Configurações do GitHub
│   └── workflows/
│       └── ci.yml                  # CI/CD pipeline
├── README.md                       # Documentação principal
├── INSTALACAO_PYTHON.md            # Guia de instalação
├── LICENSE                         # Licença do projeto
└── CHANGELOG.md                    # Histórico de mudanças
```

## 🧩 Módulos e Responsabilidades

### 1. Módulo Core (`pokemon_elite_four/core/`)

#### Responsabilidade
Implementar as classes fundamentais do sistema: Pokémon, equipes, batalhas e movimentos.

#### Arquivos e Classes

##### `pokemon.py`
```python
class Pokemon:
    """Classe principal do Pokémon"""
    def __init__(self, name, pokemon_id, type1, type2, stats, level)
    def take_damage(self, damage)
    def heal(self, amount)
    def restore_full_health(self)
    def get_types(self)
    def has_type(self, pokemon_type)
    def _load_realistic_moveset(self)

class PokemonTeam:
    """Equipe de Pokémon (sexteto)"""
    def __init__(self, pokemon_list)
    def add_pokemon(self, pokemon)
    def remove_pokemon(self, pokemon)
    def get_team_stats(self)
    def is_team_fainted(self)

class PokemonStats:
    """Estatísticas de um Pokémon"""
    def __init__(self, hp, attack, defense, sp_attack, sp_defense, speed)
    def get_total(self)
    def get_average(self)
```

##### `battle_system.py`
```python
class BattleSystem:
    """Sistema principal de batalhas"""
    def __init__(self)
    def calculate_damage(self, attacker, defender, move, critical_hit)
    def is_critical_hit(self, attacker, move)
    def does_move_hit(self, move, attacker, defender)
    def execute_turn(self, attacker, defender, move, turn_number)
    def battle_pokemon(self, pokemon1, pokemon2)
    def battle_team(self, team1, team2)

class TypeEffectiveness:
    """Sistema de efetividade de tipos"""
    @classmethod
    def get_effectiveness(cls, attack_type, defender_types)
    @classmethod
    def get_effectiveness_multiplier(cls, attack_type, defender_types)
```

##### `moves.py`
```python
class Move:
    """Representa um movimento Pokémon"""
    def __init__(self, name, move_type, category, power, accuracy, pp, priority, target, description)

class MoveSet:
    """Conjunto de movimentos de um Pokémon"""
    def __init__(self, moves)
    def get_moves_by_category(self, category)
    def get_random_move(self)
    def get_best_move(self, opponent_type)

class MoveCategory(Enum):
    """Categorias de movimentos"""
    PHYSICAL = "Physical"
    SPECIAL = "Special"
    STATUS = "Status"
```

##### `config.py`
```python
# Configurações do sistema
BATTLE_CONFIG = {
    'max_turns': 100,
    'critical_hit_base_rate': 6.25,
    'damage_variation_min': 0.85,
    'damage_variation_max': 1.0
}

OPTIMIZATION_CONFIG = {
    'default_generations': 50,
    'default_population_size': 100,
    'crossover_rate': 0.8,
    'mutation_rate': 0.1,
    'tournament_size': 3
}
```

### 2. Módulo Analysis (`pokemon_elite_four/analysis/`)

#### Responsabilidade
Implementar algoritmos de otimização, análise de dados e processamento de resultados.

#### Arquivos e Classes

##### `team_optimizer.py`
```python
class TeamOptimizer:
    """Otimizador de equipes usando algoritmo genético"""
    def __init__(self)
    def optimize_team(self, generations=50, population_size=100)
    def calculate_team_fitness(self, individual)
    def create_team_from_individual(self, individual)
    def simulate_team_battles(self, team)
    def calculate_team_balance(self, team)
    def get_available_pokemon_ids(self)

class GeneticAlgorithm:
    """Implementação do algoritmo genético"""
    def __init__(self, fitness_function, crossover_function, mutation_function)
    def run(self, population_size, generations)
    def selection(self, population, k)
    def crossover(self, parent1, parent2)
    def mutation(self, individual)
```

##### `battle_analyzer.py`
```python
class BattleAnalyzer:
    """Analisador de performance em batalhas"""
    def __init__(self, battle_system)
    def analyze_team_performance(self, team, simulations=1000)
    def analyze_individual_performance(self, team)
    def analyze_elite_four_performance(self, team)
    def generate_performance_report(self, team)
    def calculate_win_rate(self, team, opponent)
    def calculate_average_turns(self, team, opponent)
```

##### `data_processor.py`
```python
class DataProcessor:
    """Processador de dados do projeto"""
    def __init__(self)
    def load_pokemon_data(self, file_path)
    def load_elite_four_data(self, file_path)
    def preprocess_data(self, data)
    def validate_data(self, data)
    def create_derived_features(self, data)
    def export_results(self, results, file_path)
```

### 3. Módulo Utils (`pokemon_elite_four/utils/`)

#### Responsabilidade
Fornecer utilitários, funções auxiliares e configurações do sistema.

#### Arquivos e Classes

##### `functions.py`
```python
def calculate_type_effectiveness(attack_type, defender_types)
def calculate_damage_variation()
def generate_random_team()
def validate_pokemon_data(data)
def format_battle_log(battle_log)
def calculate_statistics(data)
def export_to_csv(data, file_path)
def import_from_csv(file_path)
```

##### `install_packages.py`
```python
def install_required_packages()
def check_package_versions()
def update_packages()
def install_development_packages()
def create_requirements_file()
```

##### `logging_config.py`
```python
def setup_logging(log_level=logging.INFO, log_file=None)
def get_logger(name)
def log_function_call(func)
def log_performance(func)
def log_error(error, context=None)
```

### 4. Módulo Visualization (`pokemon_elite_four/visualization/`)

#### Responsabilidade
Gerar visualizações, gráficos e relatórios do projeto.

#### Arquivos e Classes

##### `plots.py`
```python
class PlotGenerator:
    """Gerador de gráficos e visualizações"""
    def __init__(self)
    def create_team_radar_chart(self, team)
    def create_type_distribution_plot(self, data)
    def create_performance_plot(self, results)
    def create_correlation_heatmap(self, data)
    def create_battle_analysis_plot(self, battle_logs)
    def save_plot(self, plot, filename)
```

##### `reports.py`
```python
class ReportGenerator:
    """Gerador de relatórios"""
    def __init__(self)
    def generate_team_report(self, team, results)
    def generate_battle_report(self, battle_logs)
    def generate_optimization_report(self, optimization_results)
    def generate_performance_report(self, performance_data)
    def export_to_markdown(self, report, filename)
    def export_to_html(self, report, filename)
```

## 🔧 Configuração do Projeto

### 1. Arquivo `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="pokemon-elite-four",
    version="1.0.0",
    description="Sistema de análise e otimização de equipes Pokémon",
    author="Equipe de Desenvolvimento",
    author_email="contato@exemplo.com",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "scipy>=1.9.0",
        "scikit-learn>=1.1.0",
        "xgboost>=1.6.0",
        "lightgbm>=3.3.0",
        "deap>=1.3.0",
        "optuna>=3.0.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "plotly>=5.10.0",
        "jupyter>=1.0.0",
        "tqdm>=4.64.0",
        "colorama>=0.4.0",
        "pyyaml>=6.0",
        "pytest>=7.0.0",
        "black>=22.0.0",
        "flake8>=5.0.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
```

### 2. Arquivo `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pokemon-elite-four"
version = "1.0.0"
description = "Sistema de análise e otimização de equipes Pokémon"
authors = [
    {name = "Equipe de Desenvolvimento", email = "contato@exemplo.com"}
]
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.8"
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "flake8>=5.0.0",
    "mypy>=0.991",
    "pre-commit>=2.20.0"
]

[tool.black]
line-length = 88
target-version = ['py38']

[tool.flake8]
max-line-length = 88
extend-ignore = ["E203", "W503"]

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### 3. Arquivo `.gitignore`
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Project specific
output/logs/
output/temp/
*.rds
*.pkl
*.joblib
```

## 🧪 Estrutura de Testes

### 1. Organização dos Testes
```
tests/
├── __init__.py
├── test_pokemon.py              # Testes da classe Pokémon
├── test_battle_system.py        # Testes do sistema de batalhas
├── test_optimizer.py            # Testes do otimizador
├── test_integration.py          # Testes de integração
├── test_data_processing.py      # Testes de processamento de dados
├── test_visualization.py        # Testes de visualização
├── fixtures/                    # Dados de teste
│   ├── sample_pokemon.json
│   ├── sample_teams.json
│   └── sample_battle_logs.json
└── conftest.py                  # Configuração do pytest
```

### 2. Exemplo de Teste
```python
import pytest
from pokemon_elite_four.core.pokemon import Pokemon, PokemonType, PokemonStats
from pokemon_elite_four.core.battle_system import BattleSystem

class TestPokemon:
    def test_pokemon_creation(self):
        """Testa criação de Pokémon"""
        charizard = Pokemon(
            name='Charizard',
            pokemon_id=6,
            type1=PokemonType.FIRE,
            type2=PokemonType.FLYING,
            stats=PokemonStats(78, 84, 78, 109, 85, 100),
            level=60
        )
        
        assert charizard.name == 'Charizard'
        assert charizard.level == 60
        assert charizard.max_hp > 0
    
    def test_damage_calculation(self):
        """Testa cálculo de dano"""
        battle_system = BattleSystem()
        charizard = create_test_pokemon('Charizard')
        blastoise = create_test_pokemon('Blastoise')
        
        damage = battle_system.calculate_damage(charizard, blastoise, flamethrower)
        
        assert damage > 0
        assert damage <= blastoise.max_hp * 4
```

## 📊 Estrutura de Dados

### 1. Dataset Principal (`pokemon_data.csv`)
```csv
id,name,type1,type2,hp,attack,defense,sp_attack,sp_defense,speed,total,generation
1,Bulbasaur,Grass,Poison,45,49,49,65,65,45,320,1
2,Ivysaur,Grass,Poison,60,62,63,80,80,60,405,1
3,Venusaur,Grass,Poison,80,82,83,100,100,80,525,1
...
```

### 2. Dataset Elite dos 4 (`elite_four_data.csv`)
```csv
member,pokemon,level,type1,type2,moveset
Lorelei,Dewgong,54,Water,Ice,"Surf,Ice Beam,Rest,Sleep Talk"
Lorelei,Cloyster,53,Water,Ice,"Surf,Ice Beam,Spike Cannon,Clamp"
...
```

### 3. Dataset de Movimentos (`pokemon_moves.csv`)
```csv
name,type,category,power,accuracy,pp,priority,target,description
Tackle,Normal,Physical,40,100,35,0,Enemy,A physical attack
Flamethrower,Fire,Special,95,100,15,0,Enemy,A powerful fire attack
...
```

## 🔄 Fluxo de Execução

### 1. Fluxo Principal
```python
# main.py
def main():
    # 1. Carregar dados
    pokemon_data = load_pokemon_data()
    elite_four_data = load_elite_four_data()
    
    # 2. Configurar sistema
    battle_system = BattleSystem()
    optimizer = TeamOptimizer()
    
    # 3. Executar otimização
    best_team, fitness = optimizer.optimize_team()
    
    # 4. Analisar resultados
    analyzer = BattleAnalyzer(battle_system)
    results = analyzer.analyze_team_performance(best_team)
    
    # 5. Gerar relatórios
    report_generator = ReportGenerator()
    report_generator.generate_team_report(best_team, results)
```

### 2. Fluxo de Otimização
```python
# team_optimizer.py
def optimize_team(self):
    # 1. Inicializar população
    population = self.create_initial_population()
    
    # 2. Avaliar fitness
    for individual in population:
        individual.fitness = self.calculate_team_fitness(individual)
    
    # 3. Evolução
    for generation in range(generations):
        # Seleção
        parents = self.selection(population)
        
        # Cruzamento
        offspring = self.crossover(parents)
        
        # Mutação
        offspring = self.mutation(offspring)
        
        # Avaliação
        for individual in offspring:
            individual.fitness = self.calculate_team_fitness(individual)
        
        # Substituição
        population = self.replacement(population, offspring)
    
    # 4. Retornar melhor indivíduo
    return self.get_best_individual(population)
```

## 🎯 Padrões de Design Utilizados

### 1. **Singleton Pattern**
```python
class BattleSystem:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### 2. **Factory Pattern**
```python
class PokemonFactory:
    @staticmethod
    def create_pokemon(pokemon_id, level=50):
        pokemon_data = get_pokemon_data(pokemon_id)
        return Pokemon(
            name=pokemon_data['name'],
            pokemon_id=pokemon_id,
            type1=pokemon_data['type1'],
            type2=pokemon_data['type2'],
            stats=pokemon_data['stats'],
            level=level
        )
```

### 3. **Strategy Pattern**
```python
class OptimizationStrategy:
    def optimize(self, problem):
        raise NotImplementedError

class GeneticAlgorithmStrategy(OptimizationStrategy):
    def optimize(self, problem):
        return self.run_genetic_algorithm(problem)

class RandomSearchStrategy(OptimizationStrategy):
    def optimize(self, problem):
        return self.run_random_search(problem)
```

### 4. **Observer Pattern**
```python
class OptimizationObserver:
    def update(self, generation, best_fitness):
        pass

class ProgressTracker(OptimizationObserver):
    def update(self, generation, best_fitness):
        print(f"Geração {generation}: Fitness = {best_fitness:.4f}")
```

## 🔧 Configuração de Desenvolvimento

### 1. Ambiente de Desenvolvimento
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Instalar pre-commit hooks
pre-commit install

# Executar testes
pytest tests/

# Formatar código
black pokemon_elite_four/
flake8 pokemon_elite_four/
```

### 2. CI/CD Pipeline
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10, 3.11]
    
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Run tests
      run: pytest tests/ --cov=pokemon_elite_four
    
    - name: Run linting
      run: |
        black --check pokemon_elite_four/
        flake8 pokemon_elite_four/
```

## 📈 Métricas de Qualidade

### 1. **Cobertura de Código**
- **Meta**: 90%+ de cobertura
- **Ferramenta**: pytest-cov
- **Comando**: `pytest --cov=pokemon_elite_four`

### 2. **Complexidade Ciclomática**
- **Meta**: < 10 por função
- **Ferramenta**: radon
- **Comando**: `radon cc pokemon_elite_four/`

### 3. **Manutenibilidade**
- **Meta**: A+ no índice de manutenibilidade
- **Ferramenta**: radon
- **Comando**: `radon mi pokemon_elite_four/`

### 4. **Qualidade de Código**
- **Meta**: 9.0+ no score de qualidade
- **Ferramenta**: sonar-scanner
- **Comando**: `sonar-scanner`

## 🎯 Conclusões da Estrutura

### Principais Características

1. **Modularidade**: Separação clara de responsabilidades
2. **Extensibilidade**: Fácil adição de novos recursos
3. **Manutenibilidade**: Código limpo e documentado
4. **Testabilidade**: Testes abrangentes e automatizados
5. **Escalabilidade**: Arquitetura preparada para crescimento

### Benefícios da Arquitetura

1. **Desenvolvimento**: Equipe pode trabalhar em paralelo
2. **Manutenção**: Mudanças isoladas em módulos
3. **Testes**: Testes unitários e de integração
4. **Deploy**: Configuração flexível e automatizada
5. **Documentação**: Estrutura auto-documentada

### Próximos Passos

1. **Refatoração**: Melhorar código existente
2. **Extensões**: Adicionar novos módulos
3. **Otimização**: Melhorar performance
4. **Documentação**: Expandir documentação
5. **Testes**: Aumentar cobertura de testes

---

**Status da Estrutura**: ✅ Organizada | **Arquitetura**: 🏗️ Modular | **Qualidade**: 📊 Alta
