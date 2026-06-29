// ADOPTA YA! - JavaScript 
// Manipulación del DOM y manejo de eventos

// VARIABLES GLOBALES 
let totalRegistros = 0;

// REFERENCIAS AL DOM 
const formularioRegistro = document.getElementById("formulario-registro");
const listaRegistros     = document.getElementById("lista-registros");
const contadorEl         = document.getElementById("contador-registros");
const mensajeValidacion  = document.getElementById("mensaje-validacion");

// ===== FUNCIÓN: ACTUALIZAR CONTADOR =====
function actualizarContador() {
    contadorEl.textContent = "Total de solicitudes registradas: " + totalRegistros;
}

//  FUNCIÓN: MOSTRAR MENSAJE DE VALIDACIÓN 
function mostrarMensaje(texto, tipo) {
    mensajeValidacion.textContent = texto;
    mensajeValidacion.className   = "alert alert-" + tipo + " mt-3";
    mensajeValidacion.classList.remove("d-none");

    // Ocultar el mensaje después de 3 segundos
    setTimeout(function () {
        mensajeValidacion.classList.add("d-none");
    }, 3000);
}

// FUNCIÓN: CREAR TARJETA DE REGISTRO 
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

// ===== EVENTO: SUBMIT DEL FORMULARIO =====
formularioRegistro.addEventListener("submit", function (event) {
    // Evitar recarga de página
    event.preventDefault();

    // Obtener valores
    const nombre      = document.getElementById("input-nombre").value.trim();
    const descripcion = document.getElementById("input-descripcion").value.trim();
    const tipo        = document.getElementById("input-tipo").value;

    // Validar que los campos no estén vacíos
    if (nombre === "" || descripcion === "" || tipo === "") {
        mostrarMensaje("Por favor, complete todos los campos antes de enviar.", "danger");
        return;
    }

    // Crear y agregar la tarjeta al listado
    const nuevaTarjeta = crearTarjetaRegistro(nombre, descripcion, tipo);
    listaRegistros.appendChild(nuevaTarjeta);

    // Actualizar contador
    totalRegistros++;
    actualizarContador();

    // Mensaje de éxito
    mostrarMensaje("¡Solicitud registrada exitosamente!", "success");

    // Limpiar formulario
    formularioRegistro.reset();
});

// ===== EVENTO: VALIDACIÓN EN TIEMPO REAL (focus/blur) =====
const camposRequeridos = document.querySelectorAll(".campo-requerido");

camposRequeridos.forEach(function (campo) {
    campo.addEventListener("blur", function () {
        if (campo.value.trim() === "") {
            campo.classList.add("is-invalid");
        } else {
            campo.classList.remove("is-invalid");
            campo.classList.add("is-valid");
        }
    });

    campo.addEventListener("input", function () {
        if (campo.value.trim() !== "") {
            campo.classList.remove("is-invalid");
        }
    });
});