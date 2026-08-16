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

// Expresión regular, solo letras (con tildes y ñ) y espacios
const soloLetras = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$/;

// FUNCIÓN: ACTUALIZAR CONTADOR 
function actualizarContador() {
    contadorEl.textContent = "Total de solicitudes registradas: " + totalRegistros;
}

// FUNCIÓN: MOSTRAR MENSAJE DE VALIDACIÓN GENERAL 
function mostrarMensaje(texto, tipo) {
    mensajeValidacion.textContent = texto;
    mensajeValidacion.className   = "alert alert-" + tipo + " mt-3";
    mensajeValidacion.classList.remove("d-none");

    // Oculta el mensaje después de 3 segundos
    setTimeout(function () {
        mensajeValidacion.classList.add("d-none");
    }, 3000);
}

// FUNCIÓN: MARCAR CAMPO COMO VÁLIDO 
function marcarValido(campo, feedback) {
    campo.classList.remove("is-invalid");
    campo.classList.add("is-valid");
    feedback.textContent = "";
}

// FUNCIÓN: MARCAR CAMPO COMO INVÁLIDO 
function marcarInvalido(campo, feedback, mensaje) {
    campo.classList.remove("is-valid");
    campo.classList.add("is-invalid");
    feedback.textContent = mensaje;
}

// FUNCIÓN: VALIDAR NOMBRE 
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

// FUNCIÓN: VALIDAR DESCRIPCIÓN 
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

// FUNCIÓN: VALIDAR TIPO 
function validarTipo() {
    const valor = inputTipo.value;

    if (valor === "") {
        marcarInvalido(inputTipo, feedbackTipo, "Selecciona un tipo de animal.");
        return false;
    }

    marcarValido(inputTipo, feedbackTipo);
    return true;
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

// EVENTO: FILTRAR CARACTERES NO PERMITIDOS EN NOMBRE 
inputNombre.addEventListener("input", function () {
    // Elimina cualquier caracter que no sea letra o espacio mientras se escribe
    inputNombre.value = inputNombre.value.replace(/[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]/g, "");
    validarNombre();
});
inputNombre.addEventListener("blur", validarNombre);

// EVENTO: VALIDACIÓN EN TIEMPO REAL DE DESCRIPCIÓN 
inputDescripcion.addEventListener("input", validarDescripcion);
inputDescripcion.addEventListener("blur", validarDescripcion);

// EVENTO: VALIDACIÓN EN TIEMPO REAL DE TIPO
inputTipo.addEventListener("change", validarTipo);
inputTipo.addEventListener("blur", validarTipo);

// EVENTO: SUBMIT DEL FORMULARIO
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


// SECCIÓN: ANIMALES EN ADOPCIÓN (contenido dinámico desde un arreglo)

// Arreglo de objetos que representa los datos del proyecto
const animalesDisponibles = [
    { nombre: "Rocky", tipo: "Perro", edad: "2 años", estado: "Disponible" },
    { nombre: "Michi", tipo: "Gato", edad: "1 año", estado: "Disponible" },
    { nombre: "Toby", tipo: "Perro", edad: "4 años", estado: "Adoptado" },
    { nombre: "Luna", tipo: "Conejo", edad: "8 meses", estado: "Disponible" },
    { nombre: "Simba", tipo: "Gato", edad: "3 años", estado: "Adoptado" }
];

// REFERENCIAS AL DOM DE LA SECCIÓN ANIMALES
const listaAnimales    = document.getElementById("lista-animales");
const mensajeAnimales  = document.getElementById("mensaje-animales");
const spinnerAnimales  = document.getElementById("spinner-animales");

// REFERENCIAS AL DOM DEL MODAL DE DETALLES
const modalAnimalBody = document.getElementById("modalAnimalBody");
const modalAnimalEl   = document.getElementById("modalAnimal");
const modalAnimal      = new bootstrap.Modal(modalAnimalEl);

// FUNCIÓN: MOSTRAR DETALLE DE UN ANIMAL EN EL MODAL 
function mostrarDetalleAnimal(animal) {
    // Genera el contenido del modal según el animal seleccionado
    modalAnimalBody.innerHTML =
        "<p><strong>Nombre:</strong> " + animal.nombre + "</p>" +
        "<p><strong>Tipo:</strong> " + animal.tipo + "</p>" +
        "<p><strong>Edad:</strong> " + animal.edad + "</p>" +
        "<p><strong>Estado:</strong> " + animal.estado + "</p>";

    modalAnimal.show();
}

// ===== FUNCIÓN: CREAR TARJETA DE ANIMAL =====
function crearTarjetaAnimal(animal) {
    const col      = document.createElement("div");
    const card     = document.createElement("div");
    const cardBody = document.createElement("div");
    const titulo   = document.createElement("h5");
    const badge    = document.createElement("span");
    const infoEdad = document.createElement("p");
    const btnDetalle = document.createElement("button");

    col.className      = "col-md-6 col-lg-4 mb-3";
    card.className     = "card animal-card p-2";
    cardBody.className = "card-body";
    titulo.className   = "card-title";
    infoEdad.className = "card-text text-muted";
    btnDetalle.className = "btn btn-primary btn-sm mt-2";

    // Condición, el color del badge depende del estado del animal
    if (animal.estado === "Disponible") {
        badge.className = "badge bg-success mb-2";
    } else {
        badge.className = "badge bg-secondary mb-2";
    }

    titulo.textContent   = animal.nombre + " (" + animal.tipo + ")";
    badge.textContent    = animal.estado;
    infoEdad.textContent = "Edad: " + animal.edad;
    btnDetalle.textContent = "Ver detalles";

    // Evento de abrir el modal con la información del animal
    btnDetalle.addEventListener("click", function () {
        mostrarDetalleAnimal(animal);
    });

    cardBody.appendChild(badge);
    cardBody.appendChild(titulo);
    cardBody.appendChild(infoEdad);
    cardBody.appendChild(btnDetalle);
    card.appendChild(cardBody);
    col.appendChild(card);

    return col;
}

// FUNCIÓN DE RENDERIZAR LISTA DE ANIMALES
function renderizarAnimales(animales) {
    // Limpiar contenido previo antes de renderizar
    listaAnimales.innerHTML = "";

    // Condición, si no hay animales registrados, mostrar mensaje en vez de tarjetas
    if (animales.length === 0) {
        mensajeAnimales.textContent = "No hay animales disponibles en este momento.";
        mensajeAnimales.classList.remove("d-none");
        return;
    }

    mensajeAnimales.classList.add("d-none");

    // Estructura repetitiva, recorre el arreglo y genera una tarjeta por cada animal
    animales.forEach(function (animal) {
        const tarjeta = crearTarjetaAnimal(animal);
        listaAnimales.appendChild(tarjeta);
    });
}

// FUNCION DE CARGAR ANIMALES SIMULANDO UN PROCESO DE CARGA (spinner) 
function cargarAnimales(animales) {
    // Muestra el spinner mientras se "cargan" los datos
    spinnerAnimales.classList.remove("d-none");
    listaAnimales.classList.add("d-none");

    // Simula un proceso de carga de 1.2 segundos antes de renderizar los datos
    setTimeout(function () {
        renderizarAnimales(animales);
        spinnerAnimales.classList.add("d-none");
        listaAnimales.classList.remove("d-none");
    }, 1200);
}

// Cargar y renderizar la lista de animales al cargar la página
cargarAnimales(animalesDisponibles);
