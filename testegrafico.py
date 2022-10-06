import seaborn as sns
import pandas as pd
import perguntas as pg
import matplotlib.pyplot as plt

data1 = pd.read_excel('BD - Skillet.xlsx')

mais_ouvidas, menos_ouvidas = pg.musica_ouvida_album(data1)

sns.set_theme(style="whitegrid")

p111 = sns.catplot(data=mais_ouvidas, x="Popularidade", y="Músicas",kind="bar",
                   hue="Álbuns",width = 5,height=8)
p111.set_axis_labels("Popularidade","")
titulo = "Músicas mais populares de cada álbum"
plt.title(titulo)
plt.show()