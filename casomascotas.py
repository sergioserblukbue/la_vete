usuarios={
    "2525":{
        "nombre":"juan",
        "mascotas":[
            {"NombreM":"pepe",
            "tipo":"loro"},
            {"NombreM":"lola",
            "tipo":"loro"},]
    }
}
for c,v in usuarios.items():
    print(c)
    i=1
    for mascota in v["mascotas"]:
        if mascota["NombreM"]=="pepe":
            print(f"orden: {i} nombre: {mascota['NombreM']}")
            i=i+1
    op=int(input("ingrese el orden de la mascota a eliminar: "))
    v["mascotas"].pop(op-1)
    print(v)