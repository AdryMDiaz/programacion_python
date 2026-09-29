import matplotlib.pyplot as plt
import numpy as np
# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)
# Generar datos aleatorios utilizando el generador (distribución normal)
data = rng.normal(5, 2, 1500)
# Crear el histograma
plt.hist(data, bins=40, color='green', alpha=0.5, edgecolor='red')
# Configurar título y etiquetas
plt.title('Distribución de Datos con Media 5 y Desviación 2')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
# Mostrar gráfico
plt.show()