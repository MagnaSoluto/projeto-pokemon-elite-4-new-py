# 🏗️ ESTRUTURA DO PROJETO POKÉMON ELITE DOS 4 (Python)

## 🎯 Visão Geral

Este documento consolida **TODA** a informação sobre a estrutura e organização do projeto em Python. O projeto foi migrado de R para Python com melhorias significativas na performance e realismo das simulações.

## 📁 Estrutura de Diretórios

```
Projeto_Final_PDA_Python/
├── 🚀 main.py                   # Execução principal
├── 📦 pokemon_elite_four/       # Pacote Python principal
│   ├── 🔧 core/                # Classes principais
│   │   ├── pokemon.py          # Classe Pokemon e PokemonTeam
│   │   ├── moves.py            # Sistema de movimentos
│   │   ├── battle_system.py    # Sistema de batalhas GBA
│   │   └── elite_four.py       # Membros da Elite Four
│   ├── 🔍 analysis/            # Análise e otimização
│   │   ├── data_processor.py   # Processamento de dados
│   │   ├── team_optimizer.py   # Algoritmos genéticos
│   │   └── battle_analyzer.py  # Análise de resultados
│   └── 🛠️  utils/              # Funções utilitárias
│       └── visualization.py    # Visualizações
├── 📊 data/                     # Dados do projeto
├── 📈 output/                   # Resultados e saídas
├── 📚 docs/                     # Documentação consolidada
│   ├── case-tecnico/            # Case técnico
│   ├── relatorios/              # Relatórios finais
│   └── ESTRUTURA_PROJETO.md    # Este arquivo
├── 🐍 requirements.txt          # Dependências Python
├── 📖 README.md                 # Documentação principal
├── 📖 INSTALACAO_PYTHON.md     # Instruções de instalação
└── 🔧 .gitignore               # Arquivos ignorados pelo Git
```

## 🚀 Como Usar

### **Execução Completa (Recomendado)**
```bash
python3 main.py --mode demo
```

### **Execução por Modos**
```bash
# Demonstração
python3 main.py --mode demo

# Simulação de batalhas
python3 main.py --mode simulate --simulations 50

# Análise de equipe
python3 main.py --mode analyze --simulations 50

# Otimização com ML
python3 main.py --mode optimize --generations 20 --population 30
```

## 🔧 Funcionalidades Principais

### **Classes Principais Disponíveis**
- `Pokemon` - Classe para Pokémon individuais
- `PokemonTeam` - Classe para equipes de Pokémon
- `Move` - Classe para movimentos
- `MoveSet` - Classe para conjuntos de movimentos
- `BattleSystem` - Sistema de batalhas GBA
- `EliteFour` - Membros da Elite Four
- `TeamOptimizer` - Algoritmos genéticos
- `BattleAnalyzer` - Análise de resultados

### **Funcionalidades Automáticas**
- Criação automática de move sets
- Sistema de batalhas realista GBA
- Algoritmos genéticos otimizados
- Análise de performance automática

## 📊 Benefícios da Estrutura

### ✅ **Organização**
- Classes bem definidas e organizadas
- Fácil localização de funcionalidades
- Estrutura escalável e modular

### ✅ **Manutenibilidade**
- Classes reutilizáveis
- Sistema orientado a objetos
- Tratamento de erros robusto

### ✅ **Execução**
- Múltiplos modos de execução
- Sistema de batalhas realista
- Algoritmos genéticos otimizados

## 🧪 Validação

Para validar a estrutura:
```bash
python3 main.py --mode demo
```

## 📝 Notas Importantes

1. **Ambiente Virtual**: Sempre use `venv` para isolar dependências
2. **Dependências**: Instale com `pip install -r requirements.txt`
3. **Execução**: Use `python3 main.py` para executar
4. **Modos**: Escolha o modo apropriado para sua necessidade

---

*Estrutura consolidada e otimizada - Projeto Pokémon Elite dos 4*
