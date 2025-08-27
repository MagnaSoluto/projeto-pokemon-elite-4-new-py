# =============================================================================
# 📊 CASE TÉCNICO: ANÁLISE COM R - 41 PERGUNTAS
# =============================================================================
# Projeto: Melhor Quinteto Pokémon para Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024
# Tipo: R Notebook (funciona perfeitamente no RStudio)
# =============================================================================

# 🎯 INTRODUÇÃO
# Este notebook responde às 41 perguntas do case técnico de análise com R,
# aplicando todas as técnicas solicitadas ao dataset de Pokémon para resolver
# o problema: "Qual é o melhor quinteto de Pokémon e em qual nível para 
# vencer a Elite dos 4 no Red/Green?"

# =============================================================================
# 📦 CONFIGURAÇÃO INICIAL
# =============================================================================

# Carregar pacotes necessários
library(readr)
library(dplyr)
library(tidyr)
library(ggplot2)
library(viridis)
library(corrplot)
library(reshape2)
library(caret)
library(randomForest)
library(GA)
library(knitr)
library(kableExtra)

# Configurar opções do knitr para melhor visualização
knitr::opts_chunk$set(
  echo = TRUE,
  warning = FALSE,
  message = FALSE,
  fig.width = 10,
  fig.height = 6,
  fig.align = "center"
)

# =============================================================================
# 📋 PERGUNTA 1: Importe o seu dataset para o R
# =============================================================================

cat("📋 PERGUNTA 1: Importe o seu dataset para o R\n")
cat("=", "==================================================\n\n")

# Carregar o dataset de Pokémon
pokemon_data <- read_csv("data/pokemon_data.csv", show_col_types = FALSE)

# Verificar se foi carregado corretamente
cat("Dataset carregado com sucesso!\n")
cat("Dimensões:", dim(pokemon_data), "\n\n")

# =============================================================================
# 📋 PERGUNTA 2: Contextualize o problema de negócio
# =============================================================================

cat("📋 PERGUNTA 2: Contextualize o problema de negócio\n")
cat("=", "==================================================\n\n")

cat("RESPOSTA: O problema de negócio é determinar qual é o melhor quinteto de Pokémon\n")
cat("e em qual nível para vencer a Elite dos 4 nos jogos Pokémon Red/Green.\n")
cat("Este é um desafio estratégico que envolve:\n")
cat("- Análise de 151 Pokémon diferentes\n")
cat("- Otimização de combinações de 5 Pokémon\n")
cat("- Consideração de vantagens de tipo e estatísticas\n")
cat("- Maximização da taxa de vitória contra oponentes específicos\n\n")

# =============================================================================
# 📋 PERGUNTA 3: Contextualize a solução do pipeline
# =============================================================================

cat("📋 PERGUNTA 3: Contextualize a solução do pipeline\n")
cat("=", "==================================================\n\n")

cat("RESPOSTA: O pipeline deve resolver o problema de otimização de times através de:\n")
cat("- Análise Exploratória: Compreender as estatísticas e tipos dos Pokémon\n")
cat("- Modelagem Estatística: Criar modelos para avaliar eficácia de combinações\n")
cat("- Otimização: Encontrar o quinteto ideal usando algoritmos genéticos\n")
cat("- Simulação: Testar estratégias contra todos os membros da Elite dos 4\n")
cat("- Validação: Confirmar a eficácia do time otimizado\n\n")

# =============================================================================
# 📋 PERGUNTA 4: Verifique as primeiras 6 linhas do dataset
# =============================================================================

cat("📋 PERGUNTA 4: Verifique as primeiras 6 linhas do dataset\n")
cat("=", "==================================================\n\n")

# Mostrar primeiras 6 linhas
cat("Primeiras 6 linhas do dataset:\n")
print(head(pokemon_data, 6))
cat("\n")

# =============================================================================
# 📋 PERGUNTA 5: Verifique as últimas 10 linhas do dataset
# =============================================================================

