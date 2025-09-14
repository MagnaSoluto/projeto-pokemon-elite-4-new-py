"""
Otimizador de Equipes - Algoritmos Genéticos para encontrar o melhor sexteto
"""

import random
import numpy as np
from typing import List, Tuple, Dict, Optional, Callable
from dataclasses import dataclass
from ..core.pokemon import Pokemon, PokemonTeam
from ..core.battle_system import BattleSystem, BattleResult
from ..core.elite_four import EliteFour
from .data_processor import DataProcessor


@dataclass
class OptimizationResult:
    """Resultado da otimização"""
    best_team: PokemonTeam
    best_score: float
    generation: int
    fitness_history: List[float]
    team_performance: Dict[str, float]


class TeamOptimizer:
    """Otimizador de equipes usando algoritmos genéticos"""
    
    def __init__(
        self,
        pokemon_database: List[Pokemon],
        elite_four: EliteFour,
        population_size: int = 50,
        max_generations: int = 100,
        mutation_rate: float = 0.1,
        crossover_rate: float = 0.8,
        elite_size: int = 5
    ):
        self.pokemon_database = pokemon_database
        self.elite_four = elite_four
        self.battle_system = BattleSystem()
        self.data_processor = DataProcessor()
        
        # Parâmetros do algoritmo genético
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_size = elite_size
        
        # Histórico de fitness
        self.fitness_history = []
    
    def create_random_team(self) -> PokemonTeam:
        """Cria uma equipe aleatória de 6 Pokémon"""
        team_pokemon = random.sample(self.pokemon_database, min(6, len(self.pokemon_database)))
        return PokemonTeam(team_pokemon)
    
    def create_initial_population(self) -> List[PokemonTeam]:
        """Cria população inicial"""
        population = []
        for _ in range(self.population_size):
            team = self.create_random_team()
            population.append(team)
        return population
    
    def calculate_team_fitness(self, team: PokemonTeam) -> float:
        """Calcula fitness de uma equipe baseado em performance real"""
        
        # Ajusta níveis para competir com Elite Four
        for pokemon in team.pokemon:
            pokemon.level = 60  # Nível competitivo
        
        # Análise da equipe
        team_analysis = self.data_processor.create_team_analysis(team.pokemon)
        
        # Score de batalha contra Elite Four (peso maior)
        battle_score = self._calculate_battle_performance(team)
        
        # Score baseado em métricas da equipe (peso menor)
        efficiency_score = team_analysis.get('avg_efficiency', 0) * 0.1
        balance_score = team_analysis.get('avg_balance', 0) * 0.1
        type_coverage_score = (team_analysis.get('unique_types', 0) / 15) * 0.1
        
        # Score final (foco na vitória real)
        total_score = battle_score * 0.7 + efficiency_score + balance_score + type_coverage_score
        
        return total_score
    
    def _calculate_battle_performance(self, team: PokemonTeam) -> float:
        """Calcula performance em batalhas contra Elite Four"""
        
        total_wins = 0
        total_battles = 0
        
        # Testa contra cada membro da Elite Four
        for member in self.elite_four.get_all_members():
            # Simula múltiplas batalhas
            for _ in range(5):  # 5 simulações por membro (mais rápido)
                battle_log = self.battle_system.battle_teams(team, member.pokemon_team)
                total_battles += 1
                
                if battle_log.battle_result == BattleResult.WIN:
                    total_wins += 1
        
        # Taxa de vitória
        win_rate = total_wins / total_battles if total_battles > 0 else 0
        
        # Bonus por vitórias contra membros difíceis
        difficulty_bonus = 0
        if win_rate > 0.5:  # Se ganha mais de 50%
            difficulty_bonus = 0.2
        elif win_rate > 0.3:  # Se ganha mais de 30%
            difficulty_bonus = 0.1
        
        return min(1.0, win_rate + difficulty_bonus)
    
    def tournament_selection(self, population: List[PokemonTeam], tournament_size: int = 3) -> PokemonTeam:
        """Seleção por torneio"""
        tournament = random.sample(population, min(tournament_size, len(population)))
        
        # Encontra o melhor do torneio
        best_team = tournament[0]
        best_fitness = self.calculate_team_fitness(best_team)
        
        for team in tournament[1:]:
            fitness = self.calculate_team_fitness(team)
            if fitness > best_fitness:
                best_team = team
                best_fitness = fitness
        
        return best_team
    
    def crossover(self, parent1: PokemonTeam, parent2: PokemonTeam) -> Tuple[PokemonTeam, PokemonTeam]:
        """Crossover entre duas equipes"""
        
        if random.random() > self.crossover_rate:
            return parent1, parent2
        
        # Combina Pokémon dos pais
        all_pokemon = list(parent1.pokemon) + list(parent2.pokemon)
        
        # Remove duplicatas
        unique_pokemon = []
        seen_ids = set()
        for pokemon in all_pokemon:
            if pokemon.pokemon_id not in seen_ids:
                unique_pokemon.append(pokemon)
                seen_ids.add(pokemon.pokemon_id)
        
        # Cria filhos
        if len(unique_pokemon) >= 6:
            child1_pokemon = random.sample(unique_pokemon, 6)
            child2_pokemon = random.sample(unique_pokemon, 6)
        else:
            # Se não há Pokémon suficientes, completa com aleatórios
            child1_pokemon = unique_pokemon[:]
            child2_pokemon = unique_pokemon[:]
            
            while len(child1_pokemon) < 6:
                random_pokemon = random.choice(self.pokemon_database)
                if random_pokemon not in child1_pokemon:
                    child1_pokemon.append(random_pokemon)
            
            while len(child2_pokemon) < 6:
                random_pokemon = random.choice(self.pokemon_database)
                if random_pokemon not in child2_pokemon:
                    child2_pokemon.append(random_pokemon)
        
        child1 = PokemonTeam(child1_pokemon)
        child2 = PokemonTeam(child2_pokemon)
        
        return child1, child2
    
    def mutate(self, team: PokemonTeam) -> PokemonTeam:
        """Mutação de uma equipe"""
        
        if random.random() > self.mutation_rate:
            return team
        
        # Escolhe um Pokémon aleatório para substituir
        if len(team.pokemon) == 0:
            return team
        
        mutation_index = random.randint(0, len(team.pokemon) - 1)
        
        # Escolhe um novo Pokémon
        new_pokemon = random.choice(self.pokemon_database)
        
        # Verifica se não é duplicata
        while new_pokemon in team.pokemon:
            new_pokemon = random.choice(self.pokemon_database)
        
        # Cria nova equipe
        new_pokemon_list = team.pokemon[:]
        new_pokemon_list[mutation_index] = new_pokemon
        
        return PokemonTeam(new_pokemon_list)
    
    def optimize_team(self) -> OptimizationResult:
        """Executa otimização da equipe"""
        
        print("Iniciando otimização da equipe...")
        
        # Cria população inicial
        population = self.create_initial_population()
        
        # Histórico de fitness
        fitness_history = []
        
        # Loop principal
        for generation in range(self.max_generations):
            
            # Calcula fitness de toda a população
            fitness_scores = [self.calculate_team_fitness(team) for team in population]
            
            # Registra melhor fitness
            best_fitness = max(fitness_scores)
            fitness_history.append(best_fitness)
            
            print(f"Geração {generation + 1}/{self.max_generations} - Melhor Fitness: {best_fitness:.4f}")
            
            # Seleciona elite
            elite_indices = np.argsort(fitness_scores)[-self.elite_size:]
            elite_teams = [population[i] for i in elite_indices]
            
            # Cria nova população
            new_population = elite_teams[:]
            
            # Gera filhos
            while len(new_population) < self.population_size:
                # Seleção
                parent1 = self.tournament_selection(population)
                parent2 = self.tournament_selection(population)
                
                # Crossover
                child1, child2 = self.crossover(parent1, parent2)
                
                # Mutação
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                
                new_population.extend([child1, child2])
            
            # Limita população
            population = new_population[:self.population_size]
        
        # Encontra melhor equipe
        final_fitness = [self.calculate_team_fitness(team) for team in population]
        best_index = np.argmax(final_fitness)
        best_team = population[best_index]
        best_score = final_fitness[best_index]
        
        # Calcula performance da melhor equipe
        team_performance = self._analyze_team_performance(best_team)
        
        print(f"Otimização concluída! Melhor Score: {best_score:.4f}")
        
        return OptimizationResult(
            best_team=best_team,
            best_score=best_score,
            generation=self.max_generations,
            fitness_history=fitness_history,
            team_performance=team_performance
        )
    
    def _analyze_team_performance(self, team: PokemonTeam) -> Dict[str, float]:
        """Analisa performance da equipe contra Elite Four"""
        
        performance = {}
        
        for member in self.elite_four.get_all_members():
            # Simula 50 batalhas contra cada membro
            battle_stats = self.battle_system.simulate_battle(team, member.pokemon_team, 50)
            performance[member.name] = battle_stats['win_rate']
        
        return performance
    
    def optimize_with_constraints(
        self,
        required_types: Optional[List[str]] = None,
        min_total_stats: int = 0,
        max_team_size: int = 6
    ) -> OptimizationResult:
        """Otimiza equipe com restrições"""
        
        # Filtra base de dados por restrições
        filtered_database = self.pokemon_database[:]
        
        if required_types:
            type_mapping = {
                'Normal': PokemonType.NORMAL,
                'Fire': PokemonType.FIRE,
                'Water': PokemonType.WATER,
                'Electric': PokemonType.ELECTRIC,
                'Grass': PokemonType.GRASS,
                'Ice': PokemonType.ICE,
                'Fighting': PokemonType.FIGHTING,
                'Poison': PokemonType.POISON,
                'Ground': PokemonType.GROUND,
                'Flying': PokemonType.FLYING,
                'Psychic': PokemonType.PSYCHIC,
                'Bug': PokemonType.BUG,
                'Rock': PokemonType.ROCK,
                'Ghost': PokemonType.GHOST,
                'Dragon': PokemonType.DRAGON,
                'Steel': PokemonType.STEEL,
                'Dark': PokemonType.DARK
            }
            
            required_pokemon_types = [type_mapping[t] for t in required_types if t in type_mapping]
            
            if required_pokemon_types:
                filtered_database = [
                    p for p in filtered_database 
                    if any(p.has_type(pt) for pt in required_pokemon_types)
                ]
        
        if min_total_stats > 0:
            filtered_database = [
                p for p in filtered_database 
                if p.stats.total >= min_total_stats
            ]
        
        # Atualiza base de dados filtrada
        original_database = self.pokemon_database
        self.pokemon_database = filtered_database
        
        try:
            result = self.optimize_team()
        finally:
            # Restaura base de dados original
            self.pokemon_database = original_database
        
        return result
    
    def get_team_recommendations(
        self, 
        current_team: PokemonTeam, 
        num_recommendations: int = 5
    ) -> List[Tuple[Pokemon, str]]:
        """Gera recomendações de melhorias para a equipe"""
        
        recommendations = []
        
        # Analisa fraquezas da equipe
        team_analysis = self.data_processor.create_team_analysis(current_team.pokemon)
        weaknesses = team_analysis.get('weaknesses', {})
        
        # Encontra Pokémon que cobrem fraquezas
        for weakness_type, weak_pokemon in weaknesses.items():
            # Busca Pokémon que são efetivos contra o tipo fraco
            from ..core.battle_system import TypeEffectiveness
            
            for pokemon in self.pokemon_database:
                if pokemon in current_team.pokemon:
                    continue
                
                # Verifica se tem vantagem contra o tipo fraco
                has_advantage = False
                for move in pokemon.move_set.moves:
                    if move.category.value != "Status":
                        effectiveness = TypeEffectiveness.get_effectiveness(
                            move.move_type, 
                            [PokemonType(weakness_type)]
                        )
                        if effectiveness > 1.0:
                            has_advantage = True
                            break
                
                if has_advantage:
                    reason = f"Cobre fraqueza contra {weakness_type} (afeta {', '.join(weak_pokemon)})"
                    recommendations.append((pokemon, reason))
                    
                    if len(recommendations) >= num_recommendations:
                        break
            
            if len(recommendations) >= num_recommendations:
                break
        
        return recommendations[:num_recommendations]
