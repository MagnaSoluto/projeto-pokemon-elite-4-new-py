"""
Processador de Dados - Carregamento e preparação de dados Pokémon
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from ..core.pokemon import Pokemon, PokemonType, PokemonStats
from ..core.moves import create_default_moveset


class DataProcessor:
    """Processador de dados Pokémon"""
    
    def __init__(self, data_path: str = "data/"):
        self.data_path = Path(data_path)
        self.pokemon_data = None
        self.elite_four_data = None
    
    def load_pokemon_data(self, filename: str = "pokemon_data.csv") -> pd.DataFrame:
        """Carrega dados dos Pokémon"""
        file_path = self.data_path / filename
        
        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
        
        self.pokemon_data = pd.read_csv(file_path)
        return self.pokemon_data
    
    def load_elite_four_data(self, filename: str = "elite_four_data.csv") -> pd.DataFrame:
        """Carrega dados da Elite Four"""
        file_path = self.data_path / filename
        
        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
        
        self.elite_four_data = pd.read_csv(file_path)
        return self.elite_four_data
    
    def create_pokemon_from_data(self, row: pd.Series, level: int = 50) -> Pokemon:
        """Cria objeto Pokemon a partir de dados CSV"""
        
        # Mapeia tipos
        type_mapping = {
            'Normal': PokemonType.NORMAL,
            'Fire': PokemonType.FIRE,
            'Water': PokemonType.WATER,
            'Electric': PokemonType.ELECTRIC,
            'Grass': PokemonType.GRASS,
            'Ice': PokemonType.ICE,
            'Fighting': PokemonType.FIGHTING,
            'Poison': PokemonType.POISON,
            'Ground': PokemonType.GROUND,
            'Flying': PokemonType.FLYING,
            'Psychic': PokemonType.PSYCHIC,
            'Bug': PokemonType.BUG,
            'Rock': PokemonType.ROCK,
            'Ghost': PokemonType.GHOST,
            'Dragon': PokemonType.DRAGON,
            'Steel': PokemonType.STEEL,
            'Dark': PokemonType.DARK
        }
        
        type1 = type_mapping.get(row['type1'], PokemonType.NORMAL)
        type2 = type_mapping.get(row['type2'], None) if pd.notna(row['type2']) else None
        
        # Cria estatísticas
        stats = PokemonStats(
            hp=int(row['hp']),
            attack=int(row['attack']),
            defense=int(row['defense']),
            sp_attack=int(row['sp_attack']),
            sp_defense=int(row['sp_defense']),
            speed=int(row['speed'])
        )
        
        # Cria Pokémon
        pokemon = Pokemon(
            name=row['name'],
            pokemon_id=int(row['id']),
            type1=type1,
            type2=type2,
            stats=stats,
            level=level
        )
        
        # Adiciona moveset padrão
        pokemon.move_set = create_default_moveset(type1)
        
        return pokemon
    
    def create_pokemon_database(self, level: int = 50) -> List[Pokemon]:
        """Cria base de dados de Pokémon"""
        if self.pokemon_data is None:
            self.load_pokemon_data()
        
        pokemon_list = []
        for _, row in self.pokemon_data.iterrows():
            try:
                pokemon = self.create_pokemon_from_data(row, level)
                pokemon_list.append(pokemon)
            except Exception as e:
                print(f"Erro ao criar Pokémon {row['name']}: {e}")
                continue
        
        return pokemon_list
    
    def calculate_pokemon_metrics(self, pokemon: Pokemon) -> Dict[str, float]:
        """Calcula métricas de um Pokémon"""
        
        # Métricas básicas
        total_stats = pokemon.stats.total
        combat_avg = (pokemon.attack + pokemon.defense + pokemon.sp_attack + 
                     pokemon.sp_defense + pokemon.speed) / 5
        defense_avg = (pokemon.stats.hp + pokemon.defense + pokemon.sp_defense) / 3
        offense_avg = (pokemon.attack + pokemon.sp_attack + pokemon.speed) / 3
        
        # Balanceamento
        balance = 1 - (abs(pokemon.attack - pokemon.defense) + 
                      abs(pokemon.sp_attack - pokemon.sp_defense)) / total_stats
        
        # Eficiência
        efficiency = total_stats / 600
        
        # Categoria de poder
        if total_stats >= 500:
            power_category = "Alto"
        elif total_stats >= 400:
            power_category = "Médio"
        else:
            power_category = "Baixo"
        
        return {
            'total_stats': total_stats,
            'combat_avg': combat_avg,
            'defense_avg': defense_avg,
            'offense_avg': offense_avg,
            'balance': balance,
            'efficiency': efficiency,
            'power_category': power_category
        }
    
    def analyze_type_coverage(self, pokemon_list: List[Pokemon]) -> Dict[str, int]:
        """Analisa cobertura de tipos"""
        type_counts = {}
        
        for pokemon in pokemon_list:
            for pokemon_type in pokemon.get_types():
                type_name = pokemon_type.value
                type_counts[type_name] = type_counts.get(type_name, 0) + 1
        
        return type_counts
    
    def find_best_counters(
        self, 
        target_pokemon: Pokemon, 
        pokemon_database: List[Pokemon],
        top_n: int = 5
    ) -> List[Tuple[Pokemon, float]]:
        """Encontra melhores contadores para um Pokémon"""
        
        from ..core.battle_system import TypeEffectiveness
        
        counters = []
        
        for pokemon in pokemon_database:
            if pokemon.pokemon_id == target_pokemon.pokemon_id:
                continue
            
            # Calcula vantagem de tipo
            advantage = 1.0
            for move in pokemon.move_set.moves:
                if move.category.value != "Status":
                    effectiveness = TypeEffectiveness.get_effectiveness(
                        move.move_type, 
                        target_pokemon.get_types()
                    )
                    advantage = max(advantage, effectiveness)
            
            # Score baseado em vantagem e estatísticas
            score = advantage * pokemon.stats.total / 1000
            
            counters.append((pokemon, score))
        
        # Ordena por score
        counters.sort(key=lambda x: x[1], reverse=True)
        
        return counters[:top_n]
    
    def create_team_analysis(self, team: List[Pokemon]) -> Dict[str, any]:
        """Cria análise completa de uma equipe"""
        
        if len(team) == 0:
            return {}
        
        # Métricas individuais
        individual_metrics = []
        for pokemon in team:
            metrics = self.calculate_pokemon_metrics(pokemon)
            individual_metrics.append(metrics)
        
        # Métricas da equipe
        total_stats = sum(pokemon.stats.total for pokemon in team)
        avg_efficiency = np.mean([m['efficiency'] for m in individual_metrics])
        avg_balance = np.mean([m['balance'] for m in individual_metrics])
        
        # Cobertura de tipos
        type_coverage = self.analyze_type_coverage(team)
        unique_types = len(type_coverage)
        
        # Análise de fraquezas
        weaknesses = self._analyze_team_weaknesses(team)
        
        # Score geral da equipe
        team_score = (avg_efficiency * 0.4 + 
                     unique_types / 15 * 0.3 + 
                     avg_balance * 0.3)
        
        return {
            'team_size': len(team),
            'total_stats': total_stats,
            'avg_efficiency': avg_efficiency,
            'avg_balance': avg_balance,
            'type_coverage': type_coverage,
            'unique_types': unique_types,
            'weaknesses': weaknesses,
            'team_score': team_score,
            'individual_metrics': individual_metrics
        }
    
    def _analyze_team_weaknesses(self, team: List[Pokemon]) -> Dict[str, List[str]]:
        """Analisa fraquezas da equipe"""
        
        from ..core.battle_system import TypeEffectiveness
        
        weaknesses = {}
        
        # Tipos que são super efetivos contra a equipe
        for pokemon in team:
            for pokemon_type in pokemon.get_types():
                for attack_type in PokemonType:
                    effectiveness = TypeEffectiveness.get_effectiveness(
                        attack_type, 
                        [pokemon_type]
                    )
                    
                    if effectiveness > 1.0:
                        type_name = attack_type.value
                        if type_name not in weaknesses:
                            weaknesses[type_name] = []
                        weaknesses[type_name].append(pokemon.name)
        
        return weaknesses
    
    def export_analysis_to_csv(self, analysis: Dict[str, any], filename: str) -> None:
        """Exporta análise para CSV"""
        
        # Cria DataFrame com métricas individuais
        if 'individual_metrics' in analysis:
            df = pd.DataFrame(analysis['individual_metrics'])
            df.to_csv(self.data_path / f"{filename}_individual.csv", index=False)
        
        # Cria DataFrame com métricas da equipe
        team_metrics = {
            'metric': ['team_size', 'total_stats', 'avg_efficiency', 
                      'avg_balance', 'unique_types', 'team_score'],
            'value': [analysis.get(metric, 0) for metric in 
                     ['team_size', 'total_stats', 'avg_efficiency', 
                      'avg_balance', 'unique_types', 'team_score']]
        }
        
        df_team = pd.DataFrame(team_metrics)
        df_team.to_csv(self.data_path / f"{filename}_team.csv", index=False)
        
        print(f"Análise exportada para {filename}_individual.csv e {filename}_team.csv")
    
    def get_pokemon_by_name(self, name: str, pokemon_database: List[Pokemon]) -> Optional[Pokemon]:
        """Busca Pokémon por nome"""
        for pokemon in pokemon_database:
            if pokemon.name.lower() == name.lower():
                return pokemon
        return None
    
    def get_pokemon_by_type(self, pokemon_type: PokemonType, pokemon_database: List[Pokemon]) -> List[Pokemon]:
        """Busca Pokémon por tipo"""
        return [pokemon for pokemon in pokemon_database if pokemon.has_type(pokemon_type)]
    
    def get_top_pokemon_by_stat(self, stat: str, pokemon_database: List[Pokemon], top_n: int = 10) -> List[Pokemon]:
        """Retorna top Pokémon por estatística"""
        
        stat_values = []
        for pokemon in pokemon_database:
            if hasattr(pokemon.stats, stat):
                value = getattr(pokemon.stats, stat)
                stat_values.append((pokemon, value))
        
        stat_values.sort(key=lambda x: x[1], reverse=True)
        return [pokemon for pokemon, _ in stat_values[:top_n]]
