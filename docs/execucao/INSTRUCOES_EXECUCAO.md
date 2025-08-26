# 🚀 Instruções de Execução - Projeto Pokémon Elite dos 4

## 📋 Pré-requisitos

### Software Necessário
- **R** (versão 4.0 ou superior)
- **RStudio** (recomendado para melhor experiência)
- **Git** (opcional, para controle de versão)

### Sistema Operacional
- ✅ **Windows**: R 4.0+ instalado
- ✅ **macOS**: R 4.0+ instalado  
- ✅ **Linux**: R 4.0+ instalado

## 🎯 Objetivo do Projeto

Este projeto resolve o seguinte problema:
> **"Qual é o melhor quinteto de Pokémon e em qual nível para vencer a Elite dos 4 no Red/Green?"**

## 📁 Estrutura do Projeto

```
Projeto_Final_PDA/
├── 📄 README.md                    # Documentação principal
├── ⚙️  config.R                     # Configurações do projeto
├── 📦 requirements.txt              # Dependências R
├── 🎮 exemplo_execucao.R           # Exemplo de execução passo a passo
├── 📊 data/                        # Datasets
│   ├── pokemon_data.csv           # 151 Pokémon originais
│   └── elite_four_data.csv        # Elite dos 4
├── 🔧 scripts/                     # Scripts de análise
│   ├── install_packages.R         # Instalação de pacotes
│   ├── 01_data_preparation.R      # Preparação de dados
│   ├── 02_exploratory_analysis.R  # Análise exploratória
│   ├── 03_statistical_modeling.R  # Modelagem estatística
│   ├── 04_team_optimization.R     # Otimização do quinteto
│   ├── 05_battle_simulation.R     # Simulação de batalhas
│   └── main_analysis.R            # Script principal
├── 📈 output/                      # Resultados gerados
│   ├── plots/                     # Gráficos
│   ├── tables/                    # Tabelas
│   ├── models/                    # Modelos treinados
│   └── reports/                   # Relatórios
└── 📚 docs/                       # Documentação técnica
    └── documentacao_tecnica.md    # Documentação completa
```

## 🚀 Como Executar

### Opção 1: Execução Completa (Recomendada)

1. **Abra o R ou RStudio**
2. **Navegue para o diretório do projeto**
3. **Execute o script principal:**

```r
# Carregar configurações
source("config.R")

# Executar análise completa
source("scripts/main_analysis.R")
```

### Opção 2: Execução Passo a Passo

1. **Abra o R ou RStudio**
2. **Navegue para o diretório do projeto**
3. **Execute o exemplo de execução:**

```r
source("exemplo_execucao.R")
```

### Opção 3: Execução Individual

```r
# 1. Configuração
source("config.R")

# 2. Instalação de pacotes
source("scripts/install_packages.R")

# 3. Preparação de dados
source("scripts/01_data_preparation.R")

# 4. Análise exploratória
source("scripts/02_exploratory_analysis.R")

# 5. Modelagem estatística
source("scripts/03_statistical_modeling.R")

# 6. Otimização do quinteto
source("scripts/04_team_optimization.R")

# 7. Simulação de batalhas
source("scripts/05_battle_simulation.R")
```

## 📊 O que o Projeto Faz

### 1. **Análise Exploratória** 🔍
- Estatísticas descritivas dos 151 Pokémon
- Distribuição de tipos e estatísticas
- Correlações entre atributos
- Visualizações interativas

### 2. **Modelagem Estatística** 🤖
- Random Forest para classificação
- Validação cruzada (5-fold)
- Métricas de performance
- Seleção de features

### 3. **Otimização do Quinteto** 🎯
- Algoritmo genético
- Função de fitness personalizada
- Balanceamento de tipos
- Cobertura de estatísticas

### 4. **Simulação de Batalhas** ⚔️
- Sistema de turnos realista
- Cálculo de dano baseado no Pokémon
- Vantagens de tipo
- Análise de performance

