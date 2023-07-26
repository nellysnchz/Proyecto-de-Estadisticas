import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import scipy.stats as stats

# Datos de la tabla de frecuencia con valores continuos
datos = {
    'Intervalo de Valor FOB (en millones)': ['0 - 500', '501 - 1000', '1001 - 1500', '1501 - 2000', '2000+'],
    'Fr. Absoluta': [1, 2, 3, 2, 3],
    'Fr. Absoluta acumulativa': [1, 3, 6, 8, 11],
    'Fr. Relativa': [0.09, 0.18, 0.27, 0.18, 0.27],
    'Fr. Relativa Acumulada': [0.09, 0.27, 0.55, 0.73, 1.00],
    'Valor Representativo': [250, 750.5, 1250.5, 1750.5, 2000],
    'Valor Continuo': [0.09491525423728814, 0.1694915254237288, 0.23728813559322035, 0.2542372881355932, 0.2711864406779661]
}

# Crear el DataFrame con los datos
df = pd.DataFrame(datos)

# Realizar la regresión lineal
X = sm.add_constant(df['Valor Representativo'])
y = df['Fr. Absoluta']
modelo = sm.OLS(y, X).fit()

# Obtener los resultados de la regresión
resultados = modelo.summary()

# Imprimir los resultados
print(resultados)

# Gráfica de dispersión de puntos con la regresión de la línea
plt.scatter(df['Valor Representativo'], df['Fr. Absoluta'], label='Datos')
plt.plot(df['Valor Representativo'], modelo.predict(X), color='red', label='Regresión')
plt.xlabel('Valor Representativo')
plt.ylabel('Fr. Absoluta')
plt.legend()
plt.show()

# Gráfica de residuales
residuales = modelo.resid
plt.scatter(df['Valor Representativo'], residuales)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Valor Representativo')
plt.ylabel('Residuales')
plt.show()

# Gráfica de probabilidad normal
stats.probplot(residuales, plot=plt)
plt.show()

# Tabla ANOVA
tabla_anova = sm.stats.anova_lm(modelo)
print(tabla_anova)

# R cuadrado
r_cuadrado = modelo.rsquared
print("R cuadrado:", r_cuadrado)

# Pruebas de t y F
prueba_t = modelo.t_test([1, 0])
prueba_f = modelo.f_test(np.identity(2))

print("Prueba t:", prueba_t)
print("Prueba F:", prueba_f)

# Intervalos de confianza para los coeficientes de la regresión
intervalos_confianza = modelo.conf_int(alpha=0.05)
print(intervalos_confianza)
