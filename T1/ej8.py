primer_precio = float(input("Primer precio: "))
segundo_precio = float(input("Segundo precio: "))

if primer_precio > segundo_precio:
    print("El primer precio es mayor.")
elif segundo_precio > primer_precio:
    print("El segundo precio es mayor.")
else:
    print("Ambos precios son iguales.")