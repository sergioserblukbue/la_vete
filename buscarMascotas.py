def buscarMascotas(lista):
    print("busquedad de mascotas".center(60," "))
    print("="*60)
    dni=input("ingrese el dni del propietario: ")
    nombre=input("ingrese el nombre de la mascota: ")
    for mascota in lista:
        if mascota["dniPropietario"]==dni and mascota["nombre"]==nombre:
            print(f"nombre: {mascota['nombre']} tipo: {mascota['tipo']}")
            return
    print("mascota no encontrada!")
    return