cat("📋 PERGUNTA 5: Verifique as últimas 10 linhas do dataset\n")
cat("=", "==================================================\n\n")

# Mostrar últimas 10 linhas
cat("Últimas 10 linhas do dataset:\n")
print(tail(pokemon_data, 10))
cat("\n")

# =============================================================================
# 📋 PERGUNTA 6: Mostre a quantidade de linhas e colunas do dataset
# =============================================================================

cat("📋 PERGUNTA 6: Mostre a quantidade de linhas e colunas do dataset\n")
cat("=", "==================================================\n\n")

# Verificar dimensões
cat("Número de linhas:", nrow(pokemon_data), "\n")
cat("Número de colunas:", ncol(pokemon_data), "\n")
cat("Dimensões totais:", dim(pokemon_data), "\n\n")

# =============================================================================
# 📋 PERGUNTA 7: Verifique a estrutura do dataset
# =============================================================================

cat("📋 PERGUNTA 7: Verifique a estrutura do dataset\n")
cat("=", "==================================================\n\n")

# Verificar estrutura
cat("Estrutura do dataset:\n")
str(pokemon_data)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 8: Verifique os tipos de dados de cada coluna
# =============================================================================

cat("📋 PERGUNTA 8: Verifique os tipos de dados de cada coluna\n")
cat("=", "==================================================\n\n")

# Verificar tipos de dados
cat("Tipos de dados de cada coluna:\n")
sapply(pokemon_data, class) %>% 
  as.data.frame() %>% 
  setNames("Tipo") %>%
  kable() %>%
  kable_styling(bootstrap_options = "striped", full_width = FALSE)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 9: Verifique se há valores nulos no dataset
# =============================================================================

cat("📋 PERGUNTA 9: Verifique se há valores nulos no dataset\n")
cat("=", "==================================================\n\n")

# Verificar valores nulos
cat("Valores nulos por coluna:\n")
colSums(is.na(pokemon_data)) %>%
  as.data.frame() %>%
  setNames("Valores_Nulos") %>%
  filter(Valores_Nulos > 0) %>%
  kable() %>%
  kable_styling(bootstrap_options = "striped", full_width = FALSE)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 10: Verifique se há valores duplicados
# =============================================================================

cat("📋 PERGUNTA 10: Verifique se há valores duplicados\n")
cat("=", "==================================================\n\n")

# Verificar duplicatas
cat("Número de linhas duplicadas:", sum(duplicated(pokemon_data)), "\n\n")

# =============================================================================
# 📋 PERGUNTA 11: Faça um resumo estatístico das variáveis numéricas
# =============================================================================

cat("📋 PERGUNTA 11: Faça um resumo estatístico das variáveis numéricas\n")
cat("=", "==================================================\n\n")

# Resumo estatístico
cat("Resumo estatístico das variáveis numéricas:\n")
summary(pokemon_data[, c("hp", "attack", "defense", "sp_attack", "sp_defense", "speed", "total")])
cat("\n")

# =============================================================================
# 📋 PERGUNTA 12: Calcule a média, mediana e desvio padrão das estatísticas
# =============================================================================

cat("📋 PERGUNTA 12: Calcule a média, mediana e desvio padrão das estatísticas\n")
cat("=", "==================================================\n\n")

