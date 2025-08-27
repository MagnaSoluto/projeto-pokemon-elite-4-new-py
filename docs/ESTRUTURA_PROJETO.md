# 🏗️ ESTRUTURA DO PROJETO POKÉMON ELITE DOS 4

## 🎯 Visão Geral

Este documento consolida **TODA** a informação sobre a estrutura e organização do projeto.

## 📁 Estrutura de Diretórios

```
Projeto_Final_PDA/
├── 🚀 main.R                    # Execução principal
├── 📦 src/                      # Código fonte organizado
│   ├── 🔧 core/                # Funcionalidades principais
│   │   ├── config.R           # Configurações
│   │   ├── setup.R            # Setup do ambiente
│   │   ├── 01_data_preparation.R
│   │   ├── 05_battle_simulation.R
│   │   ├── main_analysis.R    # Análise principal
│   │   └── exemplo_execucao.R # Exemplo de uso
│   ├── 🔍 analysis/            # Análises exploratórias
│   │   └── 02_exploratory_analysis.R
│   ├── 📊 models/              # Modelagem e otimização
│   │   ├── 03_statistical_modeling.R
│   │   └── 04_team_optimization.R
│   ├── 🛠️  utils/              # Funções utilitárias
│   │   ├── functions.R        # Funções comuns
│   │   ├── meu_pipeline.R     # Pipeline personalizado
│   │   ├── install_packages.R # Instalação de pacotes
│   │   └── test_structure.R   # Testes de estrutura
│   └── 📈 visualization/       # Visualizações (futuro)
├── 📊 data/                     # Dados do projeto
├── 📈 output/                   # Resultados e saídas
├── ⚙️  config/                  # Configurações
└── 📚 docs/                     # Documentação consolidada
    ├── apresentacao/            # Para apresentação
    ├── case-tecnico/            # Case técnico
    ├── relatorios/              # Relatórios finais
    └── ESTRUTURA_PROJETO.md    # Este arquivo
```

## 🚀 Como Usar

### **Execução Completa (Recomendado)**
```r
source('main.R')
```

### **Execução por Etapas**
```r
source('src/core/setup.R')           # Configurar ambiente
source('src/core/01_data_preparation.R')      # Preparar dados
source('src/analysis/02_exploratory_analysis.R')  # Análise exploratória
source('src/models/03_statistical_modeling.R')    # Modelagem
source('src/models/04_team_optimization.R')       # Otimização
source('src/core/05_battle_simulation.R')         # Simulação
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

## 📊 Benefícios da Estrutura

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

## 🧪 Validação

Para validar a estrutura:
```r
source('src/utils/test_structure.R')
```

## 📝 Notas Importantes

1. **Ordem de Execução**: Sempre execute `setup.R` antes de outros scripts
2. **Dependências**: O arquivo `main.R` executa tudo automaticamente
3. **Personalização**: Modifique `config.R` para ajustar parâmetros
4. **Testes**: Use `test_structure.R` para validar mudanças

---

*Estrutura consolidada e otimizada - Projeto Pokémon Elite dos 4*
