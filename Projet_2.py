import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

#lire les données
data = pd.read_csv("datas2.csv", sep=";" )

#afficher les colonnes
print (data.columns)

#dimension du dataframe
print (data.shape)

# piechart de la colonne death
data.hospital_death.value_counts().plot.pie(autopct="%.2f")

# Afficher le graphique
plt.show()