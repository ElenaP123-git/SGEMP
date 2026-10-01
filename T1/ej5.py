# Entrada de datos (input devuelve texto, por lo que convertimos a float e int)
producto = input("Producto: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

# Cálculo del importe total
total = precio * cantidad

# Resultado
print(f"\nTotal: {total:.2f} €")