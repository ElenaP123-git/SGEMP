password_correcta = "python123"

password_introducida = input("Introduce la contraseña: ")

while password_introducida != password_correcta:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    password_introducida = input("Introduce la contraseña: ")

print("Acceso permitido")