"""
Testes para o sistema de batalhas
"""

import pytest
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent.parent))

from pokemon_elite_four.core.pokemon import Pokemon, PokemonStats
from pokemon_elite_four.core.battle_system import BattleSystem, TypeEffectiveness
from pokemon_elite_four.core.moves import Move, MoveCategory


class TestTypeEffectiveness:
    """Testes para efetividade de tipos"""
    
    def test_super_effective(self):
        """Testa ataques super efetivos"""
        # Água contra Fogo = 2x
        effectiveness = TypeEffectiveness.get_effectiveness("Water", ["Fire"])
        assert effectiveness == 2.0
        
        # Fogo contra Grama = 2x
        effectiveness = TypeEffectiveness.get_effectiveness("Fire", ["Grass"])
        assert effectiveness == 2.0
    
    def test_not_very_effective(self):
        """Testa ataques pouco efetivos"""
        # Água contra Grama = 0.5x
        effectiveness = TypeEffectiveness.get_effectiveness("Water", ["Grass"])
        assert effectiveness == 0.5
        
        # Fogo contra Água = 0.5x
        effectiveness = TypeEffectiveness.get_effectiveness("Fire", ["Water"])
        assert effectiveness == 0.5
    
    def test_no_effect(self):
        """Testa ataques sem efeito"""
        # Normal contra Fantasma = 0x
        effectiveness = TypeEffectiveness.get_effectiveness("Normal", ["Ghost"])
        assert effectiveness == 0.0
        
        # Elétrico contra Terra = 0x
        effectiveness = TypeEffectiveness.get_effectiveness("Electric", ["Ground"])
        assert effectiveness == 0.0
    
    def test_normal_effectiveness(self):
        """Testa ataques com efetividade normal"""
        # Normal contra Normal = 1x
        effectiveness = TypeEffectiveness.get_effectiveness("Normal", ["Normal"])
        assert effectiveness == 1.0
        
        # Água contra Elétrico = 1x
        effectiveness = TypeEffectiveness.get_effectiveness("Water", ["Electric"])
        assert effectiveness == 1.0
    
    def test_dual_type_effectiveness(self):
        """Testa efetividade contra Pokémon de dois tipos"""
        # Pedra contra Fogo/Voador = 4x (2x * 2x)
        effectiveness = TypeEffectiveness.get_effectiveness("Rock", ["Fire", "Flying"])
        assert effectiveness == 4.0
        
        # Luta contra Normal/Voador = 1x (2x * 0.5x)
        effectiveness = TypeEffectiveness.get_effectiveness("Fighting", ["Normal", "Flying"])
        assert effectiveness == 1.0


