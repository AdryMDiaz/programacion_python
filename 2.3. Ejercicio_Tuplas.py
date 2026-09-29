# Ejercicio de tuplas en Python
# 1. Crear la tupla contacto con la información requerida
contacto = ("Ana García", "ana@ejemplo.com", "555-1234")
# 2. Desempaquetar la tupla en tres variables
nombre, email, telefono = contacto
# 3. Imprimir cada variable en líneas separadas
print(nombre)
print(email)
print(telefono)
# 4. Crear una nueva tupla con los elementos originales más la ciudad "Madrid"
contacto_completo = contacto + ("Madrid",)
# Mostrar la nueva tupla para verificar
print("\nTupla contacto_completo:")
print(contacto_completo)