import seaborn as sns
import matplotlib.pyplot as plt
# Configurar el estilo del gráfico
sns.set_style('darkgrid')
# Cargar el conjunto de datos
df = sns.load_dataset('tips')
# Crear el histograma personalizado
sns.histplot(
    data=df, 
    x='tip', 
    bins=40, 
    stat='density', 
    kde=True, 
    color='blue'
)
# Añadir etiquetas y título
plt.xlabel('Propina')
plt.ylabel('Densidad')
plt.title('Distribución de las propinas con KDE')
# Mostrar el gráfico
plt.show()