def fibonacci_generator(n):
    """
    Generador que produce los primeros n números de la secuencia de Fibonacci.
    
    Args:
        n (int): Cantidad de números de la secuencia a generar.
        
    Yields:
        int: Números de la secuencia de Fibonacci uno por uno.
    """
    # Verificar si n es válido
    if n <= 0:
        return
    
    # Primer número de Fibonacci
    yield 0
    
    # Si solo se pide un número, terminamos
    if n == 1:
        return
    
    # Segundo número de Fibonacci
    yield 1
    
    # Si solo se piden dos números, terminamos
    if n == 2:
        return
    
    # Variables para mantener los dos últimos números de Fibonacci
    a, b = 0, 1
    
    # Generar el resto de números de Fibonacci
    for _ in range(2, n):
        # Calcular el siguiente número de Fibonacci
        a, b = b, a + b
        yield b
# Ejemplo de uso
if __name__ == "__main__":
    print("Primeros 6 números de Fibonacci:")
    for num in fibonacci_generator(6):
        print(num, end=" ")
    # Salida esperada: 0 1 1 2 3 5