def calcular_precio_final(precio, cantidad):
    return precio * cantidad

compra1 = calcular_precio_final(11, 4)
compra2 = calcular_precio_final(15.43, 2)
compra3 = calcular_precio_final(5, 15)

print("Compra 1:", compra1)
print("Compra 2:", compra2)
print("Compra 3:", compra3)

total_compra = calcular_precio_final(15, 4)
print(total_compra)