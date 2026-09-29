def procesar_numeros(numeros):
    """
    Filtra los números pares de una lista y duplica sus valores.
    
    Args:
        numeros (list): Lista de números enteros.
        
    Returns:
        list: Lista con los números pares duplicados.
    """
    # Paso 1: Filtrar solo los números pares usando filter()
    numeros_pares = filter(lambda x: x % 2 == 0, numeros)
    
    # Paso 2: Duplicar cada número par usando map()
    numeros_duplicados = map(lambda x: x * 2, numeros_pares)
    
    # Paso 3: Convertir el resultado a una lista y devolverlo
    return list(numeros_duplicados)

# Ejemplo de uso
if __name__ == "__main__":
    entrada = [1, 2, 3, 4, 5, 6]
    resultado = procesar_numeros(entrada)
    print(f"Entrada: {entrada}")
    print(f"Salida: {resultado}")
    # Salida esperada: [4, 8, 12]
