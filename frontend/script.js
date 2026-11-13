// LA PÁGINA: lee el formulario y muestra el resultado.
// Para hablar con la API usa enviarNombre(), que está en cliente.js

const formulario = document.querySelector("#saludo-form");
const campoNombre = document.querySelector("#nombre");
const mensaje = document.querySelector("#mensaje");

formulario.addEventListener("submit", async (evento) => {
  evento.preventDefault();

  const nombre = campoNombre.value.trim();
  if (!nombre) {
    mensaje.textContent = "Por favor, escribe tu nombre.";
    campoNombre.focus();
    return;
  }

  try {
    mensaje.textContent = await enviarNombre(nombre);
    campoNombre.value = "";
  } catch (error) {
    console.error("Error:", error);
    mensaje.textContent = "No se pudo conectar con el servidor. ¿Está corriendo uvicorn main:app?";
  }
});
