import numpy as np
# Datos de temperaturas diarias para tres ciudades durante un mes
temperaturas = np.array([
    [25, 28, 30, 32, 29, 27, 26, 25, 24, 28, 31, 30, 29, 28, 27, 29, 30, 31, 32, 33, 34, 31, 29, 28, 27, 26, 25, 24, 25, 26],  # Ciudad A
    [18, 17, 19, 20, 21, 20, 19, 18, 17, 16, 15, 16, 17, 18, 19, 20, 21, 22, 21, 20, 19, 18, 17, 16, 15, 14, 15, 16, 17, 18],  # Ciudad B
    [31, 32, 33, 34, 35, 36, 35, 34, 33, 32, 31, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 38, 36, 34, 32, 30, 31, 32, 33]   # Ciudad C
])
# Nombres de las ciudades para mostrar resultados
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
print("Análisis de temperaturas diarias durante un mes en tres ciudades\n")
# 1. Calcular la temperatura media para cada ciudad
medias = np.mean(temperaturas, axis=1)
print("1. Temperatura media para cada ciudad:")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}: {medias[i]:.2f}°C")
# 2. Identificar la temperatura máxima y mínima registrada en cada ciudad
maximas = np.max(temperaturas, axis=1)
minimas = np.min(temperaturas, axis=1)
print("\n2. Temperaturas máximas y mínimas:")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}: Máxima = {maximas[i]}°C, Mínima = {minimas[i]}°C")
# 3. Calcular la mediana de temperaturas para cada ciudad
medianas = np.median(temperaturas, axis=1)
print("\n3. Mediana de temperaturas:")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}: {medianas[i]}°C")
# 4. Determinar el rango intercuartílico (IQR) de temperaturas para cada ciudad
q1 = np.percentile(temperaturas, 25, axis=1)
q3 = np.percentile(temperaturas, 75, axis=1)
iqr = q3 - q1
print("\n4. Rango intercuartílico (IQR) de temperaturas:")
for i, ciudad in enumerate(ciudades):
    print(f"{ciudad}: Q1 = {q1[i]}°C, Q3 = {q3[i]}°C, IQR = {iqr[i]}°C")
# 5. Identificar los días con temperaturas atípicas (outliers) en cada ciudad
print("\n5. Días con temperaturas atípicas (outliers):")
for i, ciudad in enumerate(ciudades):
    limite_inferior = q1[i] - 1.5 * iqr[i]
    limite_superior = q3[i] + 1.5 * iqr[i]
    
    # Encontrar los índices de los outliers (días)
    outliers_indices = np.where((temperaturas[i] < limite_inferior) | (temperaturas[i] > limite_superior))[0]
    
    # Obtener los valores de los outliers
    outliers_valores = temperaturas[i][outliers_indices]
    
    print(f"{ciudad}:")
    if len(outliers_indices) > 0:
        print(f"  Límites para outliers: [{limite_inferior:.2f}, {limite_superior:.2f}]")
        for idx, valor in zip(outliers_indices, outliers_valores):
            print(f"  Día {idx+1}: {valor}°C")
    else:
        print(f"  No se encontraron outliers (límites: [{limite_inferior:.2f}, {limite_superior:.2f}])")