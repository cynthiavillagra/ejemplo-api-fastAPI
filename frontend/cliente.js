// CLIENTE DE LA API: funciones para hablar con la API de FastAPI (main.py)
// (no sabe nada del formulario; eso lo hace script.js)
// Es IGUAL al de la versión con http.server: las rutas y el formato no cambiaron.

// Dirección de nuestra API (servidor Python)
const API_URL = "http://localhost:8000";

// Enviar un nombre: POST /agregarnombres
async function enviarNombre(nombre) {
    const respuesta = await fetch(API_URL + "/agregarnombres", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre: nombre })
    });
    const datos = await respuesta.json();
    return datos.resultado;
}

// Pedir la lista de nombres: GET /listarnombres
async function listarNombres() {
    const respuesta = await fetch(API_URL + "/listarnombres");
    const datos = await respuesta.json();
    return datos.resultado;
}
