precios = [10, 250, 30, 150, 80, 300]

contador = 0
print("Precios superiores a 100€:")

for precio in precios:
    if precio > 100:
        print("- " + str(precio) + " €")
        contador += 1

print("Número de productos que cumplen la condición: " + str(contador))