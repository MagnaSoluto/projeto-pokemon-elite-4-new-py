# 📁 ESTRUTURA ORGANIZADA DO CÓDIGO

## 🎯 Visão Geral

Este documento descreve a nova estrutura organizada dos arquivos de código do projeto **Pokémon Elite dos 4 - Análise com R**.

## 🏗️ Estrutura de Diretórios

```
Projeto_Final_PDA/
├── main.R                          # 🚀 Arquivo principal de execução
├── src/                            # 📦 Código fonte organizado
│   ├── core/                       # 🔧 Funcionalidades principais
│   │   ├── config.R               # ⚙️  Configurações do projeto
│   │   ├── setup.R                # 🔧 Configuração de ambiente
│   │   ├── 01_data_preparation.R  # 📂 Preparação de dados
│   │   ├── 05_battle_simulation.R # 🎯 Simulação de batalhas
│   │   └── main_analysis.R        # 📊 Análise principal
│   ├── analysis/                   # 🔍 Análises exploratórias
│   │   └── 02_exploratory_analysis.R
│   ├── models/                     # 📊 Modelagem e otimização
│   │   ├── 03_statistical_modeling.R
│   │   └── 04_team_optimization.R
│   ├── utils/                      # 🛠️  Funções utilitárias
│   │   ├── functions.R            # 🔧 Funções comuns
│   │   ├── meu_pipeline.R         # 📊 Pipeline personalizado
│   │   ├── install_packages.R     # 📦 Instalação de pacotes
│   │   └── test_structure.R       # 🧪 Testes de estrutura
│   └── visualization/              # 📈 Visualizações (futuro)
├── data/                           # 📊 Dados do projeto
├── output/                         # 📈 Resultados e saídas
│   ├── plots/                      # 📊 Gráficos
│   ├── tables/                     # 📋 Tabelas
│   ├── models/                     # 🤖 Modelos treinados
│   └── reports/                    # 📄 Relatórios
└── docs/                           # 📚 Documentação
```

## 📋 Descrição dos Arquivos

### 🚀 **main.R** - Arquivo Principal
- **Função**: Ponto de entrada principal do projeto
- **Executa**: Todo o pipeline de análise automaticamente
- **Uso**: `source('main.R')`

### 🔧 **src/core/** - Funcionalidades Principais

#### **config.R**
- Configurações globais do projeto
- Parâmetros de modelagem
- Caminhos de diretórios
- Configurações de simulação

#### **setup.R**
- Configuração inicial do ambiente
- Carregamento de funções utilitárias
- Verificação de diretórios
- Configuração de opções do R

#### **01_data_preparation.R**
- Carregamento e limpeza de dados
- Preparação de variáveis
- Validação de dados

#### **05_battle_simulation.R**
- Simulação de batalhas Pokémon
- Cálculo de danos
- Lógica de combate

#### **main_analysis.R**
- Orquestração das análises
- Geração de relatórios
- Consolidação de resultados

### 🔍 **src/analysis/** - Análises Exploratórias

#### **02_exploratory_analysis.R**
- Análise exploratória dos dados
- Estatísticas descritivas
- Visualizações iniciais

### 📊 **src/models/** - Modelagem e Otimização

#### **03_statistical_modeling.R**
- Construção de modelos estatísticos
- Treinamento de algoritmos
- Validação de modelos

#### **04_team_optimization.R**
- Otimização de equipes Pokémon
- Algoritmos genéticos
- Seleção de melhores combinações

### 🛠️ **src/utils/** - Funções Utilitárias

#### **functions.R**
- Funções comuns reutilizáveis
- Tratamento de erros
- Validações
- Funções de visualização
- Funções de modelagem

#### **meu_pipeline.R**
- Pipeline personalizado para análise
- Função `meu_pipeline()`

#### **install_packages.R**
- Instalação automática de pacotes
- Verificação de dependências

#### **test_structure.R**
- Testes de validação da estrutura
- Verificação de arquivos e diretórios
- Validação de funcionalidades

## 🚀 Como Usar

### 1. **Execução Completa**
```r
# Na raiz do projeto
source('main.R')
```

### 2. **Configuração Inicial**
```r
# Configurar ambiente
source('src/core/setup.R')
```

### 3. **Execução por Etapas**
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

### 4. **Testes de Estrutura**
```r
# Validar estrutura do projeto
source('src/utils/test_structure.R')
```

## 🔧 Funcionalidades Principais

### **Funções Utilitárias Disponíveis**
- `load_data_safe()` - Carregamento seguro de dados
- `save_data_safe()` - Salvamento seguro de dados
- `save_plot_safe()` - Salvamento seguro de gráficos
- `calculate_model_metrics()` - Métricas de performance
- `log_message()` - Sistema de logging
- `clean_environment()` - Limpeza de ambiente

### **Configurações Automáticas**
- Criação automática de diretórios
- Verificação de arquivos de dados
- Configuração de opções do R
- Verificação de recursos do sistema

## 📊 Benefícios da Nova Estrutura

### ✅ **Organização**
- Código separado por funcionalidade
- Fácil localização de arquivos
- Estrutura escalável

### ✅ **Manutenibilidade**
- Funções reutilizáveis
- Configurações centralizadas
- Tratamento de erros consistente

### ✅ **Execução**
- Pipeline automatizado
- Execução por etapas
- Testes de validação

### ✅ **Documentação**
- Estrutura clara e intuitiva
- Comentários explicativos
- Instruções de uso

## 🧪 Validação

Para validar a estrutura do projeto:

```r
# Executar testes
source('src/utils/test_structure.R')

# Verificar ambiente
source('src/core/setup.R')
```

## 📝 Notas Importantes

1. **Ordem de Execução**: Sempre execute `setup.R` antes de outros scripts
2. **Dependências**: O arquivo `main.R` executa tudo automaticamente
3. **Personalização**: Modifique `config.R` para ajustar parâmetros
4. **Testes**: Use `test_structure.R` para validar mudanças

## 🔄 Atualizações Futuras

- **src/visualization/**: Funções específicas de visualização
- **src/tests/**: Testes unitários e de integração
- **src/benchmarks/**: Análises de performance
- **src/api/**: Interfaces para outros sistemas

---

*Esta estrutura foi organizada para facilitar o desenvolvimento, manutenção e execução do projeto Pokémon Elite dos 4.*
