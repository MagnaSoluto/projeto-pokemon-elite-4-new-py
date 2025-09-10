"""
Sistema de Pokémon - Classes e funcionalidades principais
Baseado no sistema Game Boy Advanced (FireRed/LeafGreen)
"""

import random
from typing import List, Optional, Dict, Tuple
from dataclasses import dataclass
from enum import Enum


class PokemonType(Enum):
    """Tipos de Pokémon - Geração 1 + Steel e Dark (GBA)"""
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    STEEL = "Steel"  # Adicionado em GBA
    DARK = "Dark"    # Adicionado em GBA


@dataclass
class PokemonStats:
    """Estatísticas base de um Pokémon"""
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    
    @property
    def total(self) -> int:
        """Total de estatísticas"""
        return self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
    
    def get_stat_at_level(self, stat: str, level: int) -> int:
        """Calcula estatística em um nível específico"""
        base_stat = getattr(self, stat)
        if stat == "hp":
            return int((base_stat * 2 + 31) * level / 100) + level + 10
        else:
            return int((base_stat * 2 + 31) * level / 100) + 5


class Pokemon:
    """Classe principal do Pokémon"""
    
    def __init__(
        self,
        name: str,
        pokemon_id: int,
        type1: PokemonType,
        type2: Optional[PokemonType] = None,
        stats: Optional[PokemonStats] = None,
        level: int = 50
    ):
        self.name = name
        self.pokemon_id = pokemon_id
        self.type1 = type1
        self.type2 = type2
        self.stats = stats or PokemonStats(0, 0, 0, 0, 0, 0)
        self.level = level
        self.current_hp = self.max_hp
        self.status_conditions = []
        self.move_set = []
        
    @property
    def max_hp(self) -> int:
        """HP máximo no nível atual"""
        return self.stats.get_stat_at_level("hp", self.level)
    
    @property
    def attack(self) -> int:
        """Ataque no nível atual"""
        return self.stats.get_stat_at_level("attack", self.level)
    
    @property
    def defense(self) -> int:
        """Defesa no nível atual"""
        return self.stats.get_stat_at_level("defense", self.level)
    
    @property
    def sp_attack(self) -> int:
        """Ataque especial no nível atual"""
        return self.stats.get_stat_at_level("sp_attack", self.level)
    
    @property
    def sp_defense(self) -> int:
        """Defesa especial no nível atual"""
        return self.stats.get_stat_at_level("sp_defense", self.level)
    
    @property
    def speed(self) -> int:
        """Velocidade no nível atual"""
        return self.stats.get_stat_at_level("speed", self.level)
    
    @property
    def is_fainted(self) -> bool:
        """Verifica se o Pokémon está desmaiado"""
        return self.current_hp <= 0
    
    def take_damage(self, damage: int) -> None:
        """Aplica dano ao Pokémon"""
        self.current_hp = max(0, self.current_hp - damage)
    
    def heal(self, amount: int) -> None:
        """Cura o Pokémon"""
        self.current_hp = min(self.max_hp, self.current_hp + amount)
    
    def restore_full_health(self) -> None:
        """Restaura HP completo"""
        self.current_hp = self.max_hp
        self.status_conditions.clear()
    
    def get_types(self) -> List[PokemonType]:
        """Retorna lista de tipos do Pokémon"""
        types = [self.type1]
        if self.type2:
            types.append(self.type2)
        return types
    
    def has_type(self, pokemon_type: PokemonType) -> bool:
        """Verifica se o Pokémon tem um tipo específico"""
        return pokemon_type in self.get_types()
    
    def __str__(self) -> str:
        types_str = "/".join([t.value for t in self.get_types()])
        return f"{self.name} (Lv.{self.level}) - {types_str} - HP: {self.current_hp}/{self.max_hp}"
    
    def __repr__(self) -> str:
        return f"Pokemon(name='{self.name}', id={self.pokemon_id}, level={self.level})"


class PokemonTeam:
    """Equipe de Pokémon (sexteto)"""
    
    def __init__(self, pokemon_list: List[Pokemon]):
        if len(pokemon_list) > 6:
            raise ValueError("Uma equipe pode ter no máximo 6 Pokémon")
        self.pokemon = pokemon_list[:6]  # Garante máximo de 6
        self.active_pokemon_index = 0
    
    @property
    def active_pokemon(self) -> Optional[Pokemon]:
        """Pokémon ativo na batalha"""
        if 0 <= self.active_pokemon_index < len(self.pokemon):
            return self.pokemon[self.active_pokemon_index]
        return None
    
    @property
    def alive_pokemon(self) -> List[Pokemon]:
        """Lista de Pokémon vivos"""
        return [p for p in self.pokemon if not p.is_fainted]
    
    @property
    def is_defeated(self) -> bool:
        """Verifica se toda a equipe foi derrotada"""
        return len(self.alive_pokemon) == 0
    
    def switch_pokemon(self, index: int) -> bool:
        """Troca o Pokémon ativo"""
        if 0 <= index < len(self.pokemon) and not self.pokemon[index].is_fainted:
            self.active_pokemon_index = index
            return True
        return False
    
    def get_next_alive_pokemon(self) -> Optional[Pokemon]:
        """Retorna o próximo Pokémon vivo"""
        alive = self.alive_pokemon
        if alive:
            # Tenta encontrar um Pokémon vivo após o atual
            for i in range(self.active_pokemon_index + 1, len(self.pokemon)):
                if not self.pokemon[i].is_fainted:
                    return self.pokemon[i]
            # Se não encontrar, pega o primeiro vivo
            return alive[0]
        return None
    
    def auto_switch(self) -> bool:
        """Troca automaticamente para o próximo Pokémon vivo"""
        next_pokemon = self.get_next_alive_pokemon()
        if next_pokemon:
            self.active_pokemon_index = self.pokemon.index(next_pokemon)
            return True
        return False
    
    def restore_team(self) -> None:
        """Restaura toda a equipe"""
        for pokemon in self.pokemon:
            pokemon.restore_full_health()
        self.active_pokemon_index = 0
    
    def get_team_summary(self) -> str:
        """Resumo da equipe"""
        summary = f"Equipe ({len(self.pokemon)} Pokémon):\n"
        for i, pokemon in enumerate(self.pokemon):
            status = "VIVO" if not pokemon.is_fainted else "DESMAIADO"
            summary += f"  {i+1}. {pokemon.name} (Lv.{pokemon.level}) - {status}\n"
        return summary
    
    def __len__(self) -> int:
        return len(self.pokemon)
    
    def __getitem__(self, index: int) -> Pokemon:
        return self.pokemon[index]
    
    def __iter__(self):
        return iter(self.pokemon)
