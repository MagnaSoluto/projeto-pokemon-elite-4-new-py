
# Função para calcular poder defensivo
calcular_poder_defensivo <- function(hp, defense, sp_defense) {
  # Poder defensivo = HP * (Defense + Sp_Defense) / 200
  poder <- hp * (defense + sp_defense) / 200
  return(round(poder, 2))
}

# Função para classificar tipo de Pokémon
classificar_pokemon <- function(total) {
  if (total >= 600) return('Lendário')
  else if (total >= 500) return('Poderoso')
  else if (total >= 400) return('Forte')
  else return('Normal')
}

