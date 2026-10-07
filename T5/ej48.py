class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def mostrar_info(self):
        print(self.codigo + " - " + self.nombre + " - " + str(self.precio) + " € - Stock: " + str(self.existencias))

producto1 = Producto("P001", "Monitor", 199.99, 8)
producto1.mostrar_info()