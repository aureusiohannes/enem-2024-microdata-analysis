# Importa o Pandas.
import pandas as pd

# Lê o arquivo de resultados do ENEM 2024.
df = pd.read_csv("RESULTADOS_2024.csv", sep=";", encoding="latin1", usecols=["SG_UF_PROVA"])

# Agrupa por unidade federativa em ordem decrescente e calcula a quantidade de pessoas por UF que fizeram o ENEM 2024.
total_unidade_federativa = df.groupby("SG_UF_PROVA").size().sort_values(ascending=False)

# Importa o matplotlib
import matplotlib.pyplot as plt

# Organiza o eixo x e y do gráfico. 
ufs = total_unidade_federativa.index
y = total_unidade_federativa.values

# Cria um gráfico de barras que mostra a quantidade de participantes no ENEM 2024 por unidade federativa, em ordem decrescente.
plt.figure(figsize=(10,6))
plt.bar(ufs, y)
plt.title("Quantidade de participantes por UF")
plt.xlabel("UF")
plt.ylabel("Quantidade")
plt.show()
