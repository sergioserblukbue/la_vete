import os
def limpiarpantalla():
    os.system("cls")
def menu_mascotas():
    while True:
        limpiarpantalla()
        print("gestion de mascotas".center(60," "))
        print("="*60)
        print("1 ingresar mascota")
        print("2 modificar mascota")
        print("3 eliminar mascota")
        print("4 listar mascotas")
        print("5 buscar mascota")
        print("6 regresar al menu anterior")
        op=input("seleccione una opcion: ")
        if op=="1":
            print(" llamar ingresar mascotas")
            input()
            pass
        elif op=="2":
            input()
            pass
        elif op=="3":
            input()
            pass
        elif op=="4":
            input()
            pass
        elif op=="5":
            input()
            pass
        elif op=="6":
            break
        else:
            print("opcion incorrecta!")
            input("presione enter para continuar...")
    return

menu_mascotas()