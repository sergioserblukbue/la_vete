#by Hernan Scandizzo
def ingresoMascotas(lista=[]):
    nombre=input("ingrese el nombre de la mascota:")
    anionac=input("ingrese el año de nacimiento: ")
    raza=input("ingrese la raza: ")
    tipo=input("ingrese el tipo: ")
    sexo=input("ingrese el sexo: ")
    procedimientos=[]
    dnipropietario=input("ingrese el dni del dueño: ")
    lista.append({
        "nombre":nombre,
        "anionac":anionac,
        "raza":raza,
        "tipo":tipo,
        "sexo":sexo,
        "procedimientos":procedimientos,
        "dnipropietario":dnipropietario
    })
    print(lista)
    print("se agregaron los datos correctamente!")
    input("enter para continuar...")


          