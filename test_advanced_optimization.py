#!/usr/bin/env python3
"""
Teste do Sistema de Otimização Avançado
"""

import sys
sys.path.append('.')

from pokemon_elite_four.core.pokemon import Pokemon, PokemonType, PokemonStats, PokemonTeam
from pokemon_elite_four.core.smart_battle_system import SmartBattleSystem, MoveStrategy
from pokemon_elite_four.core.elite_four import EliteFour
from pokemon_elite_four.analysis.advanced_team_optimizer import AdvancedTeamOptimizer
from pokemon_elite_four.analysis.data_processor import DataProcessor

def create_test_pokemon_database():
    """Cria base de dados de Pokémon para teste"""
    pokemon_data = [
        # Pokémon da equipe atual
        ("Lapras", 131, PokemonType.WATER, PokemonType.ICE, PokemonStats(130, 85, 80, 85, 95, 60)),
        ("Magneton", 82, PokemonType.ELECTRIC, PokemonType.STEEL, PokemonStats(50, 60, 95, 120, 70, 70)),
        ("Moltres", 146, PokemonType.FIRE, PokemonType.FLYING, PokemonStats(90, 100, 90, 125, 85, 90)),
        ("Gengar", 94, PokemonType.GHOST, PokemonType.POISON, PokemonStats(60, 65, 60, 130, 75, 110)),
        ("Mew", 151, PokemonType.PSYCHIC, None, PokemonStats(100, 100, 100, 100, 100, 100)),
        ("Golem", 76, PokemonType.ROCK, PokemonType.GROUND, PokemonStats(80, 120, 130, 55, 65, 45)),
        
        # Pokémon alternativos sugeridos
        ("Dragonite", 149, PokemonType.DRAGON, PokemonType.FLYING, PokemonStats(91, 134, 95, 100, 100, 80)),
        ("Alakazam", 65, PokemonType.PSYCHIC, None, PokemonStats(55, 50, 45, 135, 95, 120)),
        ("Snorlax", 143, PokemonType.NORMAL, None, PokemonStats(160, 110, 110, 65, 110, 30)),
        ("Jolteon", 135, PokemonType.ELECTRIC, None, PokemonStats(65, 65, 60, 110, 95, 130)),
        ("Rhydon", 112, PokemonType.GROUND, PokemonType.ROCK, PokemonStats(105, 130, 120, 45, 45, 40)),
        ("Charizard", 6, PokemonType.FIRE, PokemonType.FLYING, PokemonStats(78, 84, 78, 109, 85, 100)),
        ("Blastoise", 9, PokemonType.WATER, None, PokemonStats(79, 83, 100, 85, 105, 78)),
        ("Venusaur", 3, PokemonType.GRASS, PokemonType.POISON, PokemonStats(80, 82, 83, 100, 100, 80)),
        ("Pikachu", 25, PokemonType.ELECTRIC, None, PokemonStats(35, 55, 40, 50, 50, 90)),
        ("Raichu", 26, PokemonType.ELECTRIC, None, PokemonStats(60, 90, 55, 90, 80, 110)),
    ]
    
    pokemon_list = []
    for name, pokemon_id, type1, type2, stats in pokemon_data:
        pokemon = Pokemon(name, pokemon_id, type1, type2, stats, 60)
        pokemon_list.append(pokemon)
    
    return pokemon_list

def test_smart_battle_system():
    """Testa o sistema de batalhas inteligente"""
    print("🧠 TESTANDO SISTEMA DE BATALHAS INTELIGENTE:")
    
    # Cria Pokémon de teste
    charizard = Pokemon('Charizard', 6, PokemonType.FIRE, PokemonType.FLYING, 
                       PokemonStats(78, 84, 78, 109, 85, 100), 60)
    blastoise = Pokemon('Blastoise', 9, PokemonType.WATER, None,
                       PokemonStats(79, 83, 100, 85, 105, 78), 60)
    
    smart_system = SmartBattleSystem()
    
    # Testa diferentes estratégias
    strategies = [
        MoveStrategy.RANDOM,
        MoveStrategy.HIGHEST_DAMAGE,
        MoveStrategy.TYPE_EFFECTIVE,
        MoveStrategy.BALANCED
    ]
    
    for strategy in strategies:
        print(f"\\n  Estratégia: {strategy.value}")
        
        # Simula 10 batalhas
        wins = 0
        for _ in range(10):
            battle_log = smart_system.battle_pokemon_smart(
                charizard, blastoise, strategy, MoveStrategy.BALANCED
            )
            if battle_log.battle_result.value == "Win":
                wins += 1
        
        win_rate = wins / 10
        print(f"    Taxa de vitória: {win_rate:.1%}")

