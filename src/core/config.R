# Arquivo de Configuração do Projeto
# Projeto: Melhor Quinteto Pokémon para Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

# =============================================================================
# CONFIGURAÇÕES GERAIS
# =============================================================================

# Nome do projeto
PROJECT_NAME <- "Pokémon Elite dos 4 - Análise com R"

# Versão
PROJECT_VERSION <- "1.0.0"

# Autor
PROJECT_AUTHOR <- "Case Técnico de Análise com R"

# Data de criação
PROJECT_DATE <- "2024"

# =============================================================================
# CONFIGURAÇÕES DE DIRETÓRIOS
# =============================================================================

# Diretório raiz do projeto
PROJECT_ROOT <- getwd()

# Diretórios de dados
DATA_DIR <- file.path(PROJECT_ROOT, "data")
OUTPUT_DIR <- file.path(PROJECT_ROOT, "output")
DOCS_DIR <- file.path(PROJECT_ROOT, "docs")

# Subdiretórios de saída
PLOTS_DIR <- file.path(OUTPUT_DIR, "plots")
TABLES_DIR <- file.path(OUTPUT_DIR, "tables")
MODELS_DIR <- file.path(OUTPUT_DIR, "models")
REPORTS_DIR <- file.path(OUTPUT_DIR, "reports")

# =============================================================================
# CONFIGURAÇÕES DE DADOS
# =============================================================================

# Arquivos de dados
POKEMON_DATA_FILE <- file.path(DATA_DIR, "pokemon_data.csv")
ELITE_FOUR_DATA_FILE <- file.path(DATA_DIR, "elite_four_data.csv")

# Arquivos processados
POKEMON_PROCESSED_FILE <- file.path(DATA_DIR, "pokemon_processed.csv")
POKEMON_WITH_PREDICTIONS_FILE <- file.path(DATA_DIR, "pokemon_with_predictions.csv")

# =============================================================================
# CONFIGURAÇÕES DE MODELAGEM
# =============================================================================

# Parâmetros do Random Forest
RF_NTREE <- 500
RF_MTTRY <- 3
RF_NODESIZE <- 5

# Parâmetros do algoritmo genético
GA_POPULATION_SIZE <- 50
GA_MAX_ITERATIONS <- 100
GA_MUTATION_RATE <- 0.1
GA_CROSSOVER_RATE <- 0.8

# Parâmetros de validação cruzada
CV_FOLDS <- 5
CV_REPEATS <- 3

# =============================================================================
# CONFIGURAÇÕES DE SIMULAÇÃO
# =============================================================================

# Níveis mínimos e máximos para simulação
MIN_LEVEL <- 50
MAX_LEVEL <- 70
LEVEL_STEP <- 2

# Parâmetros de batalha
MAX_BATTLE_TURNS <- 20
DAMAGE_VARIATION_MIN <- 0.85
DAMAGE_VARIATION_MAX <- 1.0

# =============================================================================
# CONFIGURAÇÕES DE VISUALIZAÇÃO
# =============================================================================

# Tema padrão para gráficos
DEFAULT_THEME <- NULL  # Será definido após carregar ggplot2

# Cores padrão
COLOR_PALETTE <- c("#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7")

# Tamanhos padrão de gráficos
PLOT_WIDTH <- 10
PLOT_HEIGHT <- 8
PLOT_DPI <- 300

# =============================================================================
# CONFIGURAÇÕES DE RELATÓRIOS
# =============================================================================

# Formato de saída
OUTPUT_FORMAT <- "html_document"

# Configurações do knitr
KNITR_OPTS <- list(
  echo = TRUE,
  warning = FALSE,
  message = FALSE,
  fig.width = 10,
  fig.height = 8,
  dpi = 300
)

# =============================================================================
# FUNÇÕES DE CONFIGURAÇÃO
# =============================================================================

# Função para criar diretórios se não existirem
create_directories <- function() {
  dirs_to_create <- c(DATA_DIR, OUTPUT_DIR, DOCS_DIR,
                      PLOTS_DIR, TABLES_DIR, MODELS_DIR, REPORTS_DIR)
  
  for (dir in dirs_to_create) {
    if (!dir.exists(dir)) {
      dir.create(dir, recursive = TRUE, showWarnings = FALSE)
      cat("📁 Diretório criado:", dir, "\n")
    }
  }
}

# Função para verificar arquivos necessários
check_required_files <- function() {
  required_files <- c(POKEMON_DATA_FILE, ELITE_FOUR_DATA_FILE)
  missing_files <- c()
  
  for (file in required_files) {
    if (!file.exists(file)) {
      missing_files <- c(missing_files, file)
    }
  }
  
  if (length(missing_files) > 0) {
    cat("⚠️  Arquivos em falta:\n")
    for (file in missing_files) {
      cat("   -", file, "\n")
    }
    return(FALSE)
  } else {
    cat("✅ Todos os arquivos necessários encontrados!\n")
    return(TRUE)
  }
}

# Função para carregar configurações
load_config <- function() {
  cat("⚙️  Carregando configurações do projeto...\n")
  
  # Criar diretórios
  create_directories()
  
  # Verificar arquivos
  files_ok <- check_required_files()
  
  if (files_ok) {
    cat("✅ Configurações carregadas com sucesso!\n")
    return(TRUE)
  } else {
    cat("❌ Erro ao carregar configurações!\n")
    return(FALSE)
  }
}

# Função para obter informações do projeto
get_project_info <- function() {
  cat("🎮 ==========================================\n")
  cat("🎮", PROJECT_NAME, "\n")
  cat("🎮 Versão:", PROJECT_VERSION, "\n")
  cat("🎮 Autor:", PROJECT_AUTHOR, "\n")
  cat("🎮 Data:", PROJECT_DATE, "\n")
  cat("🎮 ==========================================\n\n")
  
  cat("📁 Diretórios do projeto:\n")
  cat("   - Raiz:", PROJECT_ROOT, "\n")
  cat("   - Dados:", DATA_DIR, "\n")
  cat("   - Documentação:", DOCS_DIR, "\n")
  cat("   - Saída:", OUTPUT_DIR, "\n")
  cat("   - Documentação:", DOCS_DIR, "\n\n")
  
  cat("⚙️  Configurações de modelagem:\n")
  cat("   - Random Forest:", RF_NTREE, "árvores\n")
  cat("   - Algoritmo Genético:", GA_POPULATION_SIZE, "indivíduos\n")
  cat("   - Validação Cruzada:", CV_FOLDS, "folds\n\n")
}

# =============================================================================
# EXECUÇÃO AUTOMÁTICA
# =============================================================================

# Carregar configurações automaticamente
if (interactive()) {
  load_config()
  get_project_info()
}

cat("🎮 Configurações do projeto carregadas!\n")
cat("🚀 Projeto pronto para execução!\n\n")
