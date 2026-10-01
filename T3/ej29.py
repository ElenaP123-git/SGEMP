importe = float(input("Introduce la importación de la compra: "))
es_vip_input = input("¿El cliente es VIP? (si/no): ")
es_vip = es_vip_input == "si"

if es_vip:
    descuento = 0.10
elif importe > 100:
    descuento = 0.05
else:
    descuento = 0.0

importe_final = importe * (1 - descuento)

print("Importación final: " + str(importe_final) + " €")