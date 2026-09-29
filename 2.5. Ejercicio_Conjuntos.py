# Ejercicio de operaciones con conjuntos en Python
# Definición de las listas iniciales
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
# Convertir las listas a conjuntos para poder realizar operaciones de conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)
# 1. Encontrar los elementos que aparecen en ambas listas (intersección)
interseccion = conjunto1.intersection(conjunto2)
print("Elementos que aparecen en ambas listas (intersección):")
print(interseccion)
# 2. Encontrar los elementos que solo aparecen en la primera lista (diferencia)
diferencia1 = conjunto1.difference(conjunto2)
print("\nElementos que solo aparecen en la primera lista (diferencia):")
print(diferencia1)
# 3. Encontrar los elementos que solo aparecen en la segunda lista (diferencia)
diferencia2 = conjunto2.difference(conjunto1)
print("\nElementos que solo aparecen en la segunda lista (diferencia):")
print(diferencia2)
# 4. Encontrar todos los elementos únicos que aparecen en cualquiera de las dos listas (unión)
union = conjunto1.union(conjunto2)
print("\nTodos los elementos únicos que aparecen en cualquiera de las dos listas (unión):")
print(union)