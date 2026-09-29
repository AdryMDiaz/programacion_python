# Ejercicio de comprehensions con listas
# Lista original de palabras
palabras = ["python", "programación", "lista", "comprehension", "for", "if", "else", "diccionario"]
# Utilizando list comprehension para filtrar palabras con más de 4 letras
# y convertirlas a mayúsculas
resultado = [palabra.upper() for palabra in palabras if len(palabra) > 4]
# Mostrar el resultado
print("Lista original:", palabras)
print("Resultado:", resultado)