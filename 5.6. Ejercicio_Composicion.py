class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        """
        Inicializa un objeto Libro con título, autor y año de publicación.
        
        Args:
            titulo (str): El título del libro
            autor (str): El autor del libro
            anio_publicacion (int): El año de publicación del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    
    def __str__(self):
        """
        Devuelve una representación en cadena del libro.
        
        Returns:
            str: Representación del libro
        """
        return f'"{self.titulo}" por {self.autor} ({self.anio_publicacion})'

class Biblioteca:
    def __init__(self):
        """
        Inicializa una biblioteca con una colección vacía de libros.
        """
        self.libros = []
    
    def agregar_libro(self, libro):
        """
        Agrega un libro a la colección de la biblioteca.
        
        Args:
            libro (Libro): El libro a agregar
        """
        if isinstance(libro, Libro):
            self.libros.append(libro)
        else:
            raise TypeError("El objeto debe ser una instancia de la clase Libro")
    
    def buscar_por_titulo(self, cadena_busqueda):
        """
        Busca libros que contengan la cadena de búsqueda en su título.
        
        Args:
            cadena_busqueda (str): La cadena a buscar en los títulos
            
        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        return [libro for libro in self.libros if cadena_busqueda.lower() in libro.titulo.lower()]
    
    def contar_por_autor(self, autor):
        """
        Cuenta cuántos libros hay de un autor específico.
        
        Args:
            autor (str): El autor a buscar
            
        Returns:
            int: Número de libros del autor especificado
        """
        return sum(1 for libro in self.libros if libro.autor.lower() == autor.lower())
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la biblioteca.
        
        Returns:
            str: Representación de la biblioteca
        """
        if not self.libros:
            return "La biblioteca está vacía."
        
        resultado = f"Biblioteca con {len(self.libros)} libros:\n"
        for libro in self.libros:
            resultado += f"- {libro}\n"
        return resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una biblioteca
    mi_biblioteca = Biblioteca()
    
    # Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)
    libro3 = Libro("1984", "George Orwell", 1949)
    libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    
    # Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)
    mi_biblioteca.agregar_libro(libro3)
    mi_biblioteca.agregar_libro(libro4)
    
    # Mostrar todos los libros
    print(mi_biblioteca)
    
    # Buscar libros por título
    print("\nBúsqueda de libros que contienen 'amor':")
    libros_encontrados = mi_biblioteca.buscar_por_titulo("amor")
    for libro in libros_encontrados:
        print(f"- {libro}")
    
    # Contar libros por autor
    autor = "Gabriel García Márquez"
    cantidad = mi_biblioteca.contar_por_autor(autor)
    print(f"\nHay {cantidad} libros de {autor} en la biblioteca.")