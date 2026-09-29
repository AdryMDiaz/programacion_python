import pandas as pd
# Crear el DataFrame de ventas
ventas = pd.DataFrame({
    'producto': ['Smartphone', 'Camiseta', 'Lámpara', 'Televisor', 'Pantalón', 'Sartén', 'Auriculares', 'Almohada'],
    'categoria': ['Electrónica', 'Ropa', 'Hogar', 'Electrónica', 'Ropa', 'Hogar', 'Electrónica', 'Hogar'],
    'precio': [599.99, 25.50, 45.75, 899.99, 39.99, 29.95, 89.99, 19.99],
    'stock': [15, 100, 30, 10, 75, 25, 18, 50]
})
# Mostrar el DataFrame original
print("DataFrame original:")
print(ventas)
print("\n" + "-"*50 + "\n")
# 1. Filtrar productos de la categoría 'Electrónica'
electronica = ventas[ventas['categoria'] == 'Electrónica']
print("1. Productos de la categoría 'Electrónica':")
print(electronica)
print("\n" + "-"*50 + "\n")
# 2. Encontrar productos con precio mayor a 50 y stock menor a 20
precio_stock_filtro = ventas[(ventas['precio'] > 50) & (ventas['stock'] < 20)]
print("2. Productos con precio > 50 y stock < 20:")
print(precio_stock_filtro)
print("\n" + "-"*50 + "\n")
# 3. Seleccionar productos que contengan la letra 'a' en su nombre
contiene_a = ventas[ventas['producto'].str.contains('a')]
print("3. Productos que contienen la letra 'a' en su nombre:")
print(contiene_a)
print("\n" + "-"*50 + "\n")
# 4. Utilizar query() para encontrar productos de la categoría 'Hogar' con precio menor a 30
hogar_economico = ventas.query("categoria == 'Hogar' and precio < 30")
print("4. Productos de 'Hogar' con precio < 30 (usando query):")
print(hogar_economico)