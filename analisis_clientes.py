import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

os.makedirs("images", exist_ok=True)

# Cargar los datos
df = pd.read_csv("data/wholesale_customers.csv")

# Variables de compra
columnas = [
    "Fresh", "Milk", "Grocery",
    "Frozen", "Detergents_Paper", "Delicassen"
]

# Limpiar datos
df = df.drop_duplicates()
df[columnas] = df[columnas].fillna(0)

# Estandarizar los datos
escalador = StandardScaler()
datos = escalador.fit_transform(df[columnas])

# Aplicar K-Means
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = modelo.fit_predict(datos)

# Guardar resultados
df.to_csv("data/wholesale_customers_clustered.csv", index=False)

# Cantidad de clientes por grupo
conteo = df["Cluster"].value_counts().sort_index()

# Grafica de clientes por grupo
conteo.plot(kind="bar", title="Clientes por grupo")
plt.xlabel("Grupo")
plt.ylabel("Cantidad de clientes")
plt.tight_layout()
plt.savefig("images/clientes_por_cluster.png")
plt.close()

# Analisis PCA
pca = PCA(n_components=2)
componentes = pca.fit_transform(datos)

plt.scatter(componentes[:, 0], componentes[:, 1], c=df["Cluster"])
plt.title("Distribucion de clientes por grupo")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.tight_layout()
plt.savefig("images/distribucion_clientes.png")
plt.close()

# Resultados finales
print("ANALISIS COMPLETADO")
print("\nClientes por grupo:")
print(conteo)

print("\nPromedio de compras por grupo:")
print(df.groupby("Cluster")[columnas].mean().round(2))