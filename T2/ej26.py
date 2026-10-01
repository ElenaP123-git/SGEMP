clientes_tienda_a = {"Ana", "Luis", "Marta", "Carlos"}
clientes_tienda_b = {"Marta", "Carlos", "Lucía"}

# 1. Todos los clientes (Unión)
todos = clientes_tienda_a | clientes_tienda_b
print("Todos los clientes: " + str(todos))

# 2. Clientes que están en ambas tiendas (Intersección)
ambas = clientes_tienda_a & clientes_tienda_b
print("Clientes en ambas tiendas: " + str(ambas))

# 3. Clientes que están únicamente en la tienda A (Diferencia)
solo_a = clientes_tienda_a - clientes_tienda_b
print("Clientes únicamente en la tienda A: " + str(solo_a))