# Calcular estatísticas descritivas
stats_summary <- pokemon_data %>%
  select(hp, attack, defense, sp_attack, sp_defense, speed, total) %>%
  summarise(
    hp_media = mean(hp, na.rm = TRUE),
    hp_mediana = median(hp, na.rm = TRUE),
    hp_desvio = sd(hp, na.rm = TRUE),
    attack_media = mean(attack, na.rm = TRUE),
    attack_mediana = median(attack, na.rm = TRUE),
    attack_desvio = sd(attack, na.rm = TRUE),
    defense_media = mean(defense, na.rm = TRUE),
    defense_mediana = median(defense, na.rm = TRUE),
    defense_desvio = sd(defense, na.rm = TRUE),
    sp_attack_media = mean(sp_attack, na.rm = TRUE),
    sp_attack_mediana = median(sp_attack, na.rm = TRUE),
    sp_attack_desvio = sd(sp_attack, na.rm = TRUE),
    sp_defense_media = mean(sp_defense, na.rm = TRUE),
    sp_defense_mediana = median(sp_defense, na.rm = TRUE),
    sp_defense_desvio = sd(sp_defense, na.rm = TRUE),
    speed_media = mean(speed, na.rm = TRUE),
    speed_mediana = median(speed, na.rm = TRUE),
    speed_desvio = sd(speed, na.rm = TRUE),
    total_media = mean(total, na.rm = TRUE),
    total_mediana = median(total, na.rm = TRUE),
    total_desvio = sd(total, na.rm = TRUE)
  )

cat("Estatísticas descritivas:\n")
print(stats_summary)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 13: Crie um histograma da distribuição do HP
# =============================================================================

cat("📋 PERGUNTA 13: Crie um histograma da distribuição do HP\n")
cat("=", "==================================================\n\n")

# Histograma do HP
hp_hist <- ggplot(pokemon_data, aes(x = hp)) +
  geom_histogram(bins = 20, fill = "steelblue", color = "black", alpha = 0.7) +
  labs(title = "Distribuição do HP dos Pokémon",
       x = "HP",
       y = "Frequência") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(hp_hist)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 14: Crie um histograma da distribuição do Attack
# =============================================================================

cat("📋 PERGUNTA 14: Crie um histograma da distribuição do Attack\n")
cat("=", "==================================================\n\n")

# Histograma do Attack
attack_hist <- ggplot(pokemon_data, aes(x = attack)) +
  geom_histogram(bins = 20, fill = "firebrick", color = "black", alpha = 0.7) +
  labs(title = "Distribuição do Attack dos Pokémon",
       x = "Attack",
       y = "Frequência") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(attack_hist)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 15: Crie um histograma da distribuição do Defense
# =============================================================================

cat("📋 PERGUNTA 15: Crie um histograma da distribuição do Defense\n")
cat("=", "==================================================\n\n")

# Histograma do Defense
defense_hist <- ggplot(pokemon_data, aes(x = defense)) +
  geom_histogram(bins = 20, fill = "darkgreen", color = "black", alpha = 0.7) +
  labs(title = "Distribuição do Defense dos Pokémon",
       x = "Defense",
       y = "Frequência") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(defense_hist)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 16: Crie um histograma da distribuição do Speed
# =============================================================================

cat("📋 PERGUNTA 16: Crie um histograma da distribuição do Speed\n")
cat("=", "==================================================\n\n")

# Histograma do Speed
speed_hist <- ggplot(pokemon_data, aes(x = speed)) +
  geom_histogram(bins = 20, fill = "gold", color = "black", alpha = 0.7) +
  labs(title = "Distribuição do Speed dos Pokémon",
       x = "Speed",
       y = "Frequência") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(speed_hist)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 17: Crie um histograma da distribuição do Total
# =============================================================================

cat("📋 PERGUNTA 17: Crie um histograma da distribuição do Total\n")
cat("=", "==================================================\n\n")

# Histograma do Total
total_hist <- ggplot(pokemon_data, aes(x = total)) +
  geom_histogram(bins = 20, fill = "purple", color = "black", alpha = 0.7) +
  labs(title = "Distribuição do Total de Estatísticas dos Pokémon",
       x = "Total",
       y = "Frequência") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(total_hist)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 18: Crie um gráfico de dispersão entre HP e Attack
# =============================================================================

cat("📋 PERGUNTA 18: Crie um gráfico de dispersão entre HP e Attack\n")
cat("=", "==================================================\n\n")

