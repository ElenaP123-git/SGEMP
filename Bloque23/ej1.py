class Producto:
    def __init__(self, codigo, nombre, precio, existencias):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias

    def mostrar_info(self):
        print("Código: " + self.codigo + " | Nombre: " + self.nombre + " | Precio: " + str(self.precio) + " € | Stock: " + str(self.existencias))

    def reponer(self, cantidad):
        if cantidad > 0:
            self.existencias += cantidad
            print("Stock repuesto correctamente. Nuevo stock: " + str(self.existencias))
        else:
            print("Error: La cantidad a reponer debe ser mayor que 0.")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Error: La cantidad a vender debe ser mayor que 0.")
        elif cantidad <= self.existencias:
            self.existencias -= cantidad
            print("Venta realizada correctamente. Stock restante: " + str(self.existencias))
        else:
            print("Error: Stock insuficiente para realizar la venta.")

    def valor_stock(self):
        return self.precio * self.existencias


# Lista para almacenar los objetos de tipo Producto
productos = []

opcion = 0

while opcion != 7:
    print("\n--- GESTIÓN DE PRODUCTOS ---")
    print("1. Añadir producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Vender producto")
    print("5. Reponer producto")
    print("6. Mostrar valor total del inventario")
    print("7. Salir")
    
    opcion = int(input("\nSelecciona una opción: "))
    
    match opcion:
        case 1:
            codigo = input("Introduce el código del producto: ")
            nombre = input("Introduce el nombre del producto: ")
            precio = float(input("Introduce el precio: "))
            existencias = int(input("Introduce las existencias iniciales: "))
            
            nuevo_producto = Producto(codigo, nombre, precio, existencias)
            productos.append(nuevo_producto)
            print("Producto registrado :)")
            
        case 2:
            if len(productos) == 0:
                print("No hay productos en el inventario.")
            else:
                print("\nListado de productos:")
                for p in productos:
                    p.mostrar_info()
                    
        case 3:
            codigo_buscado = input("Introduce el código del producto a buscar: ")
            producto_encontrado = None
            i = 0
            
            while i < len(productos) and producto_encontrado is None:
                if productos[i].codigo == codigo_buscado:
                    producto_encontrado = productos[i]
                i += 1
                
            if producto_encontrado:
                print("\nProducto encontrado:")
                producto_encontrado.mostrar_info()
            else:
                print("No se encontró ningún producto con ese código.")
                
        case 4:
            codigo_vender = input("Introduce el código del producto a vender: ")
            producto_vender = None
            i = 0
            
            while i < len(productos) and producto_vender is None:
                if productos[i].codigo == codigo_vender:
                    producto_vender = productos[i]
                i += 1
                
            if producto_vender:
                cant = int(input("Introduce la cantidad a vender: "))
                producto_vender.vender(cant)
            else:
                print("No se encontró ningún producto con ese código.")
                
        case 5:
            codigo_reponer = input("Introduce el código del producto a reponer: ")
            producto_reponer = None
            i = 0
            
            while i < len(productos) and producto_reponer is None:
                if productos[i].codigo == codigo_reponer:
                    producto_reponer = productos[i]
                i += 1
                
            if producto_reponer:
                cant = int(input("Introduce la cantidad a reponer: "))
                producto_reponer.reponer(cant)
            else:
                print("No se encontró ningún producto con ese código.")
                
        case 6:
            total_inventario = 0.0
            for p in productos:
                total_inventario += p.valor_stock()
                
            print("\nValor total del inventario: " + str(total_inventario) + " €")
            
        case 7:
            print("Saliendo de la aplicación...")
            
        case _:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 7.")