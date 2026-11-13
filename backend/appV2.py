import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(BASE_DIR, "nombres.json")




def agregar_nombre(nombre):

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lista_de_nombres = json.load(archivo)
    else:
        lista_de_nombres = []

    lista_de_nombres.append(nombre)

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(lista_de_nombres, archivo, ensure_ascii=False, indent=4)

    return f"Nombre '{nombre}' agregado correctamente."




def listar_nombres():

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []


if __name__ == "__main__":
    print(agregar_nombre("Juan"))

