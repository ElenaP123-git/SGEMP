def calcular_total(ventas):
    total = 0
    for venta in ventas:
        total += venta
    return total

mis_ventas = [150, 80.5, 200, 45]
print("Total de ventas:", calcular_total(mis_ventas)) # Devuelve 475.5