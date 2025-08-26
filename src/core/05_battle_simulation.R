# Script 05: Simulação de Batalhas
# Projeto: Melhor Quinteto Pokémon para Elite dos 4
# Autor: Case Técnico de Análise com R
# Data: 2024

cat("⚔️ Iniciando simulação de batalhas contra a Elite dos 4...\n\n")

# Carregar pacotes necessários
library(readr)
library(dplyr)
library(ggplot2)
library(viridis)

# 1. CARREGAR DADOS
cat("📂 Carregando dados...\n")

best_team <- read_csv("output/tables/best_team.csv", show_col_types = FALSE)
elite_four_data <- read_csv("data/elite_four_data.csv", show_col_types = FALSE)
level_recommendations <- read_csv("output/tables/level_recommendations.csv", show_col_types = FALSE)
pokemon_data <- read_csv("data/pokemon_processed.csv", show_col_types = FALSE)

cat("✅ Dados carregados com sucesso!\n\n")

# 2. FUNÇÕES DE SIMULAÇÃO DE BATALHA
cat("⚙️ Criando funções de simulação...\n")

# Função para calcular dano
calculate_damage <- function(attacker_attack, attacker_level, defender_defense, defender_level, type_advantage = 1.0) {
  # Fórmula simplificada de dano baseada no sistema Pokémon
  base_damage <- ((2 * attacker_level / 5 + 2) * 
                   attacker_attack * 60 / defender_defense) / 50 + 2
  damage <- base_damage * type_advantage * runif(1, 0.85, 1.0)  # Variação aleatória
  return(max(1, round(damage)))  # Mínimo de 1 de dano
}

# Função para calcular vantagem de tipo
get_type_advantage <- function(attacker_type, defender_type) {
  # Matriz de vantagens de tipo
  type_advantages <- list(
    Fire = c("Grass", "Ice", "Bug"),
    Water = c("Fire", "Ground", "Rock"),
    Grass = c("Water", "Ground", "Rock"),
    Electric = c("Water", "Flying"),
    Ice = c("Grass", "Ground", "Flying", "Dragon"),
    Fighting = c("Normal", "Ice", "Rock"),
    Poison = c("Grass", "Fairy"),
    Ground = c("Fire", "Electric", "Poison", "Rock"),
    Flying = c("Grass", "Fighting", "Bug"),
    Psychic = c("Fighting", "Poison"),
    Bug = c("Grass", "Psychic"),
    Rock = c("Fire", "Ice", "Flying", "Bug"),
    Ghost = c("Psychic", "Ghost"),
    Dragon = c("Dragon"),
    Fairy = c("Fighting", "Dragon", "Dark")
  )
  
  if (attacker_type %in% names(type_advantages)) {
    if (defender_type %in% type_advantages[[attacker_type]]) {
      return(2.0)  # Super efetivo
    }
  }
  return(1.0)  # Normal
}

# Função para simular uma batalha individual
simulate_battle <- function(player_pokemon, enemy_pokemon, player_level, enemy_level) {
  # Ajustar estatísticas por nível
  player_hp <- player_pokemon$hp * player_level / 100
  player_attack <- player_pokemon$attack * player_level / 100
  player_defense <- player_pokemon$defense * player_level / 100
  
  enemy_hp <- enemy_pokemon$hp * enemy_level / 100
  enemy_attack <- enemy_pokemon$attack * enemy_level / 100
  enemy_defense <- enemy_pokemon$defense * enemy_level / 100
  
  # Simular batalha por turnos
  player_current_hp <- player_hp
  enemy_current_hp <- enemy_hp
  
  battle_log <- c()
  turn <- 1
  
  while (player_current_hp > 0 && enemy_current_hp > 0 && turn <= 20 && !is.na(player_current_hp) && !is.na(enemy_current_hp)) {
    # Determinar quem ataca primeiro (baseado na velocidade)
    if (player_pokemon$speed >= enemy_pokemon$speed) {
      # Jogador ataca primeiro
      damage_to_enemy <- calculate_damage(
        player_attack, player_level, enemy_defense, enemy_level,
        get_type_advantage(player_pokemon$type1, enemy_pokemon$type1)
      )
      enemy_current_hp <- max(0, enemy_current_hp - damage_to_enemy)
      
      battle_log <- c(battle_log, 
                     paste("Turno", turn, ":", player_pokemon$name, "causou", damage_to_enemy, "de dano"))
      
      if (enemy_current_hp <= 0) break
      
      # Inimigo ataca
      damage_to_player <- calculate_damage(
        enemy_attack, enemy_level, player_defense, player_level,
        get_type_advantage(enemy_pokemon$type1, player_pokemon$type1)
      )
      player_current_hp <- max(0, player_current_hp - damage_to_player)
      
      battle_log <- c(battle_log, 
                     paste("Turno", turn, ":", enemy_pokemon$name, "causou", damage_to_player, "de dano"))
    } else {
      # Inimigo ataca primeiro
      damage_to_player <- calculate_damage(
        enemy_attack, enemy_level, player_defense, player_level,
        get_type_advantage(enemy_pokemon$type1, player_pokemon$type1)
      )
      player_current_hp <- max(0, player_current_hp - damage_to_player)
      
      battle_log <- c(battle_log, 
                     paste("Turno", turn, ":", enemy_pokemon$name, "causou", damage_to_player, "de dano"))
      
      if (player_current_hp <= 0) break
      
      # Jogador ataca
      damage_to_enemy <- calculate_damage(
        player_attack, player_level, enemy_defense, enemy_level,
        get_type_advantage(player_pokemon$name, enemy_pokemon$type1)
      )
      enemy_current_hp <- max(0, enemy_current_hp - damage_to_enemy)
      
      battle_log <- c(battle_log, 
                     paste("Turno", turn, ":", player_pokemon$name, "causou", damage_to_enemy, "de dano"))
    }
    
    turn <- turn + 1
  }
  
  # Determinar vencedor
  if (player_current_hp > 0) {
    result <- "Victory"
  } else {
    result <- "Defeat"
  }
  
  return(list(
    result = result,
    player_hp_remaining = player_current_hp,
    enemy_hp_remaining = enemy_current_hp,
    turns = turn - 1,
    battle_log = battle_log
  ))
}

