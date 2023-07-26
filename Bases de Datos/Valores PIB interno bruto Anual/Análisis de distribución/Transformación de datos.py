import numpy as np

# Datos discretos de construcción
datos_discretos = [15858, 45619, 5449, 79710, 75222, 60629, 3093]

# Transformación logarítmica
datos_transformados_log = np.log(datos_discretos)

# Transformación raíz cuadrada
datos_transformados_sqrt = np.sqrt(datos_discretos)

print("Datos discretos de construcción:", datos_discretos)
print("Transformación logarítmica:", datos_transformados_log)
print("Transformación raíz cuadrada:", datos_transformados_sqrt)