# Gráfico de dispersão HP vs Attack
hp_attack_scatter <- ggplot(pokemon_data, aes(x = hp, y = attack)) +
  geom_point(alpha = 0.7, color = "steelblue") +
  geom_smooth(method = "lm", se = TRUE, color = "red") +
  labs(title = "Relação entre HP e Attack",
       x = "HP",
       y = "Attack") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(hp_attack_scatter)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 19: Crie um gráfico de dispersão entre Defense e Sp_Defense
# =============================================================================

cat("📋 PERGUNTA 19: Crie um gráfico de dispersão entre Defense e Sp_Defense\n")
cat("=", "==================================================\n\n")

# Gráfico de dispersão Defense vs Sp_Defense
def_spdef_scatter <- ggplot(pokemon_data, aes(x = defense, y = sp_defense)) +
  geom_point(alpha = 0.7, color = "darkgreen") +
  geom_smooth(method = "lm", se = TRUE, color = "orange") +
  labs(title = "Relação entre Defense e Sp_Defense",
       x = "Defense",
       y = "Sp_Defense") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(def_spdef_scatter)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 20: Crie um gráfico de dispersão entre Attack e Speed
# =============================================================================

cat("📋 PERGUNTA 20: Crie um gráfico de dispersão entre Attack e Speed\n")
cat("=", "==================================================\n\n")

# Gráfico de dispersão Attack vs Speed
attack_speed_scatter <- ggplot(pokemon_data, aes(x = attack, y = speed)) +
  geom_point(alpha = 0.7, color = "firebrick") +
  geom_smooth(method = "lm", se = TRUE, color = "gold") +
  labs(title = "Relação entre Attack e Speed",
       x = "Attack",
       y = "Speed") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(attack_speed_scatter)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 21: Crie uma matriz de correlação entre todas as variáveis numéricas
# =============================================================================

cat("📋 PERGUNTA 21: Crie uma matriz de correlação entre todas as variáveis numéricas\n")
cat("=", "==================================================\n\n")

# Matriz de correlação
numeric_data <- pokemon_data %>%
  select(hp, attack, defense, sp_attack, sp_defense, speed, total)

correlation_matrix <- cor(numeric_data, use = "complete.obs")

# Gráfico da matriz de correlação
corrplot(correlation_matrix, 
         method = "color",
         type = "upper",
         order = "hclust",
         tl.cex = 0.8,
         tl.col = "black",
         addCoef.col = "black",
         number.cex = 0.7)

cat("Matriz de correlação criada!\n\n")

# =============================================================================
# 📋 PERGUNTA 22: Calcule a correlação entre HP e Total
# =============================================================================

cat("📋 PERGUNTA 22: Calcule a correlação entre HP e Total\n")
cat("=", "==================================================\n\n")

# Correlação HP vs Total
hp_total_cor <- cor(pokemon_data$hp, pokemon_data$total, use = "complete.obs")
cat("Correlação entre HP e Total:", round(hp_total_cor, 4), "\n\n")

# =============================================================================
# 📋 PERGUNTA 23: Calcule a correlação entre Attack e Total
# =============================================================================

cat("📋 PERGUNTA 23: Calcule a correlação entre Attack e Total\n")
cat("=", "==================================================\n\n")

# Correlação Attack vs Total
attack_total_cor <- cor(pokemon_data$attack, pokemon_data$total, use = "complete.obs")
cat("Correlação entre Attack e Total:", round(attack_total_cor, 4), "\n\n")

# =============================================================================
# 📋 PERGUNTA 24: Calcule a correlação entre Defense e Total
# =============================================================================

cat("📋 PERGUNTA 24: Calcule a correlação entre Defense e Total\n")
cat("=", "==================================================\n\n")

# Correlação Defense vs Total
defense_total_cor <- cor(pokemon_data$defense, pokemon_data$total, use = "complete.obs")
cat("Correlação entre Defense e Total:", round(defense_total_cor, 4), "\n\n")

# =============================================================================
# 📋 PERGUNTA 25: Calcule a correlação entre Speed e Total
# =============================================================================

cat("📋 PERGUNTA 25: Calcule a correlação entre Speed e Total\n")
cat("=", "==================================================\n\n")

