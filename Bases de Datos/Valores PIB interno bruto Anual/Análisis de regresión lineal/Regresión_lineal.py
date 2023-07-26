import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos A y B
datos_A = np.array([15858, 45619, 5449, 79710, 75222, 60629, 3093]).reshape(-1, 1)
datos_B = np.array([2007, 2010, 2012, 2014, 2016, 2018, 2020])

# Crear el modelo de regresión
modelo = LinearRegression()

# Ajustar el modelo con los datos
modelo.fit(datos_A, datos_B)

# Calcular los valores predichos
y_pred = modelo.predict(datos_A)

# Calcular los residuales
residuales = datos_B - y_pred

# Gráfica de residuales
plt.scatter(datos_A, residuales)
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Gráfica de Residuales')
plt.xlabel('Datos A')
plt.ylabel('Residuales')
plt.show()
