# Script 02: Análise Exploratória dos Dados
# Projeto: Melhor Quinteto Pokémon para Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

cat("🔍 Iniciando análise exploratória dos dados dos Pokémon...\n\n")

# Carregar pacotes necessários
library(readr)
library(dplyr)
library(tidyr)
library(ggplot2)
library(plotly)
library(corrplot)
library(ggpubr)
library(viridis)

# 1. CARREGAR DADOS PROCESSADOS
cat("📂 Carregando dados processados...\n")

pokemon_data <- read_csv("data/pokemon_processed.csv", show_col_types = FALSE)
elite_four_data <- read_csv("data/elite_four_data.csv", show_col_types = FALSE)

cat("✅ Dados carregados com sucesso!\n\n")

# 2. ANÁLISE DE DISTRIBUIÇÃO DAS ESTATÍSTICAS
cat("📊 Analisando distribuição das estatísticas...\n")

# Criar gráficos de distribuição para cada estatística
stats_plots <- list()

# HP
stats_plots$hp <- ggplot(pokemon_data, aes(x = hp)) +
  geom_histogram(bins = 20, fill = "steelblue", alpha = 0.7) +
  geom_vline(xintercept = mean(pokemon_data$hp), color = "red", linetype = "dashed") +
  labs(title = "Distribuição de HP", x = "HP", y = "Frequência") +
  theme_minimal()

# Attack
stats_plots$attack <- ggplot(pokemon_data, aes(x = attack)) +
  geom_histogram(bins = 20, fill = "darkred", alpha = 0.7) +
  geom_vline(xintercept = mean(pokemon_data$attack), color = "red", linetype = "dashed") +
  labs(title = "Distribuição de Ataque", x = "Ataque", y = "Frequência") +
  theme_minimal()

# Defense
stats_plots$defense <- ggplot(pokemon_data, aes(x = defense)) +
  geom_histogram(bins = 20, fill = "darkgreen", alpha = 0.7) +
  geom_vline(xintercept = mean(pokemon_data$defense), color = "red", linetype = "dashed") +
  labs(title = "Distribuição de Defesa", x = "Defesa", y = "Frequência") +
  theme_minimal()

# Speed
stats_plots$speed <- ggplot(pokemon_data, aes(x = speed)) +
  geom_histogram(bins = 20, fill = "purple", alpha = 0.7) +
  geom_vline(xintercept = mean(pokemon_data$speed), color = "red", linetype = "dashed") +
  labs(title = "Distribuição de Velocidade", x = "Velocidade", y = "Frequência") +
  theme_minimal()

# Total
stats_plots$total <- ggplot(pokemon_data, aes(x = total)) +
  geom_histogram(bins = 20, fill = "orange", alpha = 0.7) +
  geom_vline(xintercept = mean(pokemon_data$total), color = "red", linetype = "dashed") +
  labs(title = "Distribuição do Total", x = "Total", y = "Frequência") +
  theme_minimal()

# Combinar todos os gráficos
combined_stats <- ggarrange(plotlist = stats_plots, ncol = 2, nrow = 3)
ggsave("output/plots/stats_distribution.png", combined_stats, width = 12, height = 10)

cat("✅ Gráficos de distribuição salvos!\n")

# 3. ANÁLISE DE CORRELAÇÃO
cat("\n🔗 Analisando correlações entre estatísticas...\n")

# Matriz de correlação
correlation_matrix <- pokemon_data %>%
  select(hp, attack, defense, sp_attack, sp_defense, speed, total) %>%
  cor()

# Gráfico de correlação
png("output/plots/correlation_matrix.png", width = 800, height = 600)
corrplot(correlation_matrix, 
         method = "color", 
         type = "upper", 
         order = "hclust",
         tl.cex = 0.8,
         addCoef.col = "black",
         number.cex = 0.7)
dev.off()

cat("✅ Matriz de correlação salva!\n")

# 4. ANÁLISE POR TIPOS
cat("\n🎨 Analisando distribuição por tipos...\n")

# Gráfico de contagem por tipo
type_count_plot <- pokemon_data %>%
  group_by(type1) %>%
  summarise(count = n()) %>%
  arrange(desc(count)) %>%
  ggplot(aes(x = reorder(type1, count), y = count, fill = count)) +
  geom_col() +
  scale_fill_viridis() +
  coord_flip() +
  labs(title = "Distribuição de Pokémon por Tipo", 
       x = "Tipo", 
       y = "Quantidade") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("output/plots/type_distribution.png", type_count_plot, width = 10, height = 8)

# Gráfico de eficiência média por tipo
type_efficiency_plot <- pokemon_data %>%
  group_by(type1) %>%
  summarise(avg_efficiency = mean(efficiency)) %>%
  arrange(desc(avg_efficiency)) %>%
  ggplot(aes(x = reorder(type1, avg_efficiency), y = avg_efficiency, fill = avg_efficiency)) +
  geom_col() +
  scale_fill_viridis() +
  coord_flip() +
  labs(title = "Eficiência Média por Tipo", 
       x = "Tipo", 
       y = "Eficiência Média") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("output/plots/type_efficiency.png", type_efficiency_plot, width = 10, height = 8)

