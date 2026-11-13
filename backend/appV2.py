# =====================================================================
# appV2.py · LA LÓGICA: GUARDAR Y LEER NOMBRES
# ---------------------------------------------------------------------
# Qué hace: guarda nombres en el archivo nombres.json y los lee.
# Este archivo NO sabe nada de HTTP ni de FastAPI: es Python puro,
# y es el MISMO que se usaba antes de tener una API.
# La API (rutas/nombres.py) solo recibe el pedido y llama a estas funciones.
#
# Para probarlo solo, sin la API:   python appV2.py
# =====================================================================

# PASO 1 · Importar las herramientas (las dos vienen con Python, no se instalan)
import json   # para leer y escribir archivos en formato JSON
import os     # para armar rutas de archivos y saber si un archivo existe

# PASO 2 · Armar la ruta del archivo donde se guardan los nombres
# __file__ es la ruta de este archivo; dirname se queda con su carpeta (backend).
# Así nombres.json siempre queda al lado de appV2.py, sin importar desde
# qué carpeta se levante el servidor.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(BASE_DIR, "nombres.json")


# PASO 3 · Función para agregar un nombre
def agregar_nombre(nombre):

    # 3.1 · Si el archivo ya existe, leer la lista de nombres que tiene
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:   # "r" = abrir para leer
            lista_de_nombres = json.load(archivo)                    # de texto JSON a lista de Python
    # 3.2 · Si no existe (primera vez), empezar con una lista vacía
    else:
        lista_de_nombres = []

    # 3.3 · Agregar el nombre nuevo al final de la lista
    lista_de_nombres.append(nombre)

    # 3.4 · Guardar la lista completa, pisando el archivo anterior
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:       # "w" = abrir para escribir
        # ensure_ascii=False → guarda los acentos y la ñ tal cual · indent=4 → lo deja prolijo
        json.dump(lista_de_nombres, archivo, ensure_ascii=False, indent=4)

    # 3.5 · Devolver un mensaje de confirmación (es lo que después muestra la página)
    return f"Nombre '{nombre}' agregado correctamente."


# PASO 4 · Función para listar los nombres guardados
def listar_nombres():

    # Si el archivo existe, devolver la lista; si no, una lista vacía
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []


# PASO 5 · Prueba rápida
# Este bloque solo se ejecuta si corrés "python appV2.py".
# Cuando la API hace "from appV2 import ...", NO se ejecuta.
if __name__ == "__main__":
    print(agregar_nombre("Juan"))
