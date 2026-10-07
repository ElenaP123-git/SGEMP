def producto_mas_caro(productos):
    mas_caro = productos[0]
    for producto in productos:
        if producto["precio"] > mas_caro["precio"]:
            mas_caro = producto
            
    return mas_caro

productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Ratón", "precio": 15}
]

print("El producto más caro es:", producto_mas_caro(productos))