# COMPARAÇÃO DAS 41 PERGUNTAS

## PERGUNTAS DO PDF vs ARQUIVO R

| # | PDF | ARQUIVO R | STATUS |
|---|-----|-----------|--------|
| 1 | Importe o seu dataset para o R. | Importe o seu dataset para o R | ✅ CORRETO |
| 2 | Contextualize o problema de negócio relacionado ao seu dataset | Contextualize o problema de negócio relacionado ao seu dataset | ✅ CORRETO |
| 3 | Contextualize a solução que seu pipeline deverá resolver (Questão aberta) | Contextualize a solução que seu pipeline deverá resolver (Questão aberta) | ✅ CORRETO |
| 4 | Verifique as primeiras 6 linhas do dataset. | Verifique as primeiras 6 linhas do dataset | ✅ CORRETO |
| 5 | Verifique as últimas 10 linhas do dataset. | Verifique as últimas 10 linhas do dataset | ✅ CORRETO |
| 6 | Mostre a quantidade de linhas e colunas do dataset. | Mostre a quantidade de linhas e colunas do dataset | ✅ CORRETO |
| 7 | Exiba apenas os nomes das colunas do dataset. | Exiba apenas os nomes das colunas do dataset | ✅ CORRETO |
| 8 | Descreva em poucas palavras as principais variáveis do seu dataset que farão parte dos principais pipelines que irão existir nas perguntas seguintes. | Descreva em poucas palavras as principais variáveis do seu dataset | ✅ CORRETO |
| 9 | Ao explorar o seu dataset, você percebe que uma coluna que deveria ser categórica está como numérica, ou que uma coluna de datas está como caractere. Verifique o tipo de todas as colunas do dataset e ajuste para o tipo correto | Verifique o tipo de todas as colunas do dataset e ajuste para o tipo correto | ✅ CORRETO |
| 10 | Selecione apenas duas colunas do dataset. | Selecione apenas duas colunas do dataset | ✅ CORRETO |
| 11 | Filtre as linhas onde uma variável numérica seja maior que um valor definido. | Filtre as linhas onde uma variável numérica seja maior que um valor definido | ✅ CORRETO |
| 12 | Ordene o dataset de forma crescente com base em uma coluna numérica. | Ordene o dataset de forma crescente com base em uma coluna numérica | ✅ CORRETO |
| 13 | Crie uma nova coluna com base em uma operação entre duas colunas existentes. | Crie uma nova coluna com base em uma operação entre duas colunas existentes | ✅ CORRETO |
| 14 | Remova uma coluna do dataset. | Remova uma coluna do dataset | ✅ CORRETO |
| 15 | Use a função select() para escolher 3 colunas do dataset. | Use a função select() para escolher 3 colunas do dataset | ✅ CORRETO |
| 16 | Use a função filter() para selecionar linhas que atendam a uma condição. | Use a função filter() para selecionar linhas que atendam a uma condição | ✅ CORRETO |
| 17 | Selecione todas as colunas cujo nome começa com uma letra específica usando select(starts_with()). | Selecione todas as colunas cujo nome começa com uma letra específica usando select(starts_with()) | ✅ CORRETO |
| 18 | Renomeie duas colunas do dataset usando rename(). | Renomeie duas colunas do dataset usando rename() | ✅ CORRETO |
| 19 | Utilize arrange() para ordenar os dados de forma decrescente. | Utilize arrange() para ordenar os dados de forma decrescente | ✅ CORRETO |
| 20 | Crie uma nova coluna com mutate(). | Crie uma nova coluna com mutate() | ✅ CORRETO |
| 21 | Resuma os dados de uma coluna numérica usando summarise(). | Resuma os dados de uma coluna numérica usando summarise() | ✅ CORRETO |
| 22 | Agrupe os dados por uma variável categórica com group_by(). | Agrupe os dados por uma variável categórica com group_by() | ✅ CORRETO |
| 23 | Combine group_by() e summarise() para calcular a média de uma variável por grupo. | Combine group_by() e summarise() para calcular a média de uma variável por grupo | ✅ CORRETO |
| 24 | Use pivot_longer() para transformar colunas em linhas. | Use pivot_longer() para transformar colunas em linhas | ✅ CORRETO |
| 25 | Utilize um pipeline para: selecionar colunas, filtrar linhas e ordenar os dados. | Utilize um pipeline para: selecionar colunas, filtrar linhas e ordenar os dados | ✅ CORRETO |
| 26 | Use pivot_wider() para transformar linhas em colunas. | Use pivot_wider() para transformar linhas em colunas | ✅ CORRETO |
| 27 | Aplique drop_na() para remover valores ausentes. | Aplique drop_na() para remover valores ausentes | ✅ CORRETO |
| 28 | Substitua valores ausentes por 0 em uma coluna numérica. | Substitua valores ausentes por 0 em uma coluna numérica | ✅ CORRETO |
| 29 | Crie um gráfico de dispersão (scatterplot) com duas variáveis numéricas. | Crie um gráfico de dispersão (scatterplot) com duas variáveis numéricas | ✅ CORRETO |
| 30 | Crie um gráfico de barras de uma variável categórica. | Crie um gráfico de barras de uma variável categórica | ✅ CORRETO |
| 31 | Construa um histograma de uma variável numérica. | Crie um histograma de uma variável numérica | ✅ CORRETO |
| 32 | Crie um gráfico de linha para visualizar a evolução de uma variável ao longo do tempo. | Crie um gráfico de linha com duas variáveis numéricas | ⚠️ DIFERENTE |
| 33 | Adicione uma linha de tendência a um gráfico de dispersão. | Adicione uma linha de tendência a um gráfico de dispersão | ✅ CORRETO |
| 34 | Crie um boxplot para comparar a distribuição de uma variável numérica entre categorias. | Crie um boxplot de uma variável numérica por uma categórica | ✅ CORRETO |
| 35 | Personalize um gráfico com título, legenda e rótulos nos eixos. | Personalize a aparência de um gráfico (cores, títulos, temas) | ✅ CORRETO |
| 36 | Crie um mapa de calor (heatmap) com duas variáveis categóricas. | Crie um mapa de calor (heatmap) de uma matriz de correlação | ⚠️ DIFERENTE |
| 37 | Combine mais de um gráfico em uma mesma visualização usando facet_wrap(). | Use facet_wrap() para criar múltiplos gráficos | ✅ CORRETO |
| 38 | Crie uma função chamada resumo_variavel() que receba: um dataframe, o nome de uma coluna numérica, e um parâmetro opcional plot = TRUE. | Crie uma função personalizada que calcule uma métrica | ⚠️ DIFERENTE |
| 39 | Usando o operador pipe (%>%), faça as seguintes operações no seu dataset... | Salve uma função em um arquivo .R e carregue-a | ⚠️ DIFERENTE |
| 40 | Construa um pipeline seguindo as instruções abaixo... | Crie um pipeline complexo que combine múltiplas operações | ⚠️ DIFERENTE |
| 41 | Com o pipeline da questão 38, faça: a. Salve este pipeline como uma função em um arquivo R separado... | Salve o dataset processado em um arquivo CSV | ⚠️ DIFERENTE |

## RESUMO
- ✅ CORRETAS: 33 perguntas
- ⚠️ DIFERENTES: 8 perguntas (32, 36, 38, 39, 40, 41)
