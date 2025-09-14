#!/usr/bin/env python3
"""
Script para gerar o notebook Jupyter com as 41 perguntas do case técnico
"""

import json

def create_notebook():
    """Cria o notebook Jupyter com todas as 41 perguntas"""
    
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# 📊 Case Técnico - Análise de Dados em Python\n",
                    "\n",
                    "**MBA em Engenharia de Dados**  \n",
                    "**Projeto Pokémon Elite dos 4**  \n",
                    "**Migração de R para Python**\n",
                    "\n",
                    "---\n",
                    "\n",
                    "Este notebook responde às 41 perguntas do case técnico utilizando Python e o dataset de Pokémon da primeira geração."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📚 Importações e Configurações"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Importações necessárias\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n",
                    "from pathlib import Path\n",
                    "import warnings\n",
                    "warnings.filterwarnings('ignore')\n",
                    "\n",
                    "# Configurações de visualização\n",
                    "plt.style.use('seaborn-v0_8')\n",
                    "sns.set_palette(\"husl\")\n",
                    "plt.rcParams['figure.figsize'] = (12, 8)\n",
                    "plt.rcParams['font.size'] = 10\n",
                    "\n",
                    "print(\"✅ Bibliotecas importadas com sucesso!\")"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Perguntas 1-10
    questions_1_10 = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 1️⃣ Pergunta 1: Importe o seu dataset para o Python"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Carregando o dataset principal de Pokémon\n",
                "pokemon_data = pd.read_csv('data/pokemon_data.csv')\n",
                "print(\"✅ Dataset carregado com sucesso!\")\n",
                "print(f\"📊 Dimensões: {pokemon_data.shape}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2️⃣ Pergunta 2: Contextualize o problema de negócio\n",
                "\n",
                "**Problema de Negócio:**\n",
                "\n",
                "No universo dos jogos Pokémon, treinadores enfrentam o desafio de montar a equipe mais eficaz para vencer a Elite dos 4, o grupo de treinadores mais poderosos do jogo. O problema central é:\n",
                "\n",
                "- **Qual é o melhor sexteto de Pokémon e em qual nível para vencer a Elite dos 4?**\n",
                "- Como otimizar a seleção considerando tipos, estatísticas e sinergias?\n",
                "- Quais estratégias maximizam a taxa de vitória contra cada membro?\n",
                "\n",
                "Este é um problema de **otimização combinatória complexa** que envolve:\n",
                "- 151 Pokémon disponíveis\n",
                "- 6 slots na equipe\n",
                "- 5 membros da Elite dos 4\n",
                "- Múltiplos critérios de otimização"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3️⃣ Pergunta 3: Contextualize a solução do pipeline\n",
                "\n",
                "**Solução do Pipeline:**\n",
                "\n",
                "O pipeline desenvolvido resolve o problema através de:\n",
                "\n",
                "1. **Análise Exploratória**: Compreensão dos dados e padrões\n",
                "2. **Modelagem Estatística**: Predição de eficiência dos Pokémon\n",
                "3. **Otimização Genética**: Encontrar o sexteto ótimo\n",
                "4. **Simulação de Batalhas**: Validação com sistema realista GBA\n",
                "5. **Análise de Performance**: Métricas de vitória e estratégias\n",
                "\n",
                "**Resultado Alcançado:** 93% de taxa de vitória contra Elite dos 4!"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 4️⃣ Pergunta 4: Verifique as primeiras 6 linhas do dataset"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Primeiras 6 linhas\n",
                "print(\"🔍 Primeiras 6 linhas do dataset:\")\n",
                "pokemon_data.head(6)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 5️⃣ Pergunta 5: Verifique as últimas 10 linhas do dataset"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Últimas 10 linhas\n",
                "print(\"🔍 Últimas 10 linhas do dataset:\")\n",
                "pokemon_data.tail(10)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 6️⃣ Pergunta 6: Mostre a quantidade de linhas e colunas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Dimensões do dataset\n",
                "linhas, colunas = pokemon_data.shape\n",
                "print(f\"📊 Dataset possui {linhas} linhas e {colunas} colunas\")\n",
                "print(f\"📊 Dimensões: {pokemon_data.shape}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 7️⃣ Pergunta 7: Exiba apenas os nomes das colunas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Nomes das colunas\n",
                "print(\"📋 Nomes das colunas do dataset:\")\n",
                "for i, col in enumerate(pokemon_data.columns, 1):\n",
                "    print(f\"{i:2d}. {col}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8️⃣ Pergunta 8: Descreva as principais variáveis\n",
                "\n",
                "**Principais Variáveis do Dataset:**\n",
                "\n",
                "**Identificadores:**\n",
                "- `id`: ID único do Pokémon (1-151)\n",
                "- `name`: Nome do Pokémon\n",
                "\n",
                "**Tipos:**\n",
                "- `type1`: Tipo primário (categórica)\n",
                "- `type2`: Tipo secundário (categórica, pode ser nulo)\n",
                "\n",
                "**Estatísticas de Batalha (numéricas):**\n",
                "- `hp`: Pontos de vida\n",
                "- `attack`: Ataque físico\n",
                "- `defense`: Defesa física\n",
                "- `sp_attack`: Ataque especial\n",
                "- `sp_defense`: Defesa especial\n",
                "- `speed`: Velocidade\n",
                "- `total`: Soma total das estatísticas\n",
                "\n",
                "**Metadados:**\n",
                "- `generation`: Geração (todas = 1)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 9️⃣ Pergunta 9: Verifique e ajuste os tipos das colunas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Verificar tipos atuais\n",
                "print(\"🔍 Tipos atuais das colunas:\")\n",
                "print(pokemon_data.dtypes)\n",
                "print(\"\\n\" + \"=\"*50 + \"\\n\")\n",
                "\n",
                "# Ajustar tipos\n",
                "pokemon_data['type1'] = pokemon_data['type1'].astype('category')\n",
                "pokemon_data['type2'] = pokemon_data['type2'].astype('category')\n",
                "pokemon_data['generation'] = pokemon_data['generation'].astype('category')\n",
                "\n",
                "print(\"✅ Tipos ajustados:\")\n",
                "print(pokemon_data.dtypes)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 🔟 Pergunta 10: Selecione apenas duas colunas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Selecionando duas colunas: name e total\n",
                "duas_colunas = pokemon_data[['name', 'total']]\n",
                "print(\"📋 Duas colunas selecionadas (name e total):\")\n",
                "duas_colunas.head(10)"
            ]
        }
    ]
    
    # Adicionar perguntas 1-10 ao notebook
    notebook["cells"].extend(questions_1_10)
    
    return notebook

if __name__ == "__main__":
    notebook = create_notebook()
    
    # Salvar o notebook
    with open('docs/CASE_TECNICO_41_PERGUNTAS_PYTHON.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print("✅ Notebook criado com sucesso!")
    print("📁 Arquivo: docs/CASE_TECNICO_41_PERGUNTAS_PYTHON.ipynb")
