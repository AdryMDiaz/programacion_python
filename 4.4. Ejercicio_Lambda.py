# Definición de funciones lambda
cuadrado = lambda x: x ** 2
es_par = lambda x: x % 2 == 0
suma = lambda x, y: x + y
# Creación de la lista de números
numeros = [1, 2, 3, 4, 5]
# Uso de map() con la función lambda cuadrado
cuadrados = list(map(cuadrado, numeros))
# Uso de filter() con la función lambda es_par
pares = list(filter(es_par, numeros))
# Mostrar resultados
print(f"Lista original: {numeros}")
print(f"Cuadrados: {cuadrados}")
print(f"Números pares: {pares}")
# Ejemplo de uso de la función suma
print(f"Suma de 3 y 7: {suma(3, 7)}")