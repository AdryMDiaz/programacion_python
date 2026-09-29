def procesar_estudiantes(escuela, *args, **kwargs):
    """
    Procesa información de estudiantes y datos adicionales.
    
    Args:
        escuela (str): Nombre de la escuela (parámetro obligatorio)
        *args: Nombres de los estudiantes (argumentos posicionales variables)
        **kwargs: Datos adicionales (argumentos con nombre)
    
    Returns:
        dict: Diccionario con la escuela, lista de estudiantes y datos adicionales
    """
    resultado = {
        'escuela': escuela,
        'estudiantes': list(args),
        'datos_adicionales': kwargs
    }
    
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    resultado = procesar_estudiantes("IES Tecnológico", "Ana", "Carlos", "Elena", curso="1º DAW", turno="mañana")
    print(resultado)
    # Debería imprimir:
    # {'escuela': 'IES Tecnológico', 'estudiantes': ['Ana', 'Carlos', 'Elena'], 'datos_adicionales': {'curso': '1º DAW', 'turno': 'mañana'}}