class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def mostrar_datos(self):
        print("Nombre: " + self.nombre)
        print("Correo electrónico: " + self.email)
        print("Teléfono: " + self.telefono)

cliente1 = Cliente("Elena Pablo", "helen@email.com", "678593457")
cliente2 = Cliente("Javier García", "javi@email.com", "655987654")

print("Cliente 1")
cliente1.mostrar_datos()

print("Datos Cliente 2")
cliente2.mostrar_datos()