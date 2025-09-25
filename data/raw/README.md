# Dados Brutos (Raw Data)

Este diretório contém os dados originais, não processados, do projeto.

## Estrutura

- **Dados originais**: Datasets baixados ou coletados diretamente das fontes
- **Backups**: Cópias de segurança dos dados originais
- **Temporários**: Arquivos temporários de processamento (ignorados pelo Git)

## Uso

1. Coloque aqui os dados originais baixados
2. NÃO modifique os arquivos originais
3. Use scripts de processamento para gerar dados limpos em `../processed/`

## Fontes de Dados

- **Pokémon Dataset**: Kaggle Pokemon Dataset
- **Elite Four Data**: Dados coletados manualmente dos jogos
- **Movesets**: Dados de movimentos e habilidades

## Observações

- Arquivos grandes (>100MB) devem usar Git LFS
- Dados sensíveis não devem ser commitados
- Mantenha documentação sobre a origem dos dados
