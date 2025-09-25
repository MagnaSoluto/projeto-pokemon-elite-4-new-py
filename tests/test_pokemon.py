"""
Testes para a classe Pokemon e relacionadas
"""

import pytest
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent.parent))

from pokemon_elite_four.core.pokemon import Pokemon, PokemonTeam, PokemonStats


class TestPokemonStats:
    """Testes para a classe PokemonStats"""
    
    def test_stats_creation(self):
        """Testa criação de estatísticas"""
        stats = PokemonStats(78, 84, 78, 109, 85, 100)
        
        assert stats.hp == 78
        assert stats.attack == 84
        assert stats.defense == 78
        assert stats.sp_attack == 109
        assert stats.sp_defense == 85
        assert stats.speed == 100
    
    def test_stats_total(self):
        """Testa cálculo do total de estatísticas"""
        stats = PokemonStats(78, 84, 78, 109, 85, 100)
        expected_total = 78 + 84 + 78 + 109 + 85 + 100
        
        assert stats.get_total() == expected_total
    
    def test_stats_average(self):
        """Testa cálculo da média de estatísticas"""
        stats = PokemonStats(60, 60, 60, 60, 60, 60)
        
        assert stats.get_average() == 60.0


class TestPokemon:
    """Testes para a classe Pokemon"""
    
    def test_pokemon_creation(self):
        """Testa criação de Pokémon"""
        stats = PokemonStats(78, 84, 78, 109, 85, 100)
        charizard = Pokemon(
            name="Charizard",
            pokemon_id=6,
            type1="Fire",
            type2="Flying",
            stats=stats,
            level=50
        )
        
        assert charizard.name == "Charizard"
        assert charizard.pokemon_id == 6
        assert charizard.type1 == "Fire"
        assert charizard.type2 == "Flying"
        assert charizard.level == 50
        assert charizard.current_hp > 0
        assert charizard.max_hp > 0
    
    def test_pokemon_hp_calculation(self):
        """Testa cálculo de HP"""
        stats = PokemonStats(100, 50, 50, 50, 50, 50)
        pokemon = Pokemon("Test", 1, "Normal", None, stats, 50)
        
        # HP deve ser calculado baseado no level e stat base
        assert pokemon.max_hp > 100  # Deve ser maior que a stat base
        assert pokemon.current_hp == pokemon.max_hp  # Deve começar com HP cheio
    
    def test_pokemon_damage(self):
        """Testa sistema de dano"""
        stats = PokemonStats(100, 50, 50, 50, 50, 50)
        pokemon = Pokemon("Test", 1, "Normal", None, stats, 50)
        
        initial_hp = pokemon.current_hp
        damage = 20
        
        pokemon.take_damage(damage)
        
        assert pokemon.current_hp == initial_hp - damage
        assert not pokemon.is_fainted()
    
    def test_pokemon_faint(self):
        """Testa quando Pokémon desmaia"""
        stats = PokemonStats(50, 50, 50, 50, 50, 50)
        pokemon = Pokemon("Test", 1, "Normal", None, stats, 50)
        
        # Causa dano suficiente para desmaiar
        pokemon.take_damage(pokemon.max_hp)
        
        assert pokemon.current_hp <= 0
        assert pokemon.is_fainted()
    
    def test_pokemon_heal(self):
        """Testa cura de Pokémon"""
        stats = PokemonStats(100, 50, 50, 50, 50, 50)
        pokemon = Pokemon("Test", 1, "Normal", None, stats, 50)
        
        # Causa dano
        damage = 30
        pokemon.take_damage(damage)
        damaged_hp = pokemon.current_hp
        
        # Cura
        heal_amount = 15
        pokemon.heal(heal_amount)
        
        assert pokemon.current_hp == damaged_hp + heal_amount
        assert pokemon.current_hp <= pokemon.max_hp
    
    def test_pokemon_full_heal(self):
        """Testa cura completa"""
        stats = PokemonStats(100, 50, 50, 50, 50, 50)
        pokemon = Pokemon("Test", 1, "Normal", None, stats, 50)
        
        # Causa dano
        pokemon.take_damage(50)
        
        # Cura completa
        pokemon.restore_full_health()
        
        assert pokemon.current_hp == pokemon.max_hp
        assert not pokemon.is_fainted()
    
    def test_pokemon_types(self):
        """Testa sistema de tipos"""
        stats = PokemonStats(78, 84, 78, 109, 85, 100)
        charizard = Pokemon("Charizard", 6, "Fire", "Flying", stats, 50)
        
        types = charizard.get_types()
        assert "Fire" in types
        assert "Flying" in types
        assert len(types) == 2
        
        assert charizard.has_type("Fire")
        assert charizard.has_type("Flying")
        assert not charizard.has_type("Water")


