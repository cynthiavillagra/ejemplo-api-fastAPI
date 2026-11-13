# =====================================================================
# rutas/nombres.py · LOS ENDPOINTS DE NOMBRES
# ---------------------------------------------------------------------
# Qué hace: define las dos "puertas" de la API:
#   POST /agregarnombres  → recibe un nombre y lo guarda
#   GET  /listarnombres   → devuelve todos los nombres guardados
#
# Este archivo es el intermediario entre dos mundos:
#   - HTTP: recibe el JSON que manda el frontend y devuelve otro JSON
#   - Python: llama a las funciones de appV2.py, que hacen el trabajo
# =====================================================================

# PASO 1 · Importar lo necesario
from fastapi import APIRouter                        # permite definir rutas en un archivo aparte de main.py
from pydantic import BaseModel                       # para describir y validar los datos que llegan
from appV2 import agregar_nombre, listar_nombres     # las funciones que guardan y leen


# PASO 2 · Crear el router
# Es como una "mini app": acá se anotan las rutas y después main.py
# las suma a la aplicación con include_router.
router = APIRouter()


# PASO 3 · El modelo de datos: el CONTRATO de entrada
# Esta clase describe qué JSON tiene que mandar el frontend:
# un objeto con una clave "nombre" cuyo valor es un texto (str).
# Ejemplo válido: {"nombre": "Ana"}
# Si falta "nombre" o no es texto, FastAPI responde solo con un error 422.
class Nombre(BaseModel):
    nombre: str


# PASO 4 · Endpoint para agregar un nombre
# @router.post → cuando llegue un POST a /agregarnombres, ejecutar esta función.
# "datos: Nombre" → FastAPI lee el JSON del pedido, lo valida y arma un objeto Nombre.
@router.post("/agregarnombres")
def agregar(datos: Nombre):
    # datos.nombre es el texto que mandó el frontend.
    # Lo que se devuelve (un diccionario) FastAPI lo convierte en JSON:
    # {"resultado": "Nombre 'Ana' agregado correctamente."}
    return {"resultado": agregar_nombre(datos.nombre)}


# PASO 5 · Endpoint para listar los nombres
# No recibe datos: por eso es GET y la función no tiene parámetros.
# Responde, por ejemplo: {"resultado": ["Juan", "Ana"]}
@router.get("/listarnombres")
def listar():
    return {"resultado": listar_nombres()}
