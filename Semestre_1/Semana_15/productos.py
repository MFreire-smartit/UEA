# Tarea: Colecciones de datos en Python
# Programa: Registro de productos de una tienda
# Estructura utilizada: Diccionario

# Diccionario donde se almacenarán los productos
productos = {}

while True:
    print("\n===== REGISTRO DE PRODUCTOS =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar un producto
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: "))

        productos[nombre] = precio
        print("Producto agregado correctamente.")

    # Mostrar todos los productos
    elif opcion == "2":
        if len(productos) == 0:
            print("No existen productos registrados.")
        else:
            print("\n--- PRODUCTOS REGISTRADOS ---")

            for nombre, precio in productos.items():
                print(nombre, "- $", precio)

    # Buscar un producto
    elif opcion == "3":
        nombre = input("Ingrese el producto que desea buscar: ")

        if nombre in productos:
            print("Producto encontrado.")
            print(nombre, "- $", productos[nombre])
        else:
            print("El producto no está registrado.")

    # Eliminar un producto
    elif opcion == "4":
        nombre = input("Ingrese el producto que desea eliminar: ")

        if nombre in productos:
            del productos[nombre]
            print("Producto eliminado correctamente.")
        else:
            print("El producto no está registrado.")

    # Salir del programa
    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta. Intente nuevamente.")