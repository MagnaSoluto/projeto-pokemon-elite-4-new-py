# Script 01: Preparação e Limpeza dos Dados
# Projeto: Melhor Quinteto Pokémon para Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

cat("🎮 Iniciando preparação dos dados dos Pokémon...\n\n")

# Carregar pacotes necessários
library(dplyr)
library(tidyr)
library(readr)
library(stringr)

# 1. CARREGAR DADOS
cat("📂 Carregando datasets...\n")

# Dataset principal dos Pokémon
pokemon_data <- read_csv("data/pokemon_data.csv", show_col_types = FALSE)

# Dataset da Elite dos 4
elite_four_data <- read_csv("data/elite_four_data.csv", show_col_types = FALSE, na = c("", "None", "NA"))

# Limpar dados da Elite dos 4
elite_four_data <- elite_four_data %>%
  # Substituir "None" por NA
  mutate(across(everything(), ~ifelse(. == "None", NA, .))) %>%
  # Remover linhas completamente vazias
  filter(!is.na(member) & !is.na(pokemon1))

cat("✅ Datasets carregados com sucesso!\n")
cat("   - Pokémon: ", nrow(pokemon_data), "registros\n")
cat("   - Elite dos 4: ", nrow(elite_four_data), "membros\n\n")

# 2. LIMPEZA DOS DADOS DOS POKÉMON
cat("🧹 Limpando dados dos Pokémon...\n")

# Verificar valores nulos
pokemon_na_summary <- pokemon_data %>%
  summarise_all(~sum(is.na(.))) %>%
  gather(key = "coluna", value = "valores_nulos")

cat("   - Valores nulos encontrados:\n")
print(pokemon_na_summary)

# Verificar tipos de dados
cat("\n   - Tipos de dados:\n")
str(pokemon_data)

# 3. PROCESSAMENTO DOS DADOS
cat("\n⚙️ Processando dados...\n")

# Criar variáveis derivadas
pokemon_processed <- pokemon_data %>%
  # Calcular estatísticas derivadas
  mutate(
    # Média das estatísticas de combate
    combat_avg = (attack + defense + sp_attack + sp_defense + speed) / 5,
    
    # Média das estatísticas defensivas
    defense_avg = (hp + defense + sp_defense) / 3,
    
    # Média das estatísticas ofensivas
    offense_avg = (attack + sp_attack + speed) / 3,
    
    # Balanceamento (quão equilibrado é o Pokémon)
    balance = 1 - (abs(attack - defense) + abs(sp_attack - sp_defense) + abs(attack - sp_attack)) / (attack + defense + sp_attack + sp_defense),
    
    # Eficiência total (considerando todas as estatísticas)
    efficiency = total / 600,  # 600 é o máximo teórico
    
    # Categoria de poder baseada no total
    power_category = case_when(
      total >= 500 ~ "Alto",
      total >= 400 ~ "Médio",
      total >= 300 ~ "Baixo",
      TRUE ~ "Muito Baixo"
    )
  ) %>%
  # Organizar por eficiência
  arrange(desc(efficiency))

cat("✅ Dados processados com sucesso!\n")

# 4. ANÁLISE DOS TIPOS
cat("\n🎨 Analisando tipos de Pokémon...\n")

# Contagem por tipo primário
type_counts <- pokemon_processed %>%
  group_by(type1) %>%
  summarise(
    count = n(),
    avg_total = mean(total),
    avg_efficiency = mean(efficiency)
  ) %>%
  arrange(desc(count))

cat("   - Tipos mais comuns:\n")
print(head(type_counts, 5))

# 5. ESTATÍSTICAS DESCRITIVAS
cat("\n📊 Estatísticas descritivas:\n")

# Resumo das estatísticas principais
stats_summary <- pokemon_processed %>%
  select(hp, attack, defense, sp_attack, sp_defense, speed, total) %>%
  summary()

print(stats_summary)

# 6. SALVAR DADOS PROCESSADOS
cat("\n💾 Salvando dados processados...\n")

# Salvar dataset processado
write_csv(pokemon_processed, "data/pokemon_processed.csv")

# Salvar resumo dos tipos
write_csv(type_counts, "output/tables/type_analysis.csv")

# Salvar estatísticas descritivas
sink("output/tables/stats_summary.txt")
print(stats_summary)
sink()

cat("✅ Dados salvos com sucesso!\n")

# 7. RESUMO FINAL
cat("\n🎯 RESUMO DA PREPARAÇÃO DOS DADOS:\n")
cat("   - Total de Pokémon processados: ", nrow(pokemon_processed), "\n")
cat("   - Tipos únicos encontrados: ", length(unique(pokemon_processed$type1)), "\n")
cat("   - Estatísticas derivadas criadas: 6\n")
cat("   - Arquivos de saída gerados: 3\n")

# Top 10 Pokémon por eficiência
cat("\n🏆 TOP 10 POKÉMON POR EFICIÊNCIA:\n")
top_pokemon <- pokemon_processed %>%
  select(name, type1, type2, total, efficiency, power_category) %>%
  head(10)

print(top_pokemon)

cat("\n🎉 Preparação dos dados concluída com sucesso!\n")
cat("📁 Dados processados salvos em 'data/pokemon_processed.csv'\n")
cat("📊 Análises salvas em 'output/tables/'\n\n")

# Retornar dados processados para uso em outros scripts
return(list(
  pokemon_data = pokemon_processed,
  elite_four_data = elite_four_data,
  type_counts = type_counts
))
