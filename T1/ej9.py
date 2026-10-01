nombre = input("Nombre: ")
apellidos = input("Apellidos: ")
email = input("Correo electrónico: ")
ciudad = input("Ciudad: ")

# Construcción de la ficha usando f-string
print("\n----- CLIENTE -----\n")
print(f"Nombre: {nombre} {apellidos}")
print(f"Email: {email}")
print(f"Ciudad: {ciudad}")