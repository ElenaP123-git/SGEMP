class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class Cliente(Persona):
    def __init__(self, nombre, email, numero_cliente):
        # Constructor de la clase base (Persona)
        super().__init__(nombre, email)
        self.numero_cliente = numero_cliente

    def mostrar_datos(self):
        print("Número de cliente: " + str(self.numero_cliente))
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)


# Crea un cliente y muestra todos sus datos
cliente1 = Cliente("Elena Pablo", "heren@email.com", 101)
cliente1.mostrar_datos()