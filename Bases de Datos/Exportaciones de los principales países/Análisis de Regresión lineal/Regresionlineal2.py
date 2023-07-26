import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# Datos
intervalos = ['2007-2009', '2010-2012', '2013-2015', '2016-2018', '2019-2020']
frecuencia_absoluta = [3, 3, 3, 3, 1]

# Transformar datos
valores_absolutos = [500 * (i + 1) for i in range(len(frecuencia_absoluta))]
valores_relativos = [f / sum(frecuencia_absoluta) for f in frecuencia_absoluta]

# Calcular valor representativo
valor_representativo = [np.mean([int(i) for i in intervalo.split('-')]) for intervalo in intervalos]

# Crear DataFrame
df = pd.DataFrame({
    'Intervalo': intervalos,
    'Frecuencia Absoluta': frecuencia_absoluta,
    'Frecuencia Relativa': valores_relativos,
    'Valor Representativo': valor_representativo,
    'Valor Absoluto': valores_absolutos
})

# Realizar regresión lineal
X = sm.add_constant(df['Valor Representativo'])
modelo = sm.OLS(df['Frecuencia Absoluta'], X).fit()

# Resultados de la regresión
slope = modelo.params['Valor Representativo']
intercept = modelo.params['const']
r_squared = modelo.rsquared
p_value = modelo.pvalues['Valor Representativo']

# Graficar dispersión de puntos y regresión lineal
plt.scatter(df['Valor Representativo'], df['Frecuencia Absoluta'], label='Datos')
plt.plot(df['Valor Representativo'], modelo.fittedvalues, 'r', label='Regresión Lineal')
plt.xlabel('Valor Representativo')
plt.ylabel('Frecuencia Absoluta')
plt.title('Regresión Lineal')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir resultados
print("Valor de la pendiente (coeficiente):", slope)
print("Valor de la intersección (intercept):", intercept)
print("Valor R-cuadrado:", r_squared)
print("Valor p:", p_value)

# Obtener residuales
residuales = modelo.resid

# Gráfica de residuales
plt.scatter(df['Valor Representativo'], residuales)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Valor Representativo')
plt.ylabel('Residuales')
plt.title('Gráfica de Residuales')
plt.grid(True)
plt.show()

# Gráfica de probabilidad normal (Q-Q plot)
import scipy.stats as stats
stats.probplot(residuales, plot=plt)
plt.title('Gráfica de Probabilidad Normal (Q-Q plot)')
plt.grid(True)
plt.show()

# Intervalos de confianza para pendiente e intercepto
conf_intervals = modelo.conf_int()
conf_intervals.columns = ['Límite inferior', 'Límite superior']
conf_intervals.index = ['Intercepto', 'Pendiente']
print(conf_intervals)

# Tabla ANOVA
print(modelo.summary())