import os 
from ingresoMascotas import ingresoMascotas
def limpiarPantalla():
    os.system("cls" if os.name=="nt" else "clear")
    return
def menuPrincipal():
    print("sistema de gestion veterinaria".center(60," "))
    print("="*60)
    print("1 para gestion de mascotas")
    print("2 para gestion de productos")
    print("3 para salir")
    op = input("seleccione una opcion: ")
    return op
def menuMascotas():
    #coding by Roberto Fiori
    while True:
        limpiarPantalla()
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
            ingresoMascotas(listaMascotas)
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
#programa principal
listaMascotas=[]
while True:
    limpiarPantalla()
    op=menuPrincipal()
    if op == "1":
        menuMascotas()
    elif op =="2":
        pass
    elif op =="3":
        resp=input("realmente quiere salir del sistema? s/n")
        if resp.lower()=="s":
            break
    else:
        print("opcion no contemplada!")
        input("presione enter para continuar...")
print("gracias por usar el programa!")