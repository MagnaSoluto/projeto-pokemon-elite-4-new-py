#!/usr/bin/env Rscript
# Script de verificação para execução em outras máquinas
# Projeto Pokémon Elite dos 4

cat("🔍 VERIFICAÇÃO DE CONFIGURAÇÃO DO PROJETO\n")
cat("==========================================\n\n")

# 1. Verificar versão do R
cat("📊 Verificando versão do R...\n")
cat("   Versão:", R.version.string, "\n")
if (as.numeric(R.version$major) >= 4) {
  cat("   ✅ Versão do R adequada (>= 4.0)\n")
} else {
  cat("   ❌ Versão do R muito antiga (< 4.0)\n")
}

# 2. Verificar arquivos de dados
cat("\n📁 Verificando arquivos de dados...\n")
required_files <- c(
  "data/pokemon_data.csv",
  "data/elite_four_data.csv"
)

all_files_exist <- TRUE
for (file in required_files) {
  if (file.exists(file)) {
    cat("   ✅", file, "\n")
  } else {
    cat("   ❌", file, " - ARQUIVO AUSENTE!\n")
    all_files_exist <- FALSE
  }
}

# 3. Verificar estrutura de diretórios
cat("\n📂 Verificando estrutura de diretórios...\n")
required_dirs <- c("src", "data", "output", "docs")
for (dir in required_dirs) {
  if (dir.exists(dir)) {
    cat("   ✅", dir, "/\n")
  } else {
    cat("   ❌", dir, "/ - DIRETÓRIO AUSENTE!\n")
    all_files_exist <- FALSE
  }
}

# 4. Verificar pacotes R
cat("\n📦 Verificando pacotes R...\n")
required_packages <- c(
  "dplyr", "tidyr", "readr", "ggplot2", "caret", 
  "randomForest", "GA", "viridis"
)

missing_packages <- c()
for (pkg in required_packages) {
  if (require(pkg, character.only = TRUE, quietly = TRUE)) {
    cat("   ✅", pkg, "\n")
  } else {
    cat("   ❌", pkg, " - NÃO INSTALADO!\n")
    missing_packages <- c(missing_packages, pkg)
  }
}

# 5. Testar carregamento de dados
cat("\n🧪 Testando carregamento de dados...\n")
tryCatch({
  pokemon_data <- read.csv("data/pokemon_data.csv")
  elite_data <- read.csv("data/elite_four_data.csv")
  cat("   ✅ Dados carregados com sucesso\n")
  cat("   📊 Pokémon:", nrow(pokemon_data), "registros\n")
  cat("   👑 Elite dos 4:", nrow(elite_data), "membros\n")
}, error = function(e) {
  cat("   ❌ Erro ao carregar dados:", e$message, "\n")
  all_files_exist <- FALSE
})

# 6. Resumo final
cat("\n🎯 RESUMO DA VERIFICAÇÃO:\n")
cat("========================\n")

if (all_files_exist && length(missing_packages) == 0) {
  cat("✅ PROJETO PRONTO PARA EXECUÇÃO!\n")
  cat("🚀 Execute: Rscript main.R\n")
} else {
  cat("❌ PROBLEMAS ENCONTRADOS:\n")
  if (!all_files_exist) {
    cat("   - Arquivos ou diretórios ausentes\n")
  }
  if (length(missing_packages) > 0) {
    cat("   - Pacotes R ausentes:", paste(missing_packages, collapse = ", "), "\n")
    cat("   - Execute: source('src/utils/install_packages.R')\n")
  }
}

cat("\n📋 INSTRUÇÕES PARA OUTRAS MÁQUINAS:\n")
cat("====================================\n")
cat("1. Instalar R 4.0+ (https://www.r-project.org/)\n")
cat("2. Clonar o repositório\n")
cat("3. Executar: Rscript main.R\n")
cat("4. Ou instalar pacotes primeiro: source('src/utils/install_packages.R')\n")
cat("5. Depois executar: source('main.R')\n\n")

cat("🎮 Projeto Pokémon Elite dos 4 - Verificação concluída!\n")
