import pandas as pd

# -------------------------
# Configuração de exibição
# -------------------------

# Para que o Pandas exiba todas as colunas e linhas.
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# -------------------------
# Leitura dos dados
# -------------------------

# Para ler o arquivo padrão dos microdados do Enem 2024.
df = pd.read_csv("RESULTADOS_2024.csv", sep=";", encoding="latin1")

# -------------------------
# Filtro de candidatos aptos ao SiSU
# -------------------------

# Condição para ingressar em boa parte das universidades públicas através do SiSU, por município.
condicao = (
    (df["NU_NOTA_LC"] >= 400) &
    (df["NU_NOTA_CN"] >= 400) &
    (df["NU_NOTA_CH"] >= 400) &
    (df["NU_NOTA_MT"] >= 400) &
    (df["NO_MUNICIPIO_PROVA"] == "Município")
)

# DataFrame filtrado
classificados = df[condicao]

# Para imprimir a quantidade de alunos por município que obtiveram os resultados mínimos para ingressar em boa parte das universidades públicas pelo SiSU.
print(len(classificados))

# Mostrar um número específico de candidatos que atingiram a condição mínima de desempenho.
print(classificados.head())

# -------------------------
# Médias por unidade federativa
# -------------------------

# Gera a média das notas em todas as áreas por unidade federativa.
media_estado = df.groupby("SG_UF_PROVA")[[
    "NU_NOTA_LC",
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_REDACAO"
]].mean()

print(media_estado)

# -------------------------
# Criação da média simples
# -------------------------

# Criação de uma tabela chamada "MEDIA_SIMPLES", para tornar possível o agrupamento e a ordenação.
df["MEDIA_SIMPLES"] = df[
    ["NU_NOTA_LC", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
].mean(axis=1)

# -------------------------
# Ranking por unidade federativa
# -------------------------

# Imprime as médias simples por unidade federativa em ordem decrescente.
media_por_estado = (
    df.groupby("SG_UF_PROVA")["MEDIA_SIMPLES"]
    .mean()
    .sort_values(ascending=False)
)

print(media_por_estado)import pandas as pd

# -------------------------
# Configuração de exibição
# -------------------------

# Para que o Pandas exiba todas as colunas e linhas.
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# -------------------------
# Leitura dos dados
# -------------------------

# Para ler o arquivo padrão dos microdados do Enem 2024.
df = pd.read_csv("RESULTADOS_2024.csv", sep=";", encoding="latin1")

# -------------------------
# Filtro de candidatos aptos ao SiSU
# -------------------------

# Condição para ingressar em boa parte das universidades públicas através do SiSU, por município.
condicao = (
    (df["NU_NOTA_LC"] >= 400) &
    (df["NU_NOTA_CN"] >= 400) &
    (df["NU_NOTA_CH"] >= 400) &
    (df["NU_NOTA_MT"] >= 400) &
    (df["NO_MUNICIPIO_PROVA"] == "Município")
)

# DataFrame filtrado
classificados = df[condicao]

# Para imprimir a quantidade de alunos por município que obtiveram os resultados mínimos para ingressar em boa parte das universidades públicas pelo SiSU.
print(len(classificados))

# Mostrar um número específico de candidatos que atingiram a condição mínima de desempenho.
print(classificados.head())

# -------------------------
# Médias por unidade federativa
# -------------------------

# Gera a média das notas em todas as áreas por unidade federativa.
media_estado = df.groupby("SG_UF_PROVA")[[
    "NU_NOTA_LC",
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_REDACAO"
]].mean()

print(media_estado)

# -------------------------
# Criação da média simples
# -------------------------

# Criação de uma tabela chamada "MEDIA_SIMPLES", para tornar possível o agrupamento e a ordenação.
df["MEDIA_SIMPLES"] = df[
    ["NU_NOTA_LC", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
].mean(axis=1)

# -------------------------
# Ranking por unidade federativa
# -------------------------

# Imprime as médias simples por unidade federativa em ordem decrescente.
media_por_estado = (
    df.groupby("SG_UF_PROVA")["MEDIA_SIMPLES"]
    .mean()
    .sort_values(ascending=False)
)

print(media_por_estado)
