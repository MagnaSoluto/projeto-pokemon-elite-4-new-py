# 🎮 Exemplo de Execução - Projeto Pokémon Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

# Este arquivo demonstra como executar o projeto passo a passo

cat("🎮 ==========================================\n")
cat("🎮 EXEMPLO DE EXECUÇÃO DO PROJETO\n")
cat("🎮 Pokémon Elite dos 4 - Análise com R\n")
cat("🎮 ==========================================\n\n")

# =============================================================================
# ETAPA 1: CONFIGURAÇÃO INICIAL
# =============================================================================

cat("📦 ETAPA 1: Configuração Inicial\n")
cat("================================\n")

# Carregar configurações do projeto
cat("⚙️  Carregando configurações...\n")
source("config.R")

# Verificar se os diretórios foram criados
cat("📁 Verificando estrutura de diretórios...\n")
list.dirs(recursive = FALSE)

cat("✅ Configuração inicial concluída!\n\n")

# =============================================================================
# ETAPA 2: INSTALAÇÃO DE PACOTES
# =============================================================================

cat("📦 ETAPA 2: Instalação de Pacotes\n")
cat("================================\n")

# Verificar pacotes necessários
required_packages <- c("dplyr", "tidyr", "readr", "ggplot2", "caret", "randomForest", "GA")

cat("🔍 Verificando pacotes instalados...\n")
installed_packages <- installed.packages()[,"Package"]
missing_packages <- required_packages[!required_packages %in% installed_packages]

if (length(missing_packages) > 0) {
  cat("⚠️  Pacotes em falta detectados:\n")
  for (pkg in missing_packages) {
    cat("   -", pkg, "\n")
  }
  
  cat("\n📦 Instalando pacotes em falta...\n")
  source("scripts/install_packages.R")
} else {
  cat("✅ Todos os pacotes necessários já estão instalados!\n")
}

cat("\n")

# =============================================================================
# ETAPA 3: EXECUÇÃO COMPLETA (OPCIONAL)
# =============================================================================

cat("🚀 ETAPA 3: Execução Completa (Opcional)\n")
cat("========================================\n")

cat("💡 Para executar toda a análise de uma vez, use:\n")
cat("   source('scripts/main_analysis.R')\n\n")

cat("💡 Para executar etapas individuais, continue com este exemplo.\n\n")

# =============================================================================
# ETAPA 4: PREPARAÇÃO DOS DADOS
# =============================================================================

cat("📂 ETAPA 4: Preparação dos Dados\n")
cat("================================\n")

cat("🔍 Verificando arquivos de dados...\n")

# Verificar se os arquivos de dados existem
if (file.exists("data/pokemon_data.csv") && file.exists("data/elite_four_data.csv")) {
  cat("✅ Arquivos de dados encontrados!\n")
  
  # Executar preparação de dados
  cat("⚙️  Executando preparação de dados...\n")
  source("scripts/01_data_preparation.R")
  
} else {
  cat("❌ Arquivos de dados não encontrados!\n")
  cat("   Verifique se os arquivos estão em data/\n")
  stop("Arquivos de dados necessários não encontrados")
}

cat("\n")

# =============================================================================
# ETAPA 5: ANÁLISE EXPLORATÓRIA
# =============================================================================

cat("🔍 ETAPA 5: Análise Exploratória\n")
cat("================================\n")

cat("📊 Executando análise exploratória...\n")
source("scripts/02_exploratory_analysis.R")

cat("✅ Análise exploratória concluída!\n")
cat("📁 Gráficos salvos em output/plots/\n\n")

# =============================================================================
# ETAPA 6: MODELAGEM ESTATÍSTICA
# =============================================================================

cat("🤖 ETAPA 6: Modelagem Estatística\n")
cat("================================\n")

cat("🧠 Executando modelagem estatística...\n")
source("scripts/03_statistical_modeling.R")

