"""
Configurações do Projeto Pokémon Elite Four
"""

import os
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Config:
    """Configurações principais do projeto"""
    
    # Diretórios
    DATA_DIR: str = "data"
    OUTPUT_DIR: str = "output"
    MODELS_DIR: str = "output/models"
    PLOTS_DIR: str = "output/plots"
    REPORTS_DIR: str = "output/reports"
    TABLES_DIR: str = "output/tables"
    
    # Arquivos de dados
    POKEMON_DATA_FILE: str = "pokemon_data.csv"
    ELITE_FOUR_DATA_FILE: str = "elite_four_data.csv"
    
    # Configurações de batalha
    MAX_BATTLE_TURNS: int = 100
    DEFAULT_SIMULATIONS: int = 100
    
    # Configurações de otimização
    POPULATION_SIZE: int = 50
    MAX_GENERATIONS: int = 100
    MUTATION_RATE: float = 0.1
    CROSSOVER_RATE: float = 0.8
    ELITE_SIZE: int = 5
    
    # Configurações de visualização
    PLOT_WIDTH: int = 10
    PLOT_HEIGHT: int = 8
    DPI: int = 300
    
    # Configurações de logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    def __post_init__(self):
        """Cria diretórios necessários"""
        self._create_directories()
    
    def _create_directories(self):
        """Cria diretórios de saída se não existirem"""
        directories = [
            self.OUTPUT_DIR,
            self.MODELS_DIR,
            self.PLOTS_DIR,
            self.REPORTS_DIR,
            self.TABLES_DIR
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
    
    def get_data_path(self, filename: str) -> str:
        """Retorna caminho completo para arquivo de dados"""
        return os.path.join(self.DATA_DIR, filename)
    
    def get_output_path(self, filename: str, subdir: str = "") -> str:
        """Retorna caminho completo para arquivo de saída"""
        if subdir:
            return os.path.join(self.OUTPUT_DIR, subdir, filename)
        return os.path.join(self.OUTPUT_DIR, filename)
    
    def to_dict(self) -> Dict[str, Any]:
        """Converte configuração para dicionário"""
        return {
            'data_dir': self.DATA_DIR,
            'output_dir': self.OUTPUT_DIR,
            'max_battle_turns': self.MAX_BATTLE_TURNS,
            'default_simulations': self.DEFAULT_SIMULATIONS,
            'population_size': self.POPULATION_SIZE,
            'max_generations': self.MAX_GENERATIONS,
            'mutation_rate': self.MUTATION_RATE,
            'crossover_rate': self.CROSSOVER_RATE,
            'elite_size': self.ELITE_SIZE
        }


# Instância global de configuração
config = Config()
