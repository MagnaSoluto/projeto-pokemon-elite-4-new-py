# =============================================================================
# CONFIGURAÇÃO DE AMBIENTE - PROJETO POKÉMON ELITE DOS 4
# =============================================================================
# Autor: Case Técnico de Análise com R
# Data: 2024
# Descrição: Configuração inicial do ambiente e carregamento de funções

# =============================================================================
# CONFIGURAÇÃO INICIAL
# =============================================================================

cat("🔧 Configurando ambiente do projeto...\n")

# Definir diretório de trabalho
if (!exists("PROJECT_ROOT")) {
  PROJECT_ROOT <- getwd()
}

# Carregar configurações
if (file.exists("src/core/config.R")) {
  source("src/core/config.R")
} else {
  cat("⚠️  Arquivo de configuração não encontrado. Usando configurações padrão.\n")
  
  # Configurações padrão
  PROJECT_ROOT <- getwd()
  DATA_DIR <- file.path(PROJECT_ROOT, "data")
  OUTPUT_DIR <- file.path(PROJECT_ROOT, "output")
  SCRIPTS_DIR <- file.path(PROJECT_ROOT, "src")
  DOCS_DIR <- file.path(PROJECT_ROOT, "docs")
  
  PLOTS_DIR <- file.path(OUTPUT_DIR, "plots")
  TABLES_DIR <- file.path(OUTPUT_DIR, "tables")
  MODELS_DIR <- file.path(OUTPUT_DIR, "models")
  REPORTS_DIR <- file.path(OUTPUT_DIR, "reports")
}

# =============================================================================
# CARREGAMENTO DE FUNÇÕES UTILITÁRIAS
# =============================================================================

cat("📦 Carregando funções utilitárias...\n")

# Carregar funções utilitárias
if (file.exists("src/utils/functions.R")) {
  source("src/utils/functions.R")
  cat("✅ Funções utilitárias carregadas\n")
} else {
  cat("⚠️  Arquivo de funções utilitárias não encontrado\n")
}

# Carregar pipeline personalizado
if (file.exists("src/utils/meu_pipeline.R")) {
  source("src/utils/meu_pipeline.R")
  cat("✅ Pipeline personalizado carregado\n")
} else {
  cat("⚠️  Pipeline personalizado não encontrado\n")
}

# =============================================================================
# VERIFICAÇÃO DE DIRETÓRIOS
# =============================================================================

cat("📁 Verificando estrutura de diretórios...\n")

# Lista de diretórios necessários
required_dirs <- c(
  DATA_DIR,
  OUTPUT_DIR,
  PLOTS_DIR,
  TABLES_DIR,
  MODELS_DIR,
  REPORTS_DIR
)

# Criar diretórios se não existirem
for (dir in required_dirs) {
  if (!dir.exists(dir)) {
    dir.create(dir, recursive = TRUE, showWarnings = FALSE)
    cat("   ✅ Criado:", dir, "\n")
  } else {
    cat("   ✅ Existe:", dir, "\n")
  }
}

# =============================================================================
# VERIFICAÇÃO DE ARQUIVOS DE DADOS
# =============================================================================

cat("📂 Verificando arquivos de dados...\n")

# Verificar arquivos de dados principais
data_files <- c(
  "pokemon_data.csv",
  "elite_four_data.csv"
)

for (file in data_files) {
  file_path <- file.path(DATA_DIR, file)
  if (file.exists(file_path)) {
    cat("   ✅ Dados encontrados:", file, "\n")
  } else {
    cat("   ⚠️  Dados não encontrados:", file, "\n")
  }
}

# =============================================================================
# CONFIGURAÇÃO DE OPÇÕES
# =============================================================================

cat("⚙️  Configurando opções do R...\n")

# Configurar opções para melhor performance
options(
  stringsAsFactors = FALSE,
  scipen = 999,
  digits = 4,
  warn = 1
)

# Configurar tema padrão para gráficos (será aplicado quando ggplot2 for carregado)
if (requireNamespace("ggplot2", quietly = TRUE)) {
  theme_set(theme_minimal())
  cat("   ✅ Tema padrão configurado para gráficos\n")
}

# =============================================================================
# VERIFICAÇÃO DE MEMÓRIA
# =============================================================================

cat("💾 Verificando recursos do sistema...\n")

# Verificar memória disponível
if (requireNamespace("pryr", quietly = TRUE)) {
  mem_available <- pryr::mem_used()
  cat("   📊 Memória em uso:", format(mem_available, units = "MB"), "\n")
}

# Verificar número de cores disponíveis
cores_available <- parallel::detectCores()
cat("   🔧 Cores disponíveis:", cores_available, "\n")

# =============================================================================
# MENSAGEM DE CONCLUÇÃO
# =============================================================================

cat("\n🎯 Ambiente configurado com sucesso!\n")
cat("📁 Diretório de trabalho:", getwd(), "\n")
cat("📊 Diretório de dados:", DATA_DIR, "\n")
cat("📈 Diretório de saída:", OUTPUT_DIR, "\n")
cat("🔧 Diretório de scripts:", SCRIPTS_DIR, "\n")

cat("\n💡 Para executar o projeto completo, use:\n")
cat("   source('main.R')\n\n")

cat("💡 Para executar etapas individuais, use:\n")
cat("   source('src/core/01_data_preparation.R')\n")
cat("   source('src/analysis/02_exploratory_analysis.R')\n")
cat("   source('src/models/03_statistical_modeling.R')\n")
cat("   source('src/models/04_team_optimization.R')\n")
cat("   source('src/core/05_battle_simulation.R')\n\n")
