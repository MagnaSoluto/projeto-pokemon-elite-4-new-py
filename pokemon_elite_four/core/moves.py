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
    
    # Movimentos adicionais para movesets realistas
    "Wing Attack": Move("Wing Attack", PokemonType.FLYING, MoveCategory.PHYSICAL, 60, 100, 35),
    "Body Slam": Move("Body Slam", PokemonType.NORMAL, MoveCategory.PHYSICAL, 85, 100, 15),
    "Waterfall": Move("Waterfall", PokemonType.WATER, MoveCategory.PHYSICAL, 80, 100, 15),
    "Megahorn": Move("Megahorn", PokemonType.BUG, MoveCategory.PHYSICAL, 120, 85, 10),
    "Explosion": Move("Explosion", PokemonType.NORMAL, MoveCategory.PHYSICAL, 250, 100, 5),
    "Iron Tail": Move("Iron Tail", PokemonType.STEEL, MoveCategory.PHYSICAL, 100, 75, 15),
    "Sandstorm": Move("Sandstorm", PokemonType.ROCK, MoveCategory.STATUS, 0, 100, 10, target=MoveTarget.EVERYONE),
    "Bulk Up": Move("Bulk Up", PokemonType.FIGHTING, MoveCategory.STATUS, 0, 100, 20, target=MoveTarget.SELF),
    "Soft-Boiled": Move("Soft-Boiled", PokemonType.NORMAL, MoveCategory.STATUS, 0, 100, 10, target=MoveTarget.SELF),
    "Seismic Toss": Move("Seismic Toss", PokemonType.FIGHTING, MoveCategory.PHYSICAL, 0, 100, 20),
    "Wish": Move("Wish", PokemonType.NORMAL, MoveCategory.STATUS, 0, 100, 10, target=MoveTarget.SELF),
    "Tri Attack": Move("Tri Attack", PokemonType.NORMAL, MoveCategory.SPECIAL, 80, 100, 10),
    "Shell Smash": Move("Shell Smash", PokemonType.NORMAL, MoveCategory.STATUS, 0, 100, 15, target=MoveTarget.SELF),
    "Aqua Jet": Move("Aqua Jet", PokemonType.WATER, MoveCategory.PHYSICAL, 40, 100, 20, priority=1),
    "Blizzard": Move("Blizzard", PokemonType.ICE, MoveCategory.SPECIAL, 110, 70, 5),
    "Roost": Move("Roost", PokemonType.FLYING, MoveCategory.STATUS, 0, 100, 10, target=MoveTarget.SELF),
    "Fire Blast": Move("Fire Blast", PokemonType.FIRE, MoveCategory.SPECIAL, 110, 85, 5),
    "Thunder": Move("Thunder", PokemonType.ELECTRIC, MoveCategory.SPECIAL, 110, 70, 10),
    "Dragon Pulse": Move("Dragon Pulse", PokemonType.DRAGON, MoveCategory.SPECIAL, 85, 100, 10),
    "Dragon Dance": Move("Dragon Dance", PokemonType.DRAGON, MoveCategory.STATUS, 0, 100, 20, target=MoveTarget.SELF),
    "Extreme Speed": Move("Extreme Speed", PokemonType.NORMAL, MoveCategory.PHYSICAL, 80, 100, 5, priority=2),
    "Aura Sphere": Move("Aura Sphere", PokemonType.FIGHTING, MoveCategory.SPECIAL, 80, 100, 20),
    "Calm Mind": Move("Calm Mind", PokemonType.PSYCHIC, MoveCategory.STATUS, 0, 100, 20, target=MoveTarget.SELF),
    "Lovely Kiss": Move("Lovely Kiss", PokemonType.NORMAL, MoveCategory.STATUS, 0, 75, 10, target=MoveTarget.ENEMY),
    "Ice Punch": Move("Ice Punch", PokemonType.ICE, MoveCategory.PHYSICAL, 75, 100, 15),
    "Thunder Punch": Move("Thunder Punch", PokemonType.ELECTRIC, MoveCategory.PHYSICAL, 75, 100, 15),
    "X-Scissor": Move("X-Scissor", PokemonType.BUG, MoveCategory.PHYSICAL, 80, 100, 15),
    "Flail": Move("Flail", PokemonType.NORMAL, MoveCategory.PHYSICAL, 0, 100, 15),
    "Bounce": Move("Bounce", PokemonType.FLYING, MoveCategory.PHYSICAL, 85, 85, 5),
    "Transform": Move("Transform", PokemonType.NORMAL, MoveCategory.STATUS, 0, 100, 10, target=MoveTarget.ENEMY),
    "Acid Armor": Move("Acid Armor", PokemonType.POISON, MoveCategory.STATUS, 0, 100, 20, target=MoveTarget.SELF),
    "Aqua Tail": Move("Aqua Tail", PokemonType.WATER, MoveCategory.PHYSICAL, 90, 90, 10),
    "Ice Fang": Move("Ice Fang", PokemonType.ICE, MoveCategory.PHYSICAL, 65, 95, 15),
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