cat("✅ Funções de simulação criadas!\n\n")

# 3. SIMULAR BATALHAS CONTRA CADA MEMBRO
cat("⚔️ Simulando batalhas contra cada membro...\n")

# Aplicar níveis recomendados
player_levels <- level_recommendations$recommended_level

battle_results <- list()

# Simular contra cada membro da Elite dos 4
for (member_idx in 1:nrow(elite_four_data)) {
  member <- elite_four_data[member_idx, ]
  cat("   - Simulando contra", member$member, "...\n")
  
  member_battles <- list()
  
  # Simular contra cada Pokémon do membro
  for (pokemon_idx in 1:5) {
    pokemon_col <- paste0("pokemon", pokemon_idx)
    type_col <- paste0("pokemon", pokemon_idx, "_type1")
    level_col <- paste0("pokemon", pokemon_idx, "_level")
    
    enemy_pokemon_name <- member[[pokemon_col]]
    enemy_type <- member[[type_col]]
    enemy_level <- as.numeric(member[[level_col]])
    
    # Encontrar dados do Pokémon inimigo
    enemy_pokemon <- pokemon_data[pokemon_data$name == enemy_pokemon_name, ]
    
    if (nrow(enemy_pokemon) > 0) {
      # Simular batalha com cada Pokémon do time do jogador
      pokemon_battles <- list()
      
      for (player_idx in 1:5) {
        player_pokemon <- best_team[player_idx, ]
        player_level <- player_levels[player_idx]
        
        battle_result <- simulate_battle(
          player_pokemon, enemy_pokemon, player_level, enemy_level
        )
        
        pokemon_battles[[player_idx]] <- list(
          player_pokemon = player_pokemon$name,
          player_level = player_level,
          result = battle_result$result,
          player_hp_remaining = battle_result$player_hp_remaining,
          enemy_hp_remaining = battle_result$enemy_hp_remaining,
          turns = battle_result$turns
        )
      }
      
      member_battles[[pokemon_idx]] <- list(
        enemy_pokemon = enemy_pokemon_name,
        enemy_type = enemy_type,
        enemy_level = enemy_level,
        battles = pokemon_battles
      )
    }
  }
  
  battle_results[[member_idx]] <- list(
    member = member$member,
    position = member$position,
    battles = member_battles
  )
}

cat("✅ Simulações concluídas!\n\n")

# 4. ANÁLISE DOS RESULTADOS
cat("📊 Analisando resultados das batalhas...\n")

# Calcular estatísticas gerais
total_battles <- 0
total_victories <- 0
battle_summary <- data.frame()

for (member_result in battle_results) {
  for (enemy_battle in member_result$battles) {
    for (player_battle in enemy_battle$battles) {
      total_battles <- total_battles + 1
      if (player_battle$result == "Victory") {
        total_victories <- total_victories + 1
      }
      
      battle_summary <- rbind(battle_summary, data.frame(
        member = member_result$member,
        enemy_pokemon = enemy_battle$enemy_pokemon,
        player_pokemon = player_battle$player_pokemon,
        player_level = player_battle$player_level,
        result = player_battle$result,
        turns = player_battle$turns,
        player_hp_remaining = player_battle$player_hp_remaining
      ))
    }
  }
}

# Taxa de vitória geral
victory_rate <- total_victories / total_battles * 100

cat("   - Total de batalhas simuladas:", total_battles, "\n")
cat("   - Total de vitórias:", total_victories, "\n")
cat("   - Taxa de vitória geral:", round(victory_rate, 1), "%\n")

