import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# 1. Crear los DataFrames
# DataFrame de ventas
id_productos_ventas = ['A1', 'A2', 'A3', 'A4', 'A2']
fechas = [(datetime.strptime('2023-01-01', '%Y-%m-%d') + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(5)]
unidades_vendidas = [10, 5, 8, 12, 7]
ventas = pd.DataFrame({
    'id_producto': id_productos_ventas,
    'fecha': fechas,
    'unidades_vendidas': unidades_vendidas
})
# DataFrame de productos
id_productos = ['A1', 'A2', 'A3', 'A5']
nombres = ['Laptop', 'Monitor', 'Teclado', 'Mouse']
precios = [1200, 300, 100, 50]
productos = pd.DataFrame({
    'id_producto': id_productos,
    'nombre': nombres,
    'precio': precios
})
# Mostrar los DataFrames originales
print("DataFrame de ventas:")
print(ventas)
print("\nDataFrame de productos:")
print(productos)
# 2. Realizar una unión (merge) de tipo 'inner'
inner_merge = pd.merge(ventas, productos, on='id_producto', how='inner')
print("\nUnión INNER:")
print(inner_merge)
# 3. Realizar una unión (merge) de tipo 'left'
left_merge = pd.merge(ventas, productos, on='id_producto', how='left')
print("\nUnión LEFT:")
print(left_merge)
# 4. Realizar una unión (merge) de tipo 'outer'
outer_merge = pd.merge(ventas, productos, on='id_producto', how='outer')
print("\nUnión OUTER:")
print(outer_merge)
# 5. Crear una nueva columna 'valor_total' en el resultado de la unión 'inner'
inner_merge['valor_total'] = inner_merge['unidades_vendidas'] * inner_merge['precio']
print("\nUnión INNER con columna valor_total:")
print(inner_merge)