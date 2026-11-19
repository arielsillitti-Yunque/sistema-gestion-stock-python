from colorama import Fore, Back, Style
def lista_productos(identificador,nombre,categoria,descripcion,cantidad,precio):
    print("---------")
    print("🎁")
    print(Fore.RED + "ID:", identificador)
    print(Fore.RED +"Producto:", nombre)
    print(Fore.RED + "Categoria:", categoria)
    print(Fore.RED + "descripcion",descripcion)
    print(Fore.RED + "cantidad",cantidad)
    print(f"${precio}")
    print("---------")
    print("🎲")
    Style.RESET_ALL

def ingreso(nombreDelCampo):
    campo= input(f"{nombreDelCampo}: ").title().strip()
    while  campo=="":
        print(f"{nombreDelCampo},no puede estar vacio")
        campo= input(f"{nombreDelCampo}: ").title().strip()
    return campo   
    
    
stock = [["001","fideos","Almacen","fideos luchetti","500",1500],["002","Cacao","Almacen","cacao toddy","300",1300],["003","pure de tomate","almacen","pure noel","600",1200],["004","yerba","almacen","yerba rosamonte","200",2500]]

print(Back.BLUE +"-----Bienvenidos a mi sistema de gestion Colo records!-----")
print(Style.RESET_ALL)
opcion = ""

