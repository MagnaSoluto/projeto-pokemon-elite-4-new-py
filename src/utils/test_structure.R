# =============================================================================
# TESTES DE ESTRUTURA - PROJETO POKÉMON ELITE DOS 4
# =============================================================================
# Autor: Case Técnico de Análise com R
# Data: 2024
# Descrição: Testes para validar a estrutura e funcionalidades do projeto

# =============================================================================
# FUNÇÃO PRINCIPAL DE TESTE
# =============================================================================

#' Executar todos os testes de estrutura
#' @return TRUE se todos os testes passaram, FALSE caso contrário
run_structure_tests <- function() {
  cat("🧪 ==========================================\n")
  cat("🧪 EXECUTANDO TESTES DE ESTRUTURA\n")
  cat("🧪 ==========================================\n\n")
  
  test_results <- list()
  
  # Teste 1: Estrutura de diretórios
  test_results$directories <- test_directory_structure()
  
  # Teste 2: Arquivos de código
  test_results$code_files <- test_code_files()
  
  # Teste 3: Arquivos de dados
  test_results$data_files <- test_data_files()
  
  # Teste 4: Funções utilitárias
  test_results$utility_functions <- test_utility_functions()
  
  # Teste 5: Configurações
  test_results$configurations <- test_configurations()
  
  # Resumo dos resultados
  print_test_summary(test_results)
  
  # Retornar TRUE se todos os testes passaram
  all_passed <- all(unlist(test_results))
  return(all_passed)
}

# =============================================================================
# TESTES INDIVIDUAIS
# =============================================================================

#' Testar estrutura de diretórios
#' @return TRUE se passou, FALSE caso contrário
test_directory_structure <- function() {
  cat("📁 Testando estrutura de diretórios...\n")
  
  required_dirs <- c(
    "src",
    "src/core",
    "src/analysis", 
    "src/models",
    "src/utils",
    "src/visualization",
    "data",
    "output",
    "output/plots",
    "output/tables",
    "output/models",
    "output/reports",
    "docs"
  )
  
  missing_dirs <- c()
  for (dir in required_dirs) {
    if (!dir.exists(dir)) {
      missing_dirs <- c(missing_dirs, dir)
    }
  }
  
  if (length(missing_dirs) > 0) {
    cat("   ❌ Diretórios em falta:", paste(missing_dirs, collapse = ", "), "\n")
    return(FALSE)
  } else {
    cat("   ✅ Todos os diretórios necessários existem\n")
    return(TRUE)
  }
}

#' Testar arquivos de código
#' @return TRUE se passou, FALSE caso contrário
test_code_files <- function() {
  cat("📝 Testando arquivos de código...\n")
  
  required_files <- c(
    "main.R",
    "src/core/config.R",
    "src/core/setup.R",
    "src/core/01_data_preparation.R",
    "src/core/05_battle_simulation.R",
    "src/core/main_analysis.R",
    "src/analysis/02_exploratory_analysis.R",
    "src/models/03_statistical_modeling.R",
    "src/models/04_team_optimization.R",
    "src/utils/install_packages.R",
    "src/utils/functions.R",
    "src/utils/meu_pipeline.R"
  )
  
  missing_files <- c()
  for (file in required_files) {
    if (!file.exists(file)) {
      missing_files <- c(missing_files, file)
    }
  }
  
  if (length(missing_files) > 0) {
    cat("   ❌ Arquivos em falta:", paste(missing_files, collapse = ", "), "\n")
    return(FALSE)
  } else {
    cat("   ✅ Todos os arquivos de código existem\n")
    return(TRUE)
  }
}

#' Testar arquivos de dados
#' @return TRUE se passou, FALSE caso contrário
test_data_files <- function() {
  cat("📊 Testando arquivos de dados...\n")
  
  required_data_files <- c(
    "data/pokemon_data.csv",
    "data/elite_four_data.csv"
  )
  
  missing_data <- c()
  for (file in required_data_files) {
    if (!file.exists(file)) {
      missing_data <- c(missing_data, file)
    }
  }
  
  if (length(missing_data) > 0) {
    cat("   ⚠️  Arquivos de dados em falta:", paste(missing_data, collapse = ", "), "\n")
    cat("   ℹ️  Isso pode afetar a execução, mas não impede os testes de estrutura\n")
    return(TRUE) # Não é crítico para a estrutura
  } else {
    cat("   ✅ Todos os arquivos de dados existem\n")
    return(TRUE)
  }
}

#' Testar funções utilitárias
#' @return TRUE se passou, FALSE caso contrário
test_utility_functions <- function() {
  cat("🔧 Testando funções utilitárias...\n")
  
  # Tentar carregar funções
  tryCatch({
    source("src/utils/functions.R")
    cat("   ✅ Funções utilitárias carregadas com sucesso\n")
    return(TRUE)
  }, error = function(e) {
    cat("   ❌ Erro ao carregar funções utilitárias:", e$message, "\n")
    return(FALSE)
  })
}

#' Testar configurações
#' @return TRUE se passou, FALSE caso contrário
test_configurations <- function() {
  cat("⚙️  Testando configurações...\n")
  
  # Tentar carregar configurações
  tryCatch({
    source("src/core/config.R")
    cat("   ✅ Configurações carregadas com sucesso\n")
    return(TRUE)
  }, error = function(e) {
    cat("   ❌ Erro ao carregar configurações:", e$message, "\n")
    return(FALSE)
  })
}

# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================

#' Imprimir resumo dos testes
#' @param test_results Lista com resultados dos testes
print_test_summary <- function(test_results) {
  cat("\n📋 ==========================================\n")
  cat("📋 RESUMO DOS TESTES\n")
  cat("📋 ==========================================\n")
  
  total_tests <- length(test_results)
  passed_tests <- sum(unlist(test_results))
  failed_tests <- total_tests - passed_tests
  
  cat("📊 Total de testes:", total_tests, "\n")
  cat("✅ Testes aprovados:", passed_tests, "\n")
  cat("❌ Testes reprovados:", failed_tests, "\n")
  
  if (failed_tests == 0) {
    cat("\n🎉 Todos os testes passaram! Estrutura do projeto está correta.\n")
  } else {
    cat("\n⚠️  Alguns testes falharam. Verifique a estrutura do projeto.\n")
  }
  
  cat("\n")
}

#' Testar execução básica dos scripts
#' @return TRUE se passou, FALSE caso contrário
test_script_execution <- function() {
  cat("🚀 Testando execução básica dos scripts...\n")
  
  # Testar apenas o setup (sem executar análises completas)
  tryCatch({
    source("src/core/setup.R")
    cat("   ✅ Setup executado com sucesso\n")
    return(TRUE)
  }, error = function(e) {
    cat("   ❌ Erro no setup:", e$message, "\n")
    return(FALSE)
  })
}

# =============================================================================
# EXECUÇÃO AUTOMÁTICA
# =============================================================================

# Se este arquivo for executado diretamente, rodar os testes
if (!exists("TESTING_MODE")) {
  TESTING_MODE <- TRUE
  run_structure_tests()
}
