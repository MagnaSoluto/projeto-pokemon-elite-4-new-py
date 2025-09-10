"""
Visualizações e Gráficos
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
from pathlib import Path
from ..core.pokemon import Pokemon, PokemonTeam
from ..analysis.battle_analyzer import BattleStatistics
from .config import config


def setup_plot_style():
    """Configura estilo dos gráficos"""
    try:
        plt.style.use('seaborn-v0_8')
    except OSError:
        plt.style.use('seaborn')
    sns.set_palette("husl")
    
    # Configurações de fonte
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.titlesize'] = 12
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['xtick.labelsize'] = 9
    plt.rcParams['ytick.labelsize'] = 9
    plt.rcParams['legend.fontsize'] = 9


def create_team_radar(
    team: PokemonTeam, 
    title: str = "Análise Radar da Equipe",
    save_path: Optional[str] = None
) -> plt.Figure:
    """Cria gráfico radar da equipe"""
    
    setup_plot_style()
    
    # Categorias para o radar
    categories = ['HP', 'Ataque', 'Defesa', 'Sp.Ataque', 'Sp.Defesa', 'Velocidade']
    
    # Calcula médias da equipe
    team_stats = {
        'HP': np.mean([p.stats.hp for p in team.pokemon]),
        'Ataque': np.mean([p.attack for p in team.pokemon]),
        'Defesa': np.mean([p.defense for p in team.pokemon]),
        'Sp.Ataque': np.mean([p.sp_attack for p in team.pokemon]),
        'Sp.Defesa': np.mean([p.sp_defense for p in team.pokemon]),
        'Velocidade': np.mean([p.speed for p in team.pokemon])
    }
    
    # Normaliza valores (0-100)
    max_values = {'HP': 140, 'Ataque': 134, 'Defesa': 180, 'Sp.Ataque': 154, 'Sp.Defesa': 154, 'Velocidade': 140}
    normalized_stats = {cat: (team_stats[cat] / max_values[cat]) * 100 for cat in categories}
    
    # Ângulos para o radar
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # Fecha o círculo
    
    # Valores normalizados
    values = list(normalized_stats.values())
    values += values[:1]  # Fecha o círculo
    
    # Cria figura
    fig, ax = plt.subplots(figsize=(config.PLOT_WIDTH, config.PLOT_HEIGHT), subplot_kw=dict(projection='polar'))
    
    # Plota o radar
    ax.plot(angles, values, 'o-', linewidth=2, label='Equipe')
    ax.fill(angles, values, alpha=0.25)
    
    # Configura eixos
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'])
    ax.grid(True)
    
    # Título
    ax.set_title(title, size=16, fontweight='bold', pad=20)
    
    # Legenda
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config.DPI, bbox_inches='tight')
    
    return fig


def create_performance_chart(
    performance_data: Dict[str, BattleStatistics],
    title: str = "Performance contra Elite Four",
    save_path: Optional[str] = None
) -> plt.Figure:
    """Cria gráfico de performance"""
    
    setup_plot_style()
    
    # Prepara dados
    members = list(performance_data.keys())
    win_rates = [stats.win_rate for stats in performance_data.values()]
    avg_turns = [stats.avg_turns for stats in performance_data.values()]
    
    # Cria figura com subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(config.PLOT_WIDTH * 1.5, config.PLOT_HEIGHT))
    
    # Gráfico de taxa de vitória
    bars1 = ax1.bar(members, win_rates, color='skyblue', alpha=0.7)
    ax1.set_title('Taxa de Vitória por Membro', fontweight='bold')
    ax1.set_ylabel('Taxa de Vitória')
    ax1.set_ylim(0, 1)
    ax1.tick_params(axis='x', rotation=45)
    
    # Adiciona valores nas barras
    for bar, rate in zip(bars1, win_rates):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{rate:.1%}', ha='center', va='bottom')
    
    # Gráfico de turnos médios
    bars2 = ax2.bar(members, avg_turns, color='lightcoral', alpha=0.7)
    ax2.set_title('Turnos Médios por Membro', fontweight='bold')
    ax2.set_ylabel('Turnos Médios')
    ax2.tick_params(axis='x', rotation=45)
    
    # Adiciona valores nas barras
    for bar, turns in zip(bars2, avg_turns):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{turns:.1f}', ha='center', va='bottom')
    
    plt.suptitle(title, fontsize=16, fontweight='bold')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config.DPI, bbox_inches='tight')
    
    return fig


def create_type_distribution_chart(
    team: PokemonTeam,
    title: str = "Distribuição de Tipos da Equipe",
    save_path: Optional[str] = None
) -> plt.Figure:
    """Cria gráfico de distribuição de tipos"""
    
    setup_plot_style()
    
    # Conta tipos
    type_counts = {}
    for pokemon in team.pokemon:
        for pokemon_type in pokemon.get_types():
            type_name = pokemon_type.value
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
    
    # Prepara dados
    types = list(type_counts.keys())
    counts = list(type_counts.values())
    
    # Cria gráfico
    fig, ax = plt.subplots(figsize=(config.PLOT_WIDTH, config.PLOT_HEIGHT))
    
    # Gráfico de pizza
    wedges, texts, autotexts = ax.pie(counts, labels=types, autopct='%1.1f%%', startangle=90)
    
    # Melhora aparência
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config.DPI, bbox_inches='tight')
    
    return fig


def create_fitness_evolution_chart(
    fitness_history: List[float],
    title: str = "Evolução do Fitness",
    save_path: Optional[str] = None
) -> plt.Figure:
    """Cria gráfico da evolução do fitness"""
    
    setup_plot_style()
    
    fig, ax = plt.subplots(figsize=(config.PLOT_WIDTH, config.PLOT_HEIGHT))
    
    generations = range(1, len(fitness_history) + 1)
    
    ax.plot(generations, fitness_history, 'b-', linewidth=2, marker='o', markersize=4)
    ax.set_xlabel('Geração')
    ax.set_ylabel('Fitness')
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Adiciona linha de tendência
    z = np.polyfit(generations, fitness_history, 1)
    p = np.poly1d(z)
    ax.plot(generations, p(generations), "r--", alpha=0.8, label='Tendência')
    
    ax.legend()
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config.DPI, bbox_inches='tight')
    
    return fig


def create_pokemon_comparison_chart(
    pokemon_list: List[Pokemon],
    title: str = "Comparação de Pokémon",
    save_path: Optional[str] = None
) -> plt.Figure:
    """Cria gráfico de comparação entre Pokémon"""
    
    setup_plot_style()
    
    # Prepara dados
    names = [p.name for p in pokemon_list]
    stats = ['HP', 'Ataque', 'Defesa', 'Sp.Ataque', 'Sp.Defesa', 'Velocidade']
    
    data = []
    for pokemon in pokemon_list:
        data.append([
            pokemon.stats.hp,
            pokemon.attack,
            pokemon.defense,
            pokemon.sp_attack,
            pokemon.sp_defense,
            pokemon.speed
        ])
    
    # Cria DataFrame
    df = pd.DataFrame(data, index=names, columns=stats)
    
    # Cria heatmap
    fig, ax = plt.subplots(figsize=(config.PLOT_WIDTH, config.PLOT_HEIGHT))
    
    sns.heatmap(df, annot=True, cmap='YlOrRd', fmt='d', ax=ax)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('Estatísticas')
    ax.set_ylabel('Pokémon')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=config.DPI, bbox_inches='tight')
    
    return fig


def save_all_visualizations(
    team: PokemonTeam,
    performance_data: Dict[str, BattleStatistics],
    fitness_history: List[float],
    output_dir: str = None
) -> None:
    """Salva todas as visualizações"""
    
    if output_dir is None:
        output_dir = config.PLOTS_DIR
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Radar da equipe
    create_team_radar(
        team, 
        save_path=str(output_path / "team_radar.png")
    )
    
    # Performance
    create_performance_chart(
        performance_data,
        save_path=str(output_path / "performance_chart.png")
    )
    
    # Distribuição de tipos
    create_type_distribution_chart(
        team,
        save_path=str(output_path / "type_distribution.png")
    )
    
    # Evolução do fitness
    if fitness_history:
        create_fitness_evolution_chart(
            fitness_history,
            save_path=str(output_path / "fitness_evolution.png")
        )
    
    # Comparação de Pokémon
    create_pokemon_comparison_chart(
        team.pokemon,
        save_path=str(output_path / "pokemon_comparison.png")
    )
    
    print(f"Visualizações salvas em: {output_dir}")
