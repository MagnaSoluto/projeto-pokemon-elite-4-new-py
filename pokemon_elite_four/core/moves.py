"""
Sistema de Movimentos Pokémon - Game Boy Advanced
Baseado no sistema de FireRed/LeafGreen
"""

from typing import List, Optional, Dict
from dataclasses import dataclass
from enum import Enum
from .pokemon import PokemonType


class MoveCategory(Enum):
    """Categorias de movimentos"""
    PHYSICAL = "Physical"
    SPECIAL = "Special"
    STATUS = "Status"


class MoveTarget(Enum):
    """Alvos dos movimentos"""
    SELF = "Self"
    ENEMY = "Enemy"
    ALL_ENEMIES = "All Enemies"
    ALL_ALLIES = "All Allies"
    EVERYONE = "Everyone"


@dataclass
class Move:
    """Classe representando um movimento Pokémon"""
    name: str
    move_type: PokemonType
    category: MoveCategory
    power: int
    accuracy: int
    pp: int
    priority: int = 0
    target: MoveTarget = MoveTarget.ENEMY
    description: str = ""
    
    def __post_init__(self):
        """Validação pós-inicialização"""
        if self.power < 0:
            raise ValueError("Power não pode ser negativo")
        if not (0 <= self.accuracy <= 100):
            raise ValueError("Accuracy deve estar entre 0 e 100")
        if self.pp <= 0:
            raise ValueError("PP deve ser maior que 0")


class MoveSet:
    """Conjunto de movimentos de um Pokémon"""
    
    def __init__(self, moves: List[Move]):
        if len(moves) > 4:
            raise ValueError("Um Pokémon pode ter no máximo 4 movimentos")
        self.moves = moves
        self.current_pp = [move.pp for move in moves]
    
    def get_available_moves(self) -> List[Move]:
        """Retorna movimentos com PP disponível"""
        return [move for i, move in enumerate(self.moves) if self.current_pp[i] > 0]
    
    def use_move(self, move_index: int) -> bool:
        """Usa um movimento (consome PP)"""
        if 0 <= move_index < len(self.moves) and self.current_pp[move_index] > 0:
            self.current_pp[move_index] -= 1
            return True
        return False
    
    def restore_pp(self, move_index: Optional[int] = None) -> None:
        """Restaura PP de um movimento ou todos"""
        if move_index is not None:
            if 0 <= move_index < len(self.moves):
                self.current_pp[move_index] = self.moves[move_index].pp
        else:
            self.current_pp = [move.pp for move in self.moves]
    
    def get_move_by_name(self, name: str) -> Optional[Move]:
        """Busca movimento por nome"""
        for move in self.moves:
            if move.name.lower() == name.lower():
                return move
        return None
    
    def __len__(self) -> int:
        return len(self.moves)
    
    def __getitem__(self, index: int) -> Move:
        return self.moves[index]


