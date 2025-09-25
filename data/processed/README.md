# Dados Processados (Processed Data)

Este diretório contém os dados limpos e processados, prontos para análise.

## Arquivos Principais

### `pokemon_processed.csv`
- **Descrição**: Dataset principal de Pokémon limpo e processado
- **Colunas**: Name, Type 1, Type 2, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Total, Generation, Legendary
- **Registros**: ~800 Pokémon
- **Uso**: Análises principais, otimização de equipes, visualizações

### `elite_four_data.csv`
- **Descrição**: Dados dos membros da Elite dos 4 e seus Pokémon
- **Colunas**: Member, Pokemon, Level, Type1, Type2, Moveset
- **Registros**: Pokémon de cada membro da Elite Four
- **Uso**: Simulações de batalha, análise de oponentes

## Processamento Aplicado

1. **Limpeza de dados**:
   - Remoção de valores nulos
   - Padronização de nomes
   - Correção de tipos de dados

2. **Transformações**:
   - Cálculo de estatísticas derivadas
   - Normalização de valores
   - Categorização de variáveis

3. **Validações**:
   - Verificação de integridade
   - Validação de ranges
   - Consistência de dados

## Qualidade dos Dados

- ✅ **Completude**: Sem valores faltantes críticos
- ✅ **Consistência**: Formatos padronizados
- ✅ **Precisão**: Valores validados contra fontes oficiais
- ✅ **Atualidade**: Dados atualizados até Geração 6

## Uso nos Módulos

- `DataProcessor`: Carrega e valida os dados
- `TeamOptimizer`: Usa para otimização genética
- `BattleAnalyzer`: Usa para simulações
- `Notebook`: Usado nas análises exploratórias