def load_pokemon_movesets() -> dict:
    """Carrega movesets reais dos Pokémon baseado em dados hardcoded"""
    movesets = {}
    
    # Movesets específicos para Pokémon populares
    pokemon_movesets = {
        "Charizard": ["Flamethrower", "Wing Attack", "Dragon Claw", "Earthquake"],
        "Blastoise": ["Surf", "Ice Beam", "Earthquake", "Bite"],
        "Venusaur": ["Solar Beam", "Vine Whip", "Earthquake", "Sleep Powder"],
        "Pikachu": ["Thunderbolt", "Quick Attack", "Thunder Wave", "Bite"],
        "Alakazam": ["Psychic", "Confusion", "Recover", "Reflect"],
        "Dragonite": ["Hyper Beam", "Dragon Claw", "Thunderbolt", "Ice Beam"],
        "Snorlax": ["Body Slam", "Earthquake", "Rest", "Hyper Beam"],
        "Gengar": ["Shadow Ball", "Psychic", "Thunderbolt", "Toxic"],
        "Machamp": ["Cross Chop", "Earthquake", "Rock Slide", "Bulk Up"],
        "Lapras": ["Surf", "Ice Beam", "Thunderbolt", "Psychic"],
        "Gyarados": ["Waterfall", "Earthquake", "Dragon Dance", "Ice Fang"],
        "Exeggutor": ["Solar Beam", "Psychic", "Earthquake", "Sleep Powder"],
        "Rhydon": ["Earthquake", "Rock Slide", "Megahorn", "Swords Dance"],
        "Golem": ["Earthquake", "Rock Slide", "Explosion", "Swords Dance"],
        "Onix": ["Earthquake", "Rock Slide", "Iron Tail", "Sandstorm"],
        "Hitmonlee": ["Hi Jump Kick", "Earthquake", "Rock Slide", "Bulk Up"],
        "Hitmonchan": ["Mega Punch", "Earthquake", "Rock Slide", "Bulk Up"],
        "Lickitung": ["Body Slam", "Earthquake", "Swords Dance", "Rest"],
        "Weezing": ["Sludge Bomb", "Flamethrower", "Thunderbolt", "Explosion"],
        "Rhyhorn": ["Earthquake", "Rock Slide", "Megahorn", "Swords Dance"],
        "Chansey": ["Soft-Boiled", "Seismic Toss", "Thunder Wave", "Toxic"],
        "Tangela": ["Solar Beam", "Sleep Powder", "Earthquake", "Swords Dance"],
        "Kangaskhan": ["Body Slam", "Earthquake", "Rock Slide", "Swords Dance"],
        "Horsea": ["Surf", "Ice Beam", "Dragon Pulse", "Agility"],
        "Goldeen": ["Waterfall", "Megahorn", "Swords Dance", "Aqua Tail"],
        "Staryu": ["Surf", "Thunderbolt", "Ice Beam", "Recover"],
        "Mr. Mime": ["Psychic", "Thunderbolt", "Reflect", "Light Screen"],
        "Scyther": ["Wing Attack", "Swords Dance", "Quick Attack", "Agility"],
        "Jynx": ["Psychic", "Ice Beam", "Lovely Kiss", "Calm Mind"],
        "Electabuzz": ["Thunderbolt", "Psychic", "Ice Punch", "Thunder Wave"],
        "Magmar": ["Flamethrower", "Psychic", "Thunder Punch", "Will-O-Wisp"],
        "Pinsir": ["X-Scissor", "Earthquake", "Swords Dance", "Quick Attack"],
        "Tauros": ["Body Slam", "Earthquake", "Rock Slide", "Swords Dance"],
        "Magikarp": ["Splash", "Tackle", "Flail", "Bounce"],
        "Lapras": ["Surf", "Ice Beam", "Thunderbolt", "Psychic"],
        "Ditto": ["Transform", "Transform", "Transform", "Transform"],
        "Eevee": ["Quick Attack", "Tackle", "Bite", "Growl"],
        "Vaporeon": ["Surf", "Ice Beam", "Acid Armor", "Wish"],
        "Jolteon": ["Thunderbolt", "Thunder Wave", "Quick Attack", "Agility"],
        "Flareon": ["Flamethrower", "Quick Attack", "Will-O-Wisp", "Wish"],
        "Porygon": ["Tri Attack", "Thunderbolt", "Ice Beam", "Recover"],
        "Omanyte": ["Surf", "Ice Beam", "Ancient Power", "Shell Smash"],
        "Omastar": ["Surf", "Ice Beam", "Ancient Power", "Shell Smash"],
        "Kabuto": ["Waterfall", "Rock Slide", "Swords Dance", "Aqua Jet"],
        "Kabutops": ["Waterfall", "Rock Slide", "Swords Dance", "Aqua Jet"],
        "Aerodactyl": ["Wing Attack", "Rock Slide", "Earthquake", "Swords Dance"],
        "Snorlax": ["Body Slam", "Earthquake", "Rest", "Hyper Beam"],
        "Articuno": ["Ice Beam", "Blizzard", "Roost", "Reflect"],
        "Zapdos": ["Thunderbolt", "Thunder", "Roost", "Light Screen"],
        "Moltres": ["Flamethrower", "Fire Blast", "Roost", "Will-O-Wisp"],
        "Dratini": ["Dragon Pulse", "Thunder Wave", "Dragon Dance", "Extreme Speed"],
        "Dragonair": ["Dragon Pulse", "Thunder Wave", "Dragon Dance", "Extreme Speed"],
        "Dragonite": ["Dragon Pulse", "Thunder Wave", "Dragon Dance", "Extreme Speed"],
        "Mewtwo": ["Psychic", "Aura Sphere", "Recover", "Calm Mind"],
        "Mew": ["Psychic", "Aura Sphere", "Soft-Boiled", "Calm Mind"]
    }
    
    # Cria movesets usando movimentos já definidos
    for pokemon_name, move_names in pokemon_movesets.items():
        moves = []
        for move_name in move_names:
            move = get_move_by_name(move_name)
            if move:
                moves.append(move)
        
        if moves:
            movesets[pokemon_name] = MoveSet(moves)
    
    return movesets


def create_realistic_moveset(pokemon_name: str) -> MoveSet:
    """Cria moveset realista baseado no nome do Pokémon"""
    movesets = load_pokemon_movesets()
    
    if pokemon_name in movesets:
        return movesets[pokemon_name]
    else:
        # Fallback para tipo genérico se não encontrar
        from .pokemon import PokemonType
        return create_default_moveset(PokemonType.NORMAL)
