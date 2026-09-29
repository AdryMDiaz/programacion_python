import matplotlib.pyplot as plt
import numpy as np
# Crear un generador de números aleatorios con una semilla específica para reproducibilidad
rng = np.random.default_rng(seed=42)
# Generar datos aleatorios para las dos variables
x = rng.uniform(0, 50, 100)
ruido = rng.normal(0, 10, 100)
y = 2.5 * x + ruido
# Calcular la línea de regresión utilizando polyfit
m, b = np.polyfit(x, y, 1)
# Crear el gráfico de dispersión
plt.scatter(x, y, color='purple', s=50, label='Datos')
# Dibujar la línea de regresión
plt.plot(x, m*x + b, color='green', label='Línea de regresión')
# Configurar etiquetas y título
plt.title('Relación Lineal entre X e Y con Ruido Aleatorio')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
# Añadir una leyenda y cuadrícula
plt.legend()
plt.grid(True)
# Mostrar gráfico
plt.show()