import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats

# Datos de Año y Aporte Absoluto
años = [2007, 2010, 2013, 2016, 2019]
aporte_absoluto = [3859.9, 1960.7, 2323.7, 5245.9, 5743.5]

# Convertir los datos en un DataFrame de pandas
data = pd.DataFrame({'Año': años, 'Aporte Absoluto': aporte_absoluto})

# Añadir una columna de unos para el intercepto
data = sm.add_constant(data)

# Realizar el ajuste de la regresión lineal
modelo = sm.OLS(data['Aporte Absoluto'], data[['const', 'Año']])
resultados = modelo.fit()

# Obtener los coeficientes de la regresión
intercepto, pendiente = resultados.params

# Obtener la predicción de la regresión
data['Predicción'] = intercepto + pendiente * data['Año']

# Calcular los residuos
data['Residuales'] = data['Aporte Absoluto'] - data['Predicción']

# Gráfica de dispersión de puntos con la regresión de la línea
plt.scatter(data['Año'], data['Aporte Absoluto'], label='Datos reales')
plt.plot(data['Año'], data['Predicción'], color='red', label='Regresión lineal')
plt.xlabel('Año')
plt.ylabel('Aporte Absoluto')
plt.legend()
plt.title('Gráfica de dispersión de puntos con la regresión de la línea')
plt.show()

# Gráfica de residuales
plt.scatter(data['Año'], data['Residuales'])
plt.axhline(0, color='red', linestyle='dashed')
plt.xlabel('Año')
plt.ylabel('Residuales')
plt.title('Gráfica de residuales')
plt.show()

# Gráfica de probabilidad normal
stats.probplot(data['Residuales'], plot=plt)
plt.title('Gráfica de probabilidad normal')
plt.show()

# Resumen completo de la regresión
print(resultados.summary())