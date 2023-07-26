import pandas as pd

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

# Calcular la correlación entre "Valor Continuo" y "Fr. Absoluta"
correlacion = df['Valor Continuo'].corr(df['Fr. Absoluta'])

# Mostrar el resultado
print("Correlación entre Valor Continuo y Fr. Absoluta:", correlacion)