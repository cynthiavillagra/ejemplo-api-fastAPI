from fastapi import APIRouter
from pydantic import BaseModel
from appV2 import agregar_nombre, listar_nombres


router = APIRouter()


class Nombre(BaseModel):
    nombre: str


@router.post("/agregarnombres")
def agregar(datos: Nombre):
    return {"resultado": agregar_nombre(datos.nombre)}


@router.get("/listarnombres")
def listar():
    return {"resultado": listar_nombres()}