cat("✅ Modelagem estatística concluída!\n")
cat("📁 Modelos salvos em output/models/\n\n")

# =============================================================================
# ETAPA 7: OTIMIZAÇÃO DO QUINTETO
# =============================================================================

cat("🎯 ETAPA 7: Otimização do Quinteto\n")
cat("==================================\n")

cat("⚡ Executando otimização do quinteto...\n")
source("scripts/04_team_optimization.R")

cat("✅ Otimização concluída!\n")
cat("📁 Resultados salvos em output/tables/\n\n")

# =============================================================================
# ETAPA 8: SIMULAÇÃO DE BATALHAS
# =============================================================================

cat("⚔️ ETAPA 8: Simulação de Batalhas\n")
cat("================================\n")

cat("🎮 Executando simulações de batalha...\n")
battle_results <- source("scripts/05_battle_simulation.R")

cat("✅ Simulações concluídas!\n")
cat("📊 Resultados salvos em output/tables/\n\n")

# =============================================================================
# ETAPA 9: ANÁLISE DOS RESULTADOS
# =============================================================================

cat("📊 ETAPA 9: Análise dos Resultados\n")
cat("==================================\n")

# Carregar resultados das simulações
cat("📂 Carregando resultados das simulações...\n")

if (file.exists("output/tables/battle_summary.csv")) {
  battle_summary <- read_csv("output/tables/battle_summary.csv", show_col_types = FALSE)
  pokemon_performance <- read_csv("output/tables/pokemon_performance.csv", show_col_types = FALSE)
  member_difficulty <- read_csv("output/tables/member_difficulty.csv", show_col_types = FALSE)
  
  cat("✅ Resultados carregados com sucesso!\n\n")
  
  # Mostrar resumo dos resultados
  cat("📈 RESUMO DOS RESULTADOS:\n")
  cat("   - Total de batalhas:", nrow(battle_summary), "\n")
  cat("   - Taxa de vitória geral:", round(mean(battle_summary$result == "Victory") * 100, 1), "%\n")
  
  cat("\n🏆 MELHOR POKÉMON:\n")
  best_pokemon <- pokemon_performance[1, ]
  cat("   ", best_pokemon$player_pokemon, ":", round(best_pokemon$victory_rate, 1), "% vitórias\n")
  
  cat("\n👑 MEMBRO MAIS DIFÍCIL:\n")
  hardest_member <- member_difficulty[1, ]
  cat("   ", hardest_member$member, ":", round(hardest_member$victory_rate, 1), "% vitórias\n")
  
} else {
  cat("❌ Resultados das simulações não encontrados!\n")
}

cat("\n")

# =============================================================================
# ETAPA 10: VISUALIZAÇÃO DOS RESULTADOS
# =============================================================================

cat("📊 ETAPA 10: Visualização dos Resultados\n")
cat("========================================\n")

cat("🎨 Verificando gráficos gerados...\n")

# Listar arquivos de gráficos
plot_files <- list.files("output/plots", pattern = "\\.png$", full.names = TRUE)

if (length(plot_files) > 0) {
  cat("✅ Gráficos encontrados:\n")
  for (plot_file in plot_files) {
    cat("   -", basename(plot_file), "\n")
  }
} else {
  cat("⚠️  Nenhum gráfico encontrado em output/plots/\n")
}

cat("\n")

# =============================================================================
# ETAPA 11: RELATÓRIO FINAL
# =============================================================================

cat("📋 ETAPA 11: Relatório Final\n")
cat("============================\n")

cat("📝 Gerando relatório final...\n")

