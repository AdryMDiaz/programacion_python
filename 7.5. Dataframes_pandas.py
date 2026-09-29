import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# Crear datos para el DataFrame
productos = ['Laptop', 'Smartphone', 'Tablet', 'Auriculares', 'Monitor']
precios = [1200.50, 800.75, 350.25, 120.99, 250.50]
unidades_vendidas = [10, 25, 15, 40, 8]
# Generar fechas aleatorias para el año actual
año_actual = datetime.now().year
fechas = []
for _ in range(len(productos)):
    # Generar una fecha aleatoria dentro del año actual
    dia = np.random.randint(1, 365)
    fecha = datetime(año_actual, 1, 1) + timedelta(days=dia)
    fechas.append(fecha)
# Crear el DataFrame
data = {
    'producto': productos,
    'precio': precios,
    'unidades_vendidas': unidades_vendidas,
    'fecha_venta': fechas
}
df = pd.DataFrame(data)
# 1. Añadir columna de ingresos totales
df['ingresos_totales'] = df['precio'] * df['unidades_vendidas']
print("DataFrame original con ingresos totales:")
print(df)
print("\n")
# 2. Mostrar productos ordenados de mayor a menor ingreso total
df_ordenado = df.sort_values(by='ingresos_totales', ascending=False)
print("Productos ordenados por ingresos totales (mayor a menor):")
print(df_ordenado[['producto', 'ingresos_totales']])
print("\n")
# 3. Calcular y mostrar el precio promedio de todos los productos
precio_promedio = df['precio'].mean()
print(f"Precio promedio de todos los productos: ${precio_promedio:.2f}")
print("\n")
# 4. Identificar y mostrar el producto con más unidades vendidas
producto_mas_vendido = df.loc[df['unidades_vendidas'].idxmax()]
print("Producto con más unidades vendidas:")
print(f"Producto: {producto_mas_vendido['producto']}")
print(f"Unidades vendidas: {producto_mas_vendido['unidades_vendidas']}")
print(f"Precio: ${producto_mas_vendido['precio']}")
print(f"Ingresos totales: ${producto_mas_vendido['ingresos_totales']}")