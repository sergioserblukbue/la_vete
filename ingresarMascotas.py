def ingresarMascota(listaMacotas=[]):
    print("Ingreso de mascotas".center(60," "))
    print("="*60)
    nombre=input("ingrese el nombre de la mascota: ")
    anioNac=input("ingrese el año de nacimiento: ")
    raza=input("ingrese la raza: ")
    tipo=input("ingrese el tipo: ")
    sexo=input("ingrese el sexo: ")
    dniPropietario=input("ingrese el dni del dueño: ")
    listaMacotas.append({
        "nombre":nombre,
        "anioNac":anioNac,
        "raza":raza,
        "tipo":tipo,
        "sexo":sexo,
        "procedimientos":[],
        "dniPropietario":dniPropietario
    })
    print("mascota agregada correctamente!")
    print(listaMacotas)
    input("enter para continuar...")
    return