from collections import Counter
def analizar_texto(texto):
    """
    Analiza un texto y devuelve estadísticas sobre sus caracteres.
    
    Args:
        texto (str): El texto a analizar.
        
    Returns:
        dict: Un diccionario con las estadísticas del texto:
            - caracteres_mas_comunes: Lista de tuplas (caracter, frecuencia) de los 3 caracteres más comunes
            - total_caracteres: Número total de caracteres incluyendo espacios
            - total_sin_espacios: Número total de caracteres excluyendo espacios
    """
    # Calcular el total de caracteres incluyendo espacios
    total_caracteres = len(texto)
    
    # Calcular el total de caracteres sin espacios
    total_sin_espacios = len(texto.replace(" ", ""))
    
    # Crear un Counter excluyendo espacios en blanco
    contador = Counter([c for c in texto if c != " "])
    
    # Obtener los 3 caracteres más comunes
    caracteres_mas_comunes = contador.most_common(3)
    
    # Crear y devolver el diccionario con las estadísticas
    return {
        "caracteres_mas_comunes": caracteres_mas_comunes,
        "total_caracteres": total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }
# Ejemplo de uso
if __name__ == "__main__":
    resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
    print(resultado)