clientes = []

opcion = 0

while opcion != 5:
    print("\n--- GESTIÓN DE CLIENTES ---")
    print("1. Añadir cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    
    opcion = int(input("\nSelecciona una opción: "))
    
    match opcion:
        case 1:
            nombre = input("Introduce el nombre: ")
            email = input("Introduce el correo electrónico: ")
            telefono = input("Introduce el teléfono: ")
            
            nuevo_cliente = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }

            # .append() para agregar un elemento al final de una lista en Python
            clientes.append(nuevo_cliente)
            print("Cliente añadido correctamente.")
            
        case 2:
            if len(clientes) == 0:
                print("No hay clientes registrados.")
            else:
                print("\nListado de clientes:")
                for c in clientes:
                    print("- Nombre: " + c["nombre"] + " | Email: " + c["email"] + " | Teléfono: " + c["telefono"])
                    
        case 3:
            email_buscado = input("Introduce el correo electrónico del cliente a buscar: ")
            cliente_encontrado = None #none se pone cuando no se encuentra el cliente
            i = 0
            
            while i < len(clientes) and cliente_encontrado is None:
                if clientes[i]["email"] == email_buscado:
                    cliente_encontrado = clientes[i]
                i += 1
                
            if cliente_encontrado:
                print("\nCliente encontrado:")
                print("Nombre: " + cliente_encontrado["nombre"])
                print("Email: " + cliente_encontrado["email"])
                print("Teléfono: " + cliente_encontrado["telefono"])
            else:
                print("No se encontró ningún cliente con ese correo electrónico.")
                
        case 4:
            email_eliminar = input("Introduce el correo electrónico del cliente a eliminar: ")
            posicion = -1 # se pone -1 porque no hay ninguna posición en la que se encuentre el cliente
            i = 0
            
            while i < len(clientes) and posicion == -1:
                if clientes[i]["email"] == email_eliminar:
                    posicion = i
                i += 1
                
            if posicion != -1:
                cliente_borrado = clientes.pop(posicion)
                print("Cliente '" + cliente_borrado["nombre"] + "' eliminado correctamente.")
            else:
                print("No se encontró ningún cliente con ese correo electrónico.")
                
        case 5:
            print("Saliendo de la aplicación...")
            
        case _:
             print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")