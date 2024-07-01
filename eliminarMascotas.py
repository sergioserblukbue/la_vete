from persistencia import guardarDatos
def eliminarMascota(lista):
    print("Eliminar Mascotas".center(60," "))
    print("="*60)
    dni=input("ingrese el dni del propietario: ")
    for mascota in lista:
        if mascota["dniPropietario"]==dni:
            print(f"nombre: {mascota['nombre']} Tipo: {mascota['tipo']}")
    nombre=input("ingrese el nombre de la mascota a eliminar: ")
    for i in range(len(lista)):
        if lista[i]["dniPropietario"]==dni and lista[i]["nombre"]==nombre:
            lista.pop(i)
            #llamo a guardar
            guardarDatos(lista)
            print("Se eliminaron los datos correctamente")
            return
    print("no se encontro la mascota!")
    return
    