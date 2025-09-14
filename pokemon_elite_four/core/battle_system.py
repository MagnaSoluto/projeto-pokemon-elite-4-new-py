"""
Sistema de Batalhas Pokémon - Game Boy Advanced
Baseado no sistema de FireRed/LeafGreen com precisão máxima
"""

import random
import math
from typing import List, Optional, Tuple, Dict
from dataclasses import dataclass
from enum import Enum
from .pokemon import Pokemon, PokemonTeam, PokemonType
from .moves import Move, MoveCategory, MoveTarget


class BattleResult(Enum):
    """Resultados possíveis de uma batalha"""
    WIN = "Win"
    LOSS = "Loss"
    DRAW = "Draw"


@dataclass
class BattleTurn:
    """Informações de um turno de batalha"""
    turn_number: int
    attacker: Pokemon
    defender: Pokemon
    move_used: Move
    damage_dealt: int
    critical_hit: bool
    effectiveness: float
    attacker_fainted: bool
    defender_fainted: bool


@dataclass
class BattleLog:
    """Log completo de uma batalha"""
    turns: List[BattleTurn]
    winner: Optional[PokemonTeam]
    total_turns: int
    battle_result: BattleResult


class TypeEffectiveness:
    """Sistema de efetividade de tipos - GBA FireRed/LeafGreen"""
    
    # Matriz de efetividade (atacante -> defensor)
    EFFECTIVENESS_MATRIX = {
        PokemonType.NORMAL: {
            PokemonType.ROCK: 0.5,
            PokemonType.GHOST: 0.0,
            PokemonType.STEEL: 0.5
        },
        PokemonType.FIRE: {
            PokemonType.FIRE: 0.5,
            PokemonType.WATER: 0.5,
            PokemonType.GRASS: 2.0,
            PokemonType.ICE: 2.0,
            PokemonType.BUG: 2.0,
            PokemonType.ROCK: 0.5,
            PokemonType.DRAGON: 0.5,
            PokemonType.STEEL: 2.0
        },
        PokemonType.WATER: {
            PokemonType.FIRE: 2.0,
            PokemonType.WATER: 0.5,
            PokemonType.GRASS: 0.5,
            PokemonType.GROUND: 2.0,
            PokemonType.ROCK: 2.0,
            PokemonType.DRAGON: 0.5
        },
        PokemonType.ELECTRIC: {
            PokemonType.WATER: 2.0,
            PokemonType.ELECTRIC: 0.5,
            PokemonType.GRASS: 0.5,
            PokemonType.GROUND: 0.0,
            PokemonType.FLYING: 2.0,
            PokemonType.DRAGON: 0.5
        },
        PokemonType.GRASS: {
            PokemonType.FIRE: 0.5,
            PokemonType.WATER: 2.0,
            PokemonType.GRASS: 0.5,
            PokemonType.POISON: 0.5,
            PokemonType.GROUND: 2.0,
            PokemonType.FLYING: 0.5,
            PokemonType.BUG: 0.5,
            PokemonType.ROCK: 2.0,
            PokemonType.DRAGON: 0.5,
            PokemonType.STEEL: 0.5
        },
        PokemonType.ICE: {
            PokemonType.FIRE: 0.5,
            PokemonType.WATER: 0.5,
            PokemonType.GRASS: 2.0,
            PokemonType.ICE: 0.5,
            PokemonType.GROUND: 2.0,
            PokemonType.FLYING: 2.0,
            PokemonType.DRAGON: 2.0,
            PokemonType.STEEL: 0.5
        },
        PokemonType.FIGHTING: {
            PokemonType.NORMAL: 2.0,
            PokemonType.ICE: 2.0,
            PokemonType.POISON: 0.5,
            PokemonType.FLYING: 0.5,
            PokemonType.PSYCHIC: 0.5,
            PokemonType.BUG: 0.5,
            PokemonType.ROCK: 2.0,
            PokemonType.GHOST: 0.0,
            PokemonType.DARK: 2.0,
            PokemonType.STEEL: 2.0
        },
        PokemonType.POISON: {
            PokemonType.GRASS: 2.0,
            PokemonType.POISON: 0.5,
            PokemonType.GROUND: 0.5,
            PokemonType.ROCK: 0.5,
            PokemonType.GHOST: 0.5,
            PokemonType.STEEL: 0.0
        },
        PokemonType.GROUND: {
            PokemonType.FIRE: 2.0,
            PokemonType.ELECTRIC: 2.0,
            PokemonType.GRASS: 0.5,
            PokemonType.POISON: 2.0,
            PokemonType.FLYING: 0.0,
            PokemonType.BUG: 0.5,
            PokemonType.ROCK: 2.0,
            PokemonType.STEEL: 2.0
        },
        PokemonType.FLYING: {
            PokemonType.ELECTRIC: 0.5,
            PokemonType.GRASS: 2.0,
            PokemonType.FIGHTING: 2.0,
            PokemonType.BUG: 2.0,
            PokemonType.ROCK: 0.5,
            PokemonType.STEEL: 0.5
        },
        PokemonType.PSYCHIC: {
            PokemonType.FIGHTING: 2.0,
            PokemonType.POISON: 2.0,
            PokemonType.PSYCHIC: 0.5,
            PokemonType.DARK: 0.0,
            PokemonType.STEEL: 0.5
        },
        PokemonType.BUG: {
            PokemonType.FIRE: 0.5,
            PokemonType.GRASS: 2.0,
            PokemonType.FIGHTING: 0.5,
            PokemonType.POISON: 2.0,
            PokemonType.FLYING: 0.5,
            PokemonType.PSYCHIC: 2.0,
            PokemonType.GHOST: 0.5,
            PokemonType.DARK: 2.0,
            PokemonType.STEEL: 0.5
        },
        PokemonType.ROCK: {
            PokemonType.FIRE: 2.0,
            PokemonType.ICE: 2.0,
            PokemonType.FIGHTING: 0.5,
            PokemonType.GROUND: 0.5,
            PokemonType.FLYING: 2.0,
            PokemonType.BUG: 2.0,
            PokemonType.STEEL: 0.5
        },
        PokemonType.GHOST: {
            PokemonType.NORMAL: 0.0,
            PokemonType.PSYCHIC: 2.0,
            PokemonType.GHOST: 2.0,
            PokemonType.DARK: 0.5
        },
        PokemonType.DRAGON: {
            PokemonType.DRAGON: 2.0,
            PokemonType.STEEL: 0.5
        },
        PokemonType.STEEL: {
            PokemonType.FIRE: 0.5,
            PokemonType.WATER: 0.5,
            PokemonType.ELECTRIC: 0.5,
            PokemonType.ICE: 2.0,
            PokemonType.ROCK: 2.0,
            PokemonType.STEEL: 0.5
        },
        PokemonType.DARK: {
            PokemonType.FIGHTING: 0.5,
            PokemonType.PSYCHIC: 2.0,
            PokemonType.GHOST: 2.0,
            PokemonType.DARK: 0.5,
            PokemonType.STEEL: 0.5
        }
    }
    
    @classmethod
    def get_effectiveness(cls, attack_type: PokemonType, defender_types: List[PokemonType]) -> float:
        """Calcula efetividade do ataque contra os tipos do defensor"""
        effectiveness = 1.0
        
        for defender_type in defender_types:
            if attack_type in cls.EFFECTIVENESS_MATRIX:
                type_effect = cls.EFFECTIVENESS_MATRIX[attack_type].get(defender_type, 1.0)
                effectiveness *= type_effect
        
        return effectiveness


