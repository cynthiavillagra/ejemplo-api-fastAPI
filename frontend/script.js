// =====================================================================
// script.js · EL COMPORTAMIENTO DE LA PÁGINA
// ---------------------------------------------------------------------
// Qué hace: cuando se envía el formulario, lee el nombre, se lo manda
// a la API y muestra en la página el mensaje que la API responde.
// Para hablar con la API usa enviarNombre(), que está en cliente.js
// =====================================================================

// PASO 1 · Buscar en la página los elementos que vamos a usar
// querySelector busca por selector CSS: "#nombre" = el elemento con id="nombre"
const formulario = document.querySelector("#saludo-form");
const campoNombre = document.querySelector("#nombre");
const mensaje = document.querySelector("#mensaje");

// PASO 2 · Decir qué hacer cuando se envía el formulario (clic en "Enviar" o Enter)
formulario.addEventListener("submit", async (evento) => {
  // 2.1 · Evitar que el navegador recargue la página (es lo que hace un formulario por defecto)
  evento.preventDefault();

  // 2.2 · Leer lo que se escribió; trim() le saca los espacios de adelante y de atrás
  const nombre = campoNombre.value.trim();

  // 2.3 · Si quedó vacío, avisar y no llamar a la API
  if (!nombre) {
    mensaje.textContent = "Por favor, escribe tu nombre.";
    campoNombre.focus();   // vuelve a poner el cursor en el campo
    return;                // corta acá: no sigue con el resto
  }

  // 2.4 · Intentar enviar el nombre
  // try/catch: si algo falla adentro del "try", en vez de romperse la página se ejecuta el "catch".
  try {
    mensaje.textContent = await enviarNombre(nombre);   // espera la respuesta de la API y la muestra
    campoNombre.value = "";                             // vacía el campo para cargar otro nombre
  } catch (error) {
    console.error("Error:", error);                     // el detalle queda en la consola (F12)
    mensaje.textContent = "No se pudo conectar con el servidor. ¿Está corriendo uvicorn main:app?";
  }
});
