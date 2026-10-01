# Partiendo del diccionario del ejercicio anterior
cliente = {
    "nombre": "Ana López",
    "email": "ana@email.com",
    "telefono": "600123456",
    "activo": True
}

# 1. Modifica el teléfono
cliente["telefono"] = "699888777"

# 2. Añade el campo "ciudad"
cliente["ciudad"] = "Sevilla"

# 3. Cambia "activo" a False
cliente["activo"] = False

# 4. Muestra el diccionario completo
print("Diccionario completo: " + str(cliente))