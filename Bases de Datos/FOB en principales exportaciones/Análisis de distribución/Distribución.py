import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos de frecuencia por intervalo
intervalos = ['2010-2011', '2012-2013', '2014-2015', '2016-2017', '2018-2019', '2020-2021', '2022-2023']
frecuencias = [7952, 2106, 14157, 6157, 21828, 22385, 7272]

# Calcular el valor medio de cada intervalo como los valores x
valores_x = [2010.5, 2012.5, 2014.5, 2016.5, 2018.5, 2020.5, 2022.5]

# Calcular la media y desviación estándar de las frecuencias
media = np.mean(frecuencias)
desviacion_estandar = np.std(frecuencias)

# Estimar la distribución de Poisson a partir de los datos de frecuencia
distribucion_poisson = stats.poisson(mu=media)

# Generar valores de la distribución continua (normalizada) para el análisis
x = np.linspace(min(valores_x), max(valores_x), 1000)
y = distribucion_poisson.pmf(x)

# Graficar la distribución discreta y la distribución continua (Poisson)
plt.bar(valores_x, frecuencias, width=1.0, align='center', label='Distribución Discreta (Poisson)', color='b')
plt.plot(x, y * sum(frecuencias), 'ro-', label='Distribución Continua (Poisson)', linewidth=2)
plt.xlabel('Años')
plt.ylabel('Frecuencias')
plt.legend()
plt.title('Análisis de Conversión de Distribución Discreta a Distribución Continua')
plt.show()