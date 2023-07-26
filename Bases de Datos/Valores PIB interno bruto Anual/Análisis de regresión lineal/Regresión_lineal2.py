import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Datos A y B
datos_A = np.array([15858, 45619, 5449, 79710, 75222, 60629, 3093])
datos_B = np.array([2007, 2010, 2012, 2014, 2016, 2018, 2020])

# Agregar una columna de unos para el término constante en la regresión
X = sm.add_constant(datos_A)

# Crear el modelo de regresión
modelo = sm.OLS(datos_B, X)

# Ajustar el modelo con los datos
resultado = modelo.fit()

# Imprimir la tabla ANOVA
print(resultado.summary())

# Calcular el R cuadrado
r_cuadrado = resultado.rsquared
print("R cuadrado:", r_cuadrado)

# Obtener los valores constantes de la línea de regresión (interceptor) y la pendiente
interceptor, pendiente = resultado.params
print("Interceptor:", interceptor)
print("Pendiente:", pendiente)

# Realizar las pruebas de t y F
print("Prueba de t (interceptor):", resultado.tvalues[0])
print("Prueba de t (pendiente):", resultado.tvalues[1])
print("Prueba de F:", resultado.fvalue)

# Obtener los intervalos de confianza para el interceptor y la pendiente
intervalo_confianza_interceptor = resultado.conf_int(alpha=0.05)[0]
intervalo_confianza_pendiente = resultado.conf_int(alpha=0.05)[1]
print("Intervalo de confianza para el interceptor:", intervalo_confianza_interceptor)
print("Intervalo de confianza para la pendiente:", intervalo_confianza_pendiente)

# Gráfica de dispersión de puntos con la regresión lineal
plt.scatter(datos_A, datos_B)
plt.plot(datos_A, interceptor + pendiente*datos_A, color='red')
plt.title('Gráfica de Dispersión con Regresión Lineal')
plt.xlabel('Datos A')
plt.ylabel('Datos B')
plt.show()