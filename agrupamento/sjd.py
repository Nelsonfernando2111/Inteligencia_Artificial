import pandas as pd

tabela = pd.read_csv("mall_customers.csv")
print(tabela) 

colunas_cluster = ["Annual Income (k$)", "Spending Score (1-100)"]
tabela_cluster = tabela[colunas_cluster].copy()

print(tabela_cluster)
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

normalizador = StandardScaler()

tabela_cluster = normalizador.fit_transform(tabela_cluster)

tabela_cluster = pd.DataFrame(tabela_cluster, columns=colunas_cluster)
print(tabela_cluster)

modelo_kmeans = KMeans(n_clusters=5)
modelo_kmeans.fit(tabela_cluster)

tabela_cluster["Cluster"] = modelo_kmeans.labels_
print(tabela_cluster)


import plotly.express as px

grafico = px.scatter(tabela_cluster, x="Annual Income (k$)", y="Spending Score (1-100)", color="Cluster")

grafico.show()