import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Intervalos de años y frecuencias
intervalos = [2008, 2011, 2014, 2017, 2019.5]
frecuencias = [3, 3, 3, 3, 1]

# Agregamos un valor adicional al inicio para el año 2007 con frecuencia 0
x = np.array([2007] + intervalos)
y = np.array([0] + frecuencias)

# Puntos a interpolar (valores continuos entre 2007 y 2020)
x_interp = np.linspace(2007, max(intervalos), 1000)  # Ajustamos el valor máximo de x_interp

# Interpolación lineal
f = interp1d(x, y, kind='linear')

# Frecuencias interpoladas
y_interp = f(x_interp)

# Gráfica de la distribución original
plt.bar(intervalos, frecuencias, width=3, align='center', color='blue', label='Distribución Discreta')
plt.xlabel('Años')
plt.ylabel('Frecuencia')
plt.title('Distribución Discreta de Aporte Absoluto por Intervalos de Años')
plt.legend()
plt.show()

# Gráfica de la distribución continua interpolada
plt.plot(x_interp, y_interp, color='red', label='Distribución Continua Interpolada')
plt.xlabel('Años')
plt.ylabel('Frecuencia Interpolada')
plt.title('Distribución Continua Interpolada de Aporte Absoluto')
plt.legend()
plt.show()