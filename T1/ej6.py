precio = float(input("Introduce el precio del producto: "))
cantidad = int(input("Introduce la cantidad: "))

# Cálculos
subtotal = precio * cantidad
iva = subtotal * 0.21
total = subtotal + iva

# Mostrar resultados
print(f"\nSubtotal: {subtotal:.2f} €")
print(f"IVA: {iva:.2f} €")
print(f"Total: {total:.2f} €")