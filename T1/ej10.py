nombre_raw = input("Introduce un nombre (puede incluir espacios al inicio o final): ")

# 1. Eliminar espacios
nombre_sin_espacios = nombre_raw.strip()

# 2. Convertir a minúsculas
nombre_minusculas = nombre_sin_espacios.lower()

# 3. Convertir a mayúsculas
nombre_mayusculas = nombre_sin_espacios.upper()

# 4. Longitud del nombre limpio
longitud = len(nombre_sin_espacios)

# Mostrar resultados
print(f"\nOriginal: '{nombre_raw}'")
print(f"Sin espacios: '{nombre_sin_espacios}'")
print(f"Minúsculas: {nombre_minusculas}")
print(f"Mayúsculas: {nombre_mayusculas}")
print(f"Longitud (sin espacios extra): {longitud} caracteres")