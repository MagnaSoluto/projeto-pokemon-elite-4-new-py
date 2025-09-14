"""
Sistema de Batalhas Inteligente - Seleção estratégica de movimentos
"""

import random
import math
from typing import List, Optional, Tuple, Dict
from dataclasses import dataclass
from enum import Enum
from .pokemon import Pokemon, PokemonTeam, PokemonType
from .moves import Move, MoveCategory, MoveTarget
from .battle_system import BattleSystem, BattleResult, BattleLog, BattleTurn


class MoveStrategy(Enum):
    """Estratégias de seleção de movimentos"""
    RANDOM = "random"
    HIGHEST_DAMAGE = "highest_damage"
    TYPE_EFFECTIVE = "type_effective"
    STATUS_FIRST = "status_first"
    BALANCED = "balanced"


@dataclass
class MoveChoice:
    """Escolha de movimento com justificativa"""
    move: Move
    expected_damage: float
    type_effectiveness: float
    strategy: MoveStrategy
    confidence: float


class SmartBattleSystem(BattleSystem):
    """Sistema de batalhas com seleção inteligente de movimentos"""
    
    def __init__(self):
        super().__init__()
        self.move_strategies = {
            MoveStrategy.RANDOM: self._select_random_move,
            MoveStrategy.HIGHEST_DAMAGE: self._select_highest_damage_move,
            MoveStrategy.TYPE_EFFECTIVE: self._select_type_effective_move,
            MoveStrategy.STATUS_FIRST: self._select_status_first_move,
            MoveStrategy.BALANCED: self._select_balanced_move
        }
    
    def select_optimal_move(
        self,
        attacker: Pokemon,
        defender: Pokemon,
        available_moves: List[Move],
        strategy: MoveStrategy = MoveStrategy.BALANCED
    ) -> MoveChoice:
        """Seleciona o melhor movimento baseado na estratégia"""
        
        if not available_moves:
            # Fallback para movimento básico
            return MoveChoice(
                move=Move("Tackle", PokemonType.NORMAL, MoveCategory.PHYSICAL, 40, 100, 35),
                expected_damage=0,
                type_effectiveness=1.0,
                strategy=strategy,
                confidence=0.0
            )
        
        # Aplica estratégia
        move_selector = self.move_strategies.get(strategy, self._select_balanced_move)
        selected_move = move_selector(attacker, defender, available_moves)
        
        # Calcula métricas do movimento
        expected_damage = self._calculate_expected_damage(attacker, defender, selected_move)
        type_effectiveness = self._calculate_type_effectiveness(selected_move, defender)
        confidence = self._calculate_move_confidence(attacker, defender, selected_move)
        
        return MoveChoice(
            move=selected_move,
            expected_damage=expected_damage,
            type_effectiveness=type_effectiveness,
            strategy=strategy,
            confidence=confidence
        )
    
    def _select_random_move(self, attacker: Pokemon, defender: Pokemon, moves: List[Move]) -> Move:
        """Seleção aleatória (comportamento original)"""
        return random.choice(moves)
    
    def _select_highest_damage_move(self, attacker: Pokemon, defender: Pokemon, moves: List[Move]) -> Move:
        """Seleciona movimento com maior dano esperado"""
        best_move = moves[0]
        best_damage = 0
        
        for move in moves:
            if move.category == MoveCategory.STATUS:
                continue  # Pula movimentos de status
            
            expected_damage = self._calculate_expected_damage(attacker, defender, move)
            if expected_damage > best_damage:
                best_damage = expected_damage
                best_move = move
        
        return best_move
    
    def _select_type_effective_move(self, attacker: Pokemon, defender: Pokemon, moves: List[Move]) -> Move:
        """Seleciona movimento mais efetivo contra o tipo do defensor"""
        best_move = moves[0]
        best_effectiveness = 0
        
        for move in moves:
            if move.category == MoveCategory.STATUS:
                continue
            
            effectiveness = self._calculate_type_effectiveness(move, defender)
            if effectiveness > best_effectiveness:
                best_effectiveness = effectiveness
                best_move = move
        
        return best_move
    
    def _select_status_first_move(self, attacker: Pokemon, defender: Pokemon, moves: List[Move]) -> Move:
        """Prioriza movimentos de status, depois de dano"""
        status_moves = [move for move in moves if move.category == MoveCategory.STATUS]
        damage_moves = [move for move in moves if move.category != MoveCategory.STATUS]
        
        if status_moves and not self._has_status_advantage(attacker, defender):
            return random.choice(status_moves)
        elif damage_moves:
            return self._select_type_effective_move(attacker, defender, damage_moves)
        else:
            return random.choice(moves)
    
    def _select_balanced_move(self, attacker: Pokemon, defender: Pokemon, moves: List[Move]) -> Move:
        """Seleção balanceada considerando múltiplos fatores"""
        move_scores = []
        
        for move in moves:
            score = 0
            
            # Fator de dano (40%)
            if move.category != MoveCategory.STATUS:
                expected_damage = self._calculate_expected_damage(attacker, defender, move)
                score += (expected_damage / 200) * 0.4  # Normaliza para 0-1
            
            # Fator de efetividade (30%)
            effectiveness = self._calculate_type_effectiveness(move, defender)
            score += effectiveness * 0.3
            
            # Fator de precisão (20%)
            accuracy_factor = move.accuracy / 100
            score += accuracy_factor * 0.2
            
            # Fator de PP (10%)
            pp_factor = move.pp / 40  # Normaliza para 0-1
            score += pp_factor * 0.1
            
            move_scores.append((move, score))
        
        # Seleciona movimento com maior score
        move_scores.sort(key=lambda x: x[1], reverse=True)
        return move_scores[0][0]
    
    def _calculate_expected_damage(self, attacker: Pokemon, defender: Pokemon, move: Move) -> float:
        """Calcula dano esperado de um movimento"""
        if move.category == MoveCategory.STATUS:
            return 0
        
        # Determina estatísticas
        if move.category == MoveCategory.PHYSICAL:
            attack_stat = attacker.attack
            defense_stat = defender.defense
        else:  # SPECIAL
            attack_stat = attacker.sp_attack
            defense_stat = defender.sp_defense
        
        # Fórmula de dano GBA
        base_damage = ((2 * attacker.level + 10) * move.power * 
                      attack_stat / defense_stat / 50) + 2
        
        # Modificadores
        effectiveness = self._calculate_type_effectiveness(move, defender)
        critical_chance = self._calculate_critical_chance(attacker, move)
        critical_modifier = 1 + critical_chance  # Chance de crítico
        
        expected_damage = base_damage * effectiveness * critical_modifier * 0.925  # Variação média
        
        return expected_damage
    
    def _calculate_type_effectiveness(self, move: Move, defender: Pokemon) -> float:
        """Calcula efetividade do movimento contra o defensor"""
        from .battle_system import TypeEffectiveness
        return TypeEffectiveness.get_effectiveness(move.move_type, defender.get_types())
    
    def _calculate_critical_chance(self, attacker: Pokemon, move: Move) -> float:
        """Calcula chance de golpe crítico"""
        base_crit_rate = 6.25  # 1/16
        speed_modifier = min(attacker.speed / 512, 1.0)
        return (base_crit_rate * (1 + speed_modifier)) / 100
    
    def _calculate_move_confidence(self, attacker: Pokemon, defender: Pokemon, move: Move) -> float:
        """Calcula confiança na escolha do movimento"""
        if move.category == MoveCategory.STATUS:
            return 0.8  # Alta confiança em status
        
        effectiveness = self._calculate_type_effectiveness(move, defender)
        accuracy = move.accuracy / 100
        
        # Confiança baseada em efetividade e precisão
        confidence = (effectiveness * 0.6) + (accuracy * 0.4)
        return min(confidence, 1.0)
    
    def _has_status_advantage(self, attacker: Pokemon, defender: Pokemon) -> bool:
        """Verifica se o atacante já tem vantagem de status"""
        # Implementação simplificada - pode ser expandida
        return False
    
    def battle_pokemon_smart(
        self,
        pokemon1: Pokemon,
        pokemon2: Pokemon,
        pokemon1_strategy: MoveStrategy = MoveStrategy.BALANCED,
        pokemon2_strategy: MoveStrategy = MoveStrategy.BALANCED
    ) -> BattleLog:
        """Batalha entre dois Pokémon com seleção inteligente de movimentos"""
        
        # Carrega movesets se necessário
        if pokemon1.move_set is None:
            from .moves import create_realistic_moveset
            pokemon1.move_set = create_realistic_moveset(pokemon1.name)
        
        if pokemon2.move_set is None:
            from .moves import create_realistic_moveset
            pokemon2.move_set = create_realistic_moveset(pokemon2.name)
        
        # Movimentos disponíveis
        pokemon1_moves = [move for move in pokemon1.move_set.moves if move.category != MoveCategory.STATUS]
        pokemon2_moves = [move for move in pokemon2.move_set.moves if move.category != MoveCategory.STATUS]
        
        turns = []
        turn_number = 1
        
        # Loop principal da batalha
        while (not pokemon1.is_fainted and not pokemon2.is_fainted and 
               turn_number <= self.max_turns):
            
            # Determina ordem de ataque
            if pokemon1.speed >= pokemon2.speed:
                first_attacker, second_attacker = pokemon1, pokemon2
                first_moves, second_moves = pokemon1_moves, pokemon2_moves
                first_strategy, second_strategy = pokemon1_strategy, pokemon2_strategy
            else:
                first_attacker, second_attacker = pokemon2, pokemon1
                first_moves, second_moves = pokemon2_moves, pokemon1_moves
                first_strategy, second_strategy = pokemon2_strategy, pokemon1_strategy
            
            # Primeiro ataque
            if not first_attacker.is_fainted and not second_attacker.is_fainted:
                move_choice = self.select_optimal_move(
                    first_attacker, second_attacker, first_moves, first_strategy
                )
                turn = self.execute_turn(first_attacker, second_attacker, move_choice.move, turn_number)
                turns.append(turn)
                
                if second_attacker.is_fainted:
                    break
            
            # Segundo ataque
            if not first_attacker.is_fainted and not second_attacker.is_fainted:
                move_choice = self.select_optimal_move(
                    second_attacker, first_attacker, second_moves, second_strategy
                )
                turn = self.execute_turn(second_attacker, first_attacker, move_choice.move, turn_number)
                turns.append(turn)
            
            turn_number += 1
        
        # Determina vencedor
        if pokemon1.is_fainted and pokemon2.is_fainted:
            result = BattleResult.DRAW
            winner = None
        elif pokemon1.is_fainted:
            result = BattleResult.LOSS
            winner = None
        else:
            result = BattleResult.WIN
            winner = None
        
        return BattleLog(
            turns=turns,
            winner=winner,
            total_turns=turn_number - 1,
            battle_result=result
        )
    
    def battle_teams_smart(
        self,
        team1: PokemonTeam,
        team2: PokemonTeam,
        team1_strategy: MoveStrategy = MoveStrategy.BALANCED,
        team2_strategy: MoveStrategy = MoveStrategy.BALANCED
    ) -> BattleLog:
        """Batalha entre equipes com seleção inteligente de movimentos"""
        
        # Restaura equipes
        team1.restore_team()
        team2.restore_team()
        
        turns = []
        turn_number = 1
        
        # Loop principal da batalha
        while (not team1.is_defeated and not team2.is_defeated and 
               turn_number <= self.max_turns):
            
            # Pokémon ativos
            pokemon1 = team1.active_pokemon
            pokemon2 = team2.active_pokemon
            
            if pokemon1 is None or pokemon2 is None:
                break
            
            # Batalha inteligente entre os Pokémon ativos
            pokemon_battle = self.battle_pokemon_smart(
                pokemon1, pokemon2, team1_strategy, team2_strategy
            )
            turns.extend(pokemon_battle.turns)
            
            # Troca automática se necessário
            if pokemon1.is_fainted:
                team1.auto_switch()
            if pokemon2.is_fainted:
                team2.auto_switch()
            
            turn_number += 1
        
        # Determina vencedor
        if team1.is_defeated and team2.is_defeated:
            result = BattleResult.DRAW
            winner = None
        elif team1.is_defeated:
            result = BattleResult.LOSS
            winner = team2
        else:
            result = BattleResult.WIN
            winner = team1
        
        return BattleLog(
            turns=turns,
            winner=winner,
            total_turns=turn_number - 1,
            battle_result=result
        )