# Movimentos comuns da Geração 1 + GBA
COMMON_MOVES = {
    # Movimentos Físicos
    "Tackle": Move("Tackle", PokemonType.NORMAL, MoveCategory.PHYSICAL, 40, 100, 35),
    "Scratch": Move("Scratch", PokemonType.NORMAL, MoveCategory.PHYSICAL, 40, 100, 35),
    "Vine Whip": Move("Vine Whip", PokemonType.GRASS, MoveCategory.PHYSICAL, 45, 100, 25),
    "Ember": Move("Ember", PokemonType.FIRE, MoveCategory.SPECIAL, 40, 100, 25),
    "Water Gun": Move("Water Gun", PokemonType.WATER, MoveCategory.SPECIAL, 40, 100, 25),
    "Thunder Shock": Move("Thunder Shock", PokemonType.ELECTRIC, MoveCategory.SPECIAL, 40, 100, 30),
    "Confusion": Move("Confusion", PokemonType.PSYCHIC, MoveCategory.SPECIAL, 50, 100, 25),
    "Quick Attack": Move("Quick Attack", PokemonType.NORMAL, MoveCategory.PHYSICAL, 40, 100, 30, priority=1),
    "Bite": Move("Bite", PokemonType.DARK, MoveCategory.PHYSICAL, 60, 100, 25),
    "Metal Claw": Move("Metal Claw", PokemonType.STEEL, MoveCategory.PHYSICAL, 50, 95, 35),
    
    # Movimentos Especiais
    "Flamethrower": Move("Flamethrower", PokemonType.FIRE, MoveCategory.SPECIAL, 95, 100, 15),
    "Surf": Move("Surf", PokemonType.WATER, MoveCategory.SPECIAL, 95, 100, 15),
    "Thunderbolt": Move("Thunderbolt", PokemonType.ELECTRIC, MoveCategory.SPECIAL, 95, 100, 15),
    "Psychic": Move("Psychic", PokemonType.PSYCHIC, MoveCategory.SPECIAL, 90, 100, 10),
    "Solar Beam": Move("Solar Beam", PokemonType.GRASS, MoveCategory.SPECIAL, 120, 100, 10),
    "Ice Beam": Move("Ice Beam", PokemonType.ICE, MoveCategory.SPECIAL, 95, 100, 10),
    "Hyper Beam": Move("Hyper Beam", PokemonType.NORMAL, MoveCategory.SPECIAL, 150, 90, 5),
    "Earthquake": Move("Earthquake", PokemonType.GROUND, MoveCategory.PHYSICAL, 100, 100, 10),
    "Rock Slide": Move("Rock Slide", PokemonType.ROCK, MoveCategory.PHYSICAL, 75, 90, 10),
    "Dragon Claw": Move("Dragon Claw", PokemonType.DRAGON, MoveCategory.PHYSICAL, 80, 100, 15),
    
    # Movimentos de Status
    "Growl": Move("Growl", PokemonType.NORMAL, MoveCategory.STATUS, 0, 100, 40, target=MoveTarget.ENEMY),
    "Leer": Move("Leer", PokemonType.NORMAL, MoveCategory.STATUS, 0, 100, 30, target=MoveTarget.ENEMY),
    "Swords Dance": Move("Swords Dance", PokemonType.NORMAL, MoveCategory.STATUS, 0, 100, 20, target=MoveTarget.SELF),
    "Agility": Move("Agility", PokemonType.PSYCHIC, MoveCategory.STATUS, 0, 100, 30, target=MoveTarget.SELF),
    "Reflect": Move("Reflect", PokemonType.PSYCHIC, MoveCategory.STATUS, 0, 100, 20, target=MoveTarget.SELF),
    "Light Screen": Move("Light Screen", PokemonType.PSYCHIC, MoveCategory.STATUS, 0, 100, 30, target=MoveTarget.SELF),
    "Toxic": Move("Toxic", PokemonType.POISON, MoveCategory.STATUS, 0, 90, 10, target=MoveTarget.ENEMY),
    "Thunder Wave": Move("Thunder Wave", PokemonType.ELECTRIC, MoveCategory.STATUS, 0, 100, 20, target=MoveTarget.ENEMY),
    "Sleep Powder": Move("Sleep Powder", PokemonType.GRASS, MoveCategory.STATUS, 0, 75, 15, target=MoveTarget.ENEMY),
    "Stun Spore": Move("Stun Spore", PokemonType.GRASS, MoveCategory.STATUS, 0, 75, 30, target=MoveTarget.ENEMY),
}


def get_move_by_name(name: str) -> Optional[Move]:
    """Busca movimento por nome"""
    return COMMON_MOVES.get(name)


def create_default_moveset(pokemon_type: PokemonType) -> MoveSet:
    """Cria um conjunto de movimentos padrão baseado no tipo"""
    moves = []
    
    # Movimento básico baseado no tipo
    type_moves = {
        PokemonType.FIRE: ["Ember", "Flamethrower"],
        PokemonType.WATER: ["Water Gun", "Surf"],
        PokemonType.GRASS: ["Vine Whip", "Solar Beam"],
        PokemonType.ELECTRIC: ["Thunder Shock", "Thunderbolt"],
        PokemonType.PSYCHIC: ["Confusion", "Psychic"],
        PokemonType.NORMAL: ["Tackle", "Quick Attack"],
        PokemonType.FIGHTING: ["Tackle", "Quick Attack"],
        PokemonType.POISON: ["Tackle", "Toxic"],
        PokemonType.GROUND: ["Tackle", "Earthquake"],
        PokemonType.FLYING: ["Tackle", "Quick Attack"],
        PokemonType.BUG: ["Tackle", "Quick Attack"],
        PokemonType.ROCK: ["Tackle", "Rock Slide"],
        PokemonType.GHOST: ["Tackle", "Confusion"],
        PokemonType.DRAGON: ["Tackle", "Dragon Claw"],
        PokemonType.STEEL: ["Metal Claw", "Tackle"],
        PokemonType.DARK: ["Bite", "Tackle"],
        PokemonType.ICE: ["Tackle", "Ice Beam"],
    }
    
    # Adiciona movimentos baseados no tipo
    if pokemon_type in type_moves:
        for move_name in type_moves[pokemon_type][:2]:
            move = get_move_by_name(move_name)
            if move:
                moves.append(move)
    
    # Adiciona movimentos de status
    if len(moves) < 4:
        status_moves = ["Growl", "Leer", "Swords Dance", "Agility"]
        for move_name in status_moves:
            if len(moves) >= 4:
                break
            move = get_move_by_name(move_name)
            if move and move not in moves:
                moves.append(move)
    
    # Completa com movimentos básicos se necessário
    while len(moves) < 4:
        basic_moves = ["Tackle", "Quick Attack", "Growl", "Leer"]
        for move_name in basic_moves:
            if len(moves) >= 4:
                break
            move = get_move_by_name(move_name)
            if move and move not in moves:
                moves.append(move)
                break
    
    return MoveSet(moves[:4])
