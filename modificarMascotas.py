from persistencia import guardarDatos
def modificarMascotas(lista):
    dni = input("ingrese el dni del propietario: ")
    nombre=input("ingrese el nombre de la mascota: ")
    for mascota in lista:
        if mascota["dniPropietario"]==dni and mascota["nombre"]==nombre:
            print("datos de la mascota".center(25," "))
            print(f"nombre: {mascota['nombre']}")
            dato=input("ingrese el nuevo nombre, enter para no modificar: ")
            if dato!="":
                mascota['nombre']=dato
            print(f"año de nacimiento: {mascota['anioNac']}")
            dato=input("ingrese el nuevo año de nacimiento, enter para no modificar: ")
            if dato!="":
                mascota['nombre']=dato
            print(f"año de raza: {mascota['raza']}")
            dato=input("ingrese la raza, enter para no modificar: ")
            if dato!="":
                mascota['raza']=dato
            print(f"tipo: {mascota['tipo']}")
            dato=input("ingrese el nuevo tipo, enter para no modificar: ")
            if dato!="":
                mascota['tipo']=dato
            print(f"sexo: {mascota['sexo']}")
            dato=input("ingrese el sexo, enter para no modificar: ")
            if dato!="":
                mascota['sexo']=dato
            guardarDatos(lista)
            return
    print("mascota no encontrada!")
    input("enter para continuar...")
    return    
    

