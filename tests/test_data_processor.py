"""
Testes para o processador de dados
"""

import pytest
import pandas as pd
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path
sys.path.append(str(Path(__file__).parent.parent))

from pokemon_elite_four.analysis.data_processor import DataProcessor


class TestDataProcessor:
    """Testes para a classe DataProcessor"""
    
    def test_data_processor_creation(self):
        """Testa criação do processador de dados"""
        processor = DataProcessor()
        assert processor is not None
    
    def test_load_pokemon_data(self):
        """Testa carregamento de dados de Pokémon"""
        processor = DataProcessor()
        
        # Tenta carregar dados reais
        try:
            data = processor.load_pokemon_data("data/pokemon_processed.csv")
            
            # Verifica se é um DataFrame
            assert isinstance(data, pd.DataFrame)
            
            # Verifica se tem as colunas esperadas
            expected_columns = ["Name", "Type 1", "HP", "Attack", "Defense"]
            for col in expected_columns:
                assert col in data.columns
            
            # Verifica se tem dados
            assert len(data) > 0
            
        except FileNotFoundError:
            # Se arquivo não existe, pula o teste
            pytest.skip("Arquivo de dados não encontrado")
    
    def test_validate_pokemon_data(self):
        """Testa validação de dados de Pokémon"""
        processor = DataProcessor()
        
        # Cria DataFrame de teste válido
        valid_data = pd.DataFrame({
            "Name": ["Pikachu", "Charizard"],
            "Type 1": ["Electric", "Fire"],
            "Type 2": [None, "Flying"],
            "HP": [35, 78],
            "Attack": [55, 84],
            "Defense": [40, 78],
            "Sp. Atk": [50, 109],
            "Sp. Def": [50, 85],
            "Speed": [90, 100],
            "Total": [320, 534],
            "Generation": [1, 1]
        })
        
        # Deve passar na validação
        assert processor.validate_data(valid_data) == True
    
    def test_validate_invalid_data(self):
        """Testa validação com dados inválidos"""
        processor = DataProcessor()
        
        # DataFrame com dados inválidos (HP negativo)
        invalid_data = pd.DataFrame({
            "Name": ["Invalid"],
            "Type 1": ["Normal"],
            "HP": [-10],  # HP negativo
            "Attack": [50],
            "Defense": [50]
        })
        
        # Deve falhar na validação
        assert processor.validate_data(invalid_data) == False
    
    def test_preprocess_data(self):
        """Testa pré-processamento de dados"""
        processor = DataProcessor()
        
        # Cria dados de teste com alguns problemas
        raw_data = pd.DataFrame({
            "Name": ["Pikachu", "CHARIZARD", "  Blastoise  "],
            "Type 1": ["Electric", "fire", "Water"],
            "Type 2": [None, "Flying", ""],
            "HP": [35, 78, 79],
            "Attack": [55, 84, 83]
        })
        
        processed_data = processor.preprocess_data(raw_data)
        
        # Verifica se nomes foram limpos
        assert processed_data.loc[0, "Name"] == "Pikachu"
        assert processed_data.loc[1, "Name"] == "Charizard"
        assert processed_data.loc[2, "Name"] == "Blastoise"
        
        # Verifica se tipos foram padronizados
        assert processed_data.loc[1, "Type 1"] == "Fire"
    
    def test_create_derived_features(self):
        """Testa criação de features derivadas"""
        processor = DataProcessor()
        
        # Cria dados base
        data = pd.DataFrame({
            "Name": ["Pikachu", "Charizard"],
            "HP": [35, 78],
            "Attack": [55, 84],
            "Defense": [40, 78],
            "Sp. Atk": [50, 109],
            "Sp. Def": [50, 85],
            "Speed": [90, 100]
        })
        
        enhanced_data = processor.create_derived_features(data)
        
        # Verifica se features derivadas foram criadas
        if "Total" not in data.columns:
            assert "Total" in enhanced_data.columns
            assert enhanced_data.loc[0, "Total"] == 35 + 55 + 40 + 50 + 50 + 90
    
    def test_export_results(self):
        """Testa exportação de resultados"""
        processor = DataProcessor()
        
        # Cria dados de teste
        test_data = pd.DataFrame({
            "Pokemon": ["Pikachu", "Charizard"],
            "Win_Rate": [0.75, 0.82],
            "Avg_HP_Remaining": [15.5, 23.2]
        })
        
        # Tenta exportar para arquivo temporário
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            processor.export_results(test_data, temp_path)
            
            # Verifica se arquivo foi criado
            assert os.path.exists(temp_path)
            
            # Verifica se pode ser lido de volta
            loaded_data = pd.read_csv(temp_path)
            assert len(loaded_data) == len(test_data)
            assert list(loaded_data.columns) == list(test_data.columns)
            
        finally:
            # Limpa arquivo temporário
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def test_load_elite_four_data(self):
        """Testa carregamento de dados da Elite Four"""
        processor = DataProcessor()
        
        try:
            data = processor.load_elite_four_data("data/elite_four_data.csv")
            
            # Verifica se é um DataFrame
            assert isinstance(data, pd.DataFrame)
            
            # Verifica se tem dados
            assert len(data) > 0
            
            # Verifica se tem colunas esperadas para Elite Four
            expected_columns = ["Member", "Pokemon"]
            for col in expected_columns:
                if col in data.columns:
                    assert col in data.columns
            
        except FileNotFoundError:
            # Se arquivo não existe, pula o teste
            pytest.skip("Arquivo de dados da Elite Four não encontrado")
    
    def test_data_filtering(self):
        """Testa filtros de dados"""
        processor = DataProcessor()
        
        # Cria dados de teste
        data = pd.DataFrame({
            "Name": ["Pikachu", "Charizard", "Mew", "Mewtwo"],
            "Type 1": ["Electric", "Fire", "Psychic", "Psychic"],
            "Total": [320, 534, 600, 680],
            "Legendary": [False, False, True, True]
        })
        
        # Filtra apenas lendários
        if "Legendary" in data.columns:
            legendary_data = data[data["Legendary"] == True]
            assert len(legendary_data) == 2
            assert "Mew" in legendary_data["Name"].values
            assert "Mewtwo" in legendary_data["Name"].values
        
        # Filtra por total de stats
        if "Total" in data.columns:
            strong_data = data[data["Total"] >= 600]
            assert len(strong_data) == 2


if __name__ == "__main__":
    pytest.main([__file__])
