# 🚀 Guia de Instalação e Execução

## 📋 Pré-requisitos

### 🔧 **Sistema Operacional**
- **Windows**: Windows 10 ou superior
- **macOS**: macOS 10.14 ou superior  
- **Linux**: Ubuntu 18.04+ ou distribuições equivalentes

### 📊 **R e RStudio**
- **R**: Versão 4.0 ou superior
  - Download: https://www.r-project.org/
  - Verificar versão: `R --version`
- **RStudio** (opcional, mas recomendado)
  - Download: https://www.rstudio.com/

## 🎯 Instalação Rápida

### **1. Clonar o Repositório**
```bash
git clone https://github.com/MagnaSoluto/projeto-pokemon-elite-4.git
cd projeto-pokemon-elite-4
```

### **2. Executar o Projeto**
```bash
# Opção 1: Execução completa (recomendado)
Rscript main.R

# Opção 2: No R/RStudio
source('main.R')
```

## 🔍 Verificação de Configuração

### **Testar se tudo está funcionando:**
```bash
Rscript test_setup.R
```

Este script verifica:
- ✅ Versão do R
- ✅ Arquivos de dados
- ✅ Estrutura de diretórios
- ✅ Pacotes R necessários
- ✅ Carregamento de dados

## 📦 Instalação Manual de Pacotes

Se houver problemas com pacotes, execute:

```r
# No R ou RStudio
source('src/utils/install_packages.R')
```

### **Pacotes Necessários:**
- **Análise**: dplyr, tidyr, readr, stringr
- **Visualização**: ggplot2, viridis, RColorBrewer
- **Machine Learning**: caret, randomForest, glmnet
- **Otimização**: GA
- **Relatórios**: knitr, kableExtra

## 🎮 Execução por Etapas

### **Pipeline Completo:**
```r
source('main.R')
```

### **Etapas Individuais:**
```r
# 1. Preparação de dados
source('src/core/01_data_preparation.R')

# 2. Análise exploratória
source('src/analysis/02_exploratory_analysis.R')

# 3. Modelagem estatística
source('src/models/03_statistical_modeling.R')

# 4. Otimização de equipe
source('src/models/04_team_optimization.R')

# 5. Simulação de batalhas
source('src/core/05_battle_simulation.R')
```

### **Case Técnico (41 perguntas):**
```r
source('docs/case-tecnico/CASE_TECNICO_41_PERGUNTAS.R')
```

## 📁 Estrutura do Projeto

```
projeto-pokemon-elite-4/
├── 📊 data/                    # Dados originais
│   ├── pokemon_data.csv        # 151 Pokémon
│   └── elite_four_data.csv     # Elite dos 4
├── 🎯 src/                     # Código fonte
│   ├── core/                   # Scripts principais
│   ├── analysis/               # Análise exploratória
│   ├── models/                 # Modelagem e otimização
│   └── utils/                  # Funções utilitárias
├── 📈 output/                  # Resultados gerados
│   ├── plots/                  # Gráficos (15 arquivos)
│   ├── tables/                 # Tabelas de dados
│   ├── models/                 # Modelos treinados
│   └── reports/                # Relatórios
├── 📚 docs/                    # Documentação
├── 🚀 main.R                   # Execução principal
└── 🔍 test_setup.R             # Verificação de setup
```

## ⚠️ Solução de Problemas

### **Erro: "package not found"**
```r
# Instalar pacotes manualmente
install.packages(c("dplyr", "ggplot2", "caret", "GA"))
```

### **Erro: "file not found"**
- Verificar se está no diretório correto
- Executar `pwd` (Linux/Mac) ou `cd` (Windows)
- Deve estar em: `projeto-pokemon-elite-4/`

### **Erro: "permission denied"**
```bash
# Linux/Mac: Dar permissão de execução
chmod +x main.R
chmod +x test_setup.R
```

### **Erro de memória**
- Fechar outros programas
- Aumentar memória do R: `memory.limit(size = 8000)`

## 🎯 Resultados Esperados

### **Arquivos Gerados:**
- **15 gráficos** em `output/plots/`
- **15 tabelas** em `output/tables/`
- **3 modelos** em `output/models/`
- **Relatórios** em `output/reports/`

### **Quinteto Otimizado:**
1. **Victreebel** (Grass/Poison) - 84.6% vitórias
2. **Magneton** (Electric/Steel) - 73.1% vitórias  
3. **Mr. Mime** (Psychic/Fairy) - 42.3% vitórias
4. **Ponyta** (Fire) - 57.7% vitórias
5. **Butterfree** (Bug/Flying) - 38.5% vitórias

### **Taxa de Vitória:** 59.2% (130 batalhas simuladas)

## 📞 Suporte

### **Problemas Comuns:**
1. **R não encontrado**: Adicionar R ao PATH do sistema
2. **Pacotes não instalam**: Verificar conexão com internet
3. **Erro de encoding**: Usar UTF-8 no sistema

### **Contato:**
- **Issues**: [GitHub Issues](https://github.com/MagnaSoluto/projeto-pokemon-elite-4/issues)
- **Documentação**: [docs/](docs/)

## ✅ Checklist de Instalação

- [ ] R 4.0+ instalado
- [ ] Repositório clonado
- [ ] `test_setup.R` executado com sucesso
- [ ] `main.R` executado sem erros
- [ ] Arquivos gerados em `output/`
- [ ] Quinteto otimizado identificado

---

**🎮 Projeto 100% funcional e testado!**

*Desenvolvido com ❤️ e R*
