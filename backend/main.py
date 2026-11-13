# ARCHIVO PRINCIPAL: crea la aplicación y le enchufa las rutas.
# Levantar el servidor (desde la carpeta backend):  uvicorn main:app --reload

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rutas.nombres import router as rutas_nombres

# La aplicación: sobre "app" vamos configurando todo
app = FastAPI(title="API de nombres")


# Ruta de prueba: solo para comprobar que la API está viva
@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo"}


# CORS: reemplaza al do_OPTIONS y a los headers que escribíamos a mano
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Middleware propio: el "portero". Todas las requests pasan por acá.
@app.middleware("http")
async def registrar_peticion(request: Request, call_next):
    print(f"Llegó: {request.method} {request.url.path}")
    respuesta = await call_next(request)   # la deja pasar hacia el endpoint
    return respuesta


# Se ejecuta al arrancar la API (por ejemplo, para conectar una base de datos)
@app.on_event("startup")
def al_arrancar():
    print("La API está arrancando")


# Se ejecuta al cerrar la API (por ejemplo, para desconectarla)
@app.on_event("shutdown")
def al_cerrar():
    print("La API se está cerrando")


# Enchufar las rutas de nombres a la app (la "zapatilla")
app.include_router(rutas_nombres, tags=["nombres"])
