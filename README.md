Minería de Datos con IA: De la pregunta al insight



1\. Descripción del proyecto



Este proyecto utiliza técnicas de minería de datos y aprendizaje automático para identificar patrones de compra y segmentar clientes mayoristas según sus hábitos de consumo.



2\. Pregunta de investigación



¿Cómo se pueden identificar grupos de clientes mayoristas a partir de sus patrones de compra en diferentes categorías de productos?



3\. Objetivo



Aplicar el algoritmo K-Means para agrupar clientes según sus compras y encontrar información útil que apoye la toma de decisiones comerciales.



4\. Fuente de datos



Se utilizó el conjunto de datos Wholesale Customers, obtenido del repositorio UCI Machine Learning Repository.



Fuente: https://archive.ics.uci.edu/dataset/292/wholesale+customers



La base contiene 440 registros y 8 variables.



5\. Preparación de los datos



Se revisaron los tipos de datos.



Se verificaron los valores faltantes y duplicados.



Se eliminaron posibles registros duplicados.



Se seleccionaron seis variables relacionadas con las compras.



Se aplicó estandarización para preparar los datos para el algoritmo.



6\. Metodología



Se utilizó el algoritmo K-Means para identificar tres grupos de clientes.



También se aplicaron:



Método del codo para analizar el número de grupos.



Coeficiente Silhouette para evaluar la separación de los grupos.



PCA para visualizar los resultados en dos dimensiones.



El coeficiente Silhouette obtenido para tres grupos fue aproximadamente 0,5483.



7\. Resultados



El modelo identificó tres grupos:



Grupo 0: 45 clientes (10,23 %).



Grupo 1: 393 clientes (89,32 %).



Grupo 2: 2 clientes (0,45 %).



Se encontraron diferencias en los patrones de compra de las categorías analizadas.



8\. Conclusiones



La minería de datos permitió identificar comportamientos diferentes entre los clientes mayoristas. Esta información puede ayudar a las empresas a segmentar sus compradores, diseñar estrategias comerciales y mejorar la toma de decisiones.



El grupo de dos clientes requiere una revisión individual, debido a su tamaño reducido y sus compras elevadas en algunas categorías.



9\. Herramientas utilizadas



Python



Pandas



NumPy



Matplotlib



Scikit-learn



Algoritmo K-Means



Análisis PCA



10\. Archivos del proyecto



wholesale\_customers.csv: base de datos original.



wholesale\_customers\_clean.csv: base de datos limpia.



wholesale\_customers\_standardized.csv: datos estandarizados.



wholesale\_customers\_clustered.csv: resultados de la segmentación.



conclusiones.txt: conclusiones del análisis.



images/: gráficas del proyecto.

