clientes = [
    {
        "nombre": "Ana",
        "email": "ana@email.com",
        "ciudad": "Sevilla"
    },
    {
        "nombre": "Luis",
        "email": "luis@email.com",
        "ciudad": "Córdoba"
    },
    {
        "nombre": "Marta",
        "email": "marta@email.com",
        "ciudad": "Granada"
    }
]

# Recorrer la lista y mostrar los datos de cada cliente
for c in clientes:
    print("Nombre: " + c["nombre"] + ", Email: " + c["email"] + ", Ciudad: " + c["ciudad"])