class TestPokemonTeam:
    """Testes para a classe PokemonTeam"""
    
    def create_test_pokemon(self, name, pokemon_id):
        """Cria um Pokémon para testes"""
        stats = PokemonStats(100, 80, 80, 80, 80, 80)
        return Pokemon(name, pokemon_id, "Normal", None, stats, 50)
    
    def test_team_creation(self):
        """Testa criação de equipe"""
        pokemon1 = self.create_test_pokemon("Pokemon1", 1)
        pokemon2 = self.create_test_pokemon("Pokemon2", 2)
        
        team = PokemonTeam([pokemon1, pokemon2])
        
        assert len(team.pokemon) == 2
        assert pokemon1 in team.pokemon
        assert pokemon2 in team.pokemon
    
    def test_team_add_pokemon(self):
        """Testa adição de Pokémon à equipe"""
        team = PokemonTeam([])
        pokemon = self.create_test_pokemon("Test", 1)
        
        team.add_pokemon(pokemon)
        
        assert len(team.pokemon) == 1
        assert pokemon in team.pokemon
    
    def test_team_max_size(self):
        """Testa limite máximo da equipe"""
        team = PokemonTeam([])
        
        # Adiciona 6 Pokémon (limite máximo)
        for i in range(6):
            pokemon = self.create_test_pokemon(f"Pokemon{i}", i)
            team.add_pokemon(pokemon)
        
        assert len(team.pokemon) == 6
        
        # Tenta adicionar um 7º Pokémon
        extra_pokemon = self.create_test_pokemon("Extra", 7)
        team.add_pokemon(extra_pokemon)
        
        # Deve continuar com 6 Pokémon
        assert len(team.pokemon) == 6
        assert extra_pokemon not in team.pokemon
    
    def test_team_fainted_check(self):
        """Testa verificação se equipe desmaiou"""
        pokemon1 = self.create_test_pokemon("Pokemon1", 1)
        pokemon2 = self.create_test_pokemon("Pokemon2", 2)
        
        team = PokemonTeam([pokemon1, pokemon2])
        
        # Inicialmente, equipe não deve estar desmaiada
        assert not team.is_team_fainted()
        
        # Faz todos desmaiarem
        pokemon1.take_damage(pokemon1.max_hp)
        pokemon2.take_damage(pokemon2.max_hp)
        
        # Agora equipe deve estar desmaiada
        assert team.is_team_fainted()
    
    def test_team_stats(self):
        """Testa estatísticas da equipe"""
        pokemon1 = self.create_test_pokemon("Pokemon1", 1)
        pokemon2 = self.create_test_pokemon("Pokemon2", 2)
        
        team = PokemonTeam([pokemon1, pokemon2])
        team_stats = team.get_team_stats()
        
        assert "total_hp" in team_stats
        assert "avg_attack" in team_stats
        assert "avg_defense" in team_stats
        assert team_stats["total_hp"] == pokemon1.max_hp + pokemon2.max_hp


if __name__ == "__main__":
    pytest.main([__file__])
