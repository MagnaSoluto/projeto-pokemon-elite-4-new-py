"""
Módulo Core - Classes principais do sistema Pokémon
"""

from .pokemon import Pokemon, PokemonTeam
from .battle_system import BattleSystem, BattleResult
from .elite_four import EliteFour
from .moves import Move, MoveSet

__all__ = [
    "Pokemon",
    "PokemonTeam",
    "BattleSystem", 
    "BattleResult",
    "EliteFour",
    "Move",
    "MoveSet"
]
