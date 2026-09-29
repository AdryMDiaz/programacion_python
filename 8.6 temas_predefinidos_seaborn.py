import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Paso 1: Crear el DataFrame con datos ficticios
datos = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valor': [10, 15, 7, 12]
})
# Paso 2: Configurar el tema global con 'whitegrid'
sns.set_theme(style="whitegrid")
# Paso 3: Crear el gráfico de barras asignando 'Categoría' a 'hue' y desactivando la leyenda
ax = sns.barplot(
    data=datos, 
    x='Categoría', 
    y='Valor', 
    hue='Categoría', 
    palette="pastel")
# Desactivar la leyenda generada automáticamente
ax.legend_.remove()
# Paso 4: Personalizar el título del gráfico
ax.set_title('Gráfico de barras personalizado', fontsize=16, color='blue', fontweight='bold')
# Paso 5: Personalizar las etiquetas de los ejes
ax.set_xlabel('Categorías', fontsize=12, color='darkgray')
ax.set_ylabel('Valores', fontsize=12, color='darkgray')
# Paso 6: Eliminar bordes izquierdo y derecho
sns.despine(left=True, right=True)
# Paso 7: Mostrar el gráfico
plt.show()