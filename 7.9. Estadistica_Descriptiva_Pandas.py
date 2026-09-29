import pandas as pd
import numpy as np
# Datos de ventas mensuales
data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'ventas': [15200, 14800, 16700, 17500, 18200],
    'unidades': [120, 115, 140, 150, 160],
    'gastos': [5100, 4800, 5400, 5800, 6000]
}
# Crea el DataFrame
df_ventas = pd.DataFrame(data)
# 1. Utiliza el método describe() para obtener un resumen estadístico completo del DataFrame
print("\n1. Resumen estadístico completo del DataFrame:")
print(df_ventas.describe())
# 2. Calcula la media, mediana y desviación estándar de la columna 'ventas'
print("\n2. Estadísticas de la columna 'ventas':")
print(f"Media de ventas: {df_ventas['ventas'].mean()}")
print(f"Mediana de ventas: {df_ventas['ventas'].median()}")
print(f"Desviación estándar de ventas: {df_ventas['ventas'].std()}")
# 3. Encuentra el valor máximo y mínimo de la columna 'unidades'
print("\n3. Valores máximo y mínimo de la columna 'unidades':")
print(f"Valor máximo de unidades: {df_ventas['unidades'].max()}")
print(f"Valor mínimo de unidades: {df_ventas['unidades'].min()}")
# 4. Calcula la correlación entre las columnas 'ventas' y 'unidades'
print("\n4. Correlación entre 'ventas' y 'unidades':")
print(f"Correlación: {df_ventas['ventas'].corr(df_ventas['unidades'])}")
# También podemos mostrar la matriz de correlación completa
print("\nMatriz de correlación completa:")
print(df_ventas[['ventas', 'unidades', 'gastos']].corr())