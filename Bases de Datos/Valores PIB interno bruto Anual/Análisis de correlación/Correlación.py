import numpy as np

# Datos de ejemplo en forma de listas
datos_A = [15858, 45619, 5449, 79710, 75222, 60629, 3093]
datos_B = [57723, 8263, 86326, 75222, 3093, 45619, 79710]

# Convertir los datos en arrays de NumPy
array_A = np.array(datos_A)
array_B = np.array(datos_B)

# Calcular la matriz de correlación
matriz_correlacion = np.corrcoef(array_A, array_B)

# La matriz de correlación tendrá dos filas y dos columnas,
# la correlación entre los datos A y B estará en la posición (0, 1) o (1, 0).
correlacion_AB = matriz_correlacion[0, 1]

print("Correlación entre los datos A y B:", correlacion_AB)