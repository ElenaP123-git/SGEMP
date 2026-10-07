class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def valor_stock(self):
        return self.precio * self.existencias

p = Producto("P001", "Monitor", 200, 5)

print("Producto: " + p.nombre)
print("Precio: " + str(p.precio) + " €")
print("Stock: " + str(p.existencias))
print("\nValor del stock: " + str(p.valor_stock()) + " €")