class TestBattleSystem:
    """Testes para o sistema de batalhas"""
    
    def create_test_pokemon(self, name, pokemon_id, type1, type2=None):
        """Cria um Pokémon para testes"""
        stats = PokemonStats(100, 80, 80, 80, 80, 80)
        return Pokemon(name, pokemon_id, type1, type2, stats, 50)
    
    def create_test_move(self, name="Test Move", move_type="Normal", power=80):
        """Cria um movimento para testes"""
        return Move(
            name=name,
            move_type=move_type,
            category=MoveCategory.PHYSICAL,
            power=power,
            accuracy=100,
            pp=20,
            priority=0,
            target="Enemy",
            description="Movimento de teste"
        )
    
    def test_battle_system_creation(self):
        """Testa criação do sistema de batalhas"""
        battle_system = BattleSystem()
        assert battle_system is not None
    
    def test_damage_calculation_basic(self):
        """Testa cálculo básico de dano"""
        battle_system = BattleSystem()
        
        attacker = self.create_test_pokemon("Attacker", 1, "Normal")
        defender = self.create_test_pokemon("Defender", 2, "Normal")
        move = self.create_test_move("Test Move", "Normal", 80)
        
        damage = battle_system.calculate_damage(attacker, defender, move)
        
        assert damage > 0
        assert isinstance(damage, int)
    
    def test_damage_with_type_effectiveness(self):
        """Testa dano com efetividade de tipos"""
        battle_system = BattleSystem()
        
        # Atacante Água vs Defensor Fogo (super efetivo)
        water_pokemon = self.create_test_pokemon("Blastoise", 9, "Water")
        fire_pokemon = self.create_test_pokemon("Charizard", 6, "Fire")
        water_move = self.create_test_move("Water Gun", "Water", 80)
        
        # Atacante Fogo vs Defensor Água (pouco efetivo)
        fire_move = self.create_test_move("Flamethrower", "Fire", 80)
        
        super_effective_damage = battle_system.calculate_damage(
            water_pokemon, fire_pokemon, water_move
        )
        not_very_effective_damage = battle_system.calculate_damage(
            fire_pokemon, water_pokemon, fire_move
        )
        
        # Dano super efetivo deve ser maior
        assert super_effective_damage > not_very_effective_damage
    
    def test_critical_hit_calculation(self):
        """Testa cálculo de critical hit"""
        battle_system = BattleSystem()
        
        attacker = self.create_test_pokemon("Attacker", 1, "Normal")
        move = self.create_test_move()
        
        # Testa várias vezes para verificar randomização
        critical_hits = 0
        total_tests = 1000
        
        for _ in range(total_tests):
            if battle_system.is_critical_hit(attacker, move):
                critical_hits += 1
        
        # Critical hit rate deve estar próximo de 6.25% (1/16)
        critical_rate = critical_hits / total_tests
        assert 0.03 <= critical_rate <= 0.12  # Margem para randomização
    
    def test_move_accuracy(self):
        """Testa precisão de movimentos"""
        battle_system = BattleSystem()
        
        attacker = self.create_test_pokemon("Attacker", 1, "Normal")
        defender = self.create_test_pokemon("Defender", 2, "Normal")
        
        # Movimento com 100% de precisão
        accurate_move = self.create_test_move("Accurate Move", "Normal", 80)
        accurate_move.accuracy = 100
        
        # Movimento com 50% de precisão
        inaccurate_move = self.create_test_move("Inaccurate Move", "Normal", 80)
        inaccurate_move.accuracy = 50
        
        # Testa várias vezes
        accurate_hits = 0
        inaccurate_hits = 0
        total_tests = 1000
        
        for _ in range(total_tests):
            if battle_system.does_move_hit(accurate_move, attacker, defender):
                accurate_hits += 1
            if battle_system.does_move_hit(inaccurate_move, attacker, defender):
                inaccurate_hits += 1
        
        accurate_rate = accurate_hits / total_tests
        inaccurate_rate = inaccurate_hits / total_tests
        
        # Movimento preciso deve acertar mais
        assert accurate_rate > inaccurate_rate
        assert accurate_rate > 0.95  # Deve acertar quase sempre
        assert 0.35 <= inaccurate_rate <= 0.65  # Deve acertar ~50%
    
    def test_pokemon_battle_basic(self):
        """Testa batalha básica entre dois Pokémon"""
        battle_system = BattleSystem()
        
        pokemon1 = self.create_test_pokemon("Pokemon1", 1, "Normal")
        pokemon2 = self.create_test_pokemon("Pokemon2", 2, "Normal")
        
        # Salva HP inicial
        initial_hp1 = pokemon1.current_hp
        initial_hp2 = pokemon2.current_hp
        
        # Executa batalha
        result = battle_system.battle_pokemon(pokemon1, pokemon2)
        
        # Deve ter um vencedor
        assert result in [pokemon1, pokemon2]
        
        # Pelo menos um dos Pokémon deve ter perdido HP
        assert (pokemon1.current_hp < initial_hp1 or 
                pokemon2.current_hp < initial_hp2)
    
    def test_battle_turn_execution(self):
        """Testa execução de um turno de batalha"""
        battle_system = BattleSystem()
        
        attacker = self.create_test_pokemon("Attacker", 1, "Normal")
        defender = self.create_test_pokemon("Defender", 2, "Normal")
        move = self.create_test_move()
        
        initial_defender_hp = defender.current_hp
        
        # Executa um turno
        battle_system.execute_turn(attacker, defender, move, 1)
        
        # Defensor deve ter perdido HP (assumindo que o ataque acertou)
        # Pode não ter perdido se errou ou não causou dano
        assert defender.current_hp <= initial_defender_hp
    
    def test_fainted_pokemon_battle(self):
        """Testa batalha com Pokémon desmaiado"""
        battle_system = BattleSystem()
        
        pokemon1 = self.create_test_pokemon("Pokemon1", 1, "Normal")
        pokemon2 = self.create_test_pokemon("Pokemon2", 2, "Normal")
        
        # Faz pokemon1 desmaiar
        pokemon1.take_damage(pokemon1.max_hp)
        
        # Batalha não deve ocorrer
        result = battle_system.battle_pokemon(pokemon1, pokemon2)
        
        # Pokemon2 deve vencer automaticamente
        assert result == pokemon2


if __name__ == "__main__":
    pytest.main([__file__])
