# 🎮 Projeto Pokémon Elite dos 4 - Análise com R

[![R](https://img.shields.io/badge/R-4.5.1+-blue.svg)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Concluído-success.svg)](https://github.com/MagnaSoluto/projeto-pokemon-elite-4.git)

## 📋 Descrição

Este projeto resolve o desafio estratégico de **determinar qual é o melhor quinteto de Pokémon e em qual nível para vencer a Elite dos 4 nos jogos Pokémon Red/Green**. 

Utilizando técnicas avançadas de **análise de dados**, **modelagem estatística**, **otimização com algoritmos genéticos** e **simulação de batalhas**, o projeto identifica a combinação ideal de 5 Pokémon para maximizar a taxa de vitória contra todos os membros da Elite dos 4.

## 🎯 Objetivos

- ✅ **Análise Exploratória**: Compreender estatísticas e tipos dos 151 Pokémon
- ✅ **Modelagem Estatística**: Criar modelos para avaliar eficácia de combinações
- ✅ **Otimização**: Encontrar o quinteto ideal usando algoritmos genéticos
- ✅ **Simulação**: Testar estratégias contra todos os membros da Elite dos 4
- ✅ **Validação**: Confirmar a eficácia do time otimizado

## 🏆 Quinteto Otimizado Encontrado

### 🥇 Time Recomendado

| Posição | Pokémon | Tipo | Total | Nível Recomendado |
|----------|---------|------|-------|-------------------|
| 1 | **Mr. Mime** | Psychic/Fairy | 460 | 71-75 |
| 2 | **Ponyta** | Fire | 410 | 69-73 |
| 3 | **Butterfree** | Bug/Flying | 395 | 68-72 |
| 4 | **Victreebel** | Grass/Poison | 490 | 73-77 |
| 5 | **Magneton** | Electric/Steel | 465 | 71-75 |

### 📊 Performance do Time
- **Score de Otimização**: 3.1833
- **Taxa de Vitória Geral**: 63.2%
- **Cobertura de Tipos**: 38.5%
- **Total de Estatísticas**: 2,220

## 🚀 Como Executar

### 📦 Pré-requisitos
- R 4.5.1 ou superior
- RStudio (recomendado)

### 🔧 Instalação e Execução

1. **Clone o repositório**
```bash
git clone https://github.com/MagnaSoluto/projeto-pokemon-elite-4.git
cd Projeto_Final_PDAprojeto-pokemon-elite-4
```

2. **Execute o pipeline completo**
```r
# No R ou RStudio
source('main.R')
```

3. **Ou execute etapas individuais**
```r
# Preparação de dados
source('src/core/01_data_preparation.R')

# Análise exploratória
source('src/analysis/02_exploratory_analysis.R')

# Modelagem estatística
source('src/models/03_statistical_modeling.R')

# Otimização de equipe
source('src/models/04_team_optimization.R')

# Simulação de batalhas
source('src/core/05_battle_simulation.R')
```

4. **Para o Case Técnico (41 perguntas)**
```r
# Execute o notebook das 41 perguntas
source('docs/case-tecnico/CASE_TECNICO_41_PERGUNTAS.R')
```

## 📁 Estrutura do Projeto

```
Projeto_Final_PDA/
├── 📊 data/                          # Datasets originais e processados
│   ├── pokemon_data.csv              # Dataset principal dos Pokémon
│   ├── elite_four_data.csv           # Dados da Elite dos 4
│   ├── pokemon_processed.csv         # Dados processados
│   └── pokemon_with_predictions.csv  # Dados com predições
├── 🎯 src/                           # Código fonte
│   ├── core/                         # Scripts principais
│   ├── analysis/                     # Análise exploratória
│   ├── models/                       # Modelagem e otimização
│   └── utils/                        # Utilitários e funções
├── 📈 output/                        # Resultados gerados
│   ├── plots/                        # Gráficos e visualizações
│   ├── tables/                       # Tabelas de dados
│   ├── models/                       # Modelos treinados
│   └── reports/                      # Relatórios gerados
├── 📚 docs/                          # Documentação
│   ├── case-tecnico/                 # Case técnico (41 perguntas)
│   └── apresentacao/                 # Apresentações
├── 🎮 main.R                         # Script principal de execução
└── 📖 README.md                      # Este arquivo
```

## 📊 Resultados Principais

### 🔍 Análise Exploratória
- **15 visualizações** geradas automaticamente
- **Análise de correlações** entre todas as estatísticas
- **Distribuições** por tipos e poder
- **Rankings** dos melhores Pokémon por critérios

### 🤖 Modelagem Estatística
- **4 modelos** treinados e comparados
- **Regressão Linear** como melhor modelo (R² = 0.9988)
- **Random Forest** para análise de importância de variáveis
- **Validação cruzada** para robustez

### ⚔️ Simulação de Batalhas
- **125 batalhas** simuladas contra todos os membros
- **Análise de dificuldade** por membro da Elite dos 4
- **Estratégias específicas** para cada oponente
- **Recomendações de níveis** otimizados

## 📈 Visualizações Geradas

| Gráfico | Descrição |
|---------|-----------|
| `pokemon_performance.png` | Performance de cada Pokémon |
| `member_difficulty.png` | Dificuldade de cada membro |
| `team_radar.png` | Radar do time otimizado |
| `type_distribution.png` | Distribuição por tipos |
| `correlation_matrix.png` | Matriz de correlações |
| `stats_distribution.png` | Distribuição das estatísticas |

## 🎓 Case Técnico - 41 Perguntas

O projeto inclui um **notebook R completo** que responde às 41 perguntas do case técnico:

- 📋 **Perguntas 1-10**: Importação e verificação de dados
- 📊 **Perguntas 11-25**: Análise estatística e correlações
- 📈 **Perguntas 26-41**: Visualizações e análises por tipo

**Para executar**: `source('docs/case-tecnico/CASE_TECNICO_41_PERGUNTAS.R')`

## 🔧 Tecnologias Utilizadas

- **R**: Linguagem principal de análise
- **ggplot2**: Visualizações avançadas
- **caret**: Machine Learning e validação
- **randomForest**: Modelagem preditiva
- **GA**: Algoritmos genéticos para otimização
- **dplyr/tidyr**: Manipulação de dados
- **knitr/kableExtra**: Relatórios e tabelas

## 📊 Métricas de Performance

| Métrica | Valor |
|---------|-------|
| **Taxa de Vitória Geral** | 63.2% |
| **Membro Mais Difícil** | Champion (48%) |
| **Membro Mais Fácil** | Bruno (80%) |
| **Melhor Pokémon** | Victreebel (88%) |
| **Total de Batalhas** | 125 |

## 🎯 Estratégias Recomendadas

### 🏆 Melhores Contadores
- **Aerodactyl** → Use **Victreebel** (Nível 75, 1 turno)
- **Alakazam** → Use **Victreebel** (Nível 75, 1 turno)
- **Gengar** → Use **Victreebel** (Nível 75, 1 turno)
- **Dragonite** → Use **Victreebel** (Nível 75, 0 turnos)

### 💡 Dicas de Batalha
1. **Victreebel** é o MVP do time (88% vitórias)
2. **Magneton** excelente contra tipos voadores
3. **Ponyta** forte contra tipos bug e grass
4. **Mr. Mime** bom suporte com ataques especiais
5. **Butterfree** útil para status e cobertura

## 📋 Relatórios Gerados

- **Relatório Executivo**: Resumo das principais descobertas
- **Relatório Técnico**: Detalhes da metodologia e resultados
- **Relatório de Batalhas**: Análise completa das simulações
- **Relatório de Otimização**: Processo de seleção do quinteto

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autores
**Adriano Carvalho dos Santos** (RA: 10747203)  
**Jonathas William Freire Borges** (RA: 10747100)

**Case Técnico de Análise com R** - 2025 *MBA em Engenharia de Dados - Universidade Presbiteriana Mackenzie*

## 🙏 Agradecimentos

- Nintendo/Game Freak pelos dados dos Pokémon
- Comunidade R por ferramentas incríveis
- Professor Jonn Martins pelo apoio

## 📞 Suporte

Para dúvidas ou sugestões:
- 📧 Abra uma [Issue](../../issues)
- 💬 Entre em contato via [Discussions](../../discussions)
- 📖 Consulte a [documentação](docs/)

---

## 🎮 Status do Projeto

- ✅ **Análise Exploratória**: Concluída
- ✅ **Modelagem Estatística**: Concluída  
- ✅ **Otimização do Quinteto**: Concluída
- ✅ **Simulação de Batalhas**: Concluída
- ✅ **Case Técnico (41 perguntas)**: Concluído
- ✅ **Relatórios e Visualizações**: Concluídos

**🎉 PROJETO 100% FUNCIONAL E CONCLUÍDO!**

---

<div align="center">

**⚔️ Que o melhor treinador vença na Elite dos 4! ⚔️**

*Projeto desenvolvido com ❤️ e R*

</div>
