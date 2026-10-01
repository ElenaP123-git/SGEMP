# Entrada de datos
nombre = input("Nombre: ")
apellido = input("Apellido: ")

# Generación del identificador: primera letra del nombre + apellido completo
identificador = nombre[0] + apellido

# Convertir todo a minúsculas
identificador = identificador.lower()

# Resultado
print(f"\nUsuario generado: {identificador}")