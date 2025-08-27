# 🎮 Pokémon Elite dos 4 - Análise com R

## 🎯 Visão Geral

Projeto de análise de dados para otimizar equipes Pokémon para enfrentar a Elite dos 4, desenvolvido em R com foco em machine learning e otimização.

## 🚀 Execução Rápida

```r
# Executar projeto completo
source('main.R')
```

## 📁 Estrutura do Projeto

```
Projeto_Final_PDA/
├── main.R                    # 🚀 Execução principal
├── src/                      # 📦 Código fonte
│   ├── core/                # 🔧 Funcionalidades principais
│   ├── analysis/            # 🔍 Análises exploratórias
│   ├── models/              # 📊 Modelagem e otimização
│   └── utils/               # 🛠️  Funções utilitárias
├── data/                     # 📊 Dados do projeto
├── output/                   # 📈 Resultados e saídas
├── config/                   # ⚙️  Configurações
└── docs/                     # 📚 Documentação completa
```

## 📚 Documentação

### **🏗️ Estrutura**
- [Estrutura do Projeto](docs/ESTRUTURA_PROJETO.md)

### **🎯 Apresentação**
- [Apresentação Executiva](docs/apresentacao/APRESENTACAO_EXECUTIVA.md)

### **📊 Case Técnico**
- [41 Perguntas em R Markdown](docs/case-tecnico/CASE_TECNICO_41_PERGUNTAS.Rmd)
- [Instruções do Notebook](docs/case-tecnico/INSTRUCOES_NOTEBOOK.md)

## 🛠️ Como Usar

### **1. Execução Completa (Recomendado)**
```r
source('main.R')
```

### **2. Configuração Inicial**
```r
source('src/core/setup.R')
```

### **3. Execução por Etapas**
```r
# Preparação de dados
source('src/core/01_data_preparation.R')

# Análise exploratória
source('src/analysis/02_exploratory_analysis.R')

# Modelagem
source('src/models/03_statistical_modeling.R')

# Otimização
source('src/models/04_team_optimization.R')

# Simulação
source('src/core/05_battle_simulation.R')
```

### **4. Validação**
```r
# Testar estrutura
source('src/utils/test_structure.R')
```

## 📦 Dependências

Verifique [requirements.txt](config/requirements.txt) para as dependências necessárias.

## 🎯 Funcionalidades

- 📊 **Análise Exploratória**: Estatísticas e visualizações dos dados
- 🤖 **Modelagem**: Machine learning para predição de performance
- ⚔️ **Otimização**: Algoritmos genéticos para equipes ideais
- 🎮 **Simulação**: Batalhas Pokémon com diferentes configurações
- 📈 **Relatórios**: Geração automática de resultados

## 🔧 Desenvolvimento

### **Estrutura Organizada**
- Código separado por funcionalidade
- Funções reutilizáveis centralizadas
- Configurações centralizadas
- Testes automáticos de validação

### **Padrões**
- Tratamento de erros consistente
- Logging estruturado
- Documentação inline
- Nomenclatura clara

## 📊 Resultados

Os resultados são salvos automaticamente em:
- **Gráficos**: `output/plots/`
- **Tabelas**: `output/tables/`
- **Modelos**: `output/models/`
- **Relatórios**: `output/reports/`

## 🧪 Testes

```r
# Validar estrutura do projeto
source('src/utils/test_structure.R')
```

## 📝 Licença

Case Técnico de Análise com R - 2024

---

**💡 Dica**: Para começar rapidamente, use `source('main.R')` na raiz do projeto!