while opcion != "7":
    print("-------------------")
    print(Fore.YELLOW +"1. Añadir producto")
    print(Fore.YELLOW +"2. Visualizar productos")
    print(Fore.YELLOW +"3. Buscar producto")
    print(Fore.YELLOW +"4. actualizar producto")
    print(Fore.YELLOW +"5. Eliminar producto")
    print(Fore.YELLOW +"6. Reporte de stock")
    print(Fore.YELLOW +"7. Salir")
    print(Style.RESET_ALL)
    
    opcion = input("Que queres hacer? 1/2/3/4/5/6/7: ").strip()
    
    match opcion:
        case "1":
            print("-------------------")
            print(Fore.BLUE + "Agregar")
            print("-------------------")
            print(Style.RESET_ALL)
            
            identificador=ingreso("identificador")
            nombre=ingreso("nombre")
            categoria=ingreso("categoria")
            descripcion=ingreso("descripcion")
            cantidad=ingreso("cantidad")
            while True:
               precio =input("Precio del producto: $")
               if not precio.isdigit():
                   print("Error,Solo numeros enteros!")
                   continue
               elif int(precio)<=0:
                  print("El precio no puede ser 0")
                  continue
               break
           
            stock.append([identificador,nombre,categoria,descripcion,cantidad,int(precio)])
            print("Producto agregado!")
            
        case "2":
            print("-------------------")
            print(Fore.BLUE +"Visualizar")
            print("-------------------")
            print(Style.RESET_ALL)

            for producto in stock:
                lista_productos(producto[0],producto[1],producto[2],producto[3],producto[4],producto[5])  
            print(Fore.BLUE + f"Total de productos: {len(stock)}")
                
        case "3":
            print("-------------------")
            print(Fore.BLUE +"Buscar")
            print("-------------------")
            print(Style.RESET_ALL)

            
            busqueda = input("Que producto buscas?: ").strip().lower()
            while busqueda=="":
                print("Tenes que poner algo si o si !")
                busqueda = input("Que producto buscas?: ").strip().lower()
            encontrado = False
            
            for producto in stock:
                
                if busqueda == producto[0].lower() or busqueda == producto[1].lower():
                    encontrado = True
                    print("---------")
                    print("Producto encontrado!")
                   
                    lista_productos(producto[0],producto[1],producto[2],producto[3],producto[4],producto[5])

            if encontrado == False:
                print("Producto no encontrado")
            
        case "4":
            print("-------------------")
            print(Fore.BLUE +"Actualizar producto")
            print("-------------------")
            print(Style.RESET_ALL)

            busqueda = input("Cual es el nombre del producto que queres actualizar?: ").strip().lower()
            
            encontrado = False
            for item in stock:
                if busqueda == item[1].lower() or busqueda == item[0].lower():
                    print(Fore.BLUE +"Producto encontrado!")
                    print(Style.RESET_ALL)
                    lista_productos(item[0], item[1], item[2], item[3], item[4], item[5])
                    encontrado = True
                    print("""
                    1. Nombre
                    2. Categoria
                    3. Descripcion
                    4. Cantidad
                    5. Precio
                    6. Nada
                    """)
                    modificador = input("Que queres actualizar? 1/2/3/4/5/6: ")

                    match modificador:
                        case "1":
                            print("Modificar nombre")
                            item.pop(1)
                            nuevoNombre = ingreso("Nuevo nombre")
                            item.insert(1, nuevoNombre)
                            print("Producto modificado correctamente")
                        case "2":
                            print("Modificar categoria")
                            item.pop(2)
                            nuevaCategoria = ingreso("Nueva categoria")
                            item.insert(2, nuevaCategoria)
                            print("Producto modificado correctamente")
                        case "3":
                            print("Modificar descripcion")
                            item.pop(3)
                            nuevaDescripcion = ingreso("Nueva descripcion")
                            item.insert(3, nuevaDescripcion)
                            print("Producto modificado correctamente")
                        case "4":
                            print("Modificar cantidad")
                            item.pop(4)
                            nuevaCantidad = ingreso("Nueva cantidad")
                            item.insert(4, nuevaCantidad)
                            print("Producto modificado correctamente")
                        case "5":
                            print("Modificar precio")
                            item.pop(5)
                            while True:
                                nuevaPrecio = input("Nuevo precio: ").strip()
                                if not nuevaPrecio.isdigit():
                                    print("Error, solo numeros!")
                                    continue
                                if int(nuevaPrecio) <=0:
                                    print("No puede ser 0")
                                    continue
                                break
                            item.insert(5, int(nuevaPrecio))
                            print("Producto modificado correctamente")
                        case "6":
                            print("Perfecto")
                        case _:
                            print("Opcion no valida")
                    break 
            
            if encontrado == False:
                print("Producto no encontrado")

        case "5":
            print("-------------------")
            print(Fore.CYAN + "Eliminar")
            print("-------------------")
            print(Style.RESET_ALL)
                        
            producto_a_eliminar = input("Que producto queres eliminar?: ").strip().lower()
            while producto_a_eliminar == "":
                print("Tenes que ingresar algo")
                producto_a_eliminar = input("Que producto queres eliminar?: ").strip().lower()

            encontrado = False

            for producto in stock:
                if producto_a_eliminar == producto[0].lower() or producto_a_eliminar == producto[1].lower():
                    encontrado = True
                    print("---------")
                    print("Producto encontrado!")
                    lista_productos(producto[0],producto[1],producto[2],producto[3],producto[4],producto[5])
                    print("")

                    decision = input(f"Estas seguro de querer eliminar {producto[1]} Si/No: ").strip().lower()
                    if decision == "si":
                        stock.remove(producto)
                        print("Listo! Producto eliminado")
                    else:
                        print("No se elimino")
                    break 

            if encontrado == False:
                print("El producto que buscas eliminar, ya no existe")

        case "6":
            print(Fore.BLUE + "Reporte de stock")
            print(Style.RESET_ALL)
            try:
                stockMinimo = int(input("Que consideras poco stock?: "))
                print(f"Productos con stock menor a {stockMinimo}")
                hay_poco = False
                for item in stock:
                    if int(item[4]) < stockMinimo:
                        hay_poco = True
                        lista_productos(item[0],item[1],item[2],item[3],item[4],item[5])
                if not hay_poco:
                    print("No hay productos con tan poco stock")
            except:
                print("Tenes que poner un numero")
            
        case "7":
            print("-------------------")
            print(Fore.RED + "----Gracias por usar mi sistema Colo records!-----")
            print(Style.RESET_ALL)
            print("-------------------")
        case _:
            print("-------------------")
            print("Opcion no valida")
            print("-------------------")
