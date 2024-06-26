def ingresarMascota(listMascotas=[]):
    print("Ingreso de mascotas".center(60," "))
    print("="*60)
    nombre=input("ingrese el nombre de la mascota: ")
    anioNac=int(input("ingrese el año de nacimiento: "))
    raza=input("ingrese la raza: ")
    tipo=input("ingrese el tipo: ")
    sexo=input("ingrese el sexo:")
    lista=[]
    dniPropietario=input("ingrese el dni del dueño: ")
    listMascotas.append({
        "nombre":nombre,
        "anioNac":anioNac,
        "raza":raza,
        "tipo":tipo,
        "sexo":sexo,
        "procedimientos":lista,
        "dniPropietario":dniPropietario
    })
    print("se agrego una nueva mascota!")
    print(listMascotas)
    input("enter para continuar...")
    return