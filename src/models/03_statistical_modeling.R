# Script 03: Modelagem Estatística e Machine Learning
# Projeto: Melhor Quinteto Pokémon para Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

cat("🤖 Iniciando modelagem estatística dos dados dos Pokémon...\n\n")

# Carregar pacotes necessários
library(readr)
library(caret)
library(randomForest)
library(glmnet)
library(e1071)
library(rpart)
library(dplyr)
library(ggplot2)

# 1. CARREGAR DADOS PROCESSADOS
cat("📂 Carregando dados processados...\n")

pokemon_data <- read_csv("data/pokemon_processed.csv", show_col_types = FALSE)
elite_four_data <- read_csv("data/elite_four_data.csv", show_col_types = FALSE)

cat("✅ Dados carregados com sucesso!\n\n")

# 2. PREPARAÇÃO DOS DADOS PARA MODELAGEM
cat("⚙️ Preparando dados para modelagem...\n")

# Criar variável alvo: eficiência como variável contínua
pokemon_modeling <- pokemon_data %>%
  select(-id, -generation) %>%
  mutate(
    # Codificar tipos como fatores
    type1 = as.factor(type1),
    type2 = as.factor(type2),
    power_category = as.factor(power_category)
  )

# Verificar estrutura dos dados
cat("   - Estrutura dos dados para modelagem:\n")
str(pokemon_modeling)

# 3. DIVISÃO DOS DADOS (TRAIN/TEST)
cat("\n📊 Dividindo dados em treino e teste...\n")

set.seed(123)  # Para reprodutibilidade

# Criar índices para divisão
train_index <- createDataPartition(pokemon_modeling$efficiency, p = 0.8, list = FALSE)

# Dividir dados
train_data <- pokemon_modeling[train_index, ]
test_data <- pokemon_modeling[-train_index, ]

cat("   - Dados de treino: ", nrow(train_data), "registros\n")
cat("   - Dados de teste: ", nrow(test_data), "registros\n")

# 4. MODELO DE REGRESSÃO LINEAR MÚLTIPLA
cat("\n📈 Treinando modelo de regressão linear...\n")

# Modelo linear
lm_model <- lm(efficiency ~ hp + attack + defense + sp_attack + sp_defense + speed, 
               data = train_data)

# Resumo do modelo
cat("   - Resumo do modelo linear:\n")
print(summary(lm_model))

# Predições no conjunto de teste
lm_predictions <- predict(lm_model, test_data)

# Métricas de avaliação
lm_rmse <- sqrt(mean((test_data$efficiency - lm_predictions)^2))
lm_mae <- mean(abs(test_data$efficiency - lm_predictions))
lm_r2 <- cor(test_data$efficiency, lm_predictions)^2

cat("   - Métricas do modelo linear:\n")
cat("     RMSE:", round(lm_rmse, 4), "\n")
cat("     MAE:", round(lm_mae, 4), "\n")
cat("     R²:", round(lm_r2, 4), "\n")

# 5. MODELO RANDOM FOREST
cat("\n🌲 Treinando modelo Random Forest...\n")

# Configurar controle de treinamento
rf_control <- trainControl(method = "cv", number = 5)

# Treinar Random Forest
rf_model <- train(
  efficiency ~ hp + attack + defense + sp_attack + sp_defense + speed + type1 + power_category,
  data = train_data,
  method = "rf",
  trControl = rf_control,
  tuneLength = 3
)

cat("   - Melhor modelo Random Forest:\n")
print(rf_model$bestTune)

# Predições
rf_predictions <- predict(rf_model, test_data)

# Métricas
rf_rmse <- sqrt(mean((test_data$efficiency - rf_predictions)^2))
rf_mae <- mean(abs(test_data$efficiency - rf_predictions))
rf_r2 <- cor(test_data$efficiency, rf_predictions)^2

cat("   - Métricas do Random Forest:\n")
cat("     RMSE:", round(rf_rmse, 4), "\n")
cat("     MAE:", round(rf_mae, 4), "\n")
cat("     R²:", round(rf_r2, 4), "\n")

# 6. MODELO DE REGRESSÃO RIDGE/LASSO
cat("\n🎯 Treinando modelo de regressão regularizada...\n")

# Preparar dados para glmnet
x_train <- model.matrix(efficiency ~ hp + attack + defense + sp_attack + sp_defense + speed, 
                        data = train_data)[, -1]
y_train <- train_data$efficiency

x_test <- model.matrix(efficiency ~ hp + attack + defense + sp_attack + sp_defense + speed, 
                       data = test_data)[, -1]
y_test <- test_data$efficiency

# Modelo Ridge
ridge_model <- cv.glmnet(x_train, y_train, alpha = 0)
ridge_predictions <- predict(ridge_model, x_test, s = "lambda.min")