cat("✅ Gráficos de tipos salvos!\n")

# 5. ANÁLISE DE PODER
cat("\n💪 Analisando distribuição de poder...\n")

# Gráfico de distribuição por categoria de poder
power_dist_plot <- pokemon_data %>%
  group_by(power_category) %>%
  summarise(count = n()) %>%
  mutate(power_category = factor(power_category, 
                                levels = c("Muito Baixo", "Baixo", "Médio", "Alto"))) %>%
  ggplot(aes(x = power_category, y = count, fill = power_category)) +
  geom_col() +
  scale_fill_viridis(discrete = TRUE) +
  labs(title = "Distribuição por Categoria de Poder", 
       x = "Categoria", 
       y = "Quantidade") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("output/plots/power_distribution.png", power_dist_plot, width = 10, height = 6)

# 6. ANÁLISE DE BALANCEAMENTO
cat("\n⚖️ Analisando balanceamento dos Pokémon...\n")

# Gráfico de balanceamento vs eficiência
balance_plot <- pokemon_data %>%
  ggplot(aes(x = balance, y = efficiency, color = power_category)) +
  geom_point(alpha = 0.7, size = 2) +
  scale_color_viridis(discrete = TRUE) +
  labs(title = "Balanceamento vs Eficiência", 
       x = "Balanceamento", 
       y = "Eficiência",
       color = "Categoria de Poder") +
  theme_minimal()

ggsave("output/plots/balance_vs_efficiency.png", balance_plot, width = 10, height = 8)

# 7. TOP POKÉMON POR DIFERENTES CRITÉRIOS
cat("\n🏆 Identificando top Pokémon por diferentes critérios...\n")

# Top por ataque
top_attack <- pokemon_data %>%
  select(name, type1, type2, attack, total) %>%
  arrange(desc(attack)) %>%
  head(10)

# Top por defesa
top_defense <- pokemon_data %>%
  select(name, type1, type2, defense, total) %>%
  arrange(desc(defense)) %>%
  head(10)

# Top por velocidade
top_speed <- pokemon_data %>%
  select(name, type1, type2, speed, total) %>%
  arrange(desc(speed)) %>%
  head(10)

# Top por HP
top_hp <- pokemon_data %>%
  select(name, type1, type2, hp, total) %>%
  arrange(desc(hp)) %>%
  head(10)

# Salvar rankings
write_csv(top_attack, "output/tables/top_attack.csv")
write_csv(top_defense, "output/tables/top_defense.csv")
write_csv(top_speed, "output/tables/top_speed.csv")
write_csv(top_hp, "output/tables/top_hp.csv")

cat("✅ Rankings salvos!\n")

# 8. ANÁLISE DA ELITE DOS 4
cat("\n👑 Analisando composição da Elite dos 4...\n")

# Resumo dos tipos da Elite dos 4
elite_types <- elite_four_data %>%
  select(member, position, pokemon1_type1, pokemon2_type1, pokemon3_type1, pokemon4_type1, pokemon5_type1) %>%
  pivot_longer(cols = -c(member, position), 
               names_to = "pokemon", 
               values_to = "type") %>%
  group_by(type) %>%
  summarise(count = n()) %>%
  arrange(desc(count))

# Gráfico dos tipos da Elite dos 4
elite_types_plot <- elite_types %>%
  ggplot(aes(x = reorder(type, count), y = count, fill = count)) +
  geom_col() +
  scale_fill_viridis() +
  coord_flip() +
  labs(title = "Tipos de Pokémon na Elite dos 4", 
       x = "Tipo", 
       y = "Quantidade") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("output/plots/elite_four_types.png", elite_types_plot, width = 10, height = 6)

# Salvar análise da Elite dos 4
write_csv(elite_types, "output/tables/elite_four_analysis.csv")

cat("✅ Análise da Elite dos 4 salva!\n")

# 9. RESUMO FINAL
cat("\n🎯 RESUMO DA ANÁLISE EXPLORATÓRIA:\n")
cat("   - Gráficos de distribuição: 5\n")
cat("   - Matriz de correlação: 1\n")
cat("   - Gráficos de tipos: 2\n")
cat("   - Gráfico de poder: 1\n")
cat("   - Gráfico de balanceamento: 1\n")
cat("   - Rankings: 4\n")
cat("   - Análise da Elite dos 4: 1\n")
cat("   - Total de visualizações: 15\n")

cat("\n📊 Arquivos gerados:\n")
cat("   - Gráficos: output/plots/\n")
cat("   - Tabelas: output/tables/\n")

cat("\n🎉 Análise exploratória concluída com sucesso!\n")
cat("🔍 Insights principais identificados e salvos!\n\n")

# Retornar dados processados para uso em outros scripts
return(list(
  pokemon_data = pokemon_data,
  elite_four_data = elite_four_data,
  elite_types = elite_types
))
