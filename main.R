#!/usr/bin/env Rscript
# =============================================================================
# ARQUIVO PRINCIPAL DE EXECUÇÃO - PROJETO POKÉMON ELITE DOS 4
# =============================================================================
# Autor: Case Técnico de Análise com R
# Data: 2024
# Descrição: Arquivo principal que executa todo o pipeline de análise

cat("🎮 ==========================================\n")
cat("🎮 PROJETO POKÉMON ELITE DOS 4\n")
cat("🎮 Análise com R - Execução Principal\n")
cat("🎮 ==========================================\n\n")

# =============================================================================
# CONFIGURAÇÃO INICIAL
# =============================================================================

cat("⚙️  Carregando configurações...\n")
source("src/core/config.R")

# Verificar e criar diretórios necessários
cat("📁 Verificando estrutura de diretórios...\n")
dirs_to_create <- c(DATA_DIR, OUTPUT_DIR, PLOTS_DIR, TABLES_DIR, MODELS_DIR, REPORTS_DIR)
for (dir in dirs_to_create) {
  if (!dir.exists(dir)) {
    dir.create(dir, recursive = TRUE)
    cat("   ✅ Criado:", dir, "\n")
  }
}

# =============================================================================
# INSTALAÇÃO DE PACOTES
# =============================================================================

cat("\n📦 Verificando e instalando pacotes...\n")
source("src/utils/install_packages.R")

# =============================================================================
# EXECUÇÃO DO PIPELINE COMPLETO
# =============================================================================

cat("\n🚀 Iniciando execução do pipeline completo...\n")

# Etapa 1: Preparação dos dados
cat("\n📂 ETAPA 1: Preparação dos Dados\n")
cat("================================\n")
source("src/core/01_data_preparation.R")

# Etapa 2: Análise exploratória
cat("\n🔍 ETAPA 2: Análise Exploratória\n")
cat("================================\n")
source("src/analysis/02_exploratory_analysis.R")

# Etapa 3: Modelagem estatística
cat("\n📊 ETAPA 3: Modelagem Estatística\n")
cat("==================================\n")
source("src/models/03_statistical_modeling.R")

# Etapa 4: Otimização de equipe
cat("\n⚔️  ETAPA 4: Otimização de Equipe\n")
cat("==================================\n")
source("src/models/04_team_optimization.R")

# Etapa 5: Simulação de batalhas
cat("\n🎯 ETAPA 5: Simulação de Batalhas\n")
cat("==================================\n")
source("src/core/05_battle_simulation.R")

# =============================================================================
# RELATÓRIO FINAL
# =============================================================================

cat("\n📋 ETAPA 6: Geração de Relatórios\n")
cat("==================================\n")

# Executar análise principal que gera relatórios
source("src/core/main_analysis.R")

cat("\n🎉 ==========================================\n")
cat("🎉 EXECUÇÃO CONCLUÍDA COM SUCESSO!\n")
cat("🎉 ==========================================\n")
cat("\n📁 Resultados disponíveis em:\n")
cat("   - Gráficos:", PLOTS_DIR, "\n")
cat("   - Tabelas:", TABLES_DIR, "\n")
cat("   - Modelos:", MODELS_DIR, "\n")
cat("   - Relatórios:", REPORTS_DIR, "\n")
cat("\n💡 Para executar etapas individuais, use os arquivos específicos em src/\n")