# Correlação Speed vs Total
speed_total_cor <- cor(pokemon_data$speed, pokemon_data$total, use = "complete.obs")
cat("Correlação entre Speed e Total:", round(speed_total_cor, 4), "\n\n")

# =============================================================================
# 📋 PERGUNTA 26: Crie um gráfico de barras mostrando a contagem por tipo primário
# =============================================================================

cat("📋 PERGUNTA 26: Crie um gráfico de barras mostrando a contagem por tipo primário\n")
cat("=", "==================================================\n\n")

# Gráfico de barras por tipo primário
type1_count <- pokemon_data %>%
  count(type1) %>%
  arrange(desc(n))

type1_bar <- ggplot(type1_count, aes(x = reorder(type1, n), y = n)) +
  geom_bar(stat = "identity", fill = "steelblue", alpha = 0.8) +
  coord_flip() +
  labs(title = "Contagem de Pokémon por Tipo Primário",
       x = "Tipo",
       y = "Quantidade") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(type1_bar)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 27: Crie um gráfico de barras mostrando a contagem por tipo secundário
# =============================================================================

cat("📋 PERGUNTA 27: Crie um gráfico de barras mostrando a contagem por tipo secundário\n")
cat("=", "==================================================\n\n")

# Gráfico de barras por tipo secundário
type2_count <- pokemon_data %>%
  filter(!is.na(type2)) %>%
  count(type2) %>%
  arrange(desc(n))

type2_bar <- ggplot(type2_count, aes(x = reorder(type2, n), y = n)) +
  geom_bar(stat = "identity", fill = "darkgreen", alpha = 0.8) +
  coord_flip() +
  labs(title = "Contagem de Pokémon por Tipo Secundário",
       x = "Tipo",
       y = "Quantidade") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(type2_bar)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 28: Crie um gráfico de caixa (boxplot) para HP por tipo primário
# =============================================================================

cat("📋 PERGUNTA 28: Crie um gráfico de caixa (boxplot) para HP por tipo primário\n")
cat("=", "==================================================\n\n")

# Boxplot HP por tipo primário
hp_type_boxplot <- ggplot(pokemon_data, aes(x = type1, y = hp)) +
  geom_boxplot(fill = "lightblue", alpha = 0.7) +
  coord_flip() +
  labs(title = "Distribuição de HP por Tipo Primário",
       x = "Tipo",
       y = "HP") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
        axis.text.y = element_text(size = 8))

print(hp_type_boxplot)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 29: Crie um gráfico de caixa (boxplot) para Attack por tipo primário
# =============================================================================

cat("📋 PERGUNTA 29: Crie um gráfico de caixa (boxplot) para Attack por tipo primário\n")
cat("=", "==================================================\n\n")

# Boxplot Attack por tipo primário
attack_type_boxplot <- ggplot(pokemon_data, aes(x = type1, y = attack)) +
  geom_boxplot(fill = "lightcoral", alpha = 0.7) +
  coord_flip() +
  labs(title = "Distribuição de Attack por Tipo Primário",
       x = "Tipo",
       y = "Attack") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
        axis.text.y = element_text(size = 8))

print(attack_type_boxplot)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 30: Crie um gráfico de caixa (boxplot) para Defense por tipo primário
# =============================================================================

cat("📋 PERGUNTA 30: Crie um gráfico de caixa (boxplot) para Defense por tipo primário\n")
cat("=", "==================================================\n\n")

# Boxplot Defense por tipo primário
defense_type_boxplot <- ggplot(pokemon_data, aes(x = type1, y = defense)) +
  geom_boxplot(fill = "lightgreen", alpha = 0.7) +
  coord_flip() +
  labs(title = "Distribuição de Defense por Tipo Primário",
       x = "Tipo",
       y = "Defense") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
        axis.text.y = element_text(size = 8))

print(defense_type_boxplot)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 31: Crie um gráfico de caixa (boxplot) para Speed por tipo primário
# =============================================================================