# Modelo Lasso
lasso_model <- cv.glmnet(x_train, y_train, alpha = 1)
lasso_predictions <- predict(lasso_model, x_test, s = "lambda.min")

# Métricas
ridge_rmse <- sqrt(mean((y_test - ridge_predictions)^2))
lasso_rmse <- sqrt(mean((y_test - lasso_predictions)^2))

cat("   - Métricas dos modelos regularizados:\n")
cat("     Ridge RMSE:", round(ridge_rmse, 4), "\n")
cat("     Lasso RMSE:", round(lasso_rmse, 4), "\n")

# 7. ANÁLISE DE IMPORTÂNCIA DE VARIÁVEIS
cat("\n🔍 Analisando importância das variáveis...\n")

# Importância do Random Forest
rf_importance <- varImp(rf_model)
print(rf_importance)

# Gráfico de importância
importance_plot <- ggplot(rf_importance, aes(x = reorder(rownames(rf_importance), Overall), y = Overall)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(title = "Importância das Variáveis (Random Forest)", 
       x = "Variável", 
       y = "Importância") +
  theme_minimal()

ggsave("output/plots/variable_importance.png", importance_plot, width = 10, height = 8)

# 8. COMPARAÇÃO DE MODELOS
cat("\n🏆 Comparando performance dos modelos...\n")

# Criar tabela de comparação
model_comparison <- data.frame(
  Modelo = c("Regressão Linear", "Random Forest", "Ridge", "Lasso"),
  RMSE = c(lm_rmse, rf_rmse, ridge_rmse, lasso_rmse),
  MAE = c(lm_mae, rf_mae, NA, NA),
  R2 = c(lm_r2, rf_r2, NA, NA)
)

print(model_comparison)

# Salvar comparação
write_csv(model_comparison, "output/tables/model_comparison.csv")

# 9. MODELO FINAL E PREDIÇÕES
cat("\n🎯 Selecionando modelo final...\n")

# Selecionar o melhor modelo baseado no RMSE
best_model_name <- model_comparison$Modelo[which.min(model_comparison$RMSE)]
cat("   - Melhor modelo:", best_model_name, "\n")

# Fazer predições no dataset completo
if (best_model_name == "Random Forest") {
  final_predictions <- predict(rf_model, pokemon_data)
  best_model <- rf_model
} else if (best_model_name == "Regressão Linear") {
  final_predictions <- predict(lm_model, pokemon_data)
  best_model <- lm_model
} else if (best_model_name == "Ridge") {
  x_full <- model.matrix(efficiency ~ hp + attack + defense + sp_attack + sp_defense + speed, 
                         data = pokemon_data)[, -1]
  final_predictions <- predict(ridge_model, x_full, s = "lambda.min")
  best_model <- ridge_model
} else {
  x_full <- model.matrix(efficiency ~ hp + attack + defense + sp_attack + sp_defense + speed, 
                         data = pokemon_data)[, -1]
  final_predictions <- predict(lasso_model, x_full, s = "lambda.min")
  best_model <- lasso_model
}

# Adicionar predições ao dataset
pokemon_with_predictions <- pokemon_data %>%
  mutate(predicted_efficiency = final_predictions)

# Salvar dataset com predições
write_csv(pokemon_with_predictions, "data/pokemon_with_predictions.csv")

cat("✅ Predições salvas no dataset!\n")

# 10. SALVAR MODELOS
cat("\n💾 Salvando modelos treinados...\n")

# Salvar o melhor modelo
saveRDS(best_model, "output/models/best_model.rds")

# Salvar todos os modelos
saveRDS(list(
  linear = lm_model,
  random_forest = rf_model,
  ridge = ridge_model,
  lasso = lasso_model
), "output/models/all_models.rds")

cat("✅ Modelos salvos com sucesso!\n")

# 11. RESUMO FINAL
cat("\n🎯 RESUMO DA MODELAGEM ESTATÍSTICA:\n")
cat("   - Modelos treinados: 4\n")
cat("   - Melhor modelo:", best_model_name, "\n")
cat("   - Performance do melhor modelo:\n")
cat("     RMSE:", round(min(model_comparison$RMSE), 4), "\n")
cat("   - Dataset com predições salvo\n")
cat("   - Modelos salvos para uso futuro\n")

cat("\n🎉 Modelagem estatística concluída com sucesso!\n")
cat("🤖 Modelos treinados e prontos para otimização!\n\n")

# Retornar resultados para uso em outros scripts
return(list(
  best_model = best_model,
  best_model_name = best_model_name,
  model_comparison = model_comparison,
  pokemon_with_predictions = pokemon_with_predictions
))
