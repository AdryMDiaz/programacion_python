import numpy as np
# Crear un array NumPy tridimensional de tamaño 4x3x2 con valores aleatorios enteros entre 1 y 100
array_3d = np.random.randint(1, 101, size=(4, 3, 2))
# Mostrar el array generado
print("Array generado:")
print(array_3d)
print("\n")
# 1. Mostrar la forma (shape) del array
print("1. Forma (shape) del array:", array_3d.shape)
# 2. Mostrar el número de dimensiones (ndim) del array
print("2. Número de dimensiones (ndim) del array:", array_3d.ndim)
# 3. Mostrar el número total de elementos (size) del array
print("3. Número total de elementos (size) del array:", array_3d.size)
# 4. Mostrar el tipo de datos (dtype) del array
print("4. Tipo de datos (dtype) del array:", array_3d.dtype)
# 5. Mostrar el tamaño en bytes de cada elemento (itemsize) del array
print("5. Tamaño en bytes de cada elemento (itemsize) del array:", array_3d.itemsize)
# 6. Mostrar el tamaño total en bytes (nbytes) del array
print("6. Tamaño total en bytes (nbytes) del array:", array_3d.nbytes)
# Verificar si nbytes es igual a size * itemsize
es_igual = array_3d.nbytes == array_3d.size * array_3d.itemsize
print("\n¿El tamaño total en bytes (nbytes) es igual al producto del número de elementos (size) por el tamaño de cada elemento (itemsize)?")
print(f"array_3d.nbytes ({array_3d.nbytes}) == array_3d.size ({array_3d.size}) * array_3d.itemsize ({array_3d.itemsize}): {es_igual}")