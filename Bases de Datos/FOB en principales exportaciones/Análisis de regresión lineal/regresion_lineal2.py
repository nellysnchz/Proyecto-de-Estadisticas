import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Datos
data = {
    'Intervalos': ['2010-2011', '2012-2013', '2014-2015', '2016-2017', '2018-2019', '2020-2021', '2022-2023'],
    'Frecuencia': [7952, 2106, 14157, 6157, 21828, 22385, 7272]
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Crear una variable Punto_Medio para el análisis de regresión
df['Punto_Medio'] = np.arange(1, len(df) + 1)

# Análisis de regresión lineal
X = sm.add_constant(df['Punto_Medio'])
y = df['Frecuencia']
model = sm.OLS(y, X).fit()

# Obtener los resultados del análisis
summary = model.summary()
r_squared = model.rsquared
conf_int = model.conf_int()

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

# Mostrar los resultados del análisis
print("Análisis de Regresión Lineal:")
print(summary)
print("\nR cuadrado:", r_squared)
print("\nIntervalos de Confianza:")
print(conf_int)