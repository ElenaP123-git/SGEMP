clientes = [
    {"nombre": "Ana", "email": "ana@email.com", "ciudad": "Sevilla"},
    {"nombre": "Luis", "email": "luis@email.com", "ciudad": "Córdoba"},
    {"nombre": "Pedro", "email": "pedro@email.com", "ciudad": "Sevilla"},
    {"nombre": "Maria", "email": "maria@email.com", "ciudad": "Sevilla"}
]

ciudad_buscada = input("Ciudad: ")

contador = 0
for c in clientes:
    if c["ciudad"].lower() == ciudad_buscada.lower():
        contador += 1

print("Número de clientes de " + ciudad_buscada + ": " + str(contador))