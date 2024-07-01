def modificarMascota(lista=list([])):
    dni=input("ingrese el dni del dueño")
    indice=0
    ordenMascota=1
    tabla=[]
    for m in lista:
        if m["dnipropietario"]==dni:
            print(f"orden: {ordenMascota} nombre: {m['nombre']}")
            tabla.append({
                "indice":indice,
                "orden":ordenMascota
            })
            ordenMascota+=1

        indice+=1
    orden=int(input("ingrese el numero de la mascota a modificar: "))
    #muestro los datos de la mascota
    for e in tabla:
        if e["orden"]==orden:
            indice=e["indice"]
    print("datos de la mascota".center(30," "))
    print("0"*30)
    print(f"Nombre: {lista[indice]['nombre']}")
    r=input("modificar? s/n: ")
    if r=="s":
        lista[indice]["nombre"]=input("ingrese el nuevo nombre: ")
        print("se actualizo el nombre")
    print(f"año nacimiento: {lista[indice]['anionac']}")
    r=input("modificar? s/n: ")
    if r=="s":
        lista[indice]["anionac"]=input("ingrese el nuevo año de nacimiento: ")
        print("se actualizo el año de nacimiento")
    print(f"raza: {lista[indice]['raza']}")
    r=input("modificar? s/n: ")
    if r=="s":
        lista[indice]["raza"]=input("ingrese la nueva raza: ")
        print("se actualizo la raza")
    print(f"tipo: {lista[indice]['tipo']}")
    r=input("modificar? s/n: ")
    if r=="s":
        lista[indice]["tipo"]=input("ingrese el nuevo tipo: ")
        print("se actualizo el tipo")
    print(f"sexo: {lista[indice]['sexo']}")
    r=input("modificar? s/n: ")
    if r=="s":
        lista[indice]["sexo"]=input("ingrese el nuevo sexo: ")
        print("se actualizo el sexo")
    
    

