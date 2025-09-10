"""
Pokémon Elite Four - Análise e Simulação de Batalhas
====================================================

Sistema completo de análise e simulação de batalhas Pokémon para Game Boy Advanced,
focado na Elite Four com sexteto otimizado.

Autor: Adriano Carvalho dos Santos
RA: 10747203
MBA em Engenharia de Dados - Universidade Presbiteriana Mackenzie
"""

__version__ = "2.0.0"
__author__ = "Adriano Carvalho dos Santos"
__email__ = "adriano.carvalho@mackenzie.br"

# Imports principais
from .core.pokemon import Pokemon, PokemonTeam
from .core.battle_system import BattleSystem, BattleResult
from .core.elite_four import EliteFour
from .analysis.team_optimizer import TeamOptimizer
from .analysis.data_processor import DataProcessor

__all__ = [
    "Pokemon",
    "PokemonTeam", 
    "BattleSystem",
    "BattleResult",
    "EliteFour",
    "TeamOptimizer",
    "DataProcessor"
]
