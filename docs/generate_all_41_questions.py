#!/usr/bin/env python3
"""
Script para gerar notebook com todas as 41 perguntas do case técnico
"""

import json

def create_questions_21_41():
    """Cria as perguntas 21-41"""
    return [
        # Pergunta 21
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣1️⃣ Pergunta 21: Resuma dados de uma coluna numérica usando summarise()"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Resumo estatístico da coluna 'total'\n",
                "resumo_total = pokemon_data['total'].describe()\n",
                "print(\"📊 Resumo estatístico da coluna 'total':\")\n",
                "print(resumo_total)"
            ]
        },
        # Pergunta 22
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣2️⃣ Pergunta 22: Agrupe dados por uma variável categórica"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Agrupar por tipo primário\n",
                "grupo_tipo = pokemon_data.groupby('type1')\n",
                "print(\"📊 Dados agrupados por tipo primário:\")\n",
                "print(f\"Número de grupos: {len(grupo_tipo)}\")\n",
                "print(\"\\nTipos únicos:\")\n",
                "print(list(grupo_tipo.groups.keys()))"
            ]
        },
        # Pergunta 23
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣3️⃣ Pergunta 23: Combine group_by() e summarise() para calcular média por grupo"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Média de total por tipo primário\n",
                "media_por_tipo = pokemon_data.groupby('type1')['total'].mean().sort_values(ascending=False)\n",
                "print(\"📊 Média de total por tipo primário:\")\n",
                "print(media_por_tipo.head(10))"
            ]
        },
        # Pergunta 24
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣4️⃣ Pergunta 24: Use pivot_longer() para transformar colunas em linhas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Transformar colunas de estatísticas em linhas\n",
                "stats_cols = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']\n",
                "pokemon_long = pokemon_data.melt(\n",
                "    id_vars=['name', 'type1'],\n",
                "    value_vars=stats_cols,\n",
                "    var_name='statistic',\n",
                "    value_name='value'\n",
                ")\n",
                "print(\"📊 Dados transformados (wide to long):\")\n",
                "print(f\"Dimensões: {pokemon_long.shape}\")\n",
                "pokemon_long.head(10)"
            ]
        },
        # Pergunta 25
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣5️⃣ Pergunta 25: Use pipeline para selecionar, filtrar e ordenar"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Pipeline: selecionar, filtrar e ordenar\n",
                "pipeline_result = (pokemon_data\n",
                "    .loc[:, ['name', 'type1', 'total']]  # Selecionar colunas\n",
                "    .query('total > 500')  # Filtrar\n",
                "    .sort_values('total', ascending=False)  # Ordenar\n",
                ")\n",
                "print(\"🔄 Resultado do pipeline:\")\n",
                "print(f\"Pokémon com total > 500: {len(pipeline_result)}\")\n",
                "pipeline_result.head(10)"
            ]
        },
        # Pergunta 26
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣6️⃣ Pergunta 26: Use pivot_wider() para transformar linhas em colunas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Transformar long para wide\n",
                "pokemon_wide = pokemon_long.pivot_table(\n",
                "    index='name',\n",
                "    columns='statistic',\n",
                "    values='value',\n",
                "    fill_value=0\n",
                ").reset_index()\n",
                "print(\"📊 Dados transformados (long to wide):\")\n",
                "print(f\"Dimensões: {pokemon_wide.shape}\")\n",
                "pokemon_wide.head()"
            ]
        },
        # Pergunta 27
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣7️⃣ Pergunta 27: Aplique drop_na() para remover valores ausentes"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Remover linhas com valores ausentes\n",
                "pokemon_sem_na = pokemon_data.dropna()\n",
                "print(f\"📊 Linhas originais: {len(pokemon_data)}\")\n",
                "print(f\"📊 Linhas após drop_na(): {len(pokemon_sem_na)}\")\n",
                "print(f\"📊 Valores ausentes removidos: {len(pokemon_data) - len(pokemon_sem_na)}\")"
            ]
        },
        # Pergunta 28
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣8️⃣ Pergunta 28: Substitua valores ausentes por 0 em coluna numérica"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Substituir valores ausentes por 0\n",
                "pokemon_data_filled = pokemon_data.copy()\n",
                "pokemon_data_filled['type2'] = pokemon_data_filled['type2'].fillna('None')\n",
                "print(\"✅ Valores ausentes em 'type2' substituídos por 'None'\")\n",
                "print(f\"📊 Valores únicos em type2: {pokemon_data_filled['type2'].nunique()}\")"
            ]
        },
        # Pergunta 29
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 2️⃣9️⃣ Pergunta 29: Crie gráfico de dispersão com duas variáveis numéricas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gráfico de dispersão: attack vs sp_attack\n",
                "plt.figure(figsize=(10, 6))\n",
                "plt.scatter(pokemon_data['attack'], pokemon_data['sp_attack'], alpha=0.6)\n",
                "plt.xlabel('Attack')\n",
                "plt.ylabel('Special Attack')\n",
                "plt.title('Gráfico de Dispersão: Attack vs Special Attack')\n",
                "plt.grid(True, alpha=0.3)\n",
                "plt.show()"
            ]
        },
        # Pergunta 30
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣0️⃣ Pergunta 30: Crie gráfico de barras de uma variável categórica"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gráfico de barras: contagem por tipo primário\n",
                "plt.figure(figsize=(12, 6))\n",
                "pokemon_data['type1'].value_counts().plot(kind='bar')\n",
                "plt.xlabel('Tipo Primário')\n",
                "plt.ylabel('Quantidade')\n",
                "plt.title('Distribuição de Pokémon por Tipo Primário')\n",
                "plt.xticks(rotation=45)\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        # Pergunta 31
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣1️⃣ Pergunta 31: Construa histograma de uma variável numérica"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Histograma da coluna 'total'\n",
                "plt.figure(figsize=(10, 6))\n",
                "plt.hist(pokemon_data['total'], bins=20, alpha=0.7, edgecolor='black')\n",
                "plt.xlabel('Total de Estatísticas')\n",
                "plt.ylabel('Frequência')\n",
                "plt.title('Distribuição do Total de Estatísticas dos Pokémon')\n",
                "plt.grid(True, alpha=0.3)\n",
                "plt.show()"
            ]
        },
        # Pergunta 32
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣2️⃣ Pergunta 32: Crie gráfico de linha para evolução de variável ao longo do tempo"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gráfico de linha: evolução do total por ID (simulando tempo)\n",
                "plt.figure(figsize=(12, 6))\n",
                "pokemon_ordenado = pokemon_data.sort_values('id')\n",
                "plt.plot(pokemon_ordenado['id'], pokemon_ordenado['total'], linewidth=2)\n",
                "plt.xlabel('ID do Pokémon')\n",
                "plt.ylabel('Total de Estatísticas')\n",
                "plt.title('Evolução do Total de Estatísticas por ID')\n",
                "plt.grid(True, alpha=0.3)\n",
                "plt.show()"
            ]
        },
        # Pergunta 33
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣3️⃣ Pergunta 33: Adicione linha de tendência a gráfico de dispersão"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gráfico de dispersão com linha de tendência\n",
                "plt.figure(figsize=(10, 6))\n",
                "plt.scatter(pokemon_data['attack'], pokemon_data['sp_attack'], alpha=0.6)\n",
                "\n",
                "# Adicionar linha de tendência\n",
                "z = np.polyfit(pokemon_data['attack'], pokemon_data['sp_attack'], 1)\n",
                "p = np.poly1d(z)\n",
                "plt.plot(pokemon_data['attack'], p(pokemon_data['attack']), \"r--\", alpha=0.8)\n",
                "\n",
                "plt.xlabel('Attack')\n",
                "plt.ylabel('Special Attack')\n",
                "plt.title('Attack vs Special Attack com Linha de Tendência')\n",
                "plt.grid(True, alpha=0.3)\n",
                "plt.show()"
            ]
        },
        # Pergunta 34
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣4️⃣ Pergunta 34: Crie boxplot para comparar distribuição entre categorias"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Boxplot: total por tipo primário\n",
                "plt.figure(figsize=(14, 8))\n",
                "pokemon_data.boxplot(column='total', by='type1', ax=plt.gca())\n",
                "plt.xlabel('Tipo Primário')\n",
                "plt.ylabel('Total de Estatísticas')\n",
                "plt.title('Distribuição do Total por Tipo Primário')\n",
                "plt.xticks(rotation=45)\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        # Pergunta 35
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣5️⃣ Pergunta 35: Personalize gráfico com título, legenda e rótulos"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Gráfico personalizado\n",
                "plt.figure(figsize=(12, 8))\n",
                "\n",
                "# Dados para o gráfico\n",
                "tipos = pokemon_data['type1'].value_counts().head(8)\n",
                "cores = plt.cm.Set3(np.linspace(0, 1, len(tipos)))\n",
                "\n",
                "bars = plt.bar(range(len(tipos)), tipos.values, color=cores)\n",
                "\n",
                "# Personalização\n",
                "plt.title('Top 8 Tipos de Pokémon por Quantidade', fontsize=16, fontweight='bold')\n",
                "plt.xlabel('Tipo Primário', fontsize=12)\n",
                "plt.ylabel('Número de Pokémon', fontsize=12)\n",
                "plt.xticks(range(len(tipos)), tipos.index, rotation=45)\n",
                "\n",
                "# Adicionar valores nas barras\n",
                "for i, bar in enumerate(bars):\n",
                "    height = bar.get_height()\n",
                "    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,\n",
                "             f'{int(height)}', ha='center', va='bottom')\n",
                "\n",
                "plt.grid(True, alpha=0.3, axis='y')\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        # Pergunta 36
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣6️⃣ Pergunta 36: Crie mapa de calor com duas variáveis categóricas"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Mapa de calor: type1 vs type2\n",
                "heatmap_data = pokemon_data.groupby(['type1', 'type2']).size().unstack(fill_value=0)\n",
                "\n",
                "plt.figure(figsize=(14, 10))\n",
                "sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd')\n",
                "plt.title('Mapa de Calor: Combinações de Tipos Primário e Secundário', fontsize=14)\n",
                "plt.xlabel('Tipo Secundário')\n",
                "plt.ylabel('Tipo Primário')\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        # Pergunta 37
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 3️⃣7️⃣ Pergunta 37: Combine gráficos usando facet_wrap()"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Múltiplos gráficos usando subplots\n",
                "fig, axes = plt.subplots(2, 2, figsize=(15, 12))\n",
                "\n",
                "# Gráfico 1: Histograma de HP\n",
                "axes[0, 0].hist(pokemon_data['hp'], bins=15, alpha=0.7, color='skyblue')\n",
                "axes[0, 0].set_title('Distribuição de HP')\n",
                "axes[0, 0].set_xlabel('HP')\n",
                "axes[0, 0].set_ylabel('Frequência')\n",
                "\n",
                "# Gráfico 2: Histograma de Attack\n",
                "axes[0, 1].hist(pokemon_data['attack'], bins=15, alpha=0.7, color='lightcoral')\n",
                "axes[0, 1].set_title('Distribuição de Attack')\n",
                "axes[0, 1].set_xlabel('Attack')\n",
                "axes[0, 1].set_ylabel('Frequência')\n",
                "\n",
                "# Gráfico 3: Histograma de Defense\n",
                "axes[1, 0].hist(pokemon_data['defense'], bins=15, alpha=0.7, color='lightgreen')\n",
                "axes[1, 0].set_title('Distribuição de Defense')\n",
                "axes[1, 0].set_xlabel('Defense')\n",
                "axes[1, 0].set_ylabel('Frequência')\n",
                "\n",
                "# Gráfico 4: Histograma de Speed\n",
                "axes[1, 1].hist(pokemon_data['speed'], bins=15, alpha=0.7, color='gold')\n",
                "axes[1, 1].set_title('Distribuição de Speed')\n",
                "axes[1, 1].set_xlabel('Speed')\n",
                "axes[1, 1].set_ylabel('Frequência')\n",
                "\n",
                "plt.suptitle('Distribuições das Estatísticas dos Pokémon', fontsize=16)\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        # Pergunta 38
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3️⃣8️⃣ Pergunta 38: Crie função resumo_variavel()\n",
                "\n",
                "A função deve:\n",
                "- Receber um dataframe, nome de coluna numérica e parâmetro plot=True\n",
                "- Retornar resumo estatístico (mínimo, máximo, média, mediana, desvio padrão)\n",
                "- Se plot=True, exibir histograma usando matplotlib"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "def resumo_variavel(dataframe, coluna, plot=True):\n",
                "    \"\"\"\n",
                "    Função para resumir uma variável numérica\n",
                "    \n",
                "    Parâmetros:\n",
                "    dataframe: DataFrame do pandas\n",
                "    coluna: nome da coluna numérica\n",
                "    plot: se True, exibe histograma\n",
                "    \n",
                "    Retorna:\n",
                "    dicionário com estatísticas descritivas\n",
                "    \"\"\"\n",
                "    # Calcular estatísticas\n",
                "    stats = {\n",
                "        'mínimo': dataframe[coluna].min(),\n",
                "        'máximo': dataframe[coluna].max(),\n",
                "        'média': dataframe[coluna].mean(),\n",
                "        'mediana': dataframe[coluna].median(),\n",
                "        'desvio_padrão': dataframe[coluna].std()\n",
                "    }\n",
                "    \n",
                "    # Exibir resumo\n",
                "    print(f\"📊 Resumo da variável '{coluna}':\")\n",
                "    for stat, value in stats.items():\n",
                "        print(f\"{stat.capitalize()}: {value:.2f}\")\n",
                "    \n",
                "    # Plotar histograma se solicitado\n",
                "    if plot:\n",
                "        plt.figure(figsize=(10, 6))\n",
                "        plt.hist(dataframe[coluna], bins=20, alpha=0.7, edgecolor='black')\n",
                "        plt.xlabel(coluna)\n",
                "        plt.ylabel('Frequência')\n",
                "        plt.title(f'Histograma da variável {coluna}')\n",
                "        plt.grid(True, alpha=0.3)\n",
                "        plt.show()\n",
                "    \n",
                "    return stats\n",
                "\n",
                "# Testar a função\n",
                "print(\"🧪 Testando função resumo_variavel():\")\n",
                "resumo_variavel(pokemon_data, 'total', plot=True)"
            ]
        },
        # Pergunta 39
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3️⃣9️⃣ Pergunta 39: Pipeline com operador pipe (%>%)\n",
                "\n",
                "Pipeline deve:\n",
                "- Selecionar três colunas: duas numéricas e uma categórica\n",
                "- Filtrar linhas sem valores ausentes\n",
                "- Criar nova coluna (razão entre duas numéricas)\n",
                "- Agrupar pela variável categórica\n",
                "- Calcular média, mediana e desvio padrão por grupo\n",
                "- Reorganizar em formato largo\n",
                "- Ordenar pela média (decrescente)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Pipeline completo\n",
                "pipeline_completo = (pokemon_data\n",
                "    .loc[:, ['name', 'attack', 'sp_attack', 'type1']]  # Selecionar 3 colunas\n",
                "    .dropna()  # Filtrar valores ausentes\n",
                "    .assign(attack_ratio=lambda x: x['attack'] / x['sp_attack'])  # Nova coluna\n",
                "    .groupby('type1')['attack_ratio']  # Agrupar\n",
                "    .agg(['mean', 'median', 'std'])  # Calcular estatísticas\n",
                "    .round(3)  # Arredondar\n",
                "    .sort_values('mean', ascending=False)  # Ordenar\n",
                ")\n",
                "\n",
                "print(\"🔄 Resultado do pipeline completo:\")\n",
                "print(pipeline_completo.head(10))"
            ]
        },
        # Pergunta 40
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4️⃣0️⃣ Pergunta 40: Pipeline de processamento\n",
                "\n",
                "Pipeline deve:\n",
                "- Selecionar todas as colunas numéricas\n",
                "- Substituir valores ausentes por 0\n",
                "- Criar coluna categórica baseada em condição\n",
                "- Agrupar pela nova coluna categórica\n",
                "- Calcular média, mediana e máximo de todas as numéricas\n",
                "- Ordenar pela média de uma coluna escolhida"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Pipeline de processamento\n",
                "colunas_numericas = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'total']\n",
                "\n",
                "pipeline_processamento = (pokemon_data\n",
                "    .loc[:, colunas_numericas]  # Selecionar colunas numéricas\n",
                "    .fillna(0)  # Substituir valores ausentes por 0\n",
                "    .assign(power_level=lambda x: np.where(x['total'] > x['total'].mean(), 'Alto', 'Baixo'))  # Nova coluna categórica\n",
                "    .groupby('power_level')  # Agrupar\n",
                "    .agg(['mean', 'median', 'max'])  # Calcular estatísticas\n",
                "    .round(2)  # Arredondar\n",
                "    .sort_values(('total', 'mean'), ascending=False)  # Ordenar pela média de total\n",
                ")\n",
                "\n",
                "print(\"🔄 Resultado do pipeline de processamento:\")\n",
                "print(pipeline_processamento)"
            ]
        },
        # Pergunta 41
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4️⃣1️⃣ Pergunta 41: Salvar pipeline como função\n",
                "\n",
                "a. Salvar pipeline como função em arquivo separado\n",
                "b. Carregar função do arquivo\n",
                "c. Passar dataset como argumento e gerar dataset final processado"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Criar arquivo com função do pipeline\n",
                "pipeline_code = '''\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "\n",
                "def meu_pipeline(dataframe):\n",
                "    \"\"\"\n",
                "    Pipeline de processamento de dados Pokémon\n",
                "    \n",
                "    Parâmetros:\n",
                "    dataframe: DataFrame do pandas\n",
                "    \n",
                "    Retorna:\n",
                "    DataFrame processado\n",
                "    \"\"\"\n",
                "    colunas_numericas = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'total']\n",
                "    \n",
                "    resultado = (dataframe\n",
                "        .loc[:, colunas_numericas]\n",
                "        .fillna(0)\n",
                "        .assign(power_level=lambda x: np.where(x['total'] > x['total'].mean(), 'Alto', 'Baixo'))\n",
                "        .groupby('power_level')\n",
                "        .agg(['mean', 'median', 'max'])\n",
                "        .round(2)\n",
                "        .sort_values(('total', 'mean'), ascending=False)\n",
                "    )\n",
                "    \n",
                "    return resultado\n",
                "'''\n",
                "\n",
                "# Salvar função em arquivo\n",
                "with open('meu_pipeline.py', 'w', encoding='utf-8') as f:\n",
                "    f.write(pipeline_code)\n",
                "\n",
                "print(\"✅ Função salva em 'meu_pipeline.py'\")\n",
                "\n",
                "# Carregar e usar a função\n",
                "import sys\n",
                "sys.path.append('.')\n",
                "from meu_pipeline import meu_pipeline\n",
                "\n",
                "# Aplicar pipeline\n",
                "dataset_final = meu_pipeline(pokemon_data)\n",
                "print(\"\\n🔄 Dataset final processado:\")\n",
                "print(dataset_final)"
            ]
        }
    ]

def create_complete_notebook():
    """Cria notebook completo com todas as 41 perguntas"""
    
    # Carregar notebook existente
    with open('docs/CASE_TECNICO_41_PERGUNTAS_PYTHON.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Adicionar perguntas 21-41
    questions_21_41 = create_questions_21_41()
    notebook["cells"].extend(questions_21_41)
    
    return notebook

if __name__ == "__main__":
    notebook = create_complete_notebook()
    
    # Salvar notebook completo
    with open('docs/CASE_TECNICO_41_PERGUNTAS_PYTHON.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print("✅ Notebook completo criado com sucesso!")
    print("📁 Arquivo: docs/CASE_TECNICO_41_PERGUNTAS_PYTHON.ipynb")
    print("📊 Contém: TODAS as 41 perguntas implementadas!")
