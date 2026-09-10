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

**Semana 9 - Configuración de Flask y manejo de rutas**
Se transformó el proyecto en una aplicación Python con Flask, manteniendo intacta la página informativa desarrollada en semanas anteriores (`index.html`, `style.css`, `script.js` en la raíz, publicados en GitHub Pages). Se creó un entorno virtual de Python y se instaló Flask. Se organizó el proyecto en las carpetas `templates` (para los archivos HTML renderizados por Flask) y `static` (subcarpetas `css`, `js` e `img` para los recursos). Se desarrolló `app.py` con las rutas principales usando el decorador `@app.route()` y `render_template()`. Se creó una plantilla base `base.html` con los elementos comunes (encabezado, navbar, footer, Bootstrap) y se implementó herencia de plantillas con Jinja2 mediante `{% extends %}` y `{% block content %}`. Se agregaron cuatro módulos con datos de ejemplo renderizados dinámicamente con bucles `{% for %}`: Mascotas, Adoptantes, Refugios y Solicitudes. Se utilizó `url_for()` tanto para la navegación entre rutas como para cargar los archivos estáticos. En esta etapa no se conecta base de datos, y las rutas de Flask se prueban únicamente en local (`http://127.0.0.1:5000`), mientras que GitHub Pages sigue mostrando la parte frontend desarrollada en semanas previas.

