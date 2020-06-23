import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

data = pd.read_csv("gastos-por-unidade.csv", sep=";")

df = pd.DataFrame(data)

imd_process = df.loc[df['unidade']=='INSTITUTO METROPOLE DIGITAL']

ano_sum = imd_process.groupby(["ano"])["valor"].sum()

ano_sum.plot.bar()

plt.xlabel('Ano')
plt.ylabel('Valor total de gastos em 10 milhões de reais')

plt.title('Gastos Totais Do IMD Por Ano')
plt.legend()

plt.show()

df = pd.DataFrame(data)

ano_sum = df.groupby(["ano"])["valor"].sum()

ano_sum.plot.bar()

plt.xlabel('Ano')
plt.ylabel('Valor total de gastos em 1 bilhão de reais')

plt.title('Gastos Totais Das Unidades Por Ano')
plt.legend()

plt.show()
