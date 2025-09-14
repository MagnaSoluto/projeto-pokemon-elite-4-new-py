"""
Otimizador Avançado de Equipes - Melhorias significativas no sistema de otimização
"""

import random
import numpy as np
from typing import List, Tuple, Dict, Optional, Callable
from dataclasses import dataclass
from ..core.pokemon import Pokemon, PokemonTeam, PokemonType, PokemonStats
from ..core.smart_battle_system import SmartBattleSystem, MoveStrategy
from ..core.elite_four import EliteFour
from .data_processor import DataProcessor


@dataclass
class AdvancedOptimizationResult:
    """Resultado da otimização avançada"""
    best_team: PokemonTeam
    best_score: float
    generation: int
    fitness_history: List[float]
    team_performance: Dict[str, float]
    move_strategy_performance: Dict[str, float]
    individual_performance: Dict[str, float]
    optimization_metrics: Dict[str, float]


class AdvancedTeamOptimizer:
    """Otimizador avançado de equipes com múltiplas melhorias"""
    
    def __init__(
        self,
        pokemon_database: List[Pokemon],
        elite_four: EliteFour,
        population_size: int = 100,
        max_generations: int = 100,
        mutation_rate: float = 0.15,
        crossover_rate: float = 0.8,
        elite_size: int = 10
    ):
        self.pokemon_database = pokemon_database
        self.elite_four = elite_four
        self.smart_battle_system = SmartBattleSystem()
        self.data_processor = DataProcessor()
        
        # Parâmetros do algoritmo genético
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_size = elite_size
        
        # Histórico de fitness
        self.fitness_history = []
        
        # Estratégias de movimento para testar
        self.move_strategies = [
            MoveStrategy.BALANCED,
            MoveStrategy.TYPE_EFFECTIVE,
            MoveStrategy.HIGHEST_DAMAGE,
            MoveStrategy.STATUS_FIRST
        ]
    
    def create_smart_team(self) -> PokemonTeam:
        """Cria uma equipe inteligente com balanceamento de tipos"""
        team_pokemon = []
        
        # Tipos prioritários para cobertura
        priority_types = [
            PokemonType.WATER, PokemonType.FIRE, PokemonType.GRASS,
            PokemonType.ELECTRIC, PokemonType.PSYCHIC, PokemonType.DRAGON
        ]
        
        # Adiciona Pokémon de tipos prioritários
        for pokemon_type in priority_types:
            candidates = [p for p in self.pokemon_database 
                         if p.type1 == pokemon_type or p.type2 == pokemon_type]
            if candidates:
                pokemon = random.choice(candidates)
                if pokemon not in team_pokemon:
                    team_pokemon.append(pokemon)
        
        # Completa com Pokémon aleatórios se necessário
        while len(team_pokemon) < 6:
            available = [p for p in self.pokemon_database if p not in team_pokemon]
            if available:
                team_pokemon.append(random.choice(available))
            else:
                break
        
        return PokemonTeam(team_pokemon)
    
    def create_initial_population(self) -> List[PokemonTeam]:
        """Cria população inicial com diversidade"""
        population = []
        
        # 50% equipes inteligentes
        for _ in range(self.population_size // 2):
            team = self.create_smart_team()
            population.append(team)
        
        # 50% equipes aleatórias
        for _ in range(self.population_size - len(population)):
            team = self.create_random_team()
            population.append(team)
        
        return population
    
    def create_random_team(self) -> PokemonTeam:
        """Cria uma equipe aleatória"""
        team_pokemon = random.sample(self.pokemon_database, min(6, len(self.pokemon_database)))
        return PokemonTeam(team_pokemon)
    
    def calculate_advanced_fitness(self, team: PokemonTeam) -> float:
        """Calcula fitness avançado considerando múltiplos fatores"""
        
        # Ajusta níveis para competir com Elite Four
        for pokemon in team.pokemon:
            pokemon.level = 60
        
        # 1. Performance em batalhas (peso maior - 50%)
        battle_score = self._calculate_advanced_battle_performance(team)
        
        # 2. Análise de tipos e cobertura (20%)
        type_score = self._calculate_type_coverage_score(team)
        
        # 3. Balanceamento estatístico (15%)
        balance_score = self._calculate_stat_balance_score(team)
        
        # 4. Diversidade de estratégias (10%)
        strategy_score = self._calculate_strategy_diversity_score(team)
        
        # 5. Resistências e fraquezas (5%)
        resistance_score = self._calculate_resistance_score(team)
        
        # Score final ponderado
        total_score = (
            battle_score * 0.50 +
            type_score * 0.20 +
            balance_score * 0.15 +
            strategy_score * 0.10 +
            resistance_score * 0.05
        )
        
        return total_score
    
    def _calculate_advanced_battle_performance(self, team: PokemonTeam) -> float:
        """Calcula performance avançada em batalhas"""
        
        total_wins = 0
        total_battles = 0
        strategy_performance = {}
        
        # Testa contra cada membro da Elite Four
        for member in self.elite_four.get_all_members():
            member_wins = 0
            member_battles = 0
            
            # Testa múltiplas estratégias
            for strategy in self.move_strategies:
                for _ in range(3):  # 3 simulações por estratégia
                    battle_log = self.smart_battle_system.battle_teams_smart(
                        team, member.pokemon_team, strategy, MoveStrategy.BALANCED
                    )
                    
                    total_battles += 1
                    member_battles += 1
                    
                    if battle_log.battle_result.value == "Win":
                        total_wins += 1
                        member_wins += 1
                
                # Performance por estratégia
                strategy_key = f"{member.name}_{strategy.value}"
                strategy_performance[strategy_key] = member_wins / member_battles if member_battles > 0 else 0
            
            # Performance por membro
            member_performance = member_wins / member_battles if member_battles > 0 else 0
        
        return total_wins / total_battles if total_battles > 0 else 0
    
    def _calculate_type_coverage_score(self, team: PokemonTeam) -> float:
        """Calcula score de cobertura de tipos"""
        all_types = set()
        
        for pokemon in team.pokemon:
            all_types.add(pokemon.type1)
            if pokemon.type2:
                all_types.add(pokemon.type2)
        
        # Score baseado na diversidade de tipos
        type_diversity = len(all_types) / 18  # 18 tipos possíveis
        
        # Bonus por tipos importantes
        important_types = {
            PokemonType.WATER, PokemonType.FIRE, PokemonType.GRASS,
            PokemonType.ELECTRIC, PokemonType.PSYCHIC, PokemonType.DRAGON,
            PokemonType.GROUND, PokemonType.FLYING, PokemonType.ICE
        }
        
        important_coverage = len(all_types.intersection(important_types)) / len(important_types)
        
        return (type_diversity * 0.6) + (important_coverage * 0.4)
    
    def _calculate_stat_balance_score(self, team: PokemonTeam) -> float:
        """Calcula score de balanceamento estatístico"""
        if not team.pokemon:
            return 0
        
        # Coleta estatísticas
        hp_values = [p.stats.hp for p in team.pokemon]
        attack_values = [p.stats.attack for p in team.pokemon]
        defense_values = [p.stats.defense for p in team.pokemon]
        sp_attack_values = [p.stats.sp_attack for p in team.pokemon]
        sp_defense_values = [p.stats.sp_defense for p in team.pokemon]
        speed_values = [p.stats.speed for p in team.pokemon]
        
        # Calcula coeficiente de variação (menor = mais balanceado)
        def cv(values):
            if not values or np.mean(values) == 0:
                return 1.0
            return np.std(values) / np.mean(values)
        
        cvs = [cv(hp_values), cv(attack_values), cv(defense_values),
               cv(sp_attack_values), cv(sp_defense_values), cv(speed_values)]
        
        # Score baseado na média dos CVs (invertido)
        avg_cv = np.mean(cvs)
        balance_score = max(0, 1 - avg_cv)
        
        return balance_score
    
    def _calculate_strategy_diversity_score(self, team: PokemonTeam) -> float:
        """Calcula score de diversidade de estratégias"""
        if not team.pokemon:
            return 0
        
        # Analisa diversidade de movesets
        move_types = set()
        move_categories = set()
        
        for pokemon in team.pokemon:
            if pokemon.move_set:
                for move in pokemon.move_set.moves:
                    move_types.add(move.move_type)
                    move_categories.add(move.category)
        
        # Score baseado na diversidade de movimentos
        type_diversity = len(move_types) / 18
        category_diversity = len(move_categories) / 3
        
        return (type_diversity + category_diversity) / 2
    
    def _calculate_resistance_score(self, team: PokemonTeam) -> float:
        """Calcula score de resistências e fraquezas"""
        if not team.pokemon:
            return 0
        
        # Tipos comuns da Elite Four
        elite_four_types = {
            PokemonType.ICE, PokemonType.FIGHTING, PokemonType.GHOST,
            PokemonType.DRAGON, PokemonType.PSYCHIC, PokemonType.NORMAL
        }
        
        resistances = 0
        weaknesses = 0
        
        for pokemon in team.pokemon:
            for elite_type in elite_four_types:
                # Simplificado - pode ser expandido com matriz de efetividade
                if self._is_resistant(pokemon, elite_type):
                    resistances += 1
                elif self._is_weak(pokemon, elite_type):
                    weaknesses += 1
        
        # Score baseado na relação resistências/fraquezas
        if resistances + weaknesses == 0:
            return 0.5
        
        return resistances / (resistances + weaknesses)
    
    def _is_resistant(self, pokemon: Pokemon, attack_type: PokemonType) -> bool:
        """Verifica se o Pokémon é resistente ao tipo de ataque"""
        # Implementação simplificada - pode ser expandida
        resistances = {
            PokemonType.WATER: [PokemonType.WATER, PokemonType.GRASS, PokemonType.DRAGON],
            PokemonType.FIRE: [PokemonType.FIRE, PokemonType.WATER, PokemonType.DRAGON],
            PokemonType.ELECTRIC: [PokemonType.ELECTRIC, PokemonType.GRASS, PokemonType.DRAGON],
            PokemonType.PSYCHIC: [PokemonType.PSYCHIC, PokemonType.DARK],
            PokemonType.DRAGON: [PokemonType.STEEL],
            PokemonType.ICE: [PokemonType.ICE, PokemonType.WATER, PokemonType.STEEL]
        }
        
        if attack_type in resistances:
            return pokemon.type1 in resistances[attack_type] or pokemon.type2 in resistances[attack_type]
        
        return False
    
    def _is_weak(self, pokemon: Pokemon, attack_type: PokemonType) -> bool:
        """Verifica se o Pokémon é fraco ao tipo de ataque"""
        # Implementação simplificada - pode ser expandida
        weaknesses = {
            PokemonType.WATER: [PokemonType.FIRE, PokemonType.GROUND, PokemonType.ROCK],
            PokemonType.FIRE: [PokemonType.GRASS, PokemonType.ICE, PokemonType.BUG, PokemonType.STEEL],
            PokemonType.ELECTRIC: [PokemonType.WATER, PokemonType.FLYING],
            PokemonType.PSYCHIC: [PokemonType.FIGHTING, PokemonType.POISON],
            PokemonType.DRAGON: [PokemonType.DRAGON],
            PokemonType.ICE: [PokemonType.GRASS, PokemonType.GROUND, PokemonType.FLYING, PokemonType.DRAGON]
        }
        
        if attack_type in weaknesses:
            return pokemon.type1 in weaknesses[attack_type] or pokemon.type2 in weaknesses[attack_type]
        
        return False
    
    def optimize_team_advanced(self) -> AdvancedOptimizationResult:
        """Executa otimização avançada da equipe"""
        
        # Cria população inicial
        population = self.create_initial_population()
        
        # Avalia fitness inicial
        for team in population:
            team.fitness = self.calculate_advanced_fitness(team)
        
        best_team = max(population, key=lambda t: t.fitness)
        best_score = best_team.fitness
        
        print(f"Geração 0 - Melhor Fitness: {best_score:.4f}")
        
        # Evolução
        for generation in range(1, self.max_generations + 1):
            # Seleção, cruzamento e mutação
            new_population = self._evolve_population(population)
            
            # Avalia nova população
            for team in new_population:
                team.fitness = self.calculate_advanced_fitness(team)
            
            # Atualiza melhor equipe
            generation_best = max(new_population, key=lambda t: t.fitness)
            if generation_best.fitness > best_score:
                best_team = generation_best
                best_score = generation_best.fitness
            
            # Registra histórico
            self.fitness_history.append(best_score)
            
            # Log de progresso
            if generation % 10 == 0 or generation == 1:
                print(f"Geração {generation} - Melhor Fitness: {best_score:.4f}")
            
            # Atualiza população
            population = new_population
        
        # Calcula métricas finais
        team_performance = self._calculate_team_performance_metrics(best_team)
        move_strategy_performance = self._calculate_strategy_performance_metrics(best_team)
        individual_performance = self._calculate_individual_performance_metrics(best_team)
        optimization_metrics = self._calculate_optimization_metrics()
        
        return AdvancedOptimizationResult(
            best_team=best_team,
            best_score=best_score,
            generation=self.max_generations,
            fitness_history=self.fitness_history,
            team_performance=team_performance,
            move_strategy_performance=move_strategy_performance,
            individual_performance=individual_performance,
            optimization_metrics=optimization_metrics
        )
    
    def _evolve_population(self, population: List[PokemonTeam]) -> List[PokemonTeam]:
        """Evolui a população através de seleção, cruzamento e mutação"""
        new_population = []
        
        # Elitismo - mantém os melhores
        sorted_population = sorted(population, key=lambda t: t.fitness, reverse=True)
        elite = sorted_population[:self.elite_size]
        new_population.extend(elite)
        
        # Gera novos indivíduos
        while len(new_population) < self.population_size:
            # Seleção por torneio
            parent1 = self._tournament_selection(population)
            parent2 = self._tournament_selection(population)
            
            # Cruzamento
            if random.random() < self.crossover_rate:
                child1, child2 = self._crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            
            # Mutação
            if random.random() < self.mutation_rate:
                child1 = self._mutate(child1)
            if random.random() < self.mutation_rate:
                child2 = self._mutate(child2)
            
            new_population.extend([child1, child2])
        
        return new_population[:self.population_size]
    
    def _tournament_selection(self, population: List[PokemonTeam], tournament_size: int = 3) -> PokemonTeam:
        """Seleção por torneio"""
        tournament = random.sample(population, min(tournament_size, len(population)))
        return max(tournament, key=lambda t: t.fitness)
    
    def _crossover(self, parent1: PokemonTeam, parent2: PokemonTeam) -> Tuple[PokemonTeam, PokemonTeam]:
        """Cruzamento uniforme"""
        child1_pokemon = []
        child2_pokemon = []
        
        # Cruzamento uniforme
        for i in range(6):
            if random.random() < 0.5:
                if i < len(parent1.pokemon):
                    child1_pokemon.append(parent1.pokemon[i])
                if i < len(parent2.pokemon):
                    child2_pokemon.append(parent2.pokemon[i])
            else:
                if i < len(parent2.pokemon):
                    child1_pokemon.append(parent2.pokemon[i])
                if i < len(parent1.pokemon):
                    child2_pokemon.append(parent1.pokemon[i])
        
        # Remove duplicatas e completa se necessário
        child1_pokemon = self._remove_duplicates_and_complete(child1_pokemon)
        child2_pokemon = self._remove_duplicates_and_complete(child2_pokemon)
        
        return PokemonTeam(child1_pokemon), PokemonTeam(child2_pokemon)
    
    def _mutate(self, team: PokemonTeam) -> PokemonTeam:
        """Mutação por substituição"""
        if not team.pokemon:
            return team
        
        # Seleciona Pokémon aleatório para substituir
        replace_index = random.randint(0, len(team.pokemon) - 1)
        
        # Encontra substituto que não está na equipe
        available = [p for p in self.pokemon_database if p not in team.pokemon]
        if available:
            team.pokemon[replace_index] = random.choice(available)
        
        return team
    
    def _remove_duplicates_and_complete(self, pokemon_list: List[Pokemon]) -> List[Pokemon]:
        """Remove duplicatas e completa a lista se necessário"""
        unique_pokemon = []
        seen = set()
        
        for pokemon in pokemon_list:
            if pokemon not in seen:
                unique_pokemon.append(pokemon)
                seen.add(pokemon)
        
        # Completa até 6 Pokémon se necessário
        while len(unique_pokemon) < 6:
            available = [p for p in self.pokemon_database if p not in seen]
            if available:
                pokemon = random.choice(available)
                unique_pokemon.append(pokemon)
                seen.add(pokemon)
            else:
                break
        
        return unique_pokemon[:6]
    
    def _calculate_team_performance_metrics(self, team: PokemonTeam) -> Dict[str, float]:
        """Calcula métricas de performance da equipe"""
        # Implementação simplificada
        return {
            "overall_win_rate": 0.0,
            "avg_turns": 0.0,
            "consistency": 0.0
        }
    
    def _calculate_strategy_performance_metrics(self, team: PokemonTeam) -> Dict[str, float]:
        """Calcula métricas de performance por estratégia"""
        # Implementação simplificada
        return {
            "balanced_strategy": 0.0,
            "type_effective_strategy": 0.0,
            "highest_damage_strategy": 0.0,
            "status_first_strategy": 0.0
        }
    
    def _calculate_individual_performance_metrics(self, team: PokemonTeam) -> Dict[str, float]:
        """Calcula métricas de performance individual"""
        # Implementação simplificada
        return {pokemon.name: 0.0 for pokemon in team.pokemon}
    
    def _calculate_optimization_metrics(self) -> Dict[str, float]:
        """Calcula métricas de otimização"""
        if len(self.fitness_history) < 2:
            return {"convergence_rate": 0.0, "improvement_rate": 0.0}
        
        # Taxa de convergência
        convergence_rate = 0.0
        if len(self.fitness_history) > 10:
            recent_improvement = self.fitness_history[-1] - self.fitness_history[-10]
            convergence_rate = max(0, 1 - abs(recent_improvement) / self.fitness_history[-1])
        
        # Taxa de melhoria
        total_improvement = self.fitness_history[-1] - self.fitness_history[0]
        improvement_rate = total_improvement / self.fitness_history[0] if self.fitness_history[0] > 0 else 0
        
        return {
            "convergence_rate": convergence_rate,
            "improvement_rate": improvement_rate,
            "final_fitness": self.fitness_history[-1],
            "generations": len(self.fitness_history)
        }
