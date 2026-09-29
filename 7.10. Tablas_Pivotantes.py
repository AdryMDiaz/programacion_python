import pandas as pd
import numpy as np
# Crear datos aleatorios para el DataFrame
np.random.seed(42)  # Para reproducibilidad
# Crear listas con los datos
categorias = np.random.choice(['Electrónica', 'Ropa', 'Hogar'], size=30)
regiones = np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], size=30)
ventas = np.random.randint(100, 1001, size=30)  # Valores entre 100 y 1000
unidades = np.random.randint(1, 21, size=30)    # Valores entre 1 y 20
# Crear el DataFrame
df = pd.DataFrame({
    'categoría': categorias,
    'región': regiones,
    'ventas': ventas,
    'unidades': unidades
})
# Mostrar los primeros registros del DataFrame
print("DataFrame original:")
print(df.head())
print("\nInformación del DataFrame:")
print(df.info())
print("\nEstadísticas descriptivas:")
print(df.describe())
# Crear la tabla pivotante
tabla_pivot = pd.pivot_table(
    data=df,
    values='ventas',
    index='categoría',
    columns='región',
    aggfunc='sum',  # Suma total de ventas
    margins=True,   # Incluir totales por fila y columna
    margins_name='Total',
    fill_value=0     # Reemplazar NaN con ceros
)
# Mostrar la tabla pivotante
print("\nTabla pivotante de ventas por categoría y región:")
print(tabla_pivot)
# Análisis adicional: Tabla pivotante para unidades vendidas
tabla_pivot_unidades = pd.pivot_table(
    data=df,
    values='unidades',
    index='categoría',
    columns='región',
    aggfunc='sum',
    margins=True,
    margins_name='Total',
    fill_value=0
)
print("\nTabla pivotante de unidades vendidas por categoría y región:")
print(tabla_pivot_unidades)
# Análisis adicional: Promedio de ventas por unidad
df['venta_por_unidad'] = df['ventas'] / df['unidades']
tabla_pivot_promedio = pd.pivot_table(
    data=df,
    values='venta_por_unidad',
    index='categoría',
    columns='región',
    aggfunc='mean',
    margins=True,
    margins_name='Promedio',
    fill_value=0
)
print("\nTabla pivotante de promedio de venta por unidad:")
print(tabla_pivot_promedio.round(2))  # Redondear a 2 decimales para mejor visualización