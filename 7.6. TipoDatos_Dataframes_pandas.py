import pandas as pd
import numpy as np
# Crear un DataFrame con diferentes tipos de datos
df = pd.DataFrame({
    'edad': [25, 30, 35, 40, 45],
    'altura': [1.75, 1.80, 1.65, 1.90, 1.70],
    'nombre': ['Ana', 'Juan', 'María', 'Carlos', 'Laura'],
    'activo': [True, False, True, True, False]
})
# 1. Verificar y mostrar los tipos de datos iniciales
print("Tipos de datos iniciales:")
print(df.dtypes)
print()
# Calcular el uso de memoria antes de las conversiones
memoria_antes = df.memory_usage(deep=True)
print("Uso de memoria antes de las conversiones (bytes):")
print(memoria_antes)
print(f"Total: {memoria_antes.sum()} bytes")
print()
# 2. Convertir la columna 'edad' a tipo float64
df['edad'] = df['edad'].astype('float64')
# 3. Convertir la columna 'altura' a tipo int64
df['altura'] = df['altura'].astype('int64')
# 4. Convertir la columna 'nombre' a tipo category
df['nombre'] = df['nombre'].astype('category')
# 5. Mostrar los tipos de datos después de las conversiones
print("Tipos de datos después de las conversiones:")
print(df.dtypes)
print()
# 6. Calcular y mostrar el uso de memoria después de las conversiones
memoria_despues = df.memory_usage(deep=True)
print("Uso de memoria después de las conversiones (bytes):")
print(memoria_despues)
print(f"Total: {memoria_despues.sum()} bytes")
print()
# Mostrar la diferencia de memoria
print(f"Diferencia de memoria: {memoria_antes.sum() - memoria_despues.sum()} bytes")
# Mostrar el DataFrame con los tipos de datos convertidos
print("\nDataFrame con tipos de datos convertidos:")
print(df)