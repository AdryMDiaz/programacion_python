import seaborn as sns
import matplotlib.pyplot as plt
# Cargar el conjunto de datos 'tips'
datos = sns.load_dataset('tips')
# Configurar el estilo
sns.set_style('whitegrid')
# Crear el gráfico de dispersión avanzado
sns.scatterplot(
    data=datos,
    x='total_bill',
    y='tip',
    hue='sex',
    alpha=0.6,
    palette='coolwarm'
)
# Añadir la línea de regresión sin puntos de dispersión
sns.regplot(
    data=datos,
    x='total_bill',
    y='tip',
    scatter=False,
    color='red'
)
# Añadir título y etiquetas
plt.title('Relación entre el total de la cuenta y la propina')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')
# Mostrar el gráfico
plt.show()