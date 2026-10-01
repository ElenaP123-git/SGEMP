precio_original = float(input("Precio original: "))
descuento_porcentaje = float(input("Porcentaje de descuento: "))

# Cálculos
importe_descontado = precio_original * (descuento_porcentaje / 100)
precio_final = precio_original - importe_descontado

# Mostrar resultados
print(f"\nImporte descontado: {importe_descontado:.2f} €")
print(f"Precio final: {precio_final:.2f} €")