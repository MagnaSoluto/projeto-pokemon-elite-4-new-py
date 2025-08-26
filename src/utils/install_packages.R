# Script de instalação de pacotes R para o projeto Pokémon Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

cat("🎮 Instalando pacotes necessários para o projeto Pokémon Elite dos 4...\n\n")

# Lista de pacotes necessários
packages <- c(
  # Análise de dados
  "dplyr", "tidyr", "readr", "stringr", "purrr",
  
  # Visualização
  "ggplot2", "plotly", "corrplot", "ggpubr", "ggcorrplot",
  
  # Modelagem estatística
  "caret", "randomForest", "glmnet", "e1071", "rpart",
  
  # Otimização
  "ROI", "ompr", "GA",
  
  # Manipulação de dados
  "data.table", "reshape2",
  
  # Relatórios
  "rmarkdown", "knitr", "kableExtra",
  
  # Utilitários
  "scales", "viridis", "RColorBrewer"
)

# Função para instalar pacotes
install_if_missing <- function(package_name) {
  if (!require(package_name, character.only = TRUE, quietly = TRUE)) {
    cat("📦 Instalando", package_name, "...\n")
    # Definir mirror do CRAN
    options(repos = c(CRAN = "https://cloud.r-project.org"))
    install.packages(package_name, dependencies = TRUE)
    cat("✅", package_name, "instalado com sucesso!\n")
  } else {
    cat("✅", package_name, "já está instalado\n")
  }
}

# Instalar cada pacote
cat("🔍 Verificando e instalando pacotes...\n\n")

for (package in packages) {
  install_if_missing(package)
}

cat("\n🎉 Instalação de pacotes concluída!\n")
cat("📊 Todos os pacotes necessários estão disponíveis para uso.\n\n")

# Verificar se todos os pacotes foram instalados corretamente
cat("🔍 Verificando instalação...\n")
missing_packages <- c()

for (package in packages) {
  if (!require(package, character.only = TRUE, quietly = TRUE)) {
    missing_packages <- c(missing_packages, package)
  }
}

if (length(missing_packages) == 0) {
  cat("✅ Todos os pacotes foram instalados com sucesso!\n")
} else {
  cat("❌ Pacotes que falharam na instalação:\n")
  cat(paste("   -", missing_packages), sep = "\n")
  cat("\n💡 Tente instalar manualmente os pacotes que falharam.\n")
}

cat("\n🚀 O projeto está pronto para ser executado!\n")
