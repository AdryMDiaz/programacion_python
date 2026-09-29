def extraer_info(correo):
    """
    Extrae información de un correo electrónico con formato nombre@dominio.extension
    
    Args:
        correo (str): Cadena de texto con el correo electrónico
        
    Returns:
        dict: Diccionario con nombre_usuario, dominio y extension, o diccionario vacío si el formato es inválido
    """
    # Verificar si el correo contiene el símbolo @
    if '@' not in correo:
        return {}
    
    # Dividir el correo en la parte del nombre y la parte del dominio+extensión
    nombre_usuario, dominio_completo = correo.split('@', 1)
    
    # Verificar si hay un punto después del @ (para la extensión)
    if '.' not in dominio_completo:
        return {}
    
    # Obtener el dominio y la extensión
    # Usamos el último punto para separar el dominio de la extensión
    dominio, extension = dominio_completo.rsplit('.', 1)
    
    # Crear y devolver el diccionario con la información
    return {
        "nombre_usuario": nombre_usuario,
        "dominio": dominio,
        "extension": extension
    }
# Ejemplos de uso
if __name__ == "__main__":
    print(extraer_info("usuario@ejemplo.com"))
    print(extraer_info("nombre.apellido@subdominio.dominio.org"))
    print(extraer_info("correo_sin_arroba.com"))
    print(extraer_info("usuario@dominiosinpunto"))