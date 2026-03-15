## English

# enem-2024-microdata-analysis
Exploratory analysis of ENEM 2024 microdata using Python and Pandas, including filtering, statistical summaries, and state-level rankings.


## Português

# Análise dos Microdados do ENEM 2024

Este projeto realiza uma análise exploratória dos microdados do ENEM 2024 utilizando Python e a biblioteca Pandas.

## Objetivo

O objetivo deste projeto é explorar os dados públicos do ENEM e gerar algumas análises básicas, como:

- filtragem de candidatos que atendem aos critérios mínimos do SiSU
- cálculo da média simples entre as cinco áreas do exame
- cálculo das médias por unidade federativa
- ranking dos estados com base no desempenho médio

## Tecnologias utilizadas

- Python
- Pandas
- SQL

## Estrutura do projeto

analise_microdados_enem_2024.py  
Script principal contendo a leitura dos dados e as análises realizadas.

## Fonte dos dados

Os dados utilizados neste projeto são os microdados oficiais do ENEM, disponibilizados publicamente pelo INEP.

## Como executar

1. Baixe os microdados do ENEM 2024 no site do INEP.
2. Coloque o arquivo `RESULTADOS_2024.csv` no mesmo diretório do script.
3. Execute o script:

```bash
python analise_microdados_enem_2024.py
