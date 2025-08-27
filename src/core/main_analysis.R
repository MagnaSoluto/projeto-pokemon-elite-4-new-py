# Script Principal: Pipeline Completo de Análise
# Projeto: Melhor Quinteto Pokémon para Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

cat("🎮 ==========================================\n")
cat("🎮 PROJETO POKÉMON ELITE DOS 4\n")
cat("🎮 Case Técnico de Análise com R\n")
cat("🎮 ==========================================\n\n")

# 1. INSTALAÇÃO DE PACOTES
cat("📦 ETAPA 1: Instalação de Pacotes\n")
cat("================================\n")

# Verificar se os pacotes estão instalados
required_packages <- c("dplyr", "tidyr", "readr", "ggplot2", "caret", "randomForest", "GA")

missing_packages <- required_packages[!required_packages %in% installed.packages()[,"Package"]]

if (length(missing_packages) > 0) {
  cat("⚠️  Pacotes em falta detectados. Executando instalação...\n")
  source("src/utils/install_packages.R")
} else {
  cat("✅ Todos os pacotes necessários já estão instalados!\n")
}

cat("\n")

# 2. PREPARAÇÃO DOS DADOS
cat("📂 ETAPA 2: Preparação dos Dados\n")
cat("================================\n")

cat("Executando script de preparação de dados...\n")
source("src/core/01_data_preparation.R")

cat("\n")

# 3. ANÁLISE EXPLORATÓRIA
cat("🔍 ETAPA 3: Análise Exploratória\n")
cat("================================\n")

cat("Executando análise exploratória...\n")
source("src/analysis/02_exploratory_analysis.R")

cat("\n")

# 4. MODELAGEM ESTATÍSTICA
cat("🤖 ETAPA 4: Modelagem Estatística\n")
cat("================================\n")

cat("Executando modelagem estatística...\n")
source("src/models/03_statistical_modeling.R")

cat("\n")

# 5. OTIMIZAÇÃO DO QUINTETO
cat("🎯 ETAPA 5: Otimização do Quinteto\n")
cat("================================\n")

cat("Executando otimização do quinteto...\n")
source("src/models/04_team_optimization.R")

cat("\n")

# 6. SIMULAÇÃO DE BATALHAS
cat("⚔️ ETAPA 6: Simulação de Batalhas\n")
cat("================================\n")

cat("Executando simulações de batalha...\n")
source("src/core/05_battle_simulation.R")

cat("\n")

# 7. GERAÇÃO DE RELATÓRIO FINAL
cat("📊 ETAPA 7: Geração de Relatório Final\n")
cat("======================================\n")

cat("Gerando relatório final...\n")

# Carregar dados necessários para o relatório
best_team <- read.csv("output/tables/best_team.csv")
level_recommendations <- read.csv("output/tables/level_recommendations.csv")
pokemon_performance <- read.csv("output/tables/pokemon_performance.csv")
member_difficulty <- read.csv("output/tables/member_difficulty.csv")
best_counters <- read.csv("output/tables/best_counters.csv")
battle_summary <- read.csv("output/tables/battle_summary.csv")

# Calcular estatísticas
total_battles <- nrow(battle_summary)
victory_rate <- (sum(battle_summary$result == "Victory") / total_battles) * 100

# Criar relatório em markdown
report_content <- paste0(
  "# 🎮 Relatório Final: Melhor Quinteto Pokémon para Elite dos 4\n\n",
  "## 📋 Resumo Executivo\n\n",
  "Este relatório apresenta os resultados da análise completa para determinar o melhor quinteto de Pokémon ",
  "e os níveis ideais para vencer a Elite dos 4 nos jogos Pokémon Red/Green.\n\n",
  "## 🎯 Objetivos Alcançados\n\n",
  "- ✅ Análise exploratória completa dos dados dos Pokémon\n",
  "- ✅ Modelagem estatística para avaliação de eficácia\n",
  "- ✅ Otimização do quinteto usando algoritmos genéticos\n",
  "- ✅ Simulação de batalhas contra todos os membros\n",
  "- ✅ Recomendações estratégicas baseadas em dados\n\n",
  "## 🏆 Quinteto Recomendado\n\n",
  "### Time Otimizado:\n",
  "1. **", best_team$name[1], "** (Nível ", level_recommendations$recommended_level[1], ")\n",
  "2. **", best_team$name[2], "** (Nível ", level_recommendations$recommended_level[2], ")\n",
  "3. **", best_team$name[3], "** (Nível ", level_recommendations$recommended_level[3], ")\n",
  "4. **", best_team$name[4], "** (Nível ", level_recommendations$recommended_level[4], ")\n",
  "5. **", best_team$name[5], "** (Nível ", level_recommendations$recommended_level[5], ")\n\n",
  "## 📊 Resultados das Simulações\n\n",
  "- **Total de batalhas simuladas:** ", total_battles, "\n",
  "- **Taxa de vitória geral:** ", round(victory_rate, 1), "%\n",
  "- **Membro mais difícil:** ", member_difficulty$member[1], "\n",
  "- **Membro mais fácil:** ", member_difficulty$member[nrow(member_difficulty)], "\n\n",
  "## 🔍 Performance por Pokémon\n\n",
  "| Pokémon | Taxa de Vitória | Batalhas | Vitórias |\n",
  "|---------|----------------|----------|----------|\n"
)

