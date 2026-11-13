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

## Qué leer primero

1. `backend/appV2.py`: la lógica (guardar y leer nombres, Python puro)
2. `backend/rutas/nombres.py`: los dos endpoints y el modelo de datos
3. `backend/main.py`: la aplicación, CORS, el middleware y el enchufe de las rutas
4. `frontend/cliente.js`: los `fetch` que llaman a la API
5. `frontend/script.js`: el formulario y cómo se muestra la respuesta

El paso siguiente es reemplazar los nombres por un modelo de Machine Learning: ver el repo `ejemplo-api-modelo`, que tiene la misma estructura.

## Dos versiones del mismo código

| Rama | Para qué |
|---|---|
| `main` | El código comentado paso a paso, para estudiar |
| `clase` | El mismo código con comentarios mínimos (el que se escribe en clase) |
