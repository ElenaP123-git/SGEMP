def calcular_iva(precio, porcentaje_iva=0.21):
    return precio * porcentaje_iva


def calcular_descuento(precio, porcentaje_descuento):
    return precio * porcentaje_descuento


def calcular_total(precio, porcentaje_descuento=0.0, porcentaje_iva=0.21):
    descuento = calcular_descuento(precio, porcentaje_descuento)
    precio_con_descuento = precio - descuento
    iva = calcular_iva(precio_con_descuento, porcentaje_iva)
    return precio_con_descuento + iva