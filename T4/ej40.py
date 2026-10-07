# si descuento=0, no se aplica descuento si no se añade uno

def aplicar_descuento(precio, descuento=0): 
    return precio * (1 - descuento / 100)

precio_sin_descuento = aplicar_descuento(100)
descuento_diez = aplicar_descuento(100, 10)
descuento_veinte = aplicar_descuento(250, 20)