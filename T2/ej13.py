productos = ["Teclado", "Ratón", "Monitor"]

# 1. Añadir "Webcam"
productos.append("Webcam")

# 2. Añadir "Altavoces"
productos.append("Altavoces")

# 3. Eliminar "Ratón"
productos.remove("Ratón")

# 4. Cambiar "Monitor" por "Monitor 27 pulgadas" (está en la posición 1 tras borrar "Ratón")
indice_monitor = productos.index("Monitor")
productos[indice_monitor] = "Monitor 27 pulgadas"

# 5. Mostrar la lista final
print("Lista final:", productos)