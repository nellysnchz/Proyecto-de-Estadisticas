import numpy as np

# Datos de las variables
intervalos = [2010, 2012, 2014, 2016, 2018, 2020, 2022]
frecuencia = [7952, 2106, 14157, 6157, 21828, 22385, 7272]

# Calcula el coeficiente de correlación de Pearson
correlation_coef = np.corrcoef(intervalos, frecuencia)[0, 1]

print("Coeficiente de correlación de Pearson:", correlation_coef)