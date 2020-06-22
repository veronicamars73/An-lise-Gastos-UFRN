import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("gastos-por-unidade.csv", sep=";")

df = pd.DataFrame(data)

imd_process = df.loc[df['unidade']=='INSTITUTO METROPOLE DIGITAL']

ano_sum = imd_process.groupby(["ano"])["valor"].sum()

ano_sum.plot.bar(x="ano")

plt.show()
