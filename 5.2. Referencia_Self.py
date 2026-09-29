class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def describir(self):
        return f"{self.titulo} escrito por {self.autor} - {self.paginas} páginas"
    
    def es_largo(self):
        return self.paginas > 300
    
    def resumir(self, longitud=50):
        return f"{self.titulo} - Resumen de {longitud} caracteres"
# Pruebas de la clase Libro
if __name__ == "__main__":
    # Creación de instancias
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
    
    # Prueba del método describir
    print(libro1.describir())
    print(libro2.describir())
    
    # Prueba del método es_largo
    print(f"¿{libro1.titulo} es un libro largo? {libro1.es_largo()}")
    print(f"¿{libro2.titulo} es un libro largo? {libro2.es_largo()}")
    
    # Prueba del método resumir con valor predeterminado
    print(libro1.resumir())
    
    # Prueba del método resumir con valor personalizado
    print(libro2.resumir(100))