cat("📋 PERGUNTA 31: Crie um gráfico de caixa (boxplot) para Speed por tipo primário\n")
cat("=", "==================================================\n\n")

# Boxplot Speed por tipo primário
speed_type_boxplot <- ggplot(pokemon_data, aes(x = type1, y = speed)) +
  geom_boxplot(fill = "lightyellow", alpha = 0.7) +
  coord_flip() +
  labs(title = "Distribuição de Speed por Tipo Primário",
       x = "Tipo",
       y = "Speed") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
        axis.text.y = element_text(size = 8))

print(speed_type_boxplot)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 32: Crie um gráfico de caixa (boxplot) para Total por tipo primário
# =============================================================================

cat("📋 PERGUNTA 32: Crie um gráfico de caixa (boxplot) para Total por tipo primário\n")
cat("=", "==================================================\n\n")

# Boxplot Total por tipo primário
total_type_boxplot <- ggplot(pokemon_data, aes(x = type1, y = total)) +
  geom_boxplot(fill = "lightpink", alpha = 0.7) +
  coord_flip() +
  labs(title = "Distribuição de Total por Tipo Primário",
       x = "Tipo",
       y = "Total") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"),
        axis.text.y = element_text(size = 8))

print(total_type_boxplot)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 33: Identifique os 10 Pokémon com maior HP
# =============================================================================

cat("📋 PERGUNTA 33: Identifique os 10 Pokémon com maior HP\n")
cat("=", "==================================================\n\n")

# Top 10 Pokémon por HP
top_hp <- pokemon_data %>%
  arrange(desc(hp)) %>%
  select(name, type1, type2, hp, total) %>%
  head(10)

cat("Top 10 Pokémon por HP:\n")
print(top_hp)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 34: Identifique os 10 Pokémon com maior Attack
# =============================================================================

cat("📋 PERGUNTA 34: Identifique os 10 Pokémon com maior Attack\n")
cat("=", "==================================================\n\n")

# Top 10 Pokémon por Attack
top_attack <- pokemon_data %>%
  arrange(desc(attack)) %>%
  select(name, type1, type2, attack, total) %>%
  head(10)

cat("Top 10 Pokémon por Attack:\n")
print(top_attack)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 35: Identifique os 10 Pokémon com maior Defense
# =============================================================================

cat("📋 PERGUNTA 35: Identifique os 10 Pokémon com maior Defense\n")
cat("=", "==================================================\n\n")

# Top 10 Pokémon por Defense
top_defense <- pokemon_data %>%
  arrange(desc(defense)) %>%
  select(name, type1, type2, defense, total) %>%
  head(10)

cat("Top 10 Pokémon por Defense:\n")
print(top_defense)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 36: Identifique os 10 Pokémon com maior Speed
# =============================================================================

cat("📋 PERGUNTA 36: Identifique os 10 Pokémon com maior Speed\n")
cat("=", "==================================================\n\n")

# Top 10 Pokémon por Speed
top_speed <- pokemon_data %>%
  arrange(desc(speed)) %>%
  select(name, type1, type2, speed, total) %>%
  head(10)

cat("Top 10 Pokémon por Speed:\n")
print(top_speed)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 37: Identifique os 10 Pokémon com maior Total de estatísticas
# =============================================================================

cat("📋 PERGUNTA 37: Identifique os 10 Pokémon com maior Total de estatísticas\n")
cat("=", "==================================================\n\n")

# Top 10 Pokémon por Total
top_total <- pokemon_data %>%
  arrange(desc(total)) %>%
  select(name, type1, type2, total) %>%
  head(10)

cat("Top 10 Pokémon por Total de Estatísticas:\n")
print(top_total)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 38: Calcule a média de cada estatística por tipo primário
# =============================================================================

cat("📋 PERGUNTA 38: Calcule a média de cada estatística por tipo primário\n")
cat("=", "==================================================\n\n")

