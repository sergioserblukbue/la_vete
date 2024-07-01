import os
def limpiarpantalla():
    os.system("cls")
    return
def menuMascotas():
    while True:
        limpiarpantalla()
        print("Menu de gestion de Mascotas".center(60," "))
        print("="*60)
        print("1 ingreso de mascotas")
        print("2 para modificar datos de mascotas")
        print("3 eliminar registro de mascotas")
        print("4 agregar procedimientos")
        print("5 para listar datos")
        print("6 para salir")
        op = input("seleccione una opcion: ")
        if op == "1":
            pass
        elif op == "2":
            pass
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "5":
            pass
        elif op == "6":
            break
        else:
            print("opcion incorrecta!")
            input("prsione enter para continuar...")
    return

menuMascotas()