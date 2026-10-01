clientes = [
    {"nombre": "Ana", "email": "ana@email.com", "ciudad": "Sevilla"},
    {"nombre": "Luis", "email": "luis@email.com", "ciudad": "Córdoba"},
    {"nombre": "Marta", "email": "marta@email.com", "ciudad": "Granada"}
]

email_buscado = input("Introduce un correo electrónico: ")

cliente_encontrado = None
i = 0

# La condición controla tanto los límites de la lista como el éxito de la búsqueda
while i < len(clientes) and cliente_encontrado is None:
    if clientes[i]["email"] == email_buscado:
        cliente_encontrado = clientes[i]
    i += 1

if cliente_encontrado:
    print("\nCliente encontrado:")
    print("Nombre: " + cliente_encontrado["nombre"])
    print("Ciudad: " + cliente_encontrado["ciudad"])
else:
    print("\nNo existe ningún cliente con ese email.")