// ADOPTA YA! - JavaScript 
// Manipulación del DOM y manejo de eventos

// VARIABLES GLOBALES 
let totalRegistros = 0;

// REFERENCIAS AL DOM 
const formularioRegistro = document.getElementById("formulario-registro");
const listaRegistros     = document.getElementById("lista-registros");
const contadorEl         = document.getElementById("contador-registros");
const mensajeValidacion  = document.getElementById("mensaje-validacion");

const inputNombre      = document.getElementById("input-nombre");
const inputDescripcion = document.getElementById("input-descripcion");
const inputTipo        = document.getElementById("input-tipo");

const feedbackNombre      = document.getElementById("feedback-nombre");
const feedbackDescripcion = document.getElementById("feedback-descripcion");
const feedbackTipo        = document.getElementById("feedback-tipo");

// Expresión regular: solo letras (con tildes y ñ) y espacios
const soloLetras = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;

// ===== FUNCIÓN: ACTUALIZAR CONTADOR =====
function actualizarContador() {
    contadorEl.textContent = "Total de solicitudes registradas: " + totalRegistros;
}

// ===== FUNCIÓN: MOSTRAR MENSAJE DE VALIDACIÓN GENERAL =====
function mostrarMensaje(texto, tipo) {
    mensajeValidacion.textContent = texto;
    mensajeValidacion.className   = "alert alert-" + tipo + " mt-3";
    mensajeValidacion.classList.remove("d-none");

    // Ocultar el mensaje después de 3 segundos
    setTimeout(function () {
        mensajeValidacion.classList.add("d-none");
    }, 3000);
}

// ===== FUNCIÓN: MARCAR CAMPO COMO VÁLIDO =====
function marcarValido(campo, feedback) {
    campo.classList.remove("is-invalid");
    campo.classList.add("is-valid");
    feedback.textContent = "";
}

// ===== FUNCIÓN: MARCAR CAMPO COMO INVÁLIDO =====
function marcarInvalido(campo, feedback, mensaje) {
    campo.classList.remove("is-valid");
    campo.classList.add("is-invalid");
    feedback.textContent = mensaje;
}

// ===== FUNCIÓN: VALIDAR NOMBRE =====
function validarNombre() {
    const valor = inputNombre.value.trim();

    if (valor === "") {
        marcarInvalido(inputNombre, feedbackNombre, "El nombre es obligatorio.");
        return false;
    }

    if (valor.length < 3) {
        marcarInvalido(inputNombre, feedbackNombre, "El nombre debe tener al menos 3 caracteres.");
        return false;
    }

    if (!soloLetras.test(valor)) {
        marcarInvalido(inputNombre, feedbackNombre, "El nombre solo puede contener letras y espacios.");
        return false;
    }

    marcarValido(inputNombre, feedbackNombre);
    return true;
}

// ===== FUNCIÓN: VALIDAR DESCRIPCIÓN =====
function validarDescripcion() {
    const valor = inputDescripcion.value.trim();

    if (valor === "") {
        marcarInvalido(inputDescripcion, feedbackDescripcion, "La descripción es obligatoria.");
        return false;
    }

    if (valor.length < 10) {
        marcarInvalido(inputDescripcion, feedbackDescripcion, "La descripción debe tener al menos 10 caracteres.");
        return false;
    }

    marcarValido(inputDescripcion, feedbackDescripcion);
    return true;
}

// ===== FUNCIÓN: VALIDAR TIPO =====
function validarTipo() {
    const valor = inputTipo.value;

    if (valor === "") {
        marcarInvalido(inputTipo, feedbackTipo, "Selecciona un tipo de animal.");
        return false;
    }

    marcarValido(inputTipo, feedbackTipo);
    return true;
}

// ===== FUNCIÓN: CREAR TARJETA DE REGISTRO =====
function crearTarjetaRegistro(nombre, descripcion, tipo) {
    // Crear elementos
    const col      = document.createElement("div");
    const card     = document.createElement("div");
    const cardBody = document.createElement("div");
    const titulo   = document.createElement("h5");
    const badge    = document.createElement("span");
    const desc     = document.createElement("p");
    const btnElim  = document.createElement("button");

    // Asignar clases Bootstrap
    col.className      = "col-md-6 col-lg-4 mb-3";
    card.className     = "card registro-card p-2";
    cardBody.className = "card-body";
    titulo.className   = "card-title";
    badge.className    = "badge badge-tipo text-white mb-2";
    desc.className     = "card-text text-muted";
    btnElim.className  = "btn btn-danger btn-sm mt-2";

    // Asignar contenido
    titulo.textContent   = nombre;
    badge.textContent    = tipo;
    desc.textContent     = descripcion;
    btnElim.textContent  = "Eliminar";

    // Evento eliminar: elimina la tarjeta y actualiza el contador
    btnElim.addEventListener("click", function () {
        col.remove();
        totalRegistros--;
        actualizarContador();
        mostrarMensaje("Solicitud eliminada correctamente.", "warning");
    });

    // Armar estructura
    cardBody.appendChild(badge);
    cardBody.appendChild(titulo);
    cardBody.appendChild(desc);
    cardBody.appendChild(btnElim);
    card.appendChild(cardBody);
    col.appendChild(card);

    return col;
}

// ===== EVENTO: FILTRAR CARACTERES NO PERMITIDOS EN NOMBRE =====
inputNombre.addEventListener("input", function () {
    // Elimina cualquier caracter que no sea letra o espacio mientras se escribe
    inputNombre.value = inputNombre.value.replace(/[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]/g, "");
    validarNombre();
});
inputNombre.addEventListener("blur", validarNombre);

// ===== EVENTO: VALIDACIÓN EN TIEMPO REAL DE DESCRIPCIÓN =====
inputDescripcion.addEventListener("input", validarDescripcion);
inputDescripcion.addEventListener("blur", validarDescripcion);

// ===== EVENTO: VALIDACIÓN EN TIEMPO REAL DE TIPO =====
inputTipo.addEventListener("change", validarTipo);
inputTipo.addEventListener("blur", validarTipo);

// ===== EVENTO: SUBMIT DEL FORMULARIO =====
formularioRegistro.addEventListener("submit", function (event) {
    // Evitar recarga de página
    event.preventDefault();

    // Validar todos los campos
    const nombreValido      = validarNombre();
    const descripcionValida = validarDescripcion();
    const tipoValido        = validarTipo();

    // Si algún campo no es válido, no se registra
    if (!nombreValido || !descripcionValida || !tipoValido) {
        mostrarMensaje("Por favor corrige los campos marcados en rojo.", "danger");
        return;
    }

    // Obtener valores
    const nombre      = inputNombre.value.trim();
    const descripcion = inputDescripcion.value.trim();
    const tipo        = inputTipo.value;

    // Crear y agregar la tarjeta al listado
    const nuevaTarjeta = crearTarjetaRegistro(nombre, descripcion, tipo);
    listaRegistros.appendChild(nuevaTarjeta);

    // Actualizar contador
    totalRegistros++;
    actualizarContador();

    // Mensaje de éxito
    mostrarMensaje("¡Solicitud registrada exitosamente!", "success");

    // Limpiar formulario y estilos de validación
    formularioRegistro.reset();
    [inputNombre, inputDescripcion, inputTipo].forEach(function (campo) {
        campo.classList.remove("is-valid", "is-invalid");
    });
});