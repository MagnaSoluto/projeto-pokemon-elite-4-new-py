#!/usr/bin/env python3
"""
Pokémon Elite Four - Sistema Completo de Análise e Simulação
============================================================

Sistema completo de análise e simulação de batalhas Pokémon para Game Boy Advanced,
focado na Elite Four com sexteto otimizado.

Autor: Adriano Carvalho dos Santos
RA: 10747203
MBA em Engenharia de Dados - Universidade Presbiteriana Mackenzie
"""

import sys
import argparse
from pathlib import Path
from typing import List, Optional

# Adiciona o diretório do projeto ao path
sys.path.append(str(Path(__file__).parent))

from pokemon_elite_four.core.pokemon import Pokemon, PokemonTeam
from pokemon_elite_four.core.battle_system import BattleSystem
from pokemon_elite_four.core.elite_four import EliteFour
from pokemon_elite_four.analysis.data_processor import DataProcessor
from pokemon_elite_four.analysis.team_optimizer import TeamOptimizer
from pokemon_elite_four.analysis.battle_analyzer import BattleAnalyzer
from pokemon_elite_four.utils.config import config
from pokemon_elite_four.utils.logger import setup_logger
from pokemon_elite_four.utils.visualization import save_all_visualizations


def main():
    """Função principal"""
    
    # Configura argumentos da linha de comando
    parser = argparse.ArgumentParser(
        description="Pokémon Elite Four - Sistema de Análise e Simulação"
    )
    
    parser.add_argument(
        "--mode",
        choices=["optimize", "analyze", "simulate", "demo"],
        default="demo",
        help="Modo de execução"
    )
    
    parser.add_argument(
        "--simulations",
        type=int,
        default=100,
        help="Número de simulações para análise"
    )
    
    parser.add_argument(
        "--generations",
        type=int,
        default=50,
        help="Número de gerações para otimização"
    )
    
    parser.add_argument(
        "--population",
        type=int,
        default=30,
        help="Tamanho da população para otimização"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default="output",
        help="Diretório de saída"
    )
    
    args = parser.parse_args()
    
    # Configura logger
    logger = setup_logger()
    logger.info("Iniciando Pokémon Elite Four - Sistema de Análise")
    
    try:
        if args.mode == "demo":
            run_demo()
        elif args.mode == "optimize":
            run_optimization(args)
        elif args.mode == "analyze":
            run_analysis(args)
        elif args.mode == "simulate":
            run_simulation(args)
        else:
            logger.error(f"Modo inválido: {args.mode}")
            return 1
            
    except Exception as e:
        logger.error(f"Erro durante execução: {e}")
        return 1
    
    logger.info("Execução concluída com sucesso!")
    return 0


def run_demo():
    """Executa demonstração do sistema"""
    
    print("🎮 POKÉMON ELITE FOUR - DEMONSTRAÇÃO")
    print("=" * 50)
    
    # Inicializa componentes
    print("\n📊 Carregando dados...")
    data_processor = DataProcessor()
    pokemon_database = data_processor.create_pokemon_database(level=50)
    
    print(f"✅ {len(pokemon_database)} Pokémon carregados")
    
    # Cria Elite Four
    print("\n👑 Criando Elite Four...")
    elite_four = EliteFour()
    print(f"✅ {len(elite_four.get_all_members())} membros da Elite Four criados")
    
    # Cria sistema de batalhas
    print("\n⚔️ Inicializando sistema de batalhas...")
    battle_system = BattleSystem()
    print("✅ Sistema de batalhas pronto")
    
    # Demonstração de batalha
    print("\n🎯 Demonstração de Batalha:")
    print("-" * 30)
    
    # Cria equipe de demonstração
    demo_team = create_demo_team(pokemon_database)
    print(f"Equipe de demonstração: {[p.name for p in demo_team.pokemon]}")
    
    # Batalha contra Lorelei
    lorelei = elite_four.get_member_by_name("Lorelei")
    if lorelei:
        print(f"\n⚔️ Batalhando contra {lorelei.name}...")
        battle_log = battle_system.battle_teams(demo_team, lorelei.pokemon_team)
        
        print(f"Resultado: {battle_log.battle_result.value}")
        print(f"Turnos: {battle_log.total_turns}")
        
        if battle_log.battle_result.value == "Win":
            print("🎉 Vitória!")
        else:
            print("💀 Derrota...")
    
    # Análise rápida
    print("\n📈 Análise rápida da equipe...")
    team_analysis = data_processor.create_team_analysis(demo_team.pokemon)
    print(f"Score da equipe: {team_analysis['team_score']:.3f}")
    print(f"Eficiência média: {team_analysis['avg_efficiency']:.3f}")
    print(f"Tipos únicos: {team_analysis['unique_types']}")
    
    print("\n✅ Demonstração concluída!")


