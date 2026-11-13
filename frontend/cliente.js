// =====================================================================
// cliente.js · EL CLIENTE DE LA API
// ---------------------------------------------------------------------
// Qué hace: tiene las funciones que hablan con la API de FastAPI (main.py).
// No sabe nada del formulario ni de la página: eso lo hace script.js.
// Es IGUAL al de la versión con http.server: como las rutas y el formato
// del JSON no cambiaron, el frontend no se entera de que cambió el backend.
// =====================================================================

// PASO 1 · La dirección de nuestra API (el servidor Python que levanta uvicorn)
// Cuando publiques la API, acá va la dirección pública que te dé la plataforma.
const API_URL = "http://localhost:8000";

// PASO 2 · Enviar un nombre: POST /agregarnombres
// "async" permite usar "await" adentro: esperar la respuesta sin congelar la página.
async function enviarNombre(nombre) {
    // 2.1 · Hacer el pedido HTTP y esperar la respuesta
    const respuesta = await fetch(API_URL + "/agregarnombres", {
        method: "POST",                                    // POST porque le enviamos datos
        headers: { "Content-Type": "application/json" },   // avisamos que el cuerpo viaja en JSON
        body: JSON.stringify({ nombre: nombre })           // convertimos el objeto en texto: {"nombre":"Ana"}
    });
    // 2.2 · Leer el cuerpo de la respuesta y convertirlo de JSON a objeto
    const datos = await respuesta.json();
    // 2.3 · Devolver solo el mensaje: "Nombre 'Ana' agregado correctamente."
    return datos.resultado;
}

// PASO 3 · Pedir la lista de nombres: GET /listarnombres
// fetch sin opciones hace un GET: no enviamos datos, solo pedimos.
async function listarNombres() {
    const respuesta = await fetch(API_URL + "/listarnombres");
    const datos = await respuesta.json();
    return datos.resultado;   // la lista: ["Juan", "Ana", ...]
}
