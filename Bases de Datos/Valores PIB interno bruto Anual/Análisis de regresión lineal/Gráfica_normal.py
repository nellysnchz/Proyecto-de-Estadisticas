import statsmodels.api as sm
import scipy.stats as stats

# Prueba de normalidad de los residuales
prueba_normalidad = sm.stats.normal_ad(residuales)
p_valor = prueba_normalidad[1]

# Gráfica Q-Q de probabilidad normal
stats.probplot(residuales, dist='norm', plot=plt)
plt.title('Gráfica de Probabilidad Normal Normal')
plt.xlabel('Cuantiles Teóricos')
plt.ylabel('Cuantiles de los Residuales')
plt.show()

# Imprimir el resultado de la prueba de normalidad
if p_valor > 0.05:
    print("Los residuales siguen una distribución normal (p > 0.05)")
else:
    print("Los residuales no siguen una distribución normal (p <= 0.05)")