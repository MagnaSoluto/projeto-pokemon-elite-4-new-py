"""
Analisador de Batalhas - Análise detalhada de performance e estratégias
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from ..core.pokemon import Pokemon, PokemonTeam
from ..core.battle_system import BattleSystem, BattleLog, BattleResult
from ..core.elite_four import EliteFour, EliteFourMember


@dataclass
class BattleStatistics:
    """Estatísticas de batalha"""
    total_battles: int
    wins: int
    losses: int
    draws: int
    win_rate: float
    avg_turns: float
    avg_damage_dealt: float
    avg_damage_taken: float


@dataclass
class PokemonPerformance:
    """Performance de um Pokémon específico"""
    pokemon: Pokemon
    battles_participated: int
    wins: int
    losses: int
    win_rate: float
    avg_damage_dealt: float
    avg_damage_taken: float
    most_effective_against: List[str]
    least_effective_against: List[str]


class BattleAnalyzer:
    """Analisador de batalhas e performance"""
    
    def __init__(self, battle_system: BattleSystem, elite_four: EliteFour):
        self.battle_system = battle_system
        self.elite_four = elite_four
    
    def analyze_team_performance(
        self, 
        team: PokemonTeam, 
        num_simulations: int = 100
    ) -> Dict[str, BattleStatistics]:
        """Analisa performance da equipe contra Elite Four"""
        
        results = {}
        
        for member in self.elite_four.get_all_members():
            print(f"Analisando performance contra {member.name}...")
            
            # Simula batalhas
            battle_logs = []
            for _ in range(num_simulations):
                battle_log = self.battle_system.battle_teams(team, member.pokemon_team)
                battle_logs.append(battle_log)
            
            # Calcula estatísticas
            stats = self._calculate_battle_statistics(battle_logs)
            results[member.name] = stats
        
        return results
    
    def _calculate_battle_statistics(self, battle_logs: List[BattleLog]) -> BattleStatistics:
        """Calcula estatísticas de uma lista de batalhas"""
        
        total_battles = len(battle_logs)
        wins = sum(1 for log in battle_logs if log.battle_result == BattleResult.WIN)
        losses = sum(1 for log in battle_logs if log.battle_result == BattleResult.LOSS)
        draws = sum(1 for log in battle_logs if log.battle_result == BattleResult.DRAW)
        
        win_rate = wins / total_battles if total_battles > 0 else 0
        
        # Calcula turnos médios
        avg_turns = np.mean([log.total_turns for log in battle_logs])
        
        # Calcula dano médio
        total_damage_dealt = 0
        total_damage_taken = 0
        
        for log in battle_logs:
            for turn in log.turns:
                total_damage_dealt += turn.damage_dealt
        
        avg_damage_dealt = total_damage_dealt / total_battles if total_battles > 0 else 0
        avg_damage_taken = total_damage_taken / total_battles if total_battles > 0 else 0
        
        return BattleStatistics(
            total_battles=total_battles,
            wins=wins,
            losses=losses,
            draws=draws,
            win_rate=win_rate,
            avg_turns=avg_turns,
            avg_damage_dealt=avg_damage_dealt,
            avg_damage_taken=avg_damage_taken
        )
    
    def analyze_pokemon_performance(
        self, 
        pokemon: Pokemon, 
        opponent_team: PokemonTeam,
        num_simulations: int = 50
    ) -> PokemonPerformance:
        """Analisa performance de um Pokémon específico"""
        
        battles_participated = 0
        wins = 0
        losses = 0
        total_damage_dealt = 0
        total_damage_taken = 0
        
        # Cria equipe com apenas este Pokémon
        test_team = PokemonTeam([pokemon])
        
        for _ in range(num_simulations):
            battle_log = self.battle_system.battle_teams(test_team, opponent_team)
            battles_participated += 1
            
            if battle_log.battle_result == BattleResult.WIN:
                wins += 1
            else:
                losses += 1
            
            # Calcula dano
            for turn in battle_log.turns:
                if turn.attacker == pokemon:
                    total_damage_dealt += turn.damage_dealt
                if turn.defender == pokemon:
                    total_damage_taken += turn.damage_dealt
        
        win_rate = wins / battles_participated if battles_participated > 0 else 0
        avg_damage_dealt = total_damage_dealt / battles_participated if battles_participated > 0 else 0
        avg_damage_taken = total_damage_taken / battles_participated if battles_participated > 0 else 0
        
        # Analisa efetividade contra diferentes tipos
        most_effective, least_effective = self._analyze_type_effectiveness(pokemon, opponent_team)
        
        return PokemonPerformance(
            pokemon=pokemon,
            battles_participated=battles_participated,
            wins=wins,
            losses=losses,
            win_rate=win_rate,
            avg_damage_dealt=avg_damage_dealt,
            avg_damage_taken=avg_damage_taken,
            most_effective_against=most_effective,
            least_effective_against=least_effective
        )
    
    def _analyze_type_effectiveness(
        self, 
        pokemon: Pokemon, 
        opponent_team: PokemonTeam
    ) -> Tuple[List[str], List[str]]:
        """Analisa efetividade contra tipos específicos"""
        
        from ..core.battle_system import TypeEffectiveness
        
        type_performance = {}
        
        for opponent_pokemon in opponent_team.pokemon:
            for opponent_type in opponent_pokemon.get_types():
                type_name = opponent_type.value
                
                if type_name not in type_performance:
                    type_performance[type_name] = []
                
                # Calcula efetividade dos movimentos
                max_effectiveness = 0
                for move in pokemon.move_set.moves:
                    if move.category.value != "Status":
                        effectiveness = TypeEffectiveness.get_effectiveness(
                            move.move_type, 
                            [opponent_type]
                        )
                        max_effectiveness = max(max_effectiveness, effectiveness)
                
                type_performance[type_name].append(max_effectiveness)
        
        # Calcula média de efetividade por tipo
        avg_effectiveness = {}
        for type_name, effectiveness_list in type_performance.items():
            avg_effectiveness[type_name] = np.mean(effectiveness_list)
        
        # Ordena por efetividade
        sorted_types = sorted(avg_effectiveness.items(), key=lambda x: x[1], reverse=True)
        
        most_effective = [type_name for type_name, _ in sorted_types[:3]]
        least_effective = [type_name for type_name, _ in sorted_types[-3:]]
        
        return most_effective, least_effective
    
    def find_optimal_levels(
        self, 
        team: PokemonTeam, 
        level_range: Tuple[int, int] = (50, 80),
        step: int = 5
    ) -> Dict[str, int]:
        """Encontra níveis ótimos para cada Pokémon da equipe"""
        
        optimal_levels = {}
        
        for pokemon in team.pokemon:
            print(f"Otimizando nível para {pokemon.name}...")
            
            best_level = pokemon.level
            best_performance = 0
            
            for level in range(level_range[0], level_range[1] + 1, step):
                # Cria cópia do Pokémon com novo nível
                test_pokemon = Pokemon(
                    name=pokemon.name,
                    pokemon_id=pokemon.pokemon_id,
                    type1=pokemon.type1,
                    type2=pokemon.type2,
                    stats=pokemon.stats,
                    level=level
                )
                test_pokemon.move_set = pokemon.move_set
                
                # Testa contra Elite Four
                test_team = PokemonTeam([test_pokemon])
                performance = 0
                
                for member in self.elite_four.get_all_members():
                    battle_stats = self.battle_system.simulate_battle(
                        test_team, 
                        member.pokemon_team, 
                        20
                    )
                    performance += battle_stats['win_rate']
                
                if performance > best_performance:
                    best_performance = performance
                    best_level = level
            
            optimal_levels[pokemon.name] = best_level
        
        return optimal_levels
    
    def generate_battle_report(
        self, 
        team: PokemonTeam, 
        num_simulations: int = 100
    ) -> Dict[str, any]:
        """Gera relatório completo de batalhas"""
        
        print("Gerando relatório de batalhas...")
        
        # Análise geral da equipe
        team_performance = self.analyze_team_performance(team, num_simulations)
        
        # Análise individual de cada Pokémon
        individual_performance = {}
        for pokemon in team.pokemon:
            print(f"Analisando {pokemon.name}...")
            
            # Testa contra cada membro da Elite Four
            pokemon_stats = {}
            for member in self.elite_four.get_all_members():
                performance = self.analyze_pokemon_performance(
                    pokemon, 
                    member.pokemon_team, 
                    num_simulations // 5
                )
                pokemon_stats[member.name] = performance
            
            individual_performance[pokemon.name] = pokemon_stats
        
        # Encontra níveis ótimos
        optimal_levels = self.find_optimal_levels(team)
        
        # Calcula estatísticas gerais
        overall_win_rate = np.mean([stats.win_rate for stats in team_performance.values()])
        overall_avg_turns = np.mean([stats.avg_turns for stats in team_performance.values()])
        
        # Identifica membros mais difíceis
        difficulty_ranking = sorted(
            team_performance.items(), 
            key=lambda x: x[1].win_rate
        )
        
        return {
            'team_overview': {
                'overall_win_rate': overall_win_rate,
                'overall_avg_turns': overall_avg_turns,
                'team_size': len(team.pokemon)
            },
            'member_performance': team_performance,
            'individual_performance': individual_performance,
            'optimal_levels': optimal_levels,
            'difficulty_ranking': difficulty_ranking,
            'recommendations': self._generate_recommendations(team_performance, individual_performance)
        }
    
    def _generate_recommendations(
        self, 
        team_performance: Dict[str, BattleStatistics],
        individual_performance: Dict[str, Dict[str, PokemonPerformance]]
    ) -> List[str]:
        """Gera recomendações baseadas na análise"""
        
        recommendations = []
        
        # Analisa membros mais difíceis
        difficult_members = [
            member for member, stats in team_performance.items() 
            if stats.win_rate < 0.5
        ]
        
        if difficult_members:
            recommendations.append(
                f"Considere melhorar estratégias contra: {', '.join(difficult_members)}"
            )
        
        # Analisa Pokémon com baixa performance
        for pokemon_name, member_stats in individual_performance.items():
            avg_win_rate = np.mean([stats.win_rate for stats in member_stats.values()])
            if avg_win_rate < 0.3:
                recommendations.append(
                    f"Considere substituir {pokemon_name} (taxa de vitória: {avg_win_rate:.2%})"
                )
        
        # Recomendações gerais
        overall_win_rate = np.mean([stats.win_rate for stats in team_performance.values()])
        
        if overall_win_rate < 0.4:
            recommendations.append("Equipe precisa de melhorias significativas")
        elif overall_win_rate < 0.6:
            recommendations.append("Equipe tem potencial, mas pode ser otimizada")
        else:
            recommendations.append("Equipe está bem balanceada!")
        
        return recommendations
    
    def export_analysis_to_csv(
        self, 
        analysis: Dict[str, any], 
        filename: str = "battle_analysis"
    ) -> None:
        """Exporta análise para CSV"""
        
        # Exporta performance da equipe
        team_data = []
        for member, stats in analysis['member_performance'].items():
            team_data.append({
                'member': member,
                'win_rate': stats.win_rate,
                'avg_turns': stats.avg_turns,
                'avg_damage_dealt': stats.avg_damage_dealt,
                'avg_damage_taken': stats.avg_damage_taken
            })
        
        df_team = pd.DataFrame(team_data)
        df_team.to_csv(f"{filename}_team_performance.csv", index=False)
        
        # Exporta performance individual
        individual_data = []
        for pokemon_name, member_stats in analysis['individual_performance'].items():
            for member, performance in member_stats.items():
                individual_data.append({
                    'pokemon': pokemon_name,
                    'member': member,
                    'win_rate': performance.win_rate,
                    'avg_damage_dealt': performance.avg_damage_dealt,
                    'avg_damage_taken': performance.avg_damage_taken
                })
        
        df_individual = pd.DataFrame(individual_data)
        df_individual.to_csv(f"{filename}_individual_performance.csv", index=False)
        
        print(f"Análise exportada para {filename}_team_performance.csv e {filename}_individual_performance.csv")