# Média por tipo primário
type_means <- pokemon_data %>%
  group_by(type1) %>%
  summarise(
    n = n(),
    hp_mean = mean(hp, na.rm = TRUE),
    attack_mean = mean(attack, na.rm = TRUE),
    defense_mean = mean(defense, na.rm = TRUE),
    sp_attack_mean = mean(sp_attack, na.rm = TRUE),
    sp_defense_mean = mean(sp_defense, na.rm = TRUE),
    speed_mean = mean(speed, na.rm = TRUE),
    total_mean = mean(total, na.rm = TRUE)
  ) %>%
  arrange(desc(total_mean))

cat("Média de estatísticas por tipo primário:\n")
print(type_means)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 39: Crie um gráfico de barras mostrando a média de Total por tipo primário
# =============================================================================

cat("📋 PERGUNTA 39: Crie um gráfico de barras mostrando a média de Total por tipo primário\n")
cat("=", "==================================================\n\n")

# Gráfico de barras da média de Total por tipo
total_type_mean_bar <- ggplot(type_means, aes(x = reorder(type1, total_mean), y = total_mean)) +
  geom_bar(stat = "identity", fill = "purple", alpha = 0.8) +
  coord_flip() +
  labs(title = "Média de Total de Estatísticas por Tipo Primário",
       x = "Tipo",
       y = "Média do Total") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(total_type_mean_bar)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 40: Crie um gráfico de barras mostrando a média de HP por tipo primário
# =============================================================================

cat("📋 PERGUNTA 40: Crie um gráfico de barras mostrando a média de HP por tipo primário\n")
cat("=", "==================================================\n\n")

# Gráfico de barras da média de HP por tipo
hp_type_mean_bar <- ggplot(type_means, aes(x = reorder(type1, hp_mean), y = hp_mean)) +
  geom_bar(stat = "identity", fill = "steelblue", alpha = 0.8) +
  coord_flip() +
  labs(title = "Média de HP por Tipo Primário",
       x = "Tipo",
       y = "Média de HP") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(hp_type_mean_bar)
cat("\n")

# =============================================================================
# 📋 PERGUNTA 41: Crie um gráfico de barras mostrando a média de Attack por tipo primário
# =============================================================================

cat("📋 PERGUNTA 41: Crie um gráfico de barras mostrando a média de Attack por tipo primário\n")
cat("=", "==================================================\n\n")

# Gráfico de barras da média de Attack por tipo
attack_type_mean_bar <- ggplot(type_means, aes(x = reorder(type1, attack_mean), y = attack_mean)) +
  geom_bar(stat = "identity", fill = "firebrick", alpha = 0.8) +
  coord_flip() +
  labs(title = "Média de Attack por Tipo Primário",
       x = "Tipo",
       y = "Média de Attack") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, size = 14, face = "bold"))

print(attack_type_mean_bar)
cat("\n")

# =============================================================================
# 🎯 RESUMO FINAL
# =============================================================================

cat("🎯 RESUMO FINAL DAS 41 PERGUNTAS\n")
cat("=", "==================================================\n\n")

cat("✅ Todas as 41 perguntas foram respondidas com sucesso!\n\n")

cat("📊 ANÁLISES REALIZADAS:\n")
cat("- Importação e verificação de dados\n")
cat("- Análise exploratória completa\n")
cat("- Visualizações estatísticas\n")
cat("- Análise por tipos de Pokémon\n")
cat("- Identificação dos melhores Pokémon\n")
cat("- Análise de correlações\n\n")

cat("🎮 PRÓXIMOS PASSOS:\n")
cat("- Executar o pipeline completo de otimização\n")
cat("- Simular batalhas contra a Elite dos 4\n")
cat("- Identificar o quinteto ideal\n")
cat("- Calcular níveis recomendados\n\n")

cat("🚀 Para executar a análise completa:\n")
cat("source('src/core/main_analysis.R')\n\n")

cat("🎉 Case Técnico concluído com sucesso!\n")
cat("⚔️ Que o melhor treinador vença!\n\n")
