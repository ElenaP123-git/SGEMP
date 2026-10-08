from Bloque20.ej52 import Cliente

class ClienteVIP(Cliente):
    def __init__(self, nombre, email, numero_cliente, descuento):
        super().__init__(nombre, email, numero_cliente)
        self.descuento = descuento  

    def calcular_precio(self, precio):
        precio_final = precio * (1 - self.descuento)
        return precio_final


# Ejemplo de uso
vip1 = ClienteVIP("Javier Garcia", "jav.vip@email.com", 202, 0.15)

print("--- Datos del Cliente VIP ---")
vip1.mostrar_datos()
print("Descuento: " + str(vip1.descuento * 100) + "%")

precio_original = 100.0
precio_con_descuento = vip1.calcular_precio(precio_original)

print("\nPrecio original: " + str(precio_original) + " €")
print("Precio con descuento VIP: " + str(precio_con_descuento) + " €")