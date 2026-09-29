import matplotlib.pyplot as plt
import numpy as np
# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)
# Generación de datos aleatorios
x = rng.uniform(0, 10, 200)
y = rng.uniform(0, 10, 200)
colors = rng.uniform(0, 100, 200)
sizes = 200 * rng.random(200)
# Creación del gráfico de dispersión
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='plasma')
# Configurar etiquetas y título
plt.xlabel('Eje X: Valores aleatorios')
plt.ylabel('Eje Y: Valores aleatorios')
plt.title('Gráfico de dispersión multivariante con 4 variables')
# Añadir barra de colores
plt.colorbar(label='Escala de colores (0 a 100)')
# Mostrar gráfico
plt.show()