**Semana 10 - Contenido dinámico y reutilización de componentes con Jinja2**
Se avanzó en la generación de contenido dinámico del proyecto Flask, manteniendo intacta toda la estructura y funcionalidad desarrollada en la Semana 9. En app.py se agregaron variables simples (fecha_actualizacion y total_mascotas) enviadas hacia la plantilla index.html mediante render_template(), además de las listas y diccionarios de ejemplo ya existentes (mascotas, adoptantes, refugios, solicitudes). En las plantillas se utilizó la sintaxis {{ variable }} para mostrar datos dinámicos, se aplicó el filtro de Jinja2 |upper sobre la fecha de actualización, y se reforzó el uso de estructuras {% for %} e {% if %} / {% else %} ya implementadas en semanas anteriores para mostrar el estado de mascotas y solicitudes. Como principal mejora de reutilización, se separaron el navbar y el footer de base.html en componentes independientes dentro de una nueva carpeta templates/components/ (navbar.html y footer.html), incorporados en la plantilla base mediante {% include "components/navbar.html" %} y {% include "components/footer.html" %}, evitando la duplicación de código HTML en cada página. Se comprobó que todas las rutas (/, /mascotas, /adoptantes, /refugios, /solicitudes) siguen funcionando correctamente en local (http://127.0.0.1:5000) sin errores de TemplateNotFound ni recursos no encontrados. En esta etapa aún no se requiere conexión a base de datos.

Semana 11 - Validación de formularios con Flask-WTF y WTForms Se incorporaron formularios web con validación del lado del servidor utilizando Flask-WTF y WTForms, manteniendo intacta toda la estructura y funcionalidad desarrollada en las semanas anteriores. Se creó la carpeta forms/ en la raíz del proyecto, organizando una clase de formulario por cada módulo del sistema (MascotaForm, AdoptanteForm, RefugioForm y SolicitudForm), todas heredando de FlaskForm. Cada formulario utiliza los campos de WTForms correspondientes a su información (StringField, SelectField) junto con validadores como DataRequired(), Length() y Email() según el tipo de dato. En app.py se configuró una SECRET_KEY para habilitar la protección CSRF, y se agregaron cuatro nuevas rutas (/mascotas/agregar, /adoptantes/agregar, /refugios/agregar, /solicitudes/agregar) que aceptan los métodos GET y POST, procesando la información únicamente cuando form.validate_on_submit() confirma que todos los datos son válidos. Se crearon las plantillas formulario_mascota.html, formulario_adoptante.html, formulario_refugio.html y formulario_solicitud.html, todas heredando de base.html mediante {% extends %}, incorporando form.hidden_tag() para el token CSRF y mostrando los mensajes de error de cada validador debajo de su campo correspondiente. Se agregaron botones de acceso rápido a cada formulario desde sus respectivas páginas de listado. Se probaron los formularios enviando campos vacíos, valores que no cumplen las reglas de validación (por ejemplo, cédulas con menos de 10 dígitos o correos sin formato válido) y datos correctos, confirmando que la información solo se registra cuando todas las validaciones son satisfactorias. Se actualizó requirements.txt tras instalar Flask-WTF. Se comprobó que todas las rutas desarrolladas en semanas anteriores continúan funcionando correctamente en local (http://127.0.0.1:5000). En esta etapa aún no se requiere conexión a una base de datos.

Semana 12 - Persistencia de datos con SQLite en un entorno local Se incorporó persistencia real de datos utilizando SQLite como mecanismo principal de almacenamiento, manteniendo intacta toda la estructura y funcionalidad desarrollada en las semanas anteriores. Se creó la carpeta data/ en la raíz del proyecto para almacenar el archivo de base de datos local adoptaya.db, y se desarrolló el módulo database.py con las funciones conectar() e inicializar_db(), que gestionan la conexión mediante sqlite3.connect() y la creación de la tabla mascotas mediante CREATE TABLE IF NOT EXISTS, con una clave primaria autoincremental (id) y los campos nombre, tipo, edad y estado. La ruta /mascotas/agregar se modificó para insertar los datos validados por MascotaForm (Flask-WTF) directamente en la base de datos mediante una consulta INSERT parametrizada con signos de interrogación (?), evitando la concatenación directa de valores. La ruta /mascotas se modificó para recuperar los registros almacenados mediante una consulta SELECT * FROM mascotas y fetchall(), enviando la información hacia la plantilla mascotas.html mediante render_template(), donde se recorre con un ciclo {% for %} de Jinja2 y se muestra en tarjetas con estilos Bootstrap, tal como en semanas anteriores. Se comprobó la persistencia real de la información registrando varias mascotas, cerrando la aplicación Flask y ejecutándola nuevamente, confirmando que los registros permanecen almacenados en el archivo .db y se visualizan correctamente. Los módulos de adoptantes, refugios y solicitudes se mantuvieron con su almacenamiento temporal en listas de Python, tal como se permite en esta etapa, quedando preparados para incorporar persistencia progresivamente en avances posteriores. Se mantuvieron los formularios Flask-WTF, las validaciones, la protección CSRF, la herencia de plantillas con base.html, los componentes reutilizables (navbar y footer) y los estilos Bootstrap desarrollados en semanas previas. Se actualizó requirements.txt y se comprobó que todas las rutas del proyecto continúan funcionando correctamente en local (http://127.0.0.1:5000).

Semana 13 - Uso de bases de datos relacionales: MySQL, modelos y consultas básicas Se migró la persistencia del módulo de mascotas de SQLite hacia una base de datos relacional MySQL, manteniendo intacta toda la estructura y funcionalidad desarrollada en las semanas anteriores. Se instaló el conector mysql-connector-python y se centralizó la conexión en el archivo conexion/conexion.py, utilizando variables de entorno (mediante python-dotenv y un archivo .env no incluido en el repositorio) para no exponer las credenciales reales de la base de datos. Se diseñó el modelo relacional del sistema en sql/esquema.sql, creando la tabla refugios (con clave primaria id_refugio) y la tabla mascotas (con clave primaria id_mascota y una clave foránea id_refugio que la relaciona con la tabla refugios), estableciendo así la primera relación entre entidades del proyecto. La ruta /mascotas se modificó para recuperar los registros mediante una consulta SELECT con LEFT JOIN entre mascotas y refugios, mostrando el nombre

## Autor

Lilian Quijije - Desarrollo de Aplicaciones Web - 2026