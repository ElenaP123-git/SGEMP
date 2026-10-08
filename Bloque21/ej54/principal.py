from calculos import calcular_iva, calcular_descuento, calcular_total

precio_base = 100.0
desc = 0.10  # 10% de descuento

iva_calculado = calcular_iva(precio_base)
descuento_calculado = calcular_descuento(precio_base, desc)
precio_final = calcular_total(precio_base, desc)

print("Precio base: " + str(precio_base) + " €")
print("Descuento (10%): " + str(descuento_calculado) + " €")
print("IVA (21%): " + str(iva_calculado) + " €")
print("Total a pagar: " + str(precio_final) + " €")