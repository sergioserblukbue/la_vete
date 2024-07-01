import json
def cargarDatos():
    try:
        with open("./data/mascotas.json","r") as file: #r/read w/write x/creacion a/update
            return json.load(file)
    except:
        return []
def guardarDatos(lista):
    with open("./data/mascotas.json","w") as file:
        json.dump(lista, file,indent=4)
    return