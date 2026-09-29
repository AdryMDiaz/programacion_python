def suma_pares(inicio, fin):
    """
    Calcula la suma de todos los números pares en un rango dado (inclusive).
    
    Args:
        inicio (int): El número inicial del rango
        fin (int): El número final del rango
        
    Returns:
        int: La suma de todos los números pares en el rango
    """
    suma = 0
    
    # Iteramos sobre todos los números en el rango
    for numero in range(inicio, fin + 1):
        # Verificamos si el número es par usando el operador módulo
        if numero % 2 == 0:
            suma += numero
    
    return suma
# Ejemplos de uso
if __name__ == "__main__":
    # Ejemplo 1: Suma de pares de 1 a 10
    resultado1 = suma_pares(1, 10)
    print(f"La suma de los números pares entre 1 y 10 es: {resultado1}")  # Debería imprimir 30
    
    # Ejemplo 2: Suma de pares de 5 a 15
    resultado2 = suma_pares(5, 15)
    print(f"La suma de los números pares entre 5 y 15 es: {resultado2}")  # Debería imprimir 50