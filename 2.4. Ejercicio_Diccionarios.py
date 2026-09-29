# Creación del diccionario de contactos con tres personas
contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona2": {"nombre": "Carlos", "telefono": "987654321", "email": "carlos@ejemplo.com"},
    "persona3": {"nombre": "Elena", "telefono": "555123456", "email": "elena@ejemplo.com"}
}
# 1. Mostrar el correo electrónico de la segunda persona
print("Correo electrónico de la segunda persona:")
print(contactos["persona2"]["email"])
print()
# 2. Añadir un nuevo contacto
contactos["persona4"] = {"nombre": "Miguel", "telefono": "666777888", "email": "miguel@ejemplo.com"}
print("Contacto añadido correctamente.")
print()
# 3. Modificar el número de teléfono de la primera persona
contactos["persona1"]["telefono"] = "111222333"
print("Teléfono de Ana modificado a:", contactos["persona1"]["telefono"])
print()
# 4. Mostrar los nombres de todos los contactos usando un bucle
print("Lista de todos los contactos:")
for clave, datos in contactos.items():
    print(f"- {datos['nombre']}")