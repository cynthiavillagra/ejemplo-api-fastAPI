# =====================================================================
# main.py · EL ARCHIVO PRINCIPAL DEL BACKEND
# ---------------------------------------------------------------------
# Qué hace: crea la aplicación (la API), le configura CORS, le agrega
# un middleware propio y le "enchufa" las rutas de rutas/nombres.py.
#
# Cómo se reparte el trabajo en el backend:
#   main.py            → arma la aplicación (este archivo)
#   rutas/nombres.py   → define los endpoints (las "puertas" de la API)
#   appV2.py           → guarda y lee los nombres (no sabe nada de HTTP)
#   nombres.json       → el archivo donde quedan guardados los nombres
#
# Cómo se levanta el servidor (desde la carpeta backend):
#     uvicorn main:app --reload
#   main     = este archivo (main.py)
#   app      = la variable que creamos más abajo
#   --reload = reinicia el servidor solo cada vez que guardás un cambio
# =====================================================================

# PASO 1 · Importar lo necesario
from fastapi import FastAPI, Request                  # FastAPI: la clase que crea la API · Request: representa un pedido que llega
from fastapi.middleware.cors import CORSMiddleware    # la pieza que resuelve CORS
from rutas.nombres import router as rutas_nombres     # las rutas de nombres, definidas en otro archivo

# PASO 2 · Crear la aplicación
# "app" es una instancia de la clase FastAPI: sobre ella vamos configurando todo.
# El título es el que aparece en la documentación automática (/docs).
app = FastAPI(title="API de nombres")


# PASO 3 · Una ruta de prueba
# @app.get("/") es un DECORADOR: le dice a FastAPI "cuando llegue un GET a /,
# ejecutá la función de abajo". Sirve para comprobar que la API está viva
# abriendo http://localhost:8000 en el navegador.
@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo"}   # FastAPI convierte el diccionario en JSON


# PASO 4 · Configurar CORS
# El navegador bloquea, por seguridad, que una página le pida datos a un
# servidor de OTRO origen (otro dominio o puerto). El frontend se abre con
# Live Server (puerto 5500) y la API está en el 8000: son orígenes distintos.
# En la versión con http.server esto se resolvía escribiendo a mano el
# do_OPTIONS y los headers Access-Control-Allow-*. Acá lo hace este middleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # "*" = cualquier origen puede llamar a la API (cómodo para practicar;
                           #       al publicar conviene poner solo la dirección de tu frontend)
    allow_methods=["*"],   # se permiten todos los métodos (GET, POST, ...)
    allow_headers=["*"],   # se permiten todos los encabezados (incluye Content-Type)
)


# PASO 5 · Un middleware propio: el "portero"
# Un middleware es código que se ejecuta en TODAS las requests, antes y
# después del endpoint. Este solo anota en la terminal qué pedido llegó.
# "async" y "await" permiten esperar sin frenar al resto de los pedidos.
@app.middleware("http")
async def registrar_peticion(request: Request, call_next):
    print(f"Llegó: {request.method} {request.url.path}")   # por ejemplo: "Llegó: POST /agregarnombres"
    respuesta = await call_next(request)   # la deja pasar hacia el endpoint y espera su respuesta
    return respuesta                       # devuelve esa respuesta a quien hizo el pedido


# PASO 6 · Código que se ejecuta UNA vez, al arrancar la API
# Es el lugar para preparar lo que la API necesita antes de atender:
# por ejemplo, conectarse a una base de datos o cargar un modelo.
@app.on_event("startup")
def al_arrancar():
    print("La API está arrancando")


# PASO 7 · Código que se ejecuta UNA vez, al cerrar la API (Ctrl + C)
# Sirve para cerrar prolijamente lo que se abrió al arrancar.
@app.on_event("shutdown")
def al_cerrar():
    print("La API se está cerrando")


# PASO 8 · Enchufar las rutas de nombres a la app (la "zapatilla")
# include_router suma a la app todos los endpoints definidos en rutas/nombres.py.
# "tags" solo sirve para agruparlos bajo un título en /docs.
app.include_router(rutas_nombres, tags=["nombres"])