class BattleSystem:
    """Sistema principal de batalhas"""
    
    def __init__(self):
        self.battle_log = []
        self.max_turns = 100  # Evita loops infinitos
    
    def calculate_damage(
        self,
        attacker: Pokemon,
        defender: Pokemon,
        move: Move,
        critical_hit: bool = False
    ) -> int:
        """Calcula dano baseado na fórmula do GBA (FireRed/LeafGreen)"""
        
        # Determina se é ataque físico ou especial
        if move.category == MoveCategory.PHYSICAL:
            attack_stat = attacker.attack
            defense_stat = defender.defense
        elif move.category == MoveCategory.SPECIAL:
            attack_stat = attacker.sp_attack
            defense_stat = defender.sp_defense
        else:  # STATUS
            return 0
        
        # Fórmula de dano do GBA (FireRed/LeafGreen)
        # Base: ((2 * Level + 10) * Power * Attack / Defense / 50) + 2
        
        # Cálculo base do dano (fórmula Pokémon real)
        base_damage = ((2 * attacker.level + 10) * move.power * attack_stat / defense_stat / 50) + 2
        
        # Modificador de efetividade
        effectiveness = TypeEffectiveness.get_effectiveness(
            move.move_type, 
            defender.get_types()
        )
        
        # Modificador de golpe crítico
        critical_modifier = 2.0 if critical_hit else 1.0
        
        # Modificador de variação (85-100%)
        variation = random.uniform(0.85, 1.0)
        
        # Cálculo final
        damage = int(base_damage * effectiveness * critical_modifier * variation)
        
        # Mínimo de 1 de dano, máximo de 4x o HP do defensor
        max_damage = defender.max_hp * 4
        damage = max(1, min(damage, max_damage))
        
        return damage
    
    def is_critical_hit(self, attacker: Pokemon, move: Move) -> bool:
        """Determina se é golpe crítico"""
        # Taxa base de golpe crítico no GBA
        base_crit_rate = 6.25  # 1/16
        
        # Modificadores por velocidade (simplificado)
        speed_modifier = min(attacker.speed / 512, 1.0)
        
        # Taxa final
        crit_rate = base_crit_rate * (1 + speed_modifier)
        
        return random.random() * 100 < crit_rate
    
    def does_move_hit(self, move: Move, attacker: Pokemon, defender: Pokemon) -> bool:
        """Determina se o movimento acerta"""
        if move.accuracy == 0:  # Movimentos que sempre acertam
            return True
        
        # Modificador de precisão baseado na velocidade
        speed_modifier = attacker.speed / (attacker.speed + defender.speed)
        accuracy_modifier = 1.0 + (speed_modifier - 0.5) * 0.1
        
        # Taxa de acerto final
        hit_rate = move.accuracy * accuracy_modifier
        
        return random.random() * 100 < hit_rate
    
    def execute_turn(
        self,
        attacker: Pokemon,
        defender: Pokemon,
        move: Move,
        turn_number: int
    ) -> BattleTurn:
        """Executa um turno de batalha"""
        
        # Verifica se o movimento acerta
        if not self.does_move_hit(move, attacker, defender):
            return BattleTurn(
                turn_number=turn_number,
                attacker=attacker,
                defender=defender,
                move_used=move,
                damage_dealt=0,
                critical_hit=False,
                effectiveness=1.0,
                attacker_fainted=attacker.is_fainted,
                defender_fainted=defender.is_fainted
            )
        
        # Verifica golpe crítico
        critical_hit = self.is_critical_hit(attacker, move)
        
        # Calcula dano
        damage = self.calculate_damage(attacker, defender, move, critical_hit)
        
        # Aplica dano
        defender.take_damage(damage)
        
        # Calcula efetividade
        effectiveness = TypeEffectiveness.get_effectiveness(
            move.move_type, 
            defender.get_types()
        )
        
        # Cria turno
        turn = BattleTurn(
            turn_number=turn_number,
            attacker=attacker,
            defender=defender,
            move_used=move,
            damage_dealt=damage,
            critical_hit=critical_hit,
            effectiveness=effectiveness,
            attacker_fainted=attacker.is_fainted,
            defender_fainted=defender.is_fainted
        )
        
        return turn
    
    def battle_pokemon(
        self,
        pokemon1: Pokemon,
        pokemon2: Pokemon,
        pokemon1_moves: Optional[List[Move]] = None,
        pokemon2_moves: Optional[List[Move]] = None
    ) -> BattleLog:
        """Batalha entre dois Pokémon"""
        
        # Movimentos padrão se não fornecidos
        if pokemon1_moves is None:
            if pokemon1.move_set is not None:
                pokemon1_moves = [move for move in pokemon1.move_set.moves if move.category != MoveCategory.STATUS]
            else:
                # Move set realista baseado no nome do Pokémon
                from .moves import create_realistic_moveset
                pokemon1.move_set = create_realistic_moveset(pokemon1.name)
                pokemon1_moves = [move for move in pokemon1.move_set.moves if move.category != MoveCategory.STATUS]
        
        if pokemon2_moves is None:
            if pokemon2.move_set is not None:
                pokemon2_moves = [move for move in pokemon2.move_set.moves if move.category != MoveCategory.STATUS]
            else:
                # Move set realista baseado no nome do Pokémon
                from .moves import create_realistic_moveset
                pokemon2.move_set = create_realistic_moveset(pokemon2.name)
                pokemon2_moves = [move for move in pokemon2.move_set.moves if move.category != MoveCategory.STATUS]
        
        turns = []
        turn_number = 1
        
        # Loop principal da batalha
        while (not pokemon1.is_fainted and not pokemon2.is_fainted and 
               turn_number <= self.max_turns):
            
            # Determina ordem de ataque (velocidade)
            if pokemon1.speed >= pokemon2.speed:
                first_attacker, second_attacker = pokemon1, pokemon2
                first_moves, second_moves = pokemon1_moves, pokemon2_moves
            else:
                first_attacker, second_attacker = pokemon2, pokemon1
                first_moves, second_moves = pokemon2_moves, pokemon1_moves
            
            # Primeiro ataque
            if not first_attacker.is_fainted and not second_attacker.is_fainted:
                move = random.choice(first_moves)
                turn = self.execute_turn(first_attacker, second_attacker, move, turn_number)
                turns.append(turn)
                
                if second_attacker.is_fainted:
                    break
            
            # Segundo ataque (se o segundo ainda estiver vivo)
            if not first_attacker.is_fainted and not second_attacker.is_fainted:
                move = random.choice(second_moves)
                turn = self.execute_turn(second_attacker, first_attacker, move, turn_number)
                turns.append(turn)
            
            turn_number += 1
        
        # Determina vencedor
        if pokemon1.is_fainted and pokemon2.is_fainted:
            result = BattleResult.DRAW
            winner = None
        elif pokemon1.is_fainted:
            result = BattleResult.LOSS
            winner = None  # pokemon2 venceu
        else:
            result = BattleResult.WIN
            winner = None  # pokemon1 venceu
        
        return BattleLog(
            turns=turns,
            winner=winner,
            total_turns=turn_number - 1,
            battle_result=result
        )
    
    def battle_teams(
        self,
        team1: PokemonTeam,
        team2: PokemonTeam,
        auto_switch: bool = True
    ) -> BattleLog:
        """Batalha entre duas equipes"""
        
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
            
            # Batalha entre os Pokémon ativos
            pokemon_battle = self.battle_pokemon(pokemon1, pokemon2)
            turns.extend(pokemon_battle.turns)
            
            # Troca automática se necessário
            if auto_switch:
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
    
    def simulate_battle(
        self,
        team1: PokemonTeam,
        team2: PokemonTeam,
        num_simulations: int = 100
    ) -> Dict[str, float]:
        """Simula múltiplas batalhas e retorna estatísticas"""
        
        wins = 0
        losses = 0
        draws = 0
        total_turns = 0
        
        for _ in range(num_simulations):
            battle_log = self.battle_teams(team1, team2)
            
            if battle_log.battle_result == BattleResult.WIN:
                wins += 1
            elif battle_log.battle_result == BattleResult.LOSS:
                losses += 1
            else:
                draws += 1
            
            total_turns += battle_log.total_turns
        
        return {
            "win_rate": wins / num_simulations,
            "loss_rate": losses / num_simulations,
            "draw_rate": draws / num_simulations,
            "avg_turns": total_turns / num_simulations
        }
