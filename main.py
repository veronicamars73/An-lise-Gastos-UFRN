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



plt.show()
