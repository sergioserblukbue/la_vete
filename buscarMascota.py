def buscarMascota(lista):
    print("buscar mascotas".center(60," "))
    print("="*60)
    nombre=input("Ingrese el nombre de la mascota: ")
    dni=input("ingrese el dni del propietario: ")
    for mascota in lista:
        if mascota["nombre"]==nombre and mascota["dniPropietario"]==dni:
            print(f"nombre: {mascota['nombre']} raza: {mascota['raza']} tipo:{mascota['tipo']} ")
            print("="*60) 
            return
    print("Mascota no encontrada...")   
    return    