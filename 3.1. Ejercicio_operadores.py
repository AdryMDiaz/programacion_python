# Calculadora básica con las cuatro operaciones aritméticas fundamentales
# Solicitar al usuario que introduzca dos números
print("Calculadora básica")
print("----------------")
try:
    # Capturar los números del usuario
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    # Realizar las operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    # Mostrar resultados de suma, resta y multiplicación
    print(f"\nLa suma de {num1} y {num2} es: {suma}")
    print(f"La resta de {num1} y {num2} es: {resta}")
    print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
    
    # Manejar la división por cero
    if num2 != 0:
        division = num1 / num2
        print(f"La división de {num1} y {num2} es: {division}")
    else:
        print(f"La división de {num1} y {num2} es: Error - No se puede dividir por cero")
        
except ValueError:
    print("Error: Debes introducir números válidos.")