def test_advanced_optimizer():
    """Testa o otimizador avançado"""
    print("\\n🚀 TESTANDO OTIMIZADOR AVANÇADO:")
    
    # Cria base de dados
    pokemon_database = create_test_pokemon_database()
    elite_four = EliteFour()
    
    # Cria otimizador
    optimizer = AdvancedTeamOptimizer(
        pokemon_database=pokemon_database,
        elite_four=elite_four,
        population_size=50,
        max_generations=20,
        mutation_rate=0.15,
        crossover_rate=0.8
    )
    
    print("  Iniciando otimização...")
    
    # Executa otimização
    result = optimizer.optimize_team_advanced()
    
    print(f"\\n  🏆 RESULTADO DA OTIMIZAÇÃO:")
    print(f"    Melhor Score: {result.best_score:.4f}")
    print(f"    Gerações: {result.generation}")
    print(f"    Equipe Otimizada:")
    
    for i, pokemon in enumerate(result.best_team.pokemon, 1):
        types_str = f"{pokemon.type1.value}"
        if pokemon.type2:
            types_str += f"/{pokemon.type2.value}"
        print(f"      {i}. {pokemon.name} (Lv.{pokemon.level}) - {types_str}")
    
    # Testa performance da equipe otimizada
    print(f"\\n  📊 TESTE DE PERFORMANCE:")
    smart_system = SmartBattleSystem()
    
    for member in elite_four.get_all_members():
        wins = 0
        total_battles = 10
        
        for _ in range(total_battles):
            battle_log = smart_system.battle_teams_smart(
                result.best_team, member.pokemon_team, 
                MoveStrategy.BALANCED, MoveStrategy.BALANCED
            )
            if battle_log.battle_result.value == "Win":
                wins += 1
        
        win_rate = wins / total_battles
        print(f"    {member.name}: {win_rate:.1%} vitórias")

def compare_systems():
    """Compara sistema antigo vs novo"""
    print("\\n⚖️ COMPARAÇÃO DE SISTEMAS:")
    
    # Cria Pokémon de teste
    charizard = Pokemon('Charizard', 6, PokemonType.FIRE, PokemonType.FLYING, 
                       PokemonStats(78, 84, 78, 109, 85, 100), 60)
    blastoise = Pokemon('Blastoise', 9, PokemonType.WATER, None,
                       PokemonStats(79, 83, 100, 85, 105, 78), 60)
    
    # Sistema antigo (aleatório)
    from pokemon_elite_four.core.battle_system import BattleSystem
    old_system = BattleSystem()
    
    # Sistema novo (inteligente)
    smart_system = SmartBattleSystem()
    
    print("  Sistema Antigo (Aleatório):")
    old_wins = 0
    for _ in range(20):
        battle_log = old_system.battle_pokemon(charizard, blastoise)
        if battle_log.battle_result.value == "Win":
            old_wins += 1
    print(f"    Taxa de vitória: {old_wins/20:.1%}")
    
    print("  Sistema Novo (Inteligente):")
    smart_wins = 0
    for _ in range(20):
        battle_log = smart_system.battle_pokemon_smart(
            charizard, blastoise, MoveStrategy.BALANCED, MoveStrategy.BALANCED
        )
        if battle_log.battle_result.value == "Win":
            smart_wins += 1
    print(f"    Taxa de vitória: {smart_wins/20:.1%}")
    
    improvement = (smart_wins - old_wins) / 20
    print(f"  Melhoria: {improvement:+.1%}")

def main():
    """Função principal"""
    print("🎮 TESTE DO SISTEMA DE OTIMIZAÇÃO AVANÇADO")
    print("=" * 50)
    
    try:
        # Testa sistema de batalhas inteligente
        test_smart_battle_system()
        
        # Testa otimizador avançado
        test_advanced_optimizer()
        
        # Compara sistemas
        compare_systems()
        
        print("\\n✅ Todos os testes concluídos com sucesso!")
        
    except Exception as e:
        print(f"\\n❌ Erro durante os testes: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
