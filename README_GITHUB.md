# 🎮 Pokémon Elite dos 4 - Análise com R

[![R](https://img.shields.io/badge/R-4.0+-blue.svg)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen.svg)](https://github.com/MagnaSoluto/projeto-pokemon-elite-4)
[![Última Atualização](https://img.shields.io/badge/Última%20Atualização-Dezembro%202024-orange.svg)](https://github.com/seu-usuario/projeto-pokemon/commits/main)

## 🎯 Sobre o Projeto

Este projeto utiliza **análise de dados avançada** e **machine learning** em R para determinar o **melhor quinteto de Pokémon** e o **nível ideal** para vencer a Elite dos 4 nos jogos Pokémon Red/Green.

### 🌟 Características Principais

- 🧠 **Machine Learning**: Algoritmos de predição e otimização
- 📊 **Análise Exploratória**: Visualizações e estatísticas avançadas
- ⚔️ **Otimização**: Algoritmos genéticos para equipes ideais
- 🎮 **Simulação**: Batalhas Pokémon com diferentes configurações
- 📈 **Relatórios**: Geração automática de resultados

## 🚀 Começando Rápido

### **Execução Completa (Recomendado)**
```r
# Clone o repositório
git clone https://github.com/MagnaSoluto/projeto-pokemon-elite-4.git
cd projeto-pokemon-elite-4

# Execute o projeto completo
source('main.R')
```

### **Execução por Etapas**
```r
# 1. Configurar ambiente
source('src/core/setup.R')

# 2. Executar etapas individuais
source('src/core/01_data_preparation.R')      # Preparar dados
source('src/analysis/02_exploratory_analysis.R')  # Análise exploratória
source('src/models/03_statistical_modeling.R')    # Modelagem
source('src/models/04_team_optimization.R')       # Otimização
source('src/core/05_battle_simulation.R')         # Simulação
```

## 📁 Estrutura do Projeto

```
Projeto_Final_PDA/
├── 🚀 main.R                    # Execução principal
├── 📦 src/                      # Código fonte organizado
│   ├── 🔧 core/                # Funcionalidades principais
│   ├── 🔍 analysis/            # Análises exploratórias
│   ├── 📊 models/              # Modelagem e otimização
│   └── 🛠️  utils/              # Funções utilitárias
├── 📊 data/                     # Dados do projeto
├── 📈 output/                   # Resultados e saídas
├── ⚙️  config/                  # Configurações
└── 📚 docs/                     # Documentação completa
```

## 🛠️ Tecnologias Utilizadas

### **Linguagem Principal**
- **R** - Análise estatística e machine learning

### **Pacotes Principais**
- **Análise de Dados**: `dplyr`, `tidyr`, `readr`
- **Visualização**: `ggplot2`, `plotly`, `corrplot`
- **Machine Learning**: `caret`, `randomForest`, `glmnet`
- **Otimização**: `GA` (Algoritmos Genéticos)
- **Relatórios**: `rmarkdown`, `knitr`

### **Ferramentas**
- **Git** - Controle de versão
- **GitHub** - Repositório remoto
- **RStudio** - IDE recomendado

## 📊 Funcionalidades

### **🔍 Análise Exploratória**
- Estatísticas descritivas dos Pokémon
- Análise de correlações entre atributos
- Distribuição de tipos e habilidades
- Visualizações interativas

### **🤖 Modelagem**
- Predição de performance em batalhas
- Análise de eficácia por tipo
- Modelos de machine learning
- Validação cruzada

### **⚔️ Otimização**
- Algoritmos genéticos para equipes
- Seleção de melhores combinações
- Análise de sinergias entre Pokémon
- Recomendações de níveis

### **🎮 Simulação**
- Simulação de batalhas
- Cálculo de danos e eficácia
- Estratégias de combate
- Análise de resultados

## 📈 Resultados

Os resultados são salvos automaticamente em:
- **📊 Gráficos**: `output/plots/`
- **📋 Tabelas**: `output/tables/`
- **🤖 Modelos**: `output/models/`
- **📄 Relatórios**: `output/reports/`

## 🧪 Testes

```r
# Validar estrutura do projeto
source('src/utils/test_structure.R')
```

## 📚 Documentação

- **[📖 Estrutura do Código](docs/estrutura/ESTRUTURA_CODIGO.md)** - Organização do projeto
- **[🔧 Instruções de Execução](docs/execucao/INSTRUCOES_EXECUCAO.md)** - Como usar
- **[📊 Case Técnico](docs/projeto/case_técnico_análise_com_R.pdf)** - Documentação completa
- **[📋 Índice de Documentos](docs/projeto/INDICE_DOCUMENTOS.md)** - Navegação

## 🚀 Instalação

### **Pré-requisitos**
- R (versão 4.0+)
- RStudio (recomendado)
- Git

### **Passos**
1. **Clone o repositório**
   ```bash
   git clone https://github.com/MagnaSoluto/projeto-pokemon-elite-4.git
   cd projeto-pokemon-elite-4
   ```

2. **Instale as dependências**
   ```r
   source('src/utils/install_packages.R')
   ```

3. **Execute o projeto**
   ```r
   source('main.R')
   ```

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

## 📝 Licença

Este projeto é parte do **Case Técnico de Análise com R** - 2024

## 👥 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Contato

- **Autor**: Adriano Santos
- **Email**: adriano.santos@magnasoluto.com.br
- **Projeto**: Case Técnico de Análise com R

## 🙏 Agradecimentos

- Bulbapedia pelos dados dos Pokémon
- Comunidade R por ferramentas incríveis
- Professores e colegas pelo apoio

---

**⭐ Se este projeto te ajudou, considere dar uma estrela no GitHub!**

**🎯 Objetivo**: Demonstrar habilidades em análise de dados, machine learning e programação em R através de um projeto prático e divertido sobre Pokémon!