# Adicionar dados de performance
for (i in 1:nrow(pokemon_performance)) {
  pokemon <- pokemon_performance[i, ]
  report_content <- paste0(report_content,
    "| ", pokemon$player_pokemon, " | ", round(pokemon$victory_rate, 1), "% | ",
    pokemon$total_battles, " | ", pokemon$victories, " |\n"
  )
}

report_content <- paste0(report_content, "\n## 👑 Dificuldade por Membro\n\n",
  "| Membro | Taxa de Vitória | Batalhas | Vitórias |\n",
  "|--------|----------------|----------|----------|\n"
)

# Adicionar dados de dificuldade
for (i in 1:nrow(member_difficulty)) {
  member <- member_difficulty[i, ]
  report_content <- paste0(report_content,
    "| ", member$member, " | ", round(member$victory_rate, 1), "% | ",
    member$total_battles, " | ", member$victories, " |\n"
  )
}

report_content <- paste0(report_content, "\n## 💡 Estratégias Recomendadas\n\n",
  "### Melhores Contadores:\n\n"
)

# Adicionar melhores contadores
for (i in 1:nrow(best_counters)) {
  counter <- best_counters[i, ]
  report_content <- paste0(report_content,
    "- **", counter$enemy_pokemon, "** → Use **", counter$best_counter, 
    "** no nível ", counter$player_level, " (", counter$turns, " turnos)\n"
  )
}

report_content <- paste0(report_content, "\n## 📈 Visualizações Geradas\n\n",
  "O projeto gerou as seguintes visualizações:\n",
  "- `pokemon_performance.png`: Performance de cada Pokémon\n",
  "- `member_difficulty.png`: Dificuldade de cada membro\n",
  "- `type_effectiveness.png`: Efetividade dos tipos\n",
  "- `stats_distribution.png`: Distribuição das estatísticas\n\n",
  "## 🎮 Conclusões\n\n",
  "Com base na análise completa dos dados e simulações:\n\n",
  "1. **O quinteto otimizado** foi identificado usando algoritmos genéticos\n",
  "2. **Os níveis ideais** foram calculados para maximizar a eficácia\n",
  "3. **As estratégias** foram testadas contra todos os membros da Elite dos 4\n",
  "4. **A taxa de vitória** geral é de ", round(victory_rate, 1), "%\n\n",
  "## 📁 Arquivos Gerados\n\n",
  "Todos os resultados foram salvos em:\n",
  "- `output/tables/`: Tabelas com dados processados\n",
  "- `output/plots/`: Gráficos e visualizações\n",
  "- `output/models/`: Modelos treinados\n",
  "- `output/reports/`: Relatórios gerados\n\n",
  "## 🚀 Como Executar\n\n",
  "Para executar a análise completa:\n",
  "```r\n",
  "source('src/core/main_analysis.R')\n",
  "```\n\n",
  "---\n",
  "*Relatório gerado automaticamente pelo Case Técnico de Análise com R*"
)

# Salvar relatório
writeLines(report_content, "output/reports/relatorio_final.md")

cat("✅ Relatório final gerado!\n")

# 8. RESUMO EXECUTIVO
cat("\n🎉 ==========================================\n")
cat("🎉 ANÁLISE COMPLETA CONCLUÍDA!\n")
cat("🎉 ==========================================\n\n")

cat("📊 RESULTADOS PRINCIPAIS:\n")
cat("   - Quinteto otimizado identificado\n")
cat("   - Níveis ideais calculados\n")
cat("   - ", total_battles, " batalhas simuladas\n")
cat("   - Taxa de vitória: ", round(victory_rate, 1), "%\n\n")

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

# Mensagem de conclusão
cat("✅ Pipeline completo executado com sucesso!\n")
cat("🎯 Todos os arquivos de saída foram gerados!\n")
cat("📊 Verifique as pastas output/ para os resultados!\n\n")