# 5. ANÁLISE POR POKÉMON DO JOGADOR
cat("\n🔍 Analisando performance por Pokémon...\n")

pokemon_performance <- battle_summary %>%
  group_by(player_pokemon) %>%
  summarise(
    total_battles = n(),
    victories = sum(result == "Victory"),
    victory_rate = victories / total_battles * 100,
    avg_turns = mean(turns),
    avg_hp_remaining = mean(player_hp_remaining)
  ) %>%
  arrange(desc(victory_rate))

cat("   - Performance por Pokémon:\n")
for (i in 1:nrow(pokemon_performance)) {
  pokemon <- pokemon_performance[i, ]
  cat("     ", pokemon$player_pokemon, ": ", round(pokemon$victory_rate, 1), 
      "% vitórias (", pokemon$victories, "/", pokemon$total_battles, ")\n")
}

# 6. ANÁLISE POR MEMBRO DA ELITE DOS 4
cat("\n👑 Analisando dificuldade por membro...\n")

member_difficulty <- battle_summary %>%
  group_by(member) %>%
  summarise(
    total_battles = n(),
    victories = sum(result == "Victory"),
    victory_rate = victories / total_battles * 100,
    avg_turns = mean(turns)
  ) %>%
  arrange(victory_rate)

cat("   - Dificuldade por membro:\n")
for (i in 1:nrow(member_difficulty)) {
  member <- member_difficulty[i, ]
  cat("     ", member$member, ": ", round(member$victory_rate, 1), 
      "% vitórias (", member$victories, "/", member$total_battles, ")\n")
}

# 7. SALVAR RESULTADOS
cat("\n💾 Salvando resultados das simulações...\n")

# Salvar resumo das batalhas
write_csv(battle_summary, "output/tables/battle_summary.csv")

# Salvar performance por Pokémon
write_csv(pokemon_performance, "output/tables/pokemon_performance.csv")

# Salvar dificuldade por membro
write_csv(member_difficulty, "output/tables/member_difficulty.csv")

cat("✅ Resultados salvos!\n")

# 8. VISUALIZAÇÕES
cat("\n📊 Criando visualizações...\n")

# Gráfico de performance por Pokémon
performance_plot <- pokemon_performance %>%
  ggplot(aes(x = reorder(player_pokemon, victory_rate), y = victory_rate, fill = victory_rate)) +
  geom_col() +
  scale_fill_viridis() +
  coord_flip() +
  labs(title = "Taxa de Vitória por Pokémon", 
       x = "Pokémon", 
       y = "Taxa de Vitória (%)") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("output/plots/pokemon_performance.png", performance_plot, width = 10, height = 8)

# Gráfico de dificuldade por membro
difficulty_plot <- member_difficulty %>%
  ggplot(aes(x = reorder(member, victory_rate), y = victory_rate, fill = victory_rate)) +
  geom_col() +
  scale_fill_viridis() +
  labs(title = "Taxa de Vitória contra Cada Membro", 
       x = "Membro da Elite dos 4", 
       y = "Taxa de Vitória (%)") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("output/plots/member_difficulty.png", difficulty_plot, width = 10, height = 6)

cat("✅ Visualizações criadas!\n")

# 9. RECOMENDAÇÕES FINAIS
cat("\n💡 Gerando recomendações finais...\n")

# Melhor Pokémon para cada tipo de inimigo
best_counters <- battle_summary %>%
  group_by(enemy_pokemon) %>%
  filter(result == "Victory") %>%
  arrange(desc(player_hp_remaining)) %>%
  slice(1) %>%
  select(enemy_pokemon, best_counter = player_pokemon, player_level, turns)

cat("   - Melhores contadores:\n")
for (i in 1:nrow(best_counters)) {
  counter <- best_counters[i, ]
  cat("     ", counter$enemy_pokemon, " → ", counter$best_counter, 
      " (Nível ", counter$player_level, ", ", counter$turns, " turnos)\n")
}

# Salvar melhores contadores
write_csv(best_counters, "output/tables/best_counters.csv")

# 10. RESUMO FINAL
cat("\n🎯 RESUMO DAS SIMULAÇÕES:\n")
cat("   - Total de batalhas:", total_battles, "\n")
cat("   - Taxa de vitória geral:", round(victory_rate, 1), "%\n")
cat("   - Membro mais difícil:", member_difficulty$member[1], "\n")
cat("   - Membro mais fácil:", member_difficulty$member[nrow(member_difficulty)], "\n")
cat("   - Melhor Pokémon:", pokemon_performance$player_pokemon[1], "\n")

cat("\n🎉 Simulações de batalha concluídas!\n")
cat("⚔️ Time analisado e estratégias identificadas!\n\n")

# Retornar resultados para uso em outros scripts
return(list(
  battle_results = battle_results,
  battle_summary = battle_summary,
  pokemon_performance = pokemon_performance,
  member_difficulty = member_difficulty,
  best_counters = best_counters,
  victory_rate = victory_rate
))
