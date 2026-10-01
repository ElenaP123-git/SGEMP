# Crear la tupla
producto = ("P001", "Teclado", 21)

# Mostrar cada elemento
print("Código: " + producto[0])
print("Nombre: " + producto[1])
print("Tipo de IVA: " + str(producto[2]))

# Intentar modificar el código del producto
try:
    producto[0] = "P002"
except TypeError as e:
    print("\nError al intentar modificar: " + str(e))