# 🎮 Pokémon Elite Four - Sistema de Análise e Otimização

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Concluído-success.svg)](https://github.com/MagnaSoluto/projeto-pokemon-elite-4-new-py.git)
[![Case Técnico](https://img.shields.io/badge/Case_Técnico-38_Perguntas-orange.svg)](docs/CASE_TECNICO_38_PERGUNTAS_PYTHON.ipynb)
[![Apresentação](https://img.shields.io/badge/Apresentação-Interativa-brightgreen.svg)](docs/APRESENTACAO_COMPLETA.ipynb)
[![Testes](https://img.shields.io/badge/Testes-45_Passando-success.svg)](tests/)
[![Score](https://img.shields.io/badge/Score-93.5%25-gold.svg)](output/optimization/best_team.txt)
[![Qualidade](https://img.shields.io/badge/Qualidade-Profissional-purple.svg)](pyproject.toml)



---

<div align="center">

**🎯 CASE TÉCNICO DE ANÁLISE COM PYTHON**  
*MBA em Engenharia de Dados - Universidade Presbiteriana Mackenzie*

**👨‍💻 Autores:**  
Adriano Carvalho dos Santos (RA: 10747203)  
Jonathas William Freire Borges (RA: 10747100)

**⚔️ Que o melhor treinador vença na Elite dos 4! ⚔️**

---

</div>

## 📋 Visão Geral

Este projeto implementa um sistema completo de análise e otimização de equipes Pokémon para vencer a Elite dos 4, baseado nos jogos Game Boy Advanced (FireRed/LeafGreen). Utilizando algoritmos genéticos e simulações de batalhas realistas, o sistema encontra a melhor combinação de 6 Pokémon para maximizar a taxa de vitória.

### 🏆 Resultados Alcançados

- **Sistema Avançado**: Batalhas inteligentes com seleção estratégica de movimentos
- **Equipe Otimizada**: Raichu, Moltres, Starmie, Venomoth, Aerodactyl, Dewgong
- **Cobertura de Tipos**: 8 tipos únicos com excelente balanceamento
- **Performance**: 100% contra Lorelei e Bruno, 78% contra Lance, 54% contra Champion
- **Sistema de Batalhas**: Fórmula GBA precisa com golpes críticos e movesets realistas
- **Algoritmo de Otimização**: Algoritmo genético avançado com múltiplas estratégias
- **Score Final**: 0.9350 (93.5% de eficiência geral)

## 🚀 Características Principais

### ⚔️ Sistema de Batalhas Inteligente
- **Fórmula de Dano GBA**: Implementação precisa da fórmula de dano do FireRed/LeafGreen
- **Golpes Críticos**: Sistema completo com taxa base 6.25% + modificador por velocidade
- **Movesets Realistas**: 52+ Pokémon com movimentos autênticos dos jogos
- **Efetividade de Tipos**: Matriz completa de 18 tipos Pokémon
- **Sistema de Status**: Condições de status e efeitos especiais
- **Seleção Estratégica**: 4 estratégias diferentes de seleção de movimentos
- **Análise Inteligente**: Considera dano, efetividade, precisão e PP

### 🧬 Otimização Avançada
- **Algoritmo Genético**: Evolução de equipes através de seleção natural
- **Função de Fitness Avançada**: 5 fatores de avaliação (performance, tipos, balanceamento, estratégias, resistências)
- **População Inteligente**: 50% equipes balanceadas + 50% aleatórias
- **Múltiplas Estratégias**: Testa diferentes abordagens de batalha
- **Convergência Otimizada**: Parâmetros ajustados para melhor performance

### 📊 Análise Completa
- **Simulações Massivas**: 1000+ batalhas por análise
- **Métricas Detalhadas**: Taxa de vitória, turnos médios, performance individual
- **Visualizações**: Gráficos e relatórios automatizados
- **Relatórios**: Exportação em CSV e TXT

### 📈 Case Técnico - Análise Exploratória
- **Notebook Python**: 38 questões organizadas em 6 partes técnicas
- **Análise de Dados**: Pandas, NumPy, Matplotlib e Seaborn
- **Dataset Pokémon**: 800+ Pokémon com análise completa de tipos e estatísticas
- **Visualizações Avançadas**: Heatmaps, pairplots, boxplots e histogramas
- **Exportação de Dados**: Múltiplos formatos CSV para análise posterior
- **Instalação Automática**: Dependências instaladas automaticamente no notebook

### 🎮 Apresentação Interativa
- **Notebook de Apresentação**: 17 células com demonstrações ao vivo
- **Contexto Histórico**: História completa do Pokémon no Brasil
- **6 Slides Estruturados**: Apresentação otimizada para 7 minutos
- **Código Executável**: Demonstrações interativas do sistema
- **Visualizações Dinâmicas**: Gráficos matplotlib integrados
- **Simulação Completa**: Algoritmo genético executando em tempo real

## 🎯 Equipe Otimizada

### Sistema Avançado (Recomendado)

A melhor equipe encontrada pelo sistema avançado:

| # | Pokémon | Nível | Tipos | Total | Vantagens |
|---|---------|-------|-------|-------|-----------|
| 1 | **Raichu** | 60 | Electric | 485 | Velocidade + Electric coverage |
| 2 | **Moltres** | 60 | Fire/Flying | 580 | Legendary + Fire/Flying |
| 3 | **Starmie** | 60 | Water/Psychic | 520 | Water + Psychic coverage |
| 4 | **Venomoth** | 60 | Bug/Poison | 450 | Bug + Poison coverage |
| 5 | **Aerodactyl** | 60 | Rock/Flying | 515 | Velocidade + Rock coverage |
| 6 | **Dewgong** | 60 | Water/Ice | 475 | Water + Ice coverage |

### Sistema Original (Baseline)

Equipe do sistema original para comparação:

| # | Pokémon | Nível | Tipos | Total | Moveset |
|---|---------|-------|-------|-------|---------|
| 1 | **Lapras** | 60 | Water/Ice | 535 | Surf, Ice Beam, Thunderbolt, Psychic |
| 2 | **Magneton** | 60 | Electric/Steel | 465 | Thunderbolt, Flash Cannon, Thunder Wave, Light Screen |
| 3 | **Moltres** | 60 | Fire/Flying | 580 | Flamethrower, Wing Attack, Roost, Will-O-Wisp |
| 4 | **Gengar** | 60 | Ghost/Poison | 500 | Shadow Ball, Psychic, Thunderbolt, Toxic |
| 5 | **Mew** | 60 | Psychic | 600 | Psychic, Aura Sphere, Soft-Boiled, Calm Mind |
| 6 | **Golem** | 60 | Rock/Ground | 495 | Earthquake, Rock Slide, Explosion, Swords Dance |

### 📈 Performance por Membro da Elite dos 4

#### Sistema Avançado:
- **Lorelei** (Ice): 100.0% vitórias
- **Bruno** (Fighting): 100.0% vitórias  
- **Agatha** (Ghost): 98.0% vitórias
- **Lance** (Dragon): 78.0% vitórias
- **Champion** (Mixed): 54.0% vitórias

#### Sistema Original:
- **Lorelei** (Ice): 100.0% vitórias
- **Bruno** (Fighting): 100.0% vitórias  
- **Agatha** (Ghost): 100.0% vitórias
- **Lance** (Dragon): 84.0% vitórias
- **Champion** (Mixed): 48.0% vitórias

## 🛠️ Instalação e Uso

## 🎮 Apresentação Interativa

### 📋 Como Executar a Apresentação

Para executar a **apresentação interativa completa**:

```bash
cd projeto-pokemon-elite-4-new-py
source venv/bin/activate
jupyter notebook docs/APRESENTACAO_COMPLETA.ipynb
```

### 🎯 Estrutura da Apresentação (7 minutos)

- **🎯 Contexto Histórico**: Pokémon no Brasil + desafio científico
- **📊 Slide 1**: Problema de otimização (16.8 bilhões de combinações)
- **🏗️ Slide 2**: Arquitetura tecnológica + métricas do projeto
- **📓 Slide 3**: Case técnico (38 questões) + verificação dos dados
- **🏆 Slide 4**: Equipe otimizada + gráfico de performance
- **🔬 Slide 5**: Validação científica + testes de qualidade
- **🎮 Slide 6**: Demonstração ao vivo + simulação completa

### ✨ Recursos Interativos

- **Código Executável**: Todas as demonstrações rodam ao vivo
- **Gráficos Dinâmicos**: Matplotlib integrado com dados reais
- **Simulação Realista**: Algoritmo genético com barra de progresso
- **Métricas em Tempo Real**: Verificação do projeto executando
- **Contexto Completo**: História do Pokémon no Brasil incluída

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/MagnaSoluto/projeto-pokemon-elite-4-new-py.git
cd projeto-pokemon-elite-4-new-py

# Crie e ative ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt
```

### Uso Básico

```bash
# Sistema Avançado (Recomendado)
python3 test_advanced_optimization.py

# Otimizar equipe (sistema original)
python3 main.py --mode optimize --generations 50 --population 100

# Analisar equipe específica
python3 main.py --mode analyze --simulations 1000

# Simular batalha individual
python3 main.py --mode simulate

# Executar equipe de demonstração
python3 main.py --mode demo
```

### Sistema Avançado

O sistema avançado oferece funcionalidades superiores:

```python
from pokemon_elite_four.analysis.advanced_team_optimizer import AdvancedTeamOptimizer
from pokemon_elite_four.core.smart_battle_system import SmartBattleSystem, MoveStrategy

# Cria otimizador avançado
optimizer = AdvancedTeamOptimizer(
    pokemon_database=pokemon_database,
    elite_four=elite_four,
    population_size=100,
    max_generations=50
)

# Executa otimização
result = optimizer.optimize_team_advanced()

# Batalha inteligente
smart_system = SmartBattleSystem()
battle_log = smart_system.battle_teams_smart(
    team1, team2, 
    MoveStrategy.BALANCED, 
    MoveStrategy.TYPE_EFFECTIVE
)
```

## 📁 Estrutura do Projeto

```
projeto-pokemon-elite-4-new-py/
├── 📁 pokemon_elite_four/          # Pacote principal
│   ├── 📁 core/                    # Classes fundamentais
│   │   ├── pokemon.py              # Classe Pokémon e equipe
│   │   ├── battle_system.py        # Sistema de batalhas original
│   │   ├── smart_battle_system.py  # Sistema de batalhas inteligente
│   │   └── moves.py                # Movimentos e movesets
│   ├── 📁 analysis/                # Análise e otimização
│   │   ├── team_optimizer.py       # Algoritmo genético original
│   │   └── advanced_team_optimizer.py # Algoritmo genético avançado
│   └── 📁 utils/                   # Utilitários
├── 📁 data/                        # Dados dos Pokémon
│   ├── pokemon_data.csv            # Estatísticas base
│   └── elite_four_data.csv         # Dados da Elite dos 4
├── 📁 output/                      # Resultados e relatórios
│   ├── 📁 models/                  # Modelos salvos
│   ├── 📁 plots/                   # Gráficos gerados
│   └── 📁 reports/                 # Relatórios detalhados
├── 📁 docs/                        # Documentação
│   ├── IMPLEMENTACAO_TECNICA.md
│   ├── ANALISE_RESULTADOS.md
│   ├── DECISOES_CIENTIFICAS.md
│   ├── METODOLOGIA_CIENTIFICA.md
│   └── CASE_TECNICO_38_PERGUNTAS_PYTHON.ipynb # Case técnico - 32 questões Python
├── main.py                         # Script principal
├── test_advanced_optimization.py   # Teste do sistema avançado
├── requirements.txt                # Dependências Python
└── README.md                       # Este arquivo
```

## 🔬 Metodologia Científica

### 1. **Coleta de Dados**
- Dataset de 151 Pokémon da primeira geração
- Estatísticas base, tipos e movimentos
- Dados da Elite dos 4 com níveis e movesets

### 2. **Modelagem Matemática**
- Fórmula de dano GBA: `((2×Level+10)×Power×Attack/Defense/50)+2`
- Taxa de crítico: `6.25% × (1 + velocidade/512)`
- Efetividade de tipos: matriz 18×18 completa

### 3. **Algoritmo de Otimização**
- **Representação**: Cromossomo de 6 IDs de Pokémon
- **Seleção**: Torneio de tamanho 3
- **Cruzamento**: Uniforme com taxa 0.8
- **Mutação**: Substituição aleatória com taxa 0.1
- **Fitness**: 70% performance + 30% balanceamento

### 4. **Validação**
- Simulações Monte Carlo (1000+ batalhas)
- Teste estatístico de significância
- Análise de convergência do algoritmo

## 📊 Resultados Detalhados

### Performance da Equipe Otimizada
- **Taxa de Vitória Geral**: 86.0% (média ponderada)
- **Turnos Médios**: 8.2
- **Convergência**: Estabilizada na geração 20
- **Tempo de Otimização**: ~3 segundos
- **Score de Fitness**: 0.9350 (93.5%)

### Análise por Tipo
- **Electric** (Raichu): Excelente contra Water, Flying
- **Fire/Flying** (Moltres): Eficaz contra Grass, Bug, Steel
- **Water/Psychic** (Starmie): Cobertura dupla Water + Psychic
- **Bug/Poison** (Venomoth): Cobertura contra Grass, Psychic
- **Rock/Flying** (Aerodactyl): Velocidade + cobertura Rock
- **Water/Ice** (Dewgong): Cobertura Water + Ice

## 🎮 Sistema de Batalhas

### Características Técnicas
- **Fórmula GBA**: Implementação 1:1 do FireRed/LeafGreen
- **Golpes Críticos**: Taxa base 6.25% + modificador velocidade
- **Movesets**: 52+ Pokémon com movimentos autênticos
- **Efetividade**: Matriz completa de tipos
- **Status**: Condições como Paralyze, Sleep, Poison

### Movimentos Implementados
- **Físicos**: Earthquake, Rock Slide, Wing Attack, Body Slam
- **Especiais**: Flamethrower, Thunderbolt, Ice Beam, Psychic
- **Status**: Thunder Wave, Toxic, Swords Dance, Calm Mind
- **Prioridade**: Aqua Jet, Extreme Speed, Quick Attack

## 🔧 Dependências

```txt
pandas>=1.5.0
numpy>=1.21.0
scipy>=1.9.0
scikit-learn>=1.1.0
xgboost>=1.6.0
lightgbm>=3.3.0
deap>=1.3.0
optuna>=3.0.0
matplotlib>=3.5.0
seaborn>=0.11.0
plotly>=5.10.0
jupyter>=1.0.0
tqdm>=4.64.0
colorama>=0.4.0
pyyaml>=6.0
pytest>=7.0.0
black>=22.0.0
flake8>=5.0.0
```

## 📈 Próximos Passos

### Melhorias Planejadas
- [ ] Implementar mais movimentos (100+)
- [ ] Adicionar habilidades especiais dos Pokémon
- [ ] Sistema de itens e held items
- [ ] Análise de EV/IV (Effort Values/Individual Values)
- [ ] Interface gráfica web
- [ ] API REST para integração

### Expansões Futuras
- [ ] Suporte a outras gerações (2-9)
- [ ] Sistema de Mega Evolution
- [ ] Análise de competitivo PvP
- [ ] Machine Learning avançado
- [ ] Análise de metagame

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores

- **Desenvolvimento Principal**: Sistema de análise e otimização Pokémon
- **Migração R→Python**: Conversão completa do projeto original
- **Sistema de Batalhas**: Implementação GBA precisa
- **Algoritmo Genético**: Otimização de equipes

## 📞 Contato

Para dúvidas, sugestões ou colaborações:
- **GitHub Issues**: [Abrir issue](https://github.com/MagnaSoluto/projeto-pokemon-elite-4-new-py/issues)
- **Email**: [Seu email aqui]

---

## 🎯 Resumo Executivo

Este projeto representa uma solução completa e cientificamente rigorosa para o problema de otimização de equipes Pokémon. Através da implementação de um sistema de batalhas fiel aos jogos originais e algoritmos genéticos avançados, conseguimos encontrar uma equipe com **86.0% de taxa de vitória** contra a Elite dos 4.

A metodologia combina análise de dados, modelagem matemática, otimização computacional e validação estatística, resultando em uma ferramenta robusta e confiável para treinadores Pokémon e pesquisadores em otimização combinatória.

**Status**: ✅ Produção Ready | **Performance**: 🏆 86.0% Vitórias | **Tecnologia**: 🐍 Python 3.8+
