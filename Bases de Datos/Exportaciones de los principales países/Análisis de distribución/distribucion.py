import pandas as pd

# Datos de la tabla de frecuencia
datos = {
    'Intervalo de Valor FOB (en millones)': ['0 - 500', '501 - 1000', '1001 - 1500', '1501 - 2000', '2000+'],
    'Fr. Absoluta': [1, 2, 3, 2, 3],
    'Fr. Absoluta acumulativa': [1, 3, 6, 8, 11],
    'Fr. Relativa': [0.09, 0.18, 0.27, 0.18, 0.27],
    'Fr. Relativa Acumulada': [0.09, 0.27, 0.55, 0.73, 1.00]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(datos)

# Calcular los valores representativos (puntos medios) de cada intervalo
def obtener_valor_representativo(intervalo):
    if '+' in intervalo:
        return int(intervalo.split('+')[0])
    else:
        return (int(intervalo.split('-')[0]) + int(intervalo.split('-')[1])) / 2

df['Valor Representativo'] = df['Intervalo de Valor FOB (en millones)'].apply(obtener_valor_representativo)

# Interpolar linealmente para obtener valores continuos
def interpolacion_lineal(x, x0, x1, y0, y1):
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

valores_continuos = []
for i in range(len(df)-1):
    x0 = df['Valor Representativo'][i]
    x1 = df['Valor Representativo'][i+1]
    y0 = df['Fr. Absoluta acumulativa'][i]
    y1 = df['Fr. Absoluta acumulativa'][i+1]
    for x in range(int(x0)+1, int(x1)+1):
        valor_continuo = interpolacion_lineal(x, x0, x1, y0, y1)
        valores_continuos.append(valor_continuo)

# Agregar los valores continuos al DataFrame usando pd.IntervalIndex
intervalos = pd.IntervalIndex.from_tuples([(0, 500), (501, 1000), (1001, 1500), (1501, 2000), (2000, float('inf'))])
df['Valor Continuo'] = pd.cut(df['Valor Representativo'], bins=intervalos, labels=valores_continuos, right=False)

# Mostrar el DataFrame resultante con los valores continuos
print(df)