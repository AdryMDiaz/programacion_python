# Ejercicio de iteración múltiple
# Crear una matriz de multiplicación de 5x5 utilizando bucles anidados
# Inicializar una matriz vacía
matriz = []
# Crear la matriz de multiplicación con bucles anidados
for i in range(5):
    fila = []
    for j in range(5):
        # Calcular el producto de la fila por la columna
        fila.append(i * j)
    matriz.append(fila)
# Mostrar la matriz en formato de tabla
print("Matriz de multiplicación 5x5:")
for fila in matriz:
    # Convertir cada número a string y unirlos con espacios
    fila_formateada = ' '.join(str(numero) for numero in fila)
    print(fila_formateada)