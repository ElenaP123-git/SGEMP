class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def reponer(self, cantidad):
        if cantidad > 0:
            self.existencias += cantidad

    def mostrar_info(self):
        print(self.codigo + " - " + self.nombre + " - " + str(self.precio) + " € - Stock: " + str(self.existencias))

p = Producto("P001", "Monitor", 199.99, 5)
print("Stock inicial: " + str(p.existencias))

reposicion = 3
p.reponer(reposicion)
print("Reposición: " + str(reposicion))
print("Stock final: " + str(p.existencias))