# Programa que suma números enteros positivos hasta alcanzar o superar 100
suma = 0
contador = 0
print("Ingresa números enteros positivos hasta alcanzar o superar 100.")
while suma < 100:
    entrada = input(f"Suma actual: {suma}. Ingresa un número entero positivo: ")
    
    try:
        numero = int(entrada)
        if numero <= 0:
            print("Error: Debes ingresar un número entero positivo.")
        else:
            suma += numero
            contador += 1
            print(f"Número válido. Suma acumulada: {suma}")
    except ValueError:
        print("Error: Entrada inválida. Debes ingresar un número entero.")
# Mensaje final
print(f"\n¡Objetivo alcanzado! La suma final es {suma}.")
print(f"Se ingresaron {contador} números válidos para alcanzar el objetivo.")