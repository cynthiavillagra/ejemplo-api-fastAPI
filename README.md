# API de nombres con FastAPI

Ejemplo básico: un formulario (frontend) que envía un nombre a una API hecha con FastAPI (backend), que lo guarda en `nombres.json`.

## Endpoints

| Método | Ruta | Qué hace |
|---|---|---|
| POST | `/agregarnombres` | Recibe `{"nombre": "Ana"}` y lo guarda |
| GET | `/listarnombres` | Devuelve la lista de nombres |

## Cómo correrlo

Desde la carpeta `backend`:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Después abrir `frontend/index.html` con Live Server.
La documentación interactiva queda en http://localhost:8000/docs
