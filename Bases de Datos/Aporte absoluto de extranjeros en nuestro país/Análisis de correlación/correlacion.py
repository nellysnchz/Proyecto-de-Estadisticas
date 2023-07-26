import numpy as np

# Datos de Año y Aporte Absoluto
años = [2007, 2010, 2013, 2016, 2019]
aporte_absoluto = [3859.9, 1960.7, 2323.7, 5245.9, 5743.5]

# Calcula la matriz de correlación
correlacion_matrix = np.corrcoef(años, aporte_absoluto)

# El coeficiente de correlación está en la posición (0, 1) o (1, 0) de la matriz
coef_correlacion = correlacion_matrix[0, 1]

print("Coeficiente de correlación de Pearson:", coef_correlacion)