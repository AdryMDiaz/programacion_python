# Programa para determinar la categoría de edad de una persona
# Solicitar la edad al usuario
try:
    edad = int(input("Por favor, ingresa tu edad: "))
    
    # Determinar la categoría según la edad
    if edad < 0:
        print("Edad no válida")
    elif edad <= 12:
        print("Infante")
    elif edad <= 17:
        print("Adolescente")
    elif edad <= 64:
        print("Adulto")
    else:
        print("Adulto mayor")
        
except ValueError:
    print("Error: Debes ingresar un número entero.")