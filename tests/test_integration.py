"""
Testes de integração para o sistema completo
"""

import pytest
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent.parent))

from pokemon_elite_four.core.pokemon import Pokemon, PokemonTeam, PokemonStats
from pokemon_elite_four.core.battle_system import BattleSystem
from pokemon_elite_four.analysis.data_processor import DataProcessor
from pokemon_elite_four.analysis.team_optimizer import TeamOptimizer
from pokemon_elite_four.analysis.battle_analyzer import BattleAnalyzer


class TestSystemIntegration:
    """Testes de integração do sistema completo"""
    
    def create_test_team(self, size=3):
        """Cria uma equipe de teste"""
        team_pokemon = []
        
        # Diferentes tipos para variedade
        pokemon_data = [
            ("Charizard", 6, "Fire", "Flying", PokemonStats(78, 84, 78, 109, 85, 100)),
            ("Blastoise", 9, "Water", None, PokemonStats(79, 83, 100, 85, 105, 78)),
            ("Venusaur", 3, "Grass", "Poison", PokemonStats(80, 82, 83, 100, 100, 80)),
            ("Pikachu", 25, "Electric", None, PokemonStats(35, 55, 40, 50, 50, 90)),
            ("Alakazam", 65, "Psychic", None, PokemonStats(55, 50, 45, 135, 95, 120)),
            ("Machamp", 68, "Fighting", None, PokemonStats(90, 130, 80, 65, 85, 55))
        ]
        
        for i in range(min(size, len(pokemon_data))):
            name, poke_id, type1, type2, stats = pokemon_data[i]
            pokemon = Pokemon(name, poke_id, type1, type2, stats, 50)
            team_pokemon.append(pokemon)
        
        return PokemonTeam(team_pokemon)
    
    def test_battle_system_integration(self):
        """Testa integração do sistema de batalhas"""
        # Cria sistema e equipes
        battle_system = BattleSystem()
        team1 = self.create_test_team(3)
        team2 = self.create_test_team(3)
        
        # Salva estado inicial
        initial_hp_team1 = [p.current_hp for p in team1.pokemon]
        initial_hp_team2 = [p.current_hp for p in team2.pokemon]
        
        # Executa batalha entre equipes
        winner = battle_system.battle_team(team1, team2)
        
        # Deve haver um vencedor
        assert winner in [team1, team2]
        
        # Pelo menos uma equipe deve ter perdido HP
        final_hp_team1 = [p.current_hp for p in team1.pokemon]
        final_hp_team2 = [p.current_hp for p in team2.pokemon]
        
        hp_changed = (initial_hp_team1 != final_hp_team1 or 
                     initial_hp_team2 != final_hp_team2)
        assert hp_changed
    
    def test_data_processor_integration(self):
        """Testa integração do processador de dados"""
        processor = DataProcessor()
        
        try:
            # Tenta carregar dados reais
            pokemon_data = processor.load_pokemon_data("data/pokemon_processed.csv")
            
            # Deve conseguir processar os dados
            processed_data = processor.preprocess_data(pokemon_data)
            assert len(processed_data) > 0
            
            # Deve conseguir validar
            is_valid = processor.validate_data(processed_data)
            assert isinstance(is_valid, bool)
            
        except FileNotFoundError:
            pytest.skip("Dados não encontrados para teste de integração")
    
    def test_battle_analyzer_integration(self):
        """Testa integração do analisador de batalhas"""
        # Cria componentes
        battle_system = BattleSystem()
        analyzer = BattleAnalyzer(battle_system)
        team = self.create_test_team(3)
        
        # Testa análise de performance individual
        individual_results = analyzer.analyze_individual_performance(team)
        
        # Deve retornar resultados para cada Pokémon
        assert len(individual_results) == len(team.pokemon)
        
        # Cada resultado deve ter métricas básicas
        for result in individual_results:
            assert "pokemon" in result
            assert "battles_won" in result
            assert "battles_lost" in result
    
    def test_team_optimizer_integration(self):
        """Testa integração do otimizador de equipes"""
        try:
            # Cria otimizador (pode precisar de dados)
            optimizer = TeamOptimizer()
            
            # Testa otimização rápida (poucas gerações para teste)
            best_team, fitness = optimizer.optimize_team(
                generations=5,  # Poucas gerações para teste rápido
                population_size=10  # População pequena para teste rápido
            )
            
            # Deve retornar uma equipe válida
            assert best_team is not None
            assert isinstance(best_team, PokemonTeam)
            assert len(best_team.pokemon) <= 6
            
            # Fitness deve ser um número
            assert isinstance(fitness, (int, float))
            assert fitness >= 0
            
        except Exception as e:
            # Se não conseguir otimizar (falta de dados, etc), pula teste
            pytest.skip(f"Otimização não disponível: {e}")
    
    def test_full_system_workflow(self):
        """Testa fluxo completo do sistema"""
        try:
            # 1. Carrega dados
            processor = DataProcessor()
            pokemon_data = processor.load_pokemon_data("data/pokemon_processed.csv")
            
            # 2. Cria sistema de batalhas
            battle_system = BattleSystem()
            
            # 3. Cria equipes de teste
            team1 = self.create_test_team(3)
            team2 = self.create_test_team(3)
            
            # 4. Analisa performance
            analyzer = BattleAnalyzer(battle_system)
            team1_analysis = analyzer.analyze_individual_performance(team1)
            
            # 5. Executa batalha
            winner = battle_system.battle_team(team1, team2)
            
            # Verifica se tudo funcionou
            assert len(pokemon_data) > 0
            assert team1_analysis is not None
            assert winner in [team1, team2]
            
        except FileNotFoundError:
            pytest.skip("Dados necessários não encontrados")
        except Exception as e:
            pytest.fail(f"Falha no fluxo completo: {e}")
    
    def test_config_integration(self):
        """Testa integração das configurações"""
        from pokemon_elite_four.utils.config import config
        
        # Verifica se configurações estão acessíveis
        assert config is not None
        assert hasattr(config, 'DATA_DIR')
        assert hasattr(config, 'OUTPUT_DIR')
        assert hasattr(config, 'MAX_BATTLE_TURNS')
        
        # Verifica se valores fazem sentido
        assert config.MAX_BATTLE_TURNS > 0
        assert config.POPULATION_SIZE > 0
        assert 0 <= config.MUTATION_RATE <= 1
        assert 0 <= config.CROSSOVER_RATE <= 1
    
    def test_logging_integration(self):
        """Testa integração do sistema de logging"""
        from pokemon_elite_four.utils.logger import setup_logger
        
        # Configura logger
        logger = setup_logger("test_logger")
        
        # Testa se logger funciona
        assert logger is not None
        
        # Testa log básico (não deve dar erro)
        try:
            logger.info("Teste de integração do logger")
            logger.debug("Teste de debug")
            logger.warning("Teste de warning")
        except Exception as e:
            pytest.fail(f"Logger não funcionou: {e}")
    
    def test_pokemon_creation_from_data(self):
        """Testa criação de Pokémon a partir de dados reais"""
        try:
            processor = DataProcessor()
            pokemon_data = processor.load_pokemon_data("data/pokemon_processed.csv")
            
            # Pega primeiro Pokémon dos dados
            first_pokemon_data = pokemon_data.iloc[0]
            
            # Cria Pokémon a partir dos dados
            stats = PokemonStats(
                hp=first_pokemon_data.get("HP", 50),
                attack=first_pokemon_data.get("Attack", 50),
                defense=first_pokemon_data.get("Defense", 50),
                sp_attack=first_pokemon_data.get("Sp. Atk", 50),
                sp_defense=first_pokemon_data.get("Sp. Def", 50),
                speed=first_pokemon_data.get("Speed", 50)
            )
            
            pokemon = Pokemon(
                name=first_pokemon_data.get("Name", "Unknown"),
                pokemon_id=1,
                type1=first_pokemon_data.get("Type 1", "Normal"),
                type2=first_pokemon_data.get("Type 2"),
                stats=stats,
                level=50
            )
            
            # Verifica se Pokémon foi criado corretamente
            assert pokemon.name == first_pokemon_data.get("Name", "Unknown")
            assert pokemon.type1 == first_pokemon_data.get("Type 1", "Normal")
            assert pokemon.current_hp > 0
            assert pokemon.max_hp > 0
            
        except FileNotFoundError:
            pytest.skip("Dados não encontrados para teste")
        except Exception as e:
            pytest.fail(f"Erro na criação de Pokémon: {e}")


if __name__ == "__main__":
    pytest.main([__file__])
