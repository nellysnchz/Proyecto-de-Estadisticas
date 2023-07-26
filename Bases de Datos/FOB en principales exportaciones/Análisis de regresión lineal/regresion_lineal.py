import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy import stats

# Datos
data = {
    'Intervalos': ['2010-2011', '2012-2013', '2014-2015', '2016-2017', '2018-2019', '2020-2021', '2022-2023'],
    'Frecuencia': [7952, 2106, 14157, 6157, 21828, 22385, 7272]
}

df = pd.DataFrame(data)

# Convertir los intervalos a valores numéricos para facilitar el análisis
df['Intervalo_Inicio'] = df['Intervalos'].str[:4].astype(int)
df['Intervalo_Final'] = df['Intervalos'].str[-4:].astype(int)

# Calcular el punto medio de cada intervalo para el análisis de regresión
df['Punto_Medio'] = (df['Intervalo_Inicio'] + df['Intervalo_Final']) / 2

# Realizar el análisis de regresión lineal
X = df['Punto_Medio']  # Variable independiente
y = df['Frecuencia']   # Variable dependiente

X = sm.add_constant(X)  # Agregar una columna de unos para el intercepto en la regresión

# Ajustar el modelo de regresión lineal
model = sm.OLS(y, X).fit()

# Obtener los resultados del modelo
print(model.summary())

# Realizar el análisis de regresión lineal
X = df['Punto_Medio']  # Variable independiente
y = df['Frecuencia']   # Variable dependiente

X = sm.add_constant(X)  # Agregar una columna de unos para el intercepto en la regresión

# Ajustar el modelo de regresión lineal
model = sm.OLS(y, X).fit()

# Obtener los resultados del modelo
print(model.summary())

# Gráfica de residuales
residuales = model.resid

plt.figure(figsize=(8, 6))
plt.scatter(df['Punto_Medio'], residuales)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Punto Medio del Intervalo')
plt.ylabel('Residuales')
plt.title('Gráfica de Residuales')
plt.show()

# Gráfica de probabilidad normal
res = stats.probplot(residuales, plot=plt)
plt.title('Gráfica de Probabilidad Normal')
plt.show()

# Gráfica de dispersión de puntos con la regresión de la línea
plt.figure(figsize=(8, 6))
plt.scatter(df['Punto_Medio'], df['Frecuencia'], label='Datos Observados')
plt.plot(df['Punto_Medio'], model.fittedvalues, color='red', label='Regresión Lineal')
plt.xlabel('Punto Medio del Intervalo')
plt.ylabel('Frecuencia')
plt.title('Gráfica de Dispersión de Puntos con la Regresión de la Línea')
plt.legend()
plt.show()