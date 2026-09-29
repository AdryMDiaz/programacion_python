# Ejercicio de listas en Python
# 1. Crear la lista con los valores iniciales
numeros = [10, 20, 30, 40, 50]
print("Lista original:", numeros)
# 2. Añadir el número 60 al final de la lista
numeros.append(60)
print("Después de añadir 60:", numeros)
# 3. Insertar el número 15 entre el 10 y el 20
numeros.insert(1, 15)
print("Después de insertar 15:", numeros)
# 4. Eliminar el número 30 de la lista
numeros.remove(30)
print("Después de eliminar 30:", numeros)
# 5. Calcular la suma de todos los números en la lista
suma = sum(numeros)
# 6. Calcular el promedio de los números en la lista
promedio = suma / len(numeros)
# Imprimir resultados finales
print("\nResultados finales:")
print("Lista resultante:", numeros)
print("Suma de los números:", suma)
print("Promedio de los números:", promedio)