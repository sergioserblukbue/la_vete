def eliminarMascota(lista):
    dni=input("ingrese el dni del propietario: ") 
    print("lista de mascotas")
    print("="*15)
    for mascota in lista:
        if mascota["dniPropietario"]==dni:
            print(f"nombre: {mascota['nombre']} tipo: {mascota['tipo']}")
    eliXnom=input("ingrese el nombre de la mascota a eliminar: ")
    for i in range(len(lista)):
        if lista[i]["dniPropietario"]==dni and lista[i]["nombre"]==eliXnom:
            lista.pop(i)
            print("elemento removido....")
            return
    print("no se encontro la mascota!")
    return