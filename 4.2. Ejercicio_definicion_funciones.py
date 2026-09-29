def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.
        
    Returns:
        float: El área del rectángulo (base × altura).
    """
    return base * altura
# Llamar a la función con los valores 5 y 3
area = calcular_area_rectangulo(5, 3)
# Imprimir el resultado con un mensaje descriptivo
print(f"El área del rectángulo con base 5 y altura 3 es: {area} unidades cuadradas")