# Programa que solicita un número entero y maneja excepciones
try:
    # Solicitamos al usuario que introduzca un número entero
    numero = int(input("Por favor, introduce un número entero: "))
    
    # Si la conversión es exitosa, mostramos el número introducido
    print(f"Has introducido el número: {numero}")
    
except ValueError:
    # Capturamos el error si el usuario no introduce un número entero
    print("Error: Debes introducir un número entero.")
    
except KeyboardInterrupt:
    # Capturamos la interrupción del programa (Ctrl+C)
    print("\nSe ha interrumpido la ejecución del programa.")