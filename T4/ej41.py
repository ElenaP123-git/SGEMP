def buscar_producto(productos, nombre):
    return nombre in productos

lista_productos = ["Teclado", "Monitor", "Ratón"]

print(buscar_producto(lista_productos, "Monitor"))  # Devuelve True
print(buscar_producto(lista_productos, "Impresora")) # Devuelve False