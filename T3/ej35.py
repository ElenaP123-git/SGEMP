numero_ventas = 0
total_vendido = 0.0

venta = float(input("Introduce el importe de la venta (0 para terminar): "))

while venta != 0:
    numero_ventas += 1
    total_vendido += venta
    venta = float(input("Introduce el importe de la venta (0 para terminar): "))

print("\nNúmero de ventas: " + str(numero_ventas))
print("Total vendido: " + str(total_vendido) + " €")