### 5. **Relatórios e Visualizações** 📈
- Gráficos de performance
- Tabelas de resultados
- Relatórios em Markdown
- Recomendações estratégicas

## 🎮 Resultados Esperados

### Quinteto Otimizado
- **5 Pokémon** selecionados automaticamente
- **Níveis recomendados** para cada um
- **Cobertura de tipos** balanceada
- **Estatísticas otimizadas**

### Análise de Performance
- **Taxa de vitória** contra cada membro
- **Estratégias** para cada Pokémon inimigo
- **Contadores** recomendados
- **Dificuldade** de cada membro

### Visualizações
- Gráficos de distribuição
- Matriz de correlação
- Performance por Pokémon
- Dificuldade por membro

## ⚠️ Solução de Problemas

### Erro: "Pacotes não encontrados"
```r
# Execute o script de instalação
source("scripts/install_packages.R")
```

### Erro: "Arquivos não encontrados"
```r
# Verifique a estrutura de diretórios
list.files(recursive = TRUE)
```

### Erro: "Memória insuficiente"
```r
# Reduza parâmetros em config.R
GA_POPULATION_SIZE <- 25  # Reduzir de 50 para 25
GA_MAX_ITERATIONS <- 50   # Reduzir de 100 para 50
```

### Erro: "Tempo de execução muito longo"
```r
# Ajuste parâmetros de convergência
RF_NTREE <- 100           # Reduzir de 500 para 100
CV_FOLDS <- 3             # Reduzir de 5 para 3
```

## 📱 Monitoramento da Execução

### Indicadores de Progresso
- ✅ **Configuração**: Diretórios criados
- 📦 **Pacotes**: Instalação verificada
- 📂 **Dados**: Arquivos carregados
- 🔍 **Análise**: Estatísticas calculadas
- 🤖 **Modelagem**: Modelos treinados
- 🎯 **Otimização**: Quinteto encontrado
- ⚔️ **Simulação**: Batalhas executadas
- 📊 **Relatório**: Resultados salvos

### Logs de Execução
- Console mostra progresso detalhado
- Arquivos salvos automaticamente
- Timestamps em cada etapa
- Verificação de erros

## 🎯 Personalização

### Modificar Parâmetros
```r
# Editar config.R
RF_NTREE <- 1000          # Mais árvores
GA_POPULATION_SIZE <- 100 # População maior
MIN_LEVEL <- 45           # Nível mínimo menor
MAX_LEVEL <- 75           # Nível máximo maior
```

### Adicionar Novos Pokémon
1. Editar `data/pokemon_data.csv`
2. Adicionar linha com dados do Pokémon
3. Reexecutar pipeline completo

### Modificar Elite dos 4
1. Editar `data/elite_four_data.csv`
2. Alterar Pokémon, tipos ou níveis
3. Reexecutar simulações

## 📚 Recursos Adicionais

### Documentação
- `docs/documentacao_tecnica.md` - Documentação técnica completa
- `README.md` - Visão geral do projeto
- Comentários detalhados em cada script

### Exemplos de Uso
- `exemplo_execucao.R` - Demonstração passo a passo
- Comandos úteis no final de cada script
- Funções para análise adicional

### Suporte
- Verificar logs de erro no console
- Consultar documentação técnica
- Verificar arquivos de configuração

## 🎉 Conclusão

Este projeto implementa uma solução completa e profissional para o problema do melhor quinteto Pokémon, utilizando:

- ✅ **Análise de dados** robusta
- ✅ **Machine Learning** avançado
- ✅ **Otimização** com algoritmos genéticos
- ✅ **Simulação** realista de batalhas
- ✅ **Visualizações** informativas
- ✅ **Relatórios** profissionais

**Boa sorte na Elite dos 4!** 🎮⚔️

---

*Projeto desenvolvido para o Case Técnico de Análise com R*
