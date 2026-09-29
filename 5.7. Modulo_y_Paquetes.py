# operaciones_matematicas.py
# Definición de la constante PI
PI = 3.14159
# Función para sumar dos números
def sumar(a, b):
    return a + b
# Función para restar dos números
def restar(a, b):
    return a - b
# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b
# Función para dividir dos números, manejando división por cero
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
    
# calculadora.py
# Importar todas las funciones y la constante PI del módulo
from operaciones_matematicas import sumar, restar, multiplicar, dividir, PI
# Calcular y mostrar el resultado de sumar 15 y 7
resultado_suma = sumar(15, 7)
print("15 + 7 =", resultado_suma)
# Calcular y mostrar el resultado de multiplicar 3.5 por 2
resultado_multiplicacion = multiplicar(3.5, 2)
print("3.5 * 2 =", resultado_multiplicacion)
# Calcular y mostrar el área de un círculo con radio 5
radio = 5
area_circulo = PI * multiplicar(radio, radio)  # PI * r^2
print("Área del círculo con radio 5 =", area_circulo)