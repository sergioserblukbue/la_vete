def listarMascotas(lista):
    print("listado de mascotas".center(60," "))
    print("="*60)
    for mascota in lista:
        print(f"nombre: {mascota['nombre']}, tipo: {mascota['tipo']}")
    print("fin del listado".center(60,"-"))
