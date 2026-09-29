#!/usr/bin/env python3
import os
def listar_archivos_por_tamano():
    # Obtener la lista de todos los elementos en el directorio actual
    elementos = os.listdir('.')
    
    # Lista para almacenar tuplas de (nombre_archivo, tamaño)
    archivos_con_tamano = []
    
    # Filtrar solo los archivos (no directorios) y obtener su tamaño
    for elemento in elementos:
        ruta_completa = os.path.join('.', elemento)
        # Verificar si es un archivo (no directorio)
        if os.path.isfile(ruta_completa):
            # Obtener el tamaño del archivo en bytes
            tamano = os.path.getsize(ruta_completa)
            archivos_con_tamano.append((elemento, tamano))
    
    # Ordenar la lista de archivos por tamaño de forma descendente
    archivos_con_tamano.sort(key=lambda x: x[1], reverse=True)
    
    # Mostrar el nombre y tamaño de cada archivo
    print("Archivos ordenados por tamaño (de mayor a menor):")
    print("-" * 50)
    print(f"{'Nombre':<40} {'Tamaño (bytes)':>10}")
    print("-" * 50)
    
    for nombre, tamano in archivos_con_tamano:
        print(f"{nombre:<40} {tamano:>10}")
if __name__ == "__main__":
    listar_archivos_por_tamano()