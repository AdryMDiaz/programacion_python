import random
def generar_usuarios(cantidad):
    """
    Genera datos aleatorios para un conjunto de usuarios.
    
    Args:
        cantidad (int): Número de usuarios a generar
        
    Returns:
        list: Lista de diccionarios, donde cada diccionario representa un usuario
    """
    # Lista de posibles nombres
    nombres = ['Ana', 'Carlos', 'Elena', 'Miguel', 'Laura', 'Pablo', 'Sofía', 'Javier']
    
    # Lista para almacenar los usuarios generados
    usuarios = []
    
    # Generar datos para cada usuario
    for i in range(1, cantidad + 1):
        # Generar datos aleatorios
        nombre = random.choice(nombres)
        edad = random.randint(18, 65)
        puntuacion = round(random.uniform(0.0, 10.0), 1)
        
        # Crear diccionario del usuario
        usuario = {
            'id': i,
            'nombre': nombre,
            'edad': edad,
            'puntuacion': puntuacion
        }
        
        # Añadir usuario a la lista
        usuarios.append(usuario)
    
    return usuarios
# Ejemplo de uso
if __name__ == "__main__":
    usuarios = generar_usuarios(3)
    print(usuarios)