def run_optimization(args):
    """Executa otimização de equipe"""
    
    print("🧬 OTIMIZAÇÃO DE EQUIPE")
    print("=" * 30)
    
    # Carrega dados
    data_processor = DataProcessor()
    pokemon_database = data_processor.create_pokemon_database(level=50)
    
    # Cria Elite Four
    elite_four = EliteFour()
    
    # Cria otimizador
    optimizer = TeamOptimizer(
        pokemon_database=pokemon_database,
        elite_four=elite_four,
        population_size=args.population,
        max_generations=args.generations
    )
    
    print(f"🔍 Otimizando com {args.population} indivíduos por {args.generations} gerações...")
    
    # Executa otimização
    result = optimizer.optimize_team()
    
    print(f"\n🏆 MELHOR EQUIPE ENCONTRADA:")
    print(f"Score: {result.best_score:.4f}")
    print(f"Gerações: {result.generation}")
    
    print(f"\n👥 Equipe otimizada:")
    for i, pokemon in enumerate(result.best_team.pokemon, 1):
        print(f"  {i}. {pokemon.name} (Lv.{pokemon.level}) - {pokemon.stats.total} total")
    
    # Salva resultados
    save_optimization_results(result, args.output)
    
    print(f"\n✅ Otimização concluída! Resultados salvos em {args.output}")


def run_analysis(args):
    """Executa análise de equipe"""
    
    print("📊 ANÁLISE DE EQUIPE")
    print("=" * 25)
    
    # Carrega dados
    data_processor = DataProcessor()
    pokemon_database = data_processor.create_pokemon_database(level=50)
    
    # Cria Elite Four
    elite_four = EliteFour()
    
    # Cria sistema de batalhas
    battle_system = BattleSystem()
    
    # Cria analisador
    analyzer = BattleAnalyzer(battle_system, elite_four)
    
    # Cria equipe de demonstração
    team = create_demo_team(pokemon_database)
    
    print(f"🔍 Analisando equipe: {[p.name for p in team.pokemon]}")
    print(f"📈 Executando {args.simulations} simulações...")
    
    # Executa análise
    analysis = analyzer.generate_battle_report(team, args.simulations)
    
    # Mostra resultados
    print(f"\n📊 RESULTADOS DA ANÁLISE:")
    print(f"Taxa de vitória geral: {analysis['team_overview']['overall_win_rate']:.1%}")
    print(f"Turnos médios: {analysis['team_overview']['overall_avg_turns']:.1f}")
    
    print(f"\n👑 Performance por membro:")
    for member, stats in analysis['member_performance'].items():
        print(f"  {member}: {stats.win_rate:.1%} vitórias")
    
    # Salva análise
    analyzer.export_analysis_to_csv(analysis, f"{args.output}/battle_analysis")
    
    print(f"\n✅ Análise concluída! Resultados salvos em {args.output}")


def run_simulation(args):
    """Executa simulação de batalhas"""
    
    print("⚔️ SIMULAÇÃO DE BATALHAS")
    print("=" * 30)
    
    # Carrega dados
    data_processor = DataProcessor()
    pokemon_database = data_processor.create_pokemon_database(level=50)
    
    # Cria Elite Four
    elite_four = EliteFour()
    
    # Cria sistema de batalhas
    battle_system = BattleSystem()
    
    # Cria equipe de demonstração
    team = create_demo_team(pokemon_database)
    
    print(f"🎯 Simulando {args.simulations} batalhas...")
    
    # Simula contra cada membro
    for member in elite_four.get_all_members():
        print(f"\n⚔️ Batalhando contra {member.name}...")
        
        stats = battle_system.simulate_battle(team, member.pokemon_team, args.simulations)
        
        print(f"  Taxa de vitória: {stats['win_rate']:.1%}")
        print(f"  Turnos médios: {stats['avg_turns']:.1f}")
    
    print(f"\n✅ Simulação concluída!")


def create_demo_team(pokemon_database: List[Pokemon]) -> PokemonTeam:
    """Cria equipe de demonstração"""
    
    # Pokémon populares para demonstração
    demo_names = ["Charizard", "Blastoise", "Venusaur", "Pikachu", "Alakazam", "Dragonite"]
    
    demo_pokemon = []
    for name in demo_names:
        pokemon = next((p for p in pokemon_database if p.name == name), None)
        if pokemon:
            # Ajusta nível para competir com Elite Four
            pokemon.level = 60
            demo_pokemon.append(pokemon)
    
    # Completa com Pokémon aleatórios se necessário
    while len(demo_pokemon) < 6:
        random_pokemon = next((p for p in pokemon_database if p not in demo_pokemon), None)
        if random_pokemon:
            random_pokemon.level = 60
            demo_pokemon.append(random_pokemon)
    
    return PokemonTeam(demo_pokemon[:6])


def save_optimization_results(result, output_dir: str):
    """Salva resultados da otimização"""
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Salva equipe
    team_file = output_path / "best_team.txt"
    with open(team_file, 'w', encoding='utf-8') as f:
        f.write("MELHOR EQUIPE ENCONTRADA\n")
        f.write("=" * 30 + "\n\n")
        f.write(f"Score: {result.best_score:.4f}\n")
        f.write(f"Gerações: {result.generation}\n\n")
        
        f.write("Equipe:\n")
        for i, pokemon in enumerate(result.best_team.pokemon, 1):
            f.write(f"{i}. {pokemon.name} (Lv.{pokemon.level})\n")
            f.write(f"   Tipos: {'/'.join([t.value for t in pokemon.get_types()])}\n")
            f.write(f"   Total: {pokemon.stats.total}\n\n")
    
    # Salva performance
    perf_file = output_path / "team_performance.txt"
    with open(perf_file, 'w', encoding='utf-8') as f:
        f.write("PERFORMANCE DA EQUIPE\n")
        f.write("=" * 25 + "\n\n")
        
        for member, win_rate in result.team_performance.items():
            f.write(f"{member}: {win_rate:.1%}\n")
    
    print(f"Resultados salvos em {output_path}")


if __name__ == "__main__":
    sys.exit(main())
