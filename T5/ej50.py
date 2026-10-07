class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def vender(self, cantidad):
        if cantidad > 0 and cantidad <= self.existencias:
            self.existencias -= cantidad
            print("Venta completada.")
        elif cantidad <= 0:
            print("Error: La cantidad a vender debe ser mayor que 0.")
        else:
            print("Error: Stock insuficiente para realizar la venta.")

p = Producto("P001", "Monitor", 200, 5)
p.vender(3)
print("Stock restante: " + str(p.existencias))