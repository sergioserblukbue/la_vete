import os
from ingresarMascota import ingresarMascota
def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")
    return
def menuPrincipal():
    limpiarPantalla()
    print("sistema de gestion veterinaria".center(60, " "))
    print("="*60)
    print("1 gestion de mascotas")
    print("2 gestion de productos")
    print("3 salir")
    op=input("seleccione una opcion: ")
    return op
def menu_mascotas():
    while True:
        limpiarPantalla()
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
            ingresarMascota(listMascotas)
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
#empieza el programa
listMascotas=[]
while True:
    op=menuPrincipal()
    if op == "1":
        menu_mascotas()
    elif op == "2":
        #menu_productos()
        pass
    elif op == "3":
        break
    else:
        print("opcion incorrecta!")
        input("presione enter para continuar...")
