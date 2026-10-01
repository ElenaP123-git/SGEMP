opcion = 0

while opcion != 3:
    print("\n--- MENÚ ---")
    print("1. Mostrar mensaje")
    print("2. Mostrar fecha ficticia")
    print("3. Salir")
    
    opcion = int(input("Selecciona una opción: "))
    
    if opcion == 1:
        print("¡Hola! Has seleccionado mostrar mensaje.")
        print("Presiona Enter para continuar...")
        input()
    elif opcion == 2:
        print("Fecha ficticia: 01/01/2030")
        print("Presiona Enter para continuar...")
        input()
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
        print("Presiona Enter para continuar...")
        input()