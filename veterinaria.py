import os
from modificarMascotas import modificarMascotas
from buscarMascotas import buscarMascotas
from listarMascotas import listarMascotas 
from eliminarMascotas import eliminarMascota
from persistencia import *
from ingresarMascotas import ingresarMascota
def limpiarPantalla():
    os.system("cls" if os.name=="nt" else "clear" )
    return
def menuPrincipal():
    limpiarPantalla()
    print("sistema de gestion veterinaria".center(60," "))
    print("="*60)
    print("1 gestion de mascotas")
    print("2 gestion de productos")
    print("3 para salir")
    op = input("seleccione una opcion: ")
    return op
def menuMascotas():
    while True:
        limpiarPantalla()
        print("gestion de mascotas".center(60," "))
        print("="*60)
        print("1 ingresar mascotas")
        print("2 modificar datos de mascotas")
        print("3 eliminar datos mascota")
        print("4 listar mascotas")
        print("5 buscar Mascota")
        print("6 regresar al menu principal")
        op = input("seleccione una opcion: ")
        if op =="1":
            ingresarMascota(listaMascotas)
        elif op =="2":
            modificarMascotas(listaMascotas)
            input("enter para continuar....")
        elif op =="3":
            eliminarMascota(listaMascotas)
            input("enter para continuar....")
        elif op =="4":
            listarMascotas(listaMascotas)
            input("presione enter para continuar...")
        elif op =="5":
            buscarMascotas(listaMascotas)
            input("presione enter para continuar...")
        elif op =="6":
            break
        else:
            print("opcion incorrecta!")
            input("presione enter para continuar...")
#aca inicia el programa
listaMascotas=cargarDatos()
while True:
    op = menuPrincipal()
    if op=="1":
        menuMascotas()
    elif op=="2":
        pass
    elif op=="3":
        break
    else:
        print("opcion incorrecta!")
        input("enter para continuar...")
print("gracias por usar el programa!")