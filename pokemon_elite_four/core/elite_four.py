"""
Elite Four - Sistema baseado no FireRed/LeafGreen (GBA)
Dados precisos dos membros e seus Pokémon
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from .pokemon import Pokemon, PokemonTeam, PokemonType, PokemonStats
from .moves import MoveSet, create_default_moveset, get_move_by_name


@dataclass
class EliteFourMember:
    """Membro da Elite Four"""
    name: str
    position: int
    pokemon_team: PokemonTeam
    specialty_type: Optional[PokemonType] = None
    difficulty: str = "Medium"


class EliteFour:
    """Sistema da Elite Four - FireRed/LeafGreen"""
    
    def __init__(self):
        self.members = self._create_elite_four_members()
        self.current_member_index = 0
    
    def _create_elite_four_members(self) -> List[EliteFourMember]:
        """Cria os membros da Elite Four baseado no GBA"""
        members = []
        
        # Lorelei - Especialista em Gelo
        lorelei_team = self._create_lorelei_team()
        members.append(EliteFourMember(
            name="Lorelei",
            position=1,
            pokemon_team=lorelei_team,
            specialty_type=PokemonType.ICE,
            difficulty="Medium"
        ))
        
        # Bruno - Especialista em Lutador
        bruno_team = self._create_bruno_team()
        members.append(EliteFourMember(
            name="Bruno",
            position=2,
            pokemon_team=bruno_team,
            specialty_type=PokemonType.FIGHTING,
            difficulty="Easy"
        ))
        
        # Agatha - Especialista em Fantasma
        agatha_team = self._create_agatha_team()
        members.append(EliteFourMember(
            name="Agatha",
            position=3,
            pokemon_team=agatha_team,
            specialty_type=PokemonType.GHOST,
            difficulty="Medium"
        ))
        
        # Lance - Especialista em Dragão
        lance_team = self._create_lance_team()
        members.append(EliteFourMember(
            name="Lance",
            position=4,
            pokemon_team=lance_team,
            specialty_type=PokemonType.DRAGON,
            difficulty="Hard"
        ))
        
        # Champion - Time variado
        champion_team = self._create_champion_team()
        members.append(EliteFourMember(
            name="Champion",
            position=5,
            pokemon_team=champion_team,
            specialty_type=None,
            difficulty="Very Hard"
        ))
        
        return members
    
    def _create_lorelei_team(self) -> PokemonTeam:
        """Time da Lorelei - FireRed/LeafGreen"""
        pokemon_list = []
        
        # Dewgong (Lv.54)
        dewgong = Pokemon(
            name="Dewgong",
            pokemon_id=87,
            type1=PokemonType.WATER,
            type2=PokemonType.ICE,
            stats=PokemonStats(90, 70, 80, 70, 95, 70),
            level=54
        )
        dewgong.move_set = self._create_ice_moveset()
        pokemon_list.append(dewgong)
        
        # Cloyster (Lv.53)
        cloyster = Pokemon(
            name="Cloyster",
            pokemon_id=91,
            type1=PokemonType.WATER,
            type2=PokemonType.ICE,
            stats=PokemonStats(50, 95, 180, 85, 45, 70),
            level=53
        )
        cloyster.move_set = self._create_ice_moveset()
        pokemon_list.append(cloyster)
        
        # Slowbro (Lv.54)
        slowbro = Pokemon(
            name="Slowbro",
            pokemon_id=80,
            type1=PokemonType.WATER,
            type2=PokemonType.PSYCHIC,
            stats=PokemonStats(95, 75, 110, 100, 80, 30),
            level=54
        )
        slowbro.move_set = self._create_psychic_moveset()
        pokemon_list.append(slowbro)
        
        # Jynx (Lv.56)
        jynx = Pokemon(
            name="Jynx",
            pokemon_id=124,
            type1=PokemonType.ICE,
            type2=PokemonType.PSYCHIC,
            stats=PokemonStats(65, 50, 35, 115, 95, 95),
            level=56
        )
        jynx.move_set = self._create_psychic_moveset()
        pokemon_list.append(jynx)
        
        # Lapras (Lv.56)
        lapras = Pokemon(
            name="Lapras",
            pokemon_id=131,
            type1=PokemonType.WATER,
            type2=PokemonType.ICE,
            stats=PokemonStats(130, 85, 80, 85, 95, 60),
            level=56
        )
        lapras.move_set = self._create_ice_moveset()
        pokemon_list.append(lapras)
        
        return PokemonTeam(pokemon_list)
    
    def _create_bruno_team(self) -> PokemonTeam:
        """Time do Bruno - FireRed/LeafGreen"""
        pokemon_list = []
        
        # Onix (Lv.53)
        onix = Pokemon(
            name="Onix",
            pokemon_id=95,
            type1=PokemonType.ROCK,
            type2=PokemonType.GROUND,
            stats=PokemonStats(35, 45, 160, 30, 45, 70),
            level=53
        )
        onix.move_set = self._create_rock_moveset()
        pokemon_list.append(onix)
        
        # Hitmonchan (Lv.55)
        hitmonchan = Pokemon(
            name="Hitmonchan",
            pokemon_id=107,
            type1=PokemonType.FIGHTING,
            type2=None,
            stats=PokemonStats(50, 105, 79, 35, 110, 76),
            level=55
        )
        hitmonchan.move_set = self._create_fighting_moveset()
        pokemon_list.append(hitmonchan)
        
        # Hitmonlee (Lv.55)
        hitmonlee = Pokemon(
            name="Hitmonlee",
            pokemon_id=106,
            type1=PokemonType.FIGHTING,
            type2=None,
            stats=PokemonStats(50, 120, 53, 35, 110, 87),
            level=55
        )
        hitmonlee.move_set = self._create_fighting_moveset()
        pokemon_list.append(hitmonlee)
        
        # Onix (Lv.56) - Segundo Onix
        onix2 = Pokemon(
            name="Onix",
            pokemon_id=95,
            type1=PokemonType.ROCK,
            type2=PokemonType.GROUND,
            stats=PokemonStats(35, 45, 160, 30, 45, 70),
            level=56
        )
        onix2.move_set = self._create_rock_moveset()
        pokemon_list.append(onix2)
        
        # Machamp (Lv.58)
        machamp = Pokemon(
            name="Machamp",
            pokemon_id=68,
            type1=PokemonType.FIGHTING,
            type2=None,
            stats=PokemonStats(90, 130, 80, 65, 85, 55),
            level=58
        )
        machamp.move_set = self._create_fighting_moveset()
        pokemon_list.append(machamp)
        
        return PokemonTeam(pokemon_list)
    
    def _create_agatha_team(self) -> PokemonTeam:
        """Time da Agatha - FireRed/LeafGreen"""
        pokemon_list = []
        
        # Gengar (Lv.56)
        gengar = Pokemon(
            name="Gengar",
            pokemon_id=94,
            type1=PokemonType.GHOST,
            type2=PokemonType.POISON,
            stats=PokemonStats(60, 65, 60, 130, 75, 110),
            level=56
        )
        gengar.move_set = self._create_ghost_moveset()
        pokemon_list.append(gengar)
        
        # Golbat (Lv.56)
        golbat = Pokemon(
            name="Golbat",
            pokemon_id=42,
            type1=PokemonType.POISON,
            type2=PokemonType.FLYING,
            stats=PokemonStats(75, 80, 70, 65, 75, 90),
            level=56
        )
        golbat.move_set = self._create_poison_moveset()
        pokemon_list.append(golbat)
        
        # Haunter (Lv.55)
        haunter = Pokemon(
            name="Haunter",
            pokemon_id=93,
            type1=PokemonType.GHOST,
            type2=PokemonType.POISON,
            stats=PokemonStats(45, 50, 45, 115, 55, 95),
            level=55
        )
        haunter.move_set = self._create_ghost_moveset()
        pokemon_list.append(haunter)
        
        # Arbok (Lv.58)
        arbok = Pokemon(
            name="Arbok",
            pokemon_id=24,
            type1=PokemonType.POISON,
            type2=None,
            stats=PokemonStats(60, 95, 69, 65, 79, 80),
            level=58
        )
        arbok.move_set = self._create_poison_moveset()
        pokemon_list.append(arbok)
        
        # Gengar (Lv.60) - Segundo Gengar
        gengar2 = Pokemon(
            name="Gengar",
            pokemon_id=94,
            type1=PokemonType.GHOST,
            type2=PokemonType.POISON,
            stats=PokemonStats(60, 65, 60, 130, 75, 110),
            level=60
        )
        gengar2.move_set = self._create_ghost_moveset()
        pokemon_list.append(gengar2)
        
        return PokemonTeam(pokemon_list)
    
    def _create_lance_team(self) -> PokemonTeam:
        """Time do Lance - FireRed/LeafGreen"""
        pokemon_list = []
        
        # Gyarados (Lv.58)
        gyarados = Pokemon(
            name="Gyarados",
            pokemon_id=130,
            type1=PokemonType.WATER,
            type2=PokemonType.FLYING,
            stats=PokemonStats(95, 125, 79, 60, 100, 81),
            level=58
        )
        gyarados.move_set = self._create_water_moveset()
        pokemon_list.append(gyarados)
        
        # Dragonair (Lv.56)
        dragonair = Pokemon(
            name="Dragonair",
            pokemon_id=148,
            type1=PokemonType.DRAGON,
            type2=None,
            stats=PokemonStats(61, 84, 65, 70, 70, 70),
            level=56
        )
        dragonair.move_set = self._create_dragon_moveset()
        pokemon_list.append(dragonair)
        
        # Dragonair (Lv.54) - Segundo Dragonair
        dragonair2 = Pokemon(
            name="Dragonair",
            pokemon_id=148,
            type1=PokemonType.DRAGON,
            type2=None,
            stats=PokemonStats(61, 84, 65, 70, 70, 70),
            level=54
        )
        dragonair2.move_set = self._create_dragon_moveset()
        pokemon_list.append(dragonair2)
        
        # Aerodactyl (Lv.58)
        aerodactyl = Pokemon(
            name="Aerodactyl",
            pokemon_id=142,
            type1=PokemonType.ROCK,
            type2=PokemonType.FLYING,
            stats=PokemonStats(80, 105, 65, 60, 75, 130),
            level=58
        )
        aerodactyl.move_set = self._create_rock_moveset()
        pokemon_list.append(aerodactyl)
        
        # Dragonite (Lv.62)
        dragonite = Pokemon(
            name="Dragonite",
            pokemon_id=149,
            type1=PokemonType.DRAGON,
            type2=PokemonType.FLYING,
            stats=PokemonStats(91, 134, 95, 100, 100, 80),
            level=62
        )
        dragonite.move_set = self._create_dragon_moveset()
        pokemon_list.append(dragonite)
        
        return PokemonTeam(pokemon_list)
    
    def _create_champion_team(self) -> PokemonTeam:
        """Time do Champion - FireRed/LeafGreen (Blue)"""
        pokemon_list = []
        
        # Pidgeot (Lv.61)
        pidgeot = Pokemon(
            name="Pidgeot",
            pokemon_id=18,
            type1=PokemonType.NORMAL,
            type2=PokemonType.FLYING,
            stats=PokemonStats(83, 80, 75, 70, 70, 101),
            level=61
        )
        pidgeot.move_set = self._create_flying_moveset()
        pokemon_list.append(pidgeot)
        
        # Alakazam (Lv.59)
        alakazam = Pokemon(
            name="Alakazam",
            pokemon_id=65,
            type1=PokemonType.PSYCHIC,
            type2=None,
            stats=PokemonStats(55, 50, 45, 135, 95, 120),
            level=59
        )
        alakazam.move_set = self._create_psychic_moveset()
        pokemon_list.append(alakazam)
        
        # Rhydon (Lv.61)
        rhydon = Pokemon(
            name="Rhydon",
            pokemon_id=112,
            type1=PokemonType.GROUND,
            type2=PokemonType.ROCK,
            stats=PokemonStats(105, 130, 120, 45, 45, 40),
            level=61
        )
        rhydon.move_set = self._create_ground_moveset()
        pokemon_list.append(rhydon)
        
        # Arcanine (Lv.61)
        arcanine = Pokemon(
            name="Arcanine",
            pokemon_id=59,
            type1=PokemonType.FIRE,
            type2=None,
            stats=PokemonStats(90, 110, 80, 100, 80, 95),
            level=61
        )
        arcanine.move_set = self._create_fire_moveset()
        pokemon_list.append(arcanine)
        
        # Exeggutor (Lv.61)
        exeggutor = Pokemon(
            name="Exeggutor",
            pokemon_id=103,
            type1=PokemonType.GRASS,
            type2=PokemonType.PSYCHIC,
            stats=PokemonStats(95, 95, 85, 125, 75, 55),
            level=61
        )
        exeggutor.move_set = self._create_grass_moveset()
        pokemon_list.append(exeggutor)
        
        # Blastoise (Lv.63) - Starter
        blastoise = Pokemon(
            name="Blastoise",
            pokemon_id=9,
            type1=PokemonType.WATER,
            type2=None,
            stats=PokemonStats(79, 83, 100, 85, 105, 78),
            level=63
        )
        blastoise.move_set = self._create_water_moveset()
        pokemon_list.append(blastoise)
        
        return PokemonTeam(pokemon_list)
    
    def _create_ice_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon de gelo"""
        moves = [
            get_move_by_name("Ice Beam"),
            get_move_by_name("Surf"),
            get_move_by_name("Confusion"),
            get_move_by_name("Growl")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_psychic_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon psíquico"""
        moves = [
            get_move_by_name("Psychic"),
            get_move_by_name("Confusion"),
            get_move_by_name("Thunder Wave"),
            get_move_by_name("Agility")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_fighting_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon lutador"""
        moves = [
            get_move_by_name("Tackle"),
            get_move_by_name("Quick Attack"),
            get_move_by_name("Swords Dance"),
            get_move_by_name("Leer")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_rock_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon de pedra"""
        moves = [
            get_move_by_name("Rock Slide"),
            get_move_by_name("Tackle"),
            get_move_by_name("Leer"),
            get_move_by_name("Growl")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_ghost_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon fantasma"""
        moves = [
            get_move_by_name("Confusion"),
            get_move_by_name("Tackle"),
            get_move_by_name("Toxic"),
            get_move_by_name("Growl")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_poison_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon venenoso"""
        moves = [
            get_move_by_name("Tackle"),
            get_move_by_name("Toxic"),
            get_move_by_name("Bite"),
            get_move_by_name("Growl")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_water_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon de água"""
        moves = [
            get_move_by_name("Surf"),
            get_move_by_name("Water Gun"),
            get_move_by_name("Tackle"),
            get_move_by_name("Growl")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_dragon_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon dragão"""
        moves = [
            get_move_by_name("Dragon Claw"),
            get_move_by_name("Tackle"),
            get_move_by_name("Agility"),
            get_move_by_name("Leer")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_flying_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon voador"""
        moves = [
            get_move_by_name("Tackle"),
            get_move_by_name("Quick Attack"),
            get_move_by_name("Growl"),
            get_move_by_name("Leer")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_ground_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon de terra"""
        moves = [
            get_move_by_name("Earthquake"),
            get_move_by_name("Tackle"),
            get_move_by_name("Leer"),
            get_move_by_name("Growl")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_fire_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon de fogo"""
        moves = [
            get_move_by_name("Flamethrower"),
            get_move_by_name("Ember"),
            get_move_by_name("Tackle"),
            get_move_by_name("Growl")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def _create_grass_moveset(self) -> MoveSet:
        """Cria moveset para Pokémon de grama"""
        moves = [
            get_move_by_name("Solar Beam"),
            get_move_by_name("Vine Whip"),
            get_move_by_name("Confusion"),
            get_move_by_name("Sleep Powder")
        ]
        return MoveSet([m for m in moves if m is not None])
    
    def get_member(self, position: int) -> Optional[EliteFourMember]:
        """Retorna membro por posição"""
        for member in self.members:
            if member.position == position:
                return member
        return None
    
    def get_member_by_name(self, name: str) -> Optional[EliteFourMember]:
        """Retorna membro por nome"""
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None
    
    def get_all_members(self) -> List[EliteFourMember]:
        """Retorna todos os membros"""
        return self.members.copy()
    
    def get_difficulty_summary(self) -> Dict[str, List[str]]:
        """Retorna resumo de dificuldade"""
        difficulty_groups = {}
        for member in self.members:
            if member.difficulty not in difficulty_groups:
                difficulty_groups[member.difficulty] = []
            difficulty_groups[member.difficulty].append(member.name)
        return difficulty_groups
