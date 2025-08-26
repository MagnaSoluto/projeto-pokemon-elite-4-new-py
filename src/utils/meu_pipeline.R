# Função meu_pipeline
# Arquivo: meu_pipeline.R

meu_pipeline <- function(dataframe, coluna_numerica, plot = TRUE) {
  # Verificar se a coluna existe
  if (!coluna_numerica %in% names(dataframe)) {
    stop("Coluna não encontrada no dataframe")
    
  # Verificar se a coluna é numérica
  if (!is.numeric(dataframe[[coluna_numerica]])) {
    stop("A coluna deve ser numérica")
  }
  
  # Calcular resumo estatístico
  resumo <- dataframe %>%
    summarise(
      minimo = min(!!sym(coluna_numerica), na.rm = TRUE),
      maximo = max(!!sym(coluna_numerica), na.rm = TRUE),
      media = mean(!!sym(coluna_numerica), na.rm = TRUE),
      mediana = median(!!sym(coluna_numerica), na.rm = TRUE),
      desvio_padrao = sd(!!sym(coluna_numerica), na.rm = TRUE)
    )
  
  # Criar histograma se plot = TRUE
  if (plot) {
    histograma <- dataframe %>%
      ggplot(aes(x = !!sym(coluna_numerica))) +
      geom_histogram(bins = 20, fill = "steelblue", alpha = 0.7) +
      labs(
        title = paste("Histograma de", coluna_numerica),
        x = coluna_numerica,
        y = "Frequência"
        
      ) +
      theme_minimal()
    )
    
    print(histograma)
  }
  
  return(resumo)
}
