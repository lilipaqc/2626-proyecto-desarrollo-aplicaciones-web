# AdoptaYA!

Plataforma web para la adopción responsable de animales y gestión de donaciones para su bienestar en Ecuador. Proyecto integrador de la asignatura Desarrollo de Aplicaciones Web - Universidad Estatal Amazónica (UEA).

## Descripción del proyecto

AdoptaYA! busca conectar animales en situación de abandono con personas que quieran darles un hogar. La plataforma permite explorar animales disponibles para adopción, registrar solicitudes de adopción y conocer los servicios que ofrece la organización (adopciones, donaciones, red de veterinarias).

## Tecnologías usadas

- HTML5 (estructura semántica)
- CSS3 (estilos personalizados)
- Bootstrap 5.3.3 (componentes y diseño responsivo)
- JavaScript (DOM, eventos, validaciones y contenido dinámico)
- GitHub y GitHub Pages (control de versiones y publicación)

## Estructura del proyecto

```
index.html    -> estructura y contenido de la página
style.css     -> estilos personalizados
script.js     -> validaciones y contenido dinámico
```

## Bitácora semana a semana

**Semana 2 - Primera página web**
Instalación de Visual Studio Code y creación del primer `index.html` con estructura básica de HTML, subido a GitHub.

**Semana 3 - Estructura HTML5 semántica**
Se organizó la página con etiquetas semánticas: `header`, `nav`, `main`, `section`, `article`, `aside` y `footer`. Se agregaron las secciones Inicio, Quiénes Somos, Servicios y Contacto, además de una imagen, un video de YouTube incrustado y enlaces a redes sociales.

**Semana 4 - CSS3, diseño responsivo y Bootstrap**
Se integró Bootstrap mediante CDN. Se mejoró visualmente cada sección con tarjetas, botones, formulario de contacto y sistema de grillas (`container`, `row`, `col`). Se agregaron estilos propios en `style.css` y una media query para pantallas pequeñas.

**Semana 5 - JavaScript, DOM y eventos**
Se creó el archivo `script.js` y se agregó la sección de Solicitudes de Adopción con un formulario. Se implementó el registro dinámico de datos usando `createElement()`, `appendChild()` y `addEventListener()`, sin recargar la página, incluyendo eliminación de registros y contador total.

**Semana 6 - Validaciones dinámicas del formulario**
Se mejoraron las validaciones del formulario de solicitudes en tiempo real: nombre (mínimo de caracteres, solo letras), descripción (mínimo de caracteres) y tipo de animal (obligatorio). Se usaron expresiones regulares y las clases de Bootstrap `is-valid` / `is-invalid` con mensajes de feedback por campo.

**Semana 7 - Uso de plantillas para contenido dinámico**
Se reorganizó el proyecto simulando una estructura de plantillas, marcando con comentarios las secciones que a futuro podrían separarse en archivos de Flask (header, nav, contenido principal, footer). Se agregó la sección "Animales en Adopción", cuyos datos se generan desde un arreglo de objetos en JavaScript y se renderizan dinámicamente con un bucle, incluyendo un mensaje condicional si no hay animales disponibles.

**Semana 8 - Mejora de interfaces con Bootstrap**
Se reforzó la interfaz visual del proyecto manteniendo intacta la lógica y las validaciones ya desarrolladas. Se agregó un modal de Bootstrap en la sección "Animales en Adopción" que muestra los detalles de cada animal (nombre, tipo, edad y estado) al presionar el botón "Ver detalles" de su tarjeta. Se incorporó también un spinner de Bootstrap que simula un proceso de carga de datos antes de renderizar la lista de animales. Se conservaron el navbar, el sistema de rejilla, el formulario con `form-label`/`form-control`, los botones y las alertas ya implementados en semanas anteriores, comprobando que la interfaz siga siendo responsiva en computadora, tablet y celular.

## Autor

Lilian Quijije - Desarrollo de Aplicaciones Web - 2026