# =============================================================================
# FUNÇÕES UTILITÁRIAS - PROJETO POKÉMON ELITE DOS 4
# =============================================================================
# Autor: Case Técnico de Análise com R
# Data: 2024
# Descrição: Funções utilitárias comuns usadas em todo o projeto

# =============================================================================
# FUNÇÕES DE DADOS
# =============================================================================

#' Função para carregar dados com tratamento de erros
#' @param file_path Caminho para o arquivo
#' @param file_type Tipo do arquivo (csv, rds, etc.)
#' @return Dataframe carregado
load_data_safe <- function(file_path, file_type = "csv") {
  tryCatch({
    if (file_type == "csv") {
      data <- read.csv(file_path, stringsAsFactors = FALSE)
    } else if (file_type == "rds") {
      data <- readRDS(file_path)
    } else {
      stop("Tipo de arquivo não suportado")
    }
    
    cat("✅ Dados carregados com sucesso:", file_path, "\n")
    cat("   Dimensões:", nrow(data), "x", ncol(data), "\n")
    
    return(data)
  }, error = function(e) {
    cat("❌ Erro ao carregar dados:", e$message, "\n")
    stop(e)
  })
}

#' Função para salvar dados com tratamento de erros
#' @param data Dados para salvar
#' @param file_path Caminho para salvar
#' @param file_type Tipo do arquivo
save_data_safe <- function(data, file_path, file_type = "csv") {
  tryCatch({
    dir.create(dirname(file_path), recursive = TRUE, showWarnings = FALSE)
    
    if (file_type == "csv") {
      write.csv(data, file_path, row.names = FALSE)
    } else if (file_type == "rds") {
      saveRDS(data, file_path)
    } else {
      stop("Tipo de arquivo não suportado")
    }
    
    cat("✅ Dados salvos com sucesso:", file_path, "\n")
  }, error = function(e) {
    cat("❌ Erro ao salvar dados:", e$message, "\n")
    stop(e)
  })
}

# =============================================================================
# FUNÇÕES DE VALIDAÇÃO
# =============================================================================

#' Verificar se uma coluna existe no dataframe
#' @param df Dataframe
#' @param col_name Nome da coluna
#' @return TRUE se existe, FALSE caso contrário
column_exists <- function(df, col_name) {
  return(col_name %in% names(df))
}

#' Verificar se uma coluna é numérica
#' @param df Dataframe
#' @param col_name Nome da coluna
#' @return TRUE se é numérica, FALSE caso contrário
is_numeric_column <- function(df, col_name) {
  if (!column_exists(df, col_name)) {
    return(FALSE)
  }
  return(is.numeric(df[[col_name]]))
}

#' Verificar se um dataframe tem as colunas necessárias
#' @param df Dataframe
#' @param required_cols Vetor com nomes das colunas necessárias
#' @return TRUE se todas existem, FALSE caso contrário
validate_required_columns <- function(df, required_cols) {
  missing_cols <- required_cols[!required_cols %in% names(df)]
  if (length(missing_cols) > 0) {
    cat("❌ Colunas em falta:", paste(missing_cols, collapse = ", "), "\n")
    return(FALSE)
  }
  return(TRUE)
}

# =============================================================================
# FUNÇÕES DE VISUALIZAÇÃO
# =============================================================================

#' Salvar gráfico com configurações padrão
#' @param plot Objeto ggplot
#' @param filename Nome do arquivo
#' @param width Largura
#' @param height Altura
#' @param dpi Resolução
save_plot_safe <- function(plot, filename, width = 10, height = 8, dpi = 300) {
  tryCatch({
    full_path <- file.path(PLOTS_DIR, filename)
    ggsave(full_path, plot, width = width, height = height, dpi = dpi)
    cat("✅ Gráfico salvo:", full_path, "\n")
  }, error = function(e) {
    cat("❌ Erro ao salvar gráfico:", e$message, "\n")
  })
}

#' Aplicar tema padrão aos gráficos
#' @param plot Objeto ggplot
#' @return ggplot com tema aplicado
apply_default_theme <- function(plot) {
  plot + 
    theme_minimal() +
    theme(
      plot.title = element_text(size = 14, face = "bold"),
      axis.title = element_text(size = 12),
      axis.text = element_text(size = 10),
      legend.title = element_text(size = 12),
      legend.text = element_text(size = 10)
    )
}

# =============================================================================
# FUNÇÕES DE MODELAGEM
# =============================================================================

#' Calcular métricas de performance do modelo
#' @param actual Valores reais
#' @param predicted Valores preditos
#' @return Lista com métricas
calculate_model_metrics <- function(actual, predicted) {
  # RMSE
  rmse <- sqrt(mean((actual - predicted)^2))
  
  # MAE
  mae <- mean(abs(actual - predicted))
  
  # R²
  ss_res <- sum((actual - predicted)^2)
  ss_tot <- sum((actual - mean(actual))^2)
  r_squared <- 1 - (ss_res / ss_tot)
  
  # MAPE
  mape <- mean(abs((actual - predicted) / actual)) * 100
  
  return(list(
    RMSE = rmse,
    MAE = mae,
    R_squared = r_squared,
    MAPE = mape
  ))
}

#' Salvar modelo com tratamento de erros
#' @param model Modelo para salvar
#' @param filename Nome do arquivo
save_model_safe <- function(model, filename) {
  tryCatch({
    full_path <- file.path(MODELS_DIR, filename)
    saveRDS(model, full_path)
    cat("✅ Modelo salvo:", full_path, "\n")
  }, error = function(e) {
    cat("❌ Erro ao salvar modelo:", e$message, "\n")
    stop(e)
  })
}

# =============================================================================
# FUNÇÕES DE LOG
# =============================================================================

#' Função para logging com timestamp
#' @param message Mensagem para log
#' @param level Nível do log (INFO, WARNING, ERROR)
log_message <- function(message, level = "INFO") {
  timestamp <- format(Sys.time(), "%Y-%m-%d %H:%M:%S")
  cat(sprintf("[%s] %s: %s\n", timestamp, level, message))
}

#' Função para logging de progresso
#' @param current Valor atual
#' @param total Valor total
#' @param message Mensagem adicional
log_progress <- function(current, total, message = "") {
  percentage <- round((current / total) * 100, 1)
  cat(sprintf("\r📊 Progresso: %d/%d (%s%%) %s", 
              current, total, percentage, message))
  if (current == total) cat("\n")
}

# =============================================================================
# FUNÇÕES DE LIMPEZA
# =============================================================================

#' Limpar variáveis temporárias
#' @param keep_vars Vetor com nomes de variáveis para manter
clean_environment <- function(keep_vars = c()) {
  all_vars <- ls(envir = .GlobalEnv)
  vars_to_remove <- all_vars[!all_vars %in% keep_vars]
  
  if (length(vars_to_remove) > 0) {
    rm(list = vars_to_remove, envir = .GlobalEnv)
    cat("🧹 Ambiente limpo. Variáveis mantidas:", paste(keep_vars, collapse = ", "), "\n")
  }
}

#' Função para verificar uso de memória
check_memory_usage <- function() {
  if (requireNamespace("pryr", quietly = TRUE)) {
    mem_usage <- pryr::mem_used()
    cat("💾 Uso de memória:", format(mem_usage, units = "MB"), "\n")
  }
}