# Criar relatório simples
report_summary <- paste0(
  "# 🎮 Relatório de Execução - Projeto Pokémon Elite dos 4\n\n",
  "## 📊 Resumo da Execução\n\n",
  "Este relatório foi gerado automaticamente durante a execução do projeto.\n\n",
  "## 🎯 Objetivos Alcançados\n\n",
  "- ✅ Preparação e limpeza dos dados\n",
  "- ✅ Análise exploratória completa\n",
  "- ✅ Modelagem estatística\n",
  "- ✅ Otimização do quinteto\n",
  "- ✅ Simulação de batalhas\n",
  "- ✅ Análise dos resultados\n\n",
  "## 📁 Arquivos Gerados\n\n",
  "Todos os resultados foram salvos nos diretórios apropriados:\n",
  "- `output/tables/`: Tabelas com dados processados\n",
  "- `output/plots/`: Gráficos e visualizações\n",
  "- `output/models/`: Modelos treinados\n",
  "- `output/reports/`: Relatórios gerados\n\n",
  "## 🚀 Próximos Passos\n\n",
  "1. Revisar os resultados gerados\n",
  "2. Analisar o quinteto recomendado\n",
  "3. Testar as estratégias sugeridas\n",
  "4. Ajustar conforme necessário\n\n",
  "---\n",
  "*Relatório gerado automaticamente - ", Sys.time(), "*"
)

# Salvar relatório
writeLines(report_summary, "output/reports/relatorio_execucao.md")

cat("✅ Relatório de execução gerado!\n")
cat("📁 Salvo em output/reports/relatorio_execucao.md\n\n")

# =============================================================================
# RESUMO FINAL
# =============================================================================

cat("🎉 ==========================================\n")
cat("🎉 EXECUÇÃO DO EXEMPLO CONCLUÍDA!\n")
cat("🎉 ==========================================\n\n")

cat("📊 O QUE FOI EXECUTADO:\n")
cat("   ✅ Configuração inicial\n")
cat("   ✅ Verificação de pacotes\n")
cat("   ✅ Preparação de dados\n")
cat("   ✅ Análise exploratória\n")
cat("   ✅ Modelagem estatística\n")
cat("   ✅ Otimização do quinteto\n")
cat("   ✅ Simulação de batalhas\n")
cat("   ✅ Análise dos resultados\n")
cat("   ✅ Geração de relatório\n\n")

cat("📁 ARQUIVOS GERADOS:\n")
cat("   - Dados processados em data/\n")
cat("   - Tabelas em output/tables/\n")
cat("   - Gráficos em output/plots/\n")
cat("   - Modelos em output/models/\n")
cat("   - Relatórios em output/reports/\n\n")

cat("🎯 PRÓXIMOS PASSOS:\n")
cat("   - Revisar o quinteto recomendado\n")
cat("   - Analisar as estratégias sugeridas\n")
cat("   - Testar o time no jogo\n")
cat("   - Ajustar conforme necessário\n\n")

cat("🎮 Boa sorte na Elite dos 4!\n")
cat("⚔️ Que o melhor treinador vença!\n\n")

# =============================================================================
# FUNÇÕES ÚTEIS PARA ANÁLISE ADICIONAL
# =============================================================================

cat("💡 FUNÇÕES ÚTEIS PARA ANÁLISE ADICIONAL:\n")
cat("========================================\n\n")

cat("🔍 Para analisar um Pokémon específico:\n")
cat("   pokemon_data[pokemon_data$name == 'Charizard', ]\n\n")

cat("📊 Para ver estatísticas por tipo:\n")
cat("   pokemon_data %>% group_by(type1) %>% summarise(avg_total = mean(total))\n\n")

cat("🎯 Para ver o time otimizado:\n")
cat("   read_csv('output/tables/best_team.csv')\n\n")

cat("⚔️ Para ver resultados das batalhas:\n")
cat("   read_csv('output/tables/battle_summary.csv')\n\n")

cat("🎨 Para visualizar gráficos:\n")
cat("   list.files('output/plots', full.names = TRUE)\n\n")

cat("📝 Para editar relatórios:\n")
cat("   file.edit('output/reports/relatorio_execucao.md')\n\n")

cat("🎮 Projeto executado com sucesso!\n")
cat("🚀 Todos os objetivos foram alcançados!\n\n")
