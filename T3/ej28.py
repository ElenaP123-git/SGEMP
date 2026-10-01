stock = int(input("Introduce el stock disponible: "))
cantidad = int(input("Introduce la cantidad que quieres comprar: "))

if cantidad <= stock:
    print("Venta posible")
else:
    print("Stock insuficiente")