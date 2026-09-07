from flask import Flask, render_template, redirect, url_for

from forms.mascota_form import MascotaForm
from forms.adoptante_form import AdoptanteForm
from forms.refugio_form import RefugioForm
from forms.solicitud_form import SolicitudForm

from database import conectar, inicializar_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-adoptaya-2026'  # necesaria para CSRF

# Inicializa la base de datos (crea la tabla si no existe)
inicializar_db()

# ---------------------------------------------------------
# Datos de ejemplo (estáticos) para los módulos que aún no
# tienen persistencia en base de datos
# ---------------------------------------------------------
adoptantes = [
    {"nombre": "María López", "cedula": "1712345678", "telefono": "0991234567", "mascota_interes": "Rocky"},
    {"nombre": "Carlos Pérez", "cedula": "1798765432", "telefono": "0987654321", "mascota_interes": "Luna"},
    {"nombre": "Andrea Torres", "cedula": "1755566677", "telefono": "0965544332", "mascota_interes": "Michi"},
]

refugios = [
    {"nombre": "Refugio Huellitas", "ciudad": "Quito", "contacto": "huellitas@correo.com"},
    {"nombre": "Patitas Felices", "ciudad": "Ambato", "contacto": "patitasfelices@correo.com"},
    {"nombre": "Segunda Oportunidad", "ciudad": "Quito", "contacto": "segundaoportunidad@correo.com"},
]

solicitudes = [
    {"solicitante": "María López", "mascota": "Rocky", "fecha": "2026-08-10", "estado": "En revisión"},
    {"solicitante": "Carlos Pérez", "mascota": "Luna", "fecha": "2026-08-12", "estado": "Aprobada"},
    {"solicitante": "Andrea Torres", "mascota": "Michi", "fecha": "2026-08-14", "estado": "Pendiente"},
]

# ---------------------------------------------------------
# Rutas principales
# ---------------------------------------------------------
@app.route('/')
def index():
    fecha_actualizacion = "06 de septiembre de 2026"

    conn = conectar()
    total_mascotas = conn.execute('SELECT COUNT(*) FROM mascotas').fetchone()[0]
    conn.close()

    return render_template(
        'index.html',
        fecha_actualizacion=fecha_actualizacion,
        total_mascotas=total_mascotas
    )

@app.route('/mascotas')
def mascotas_view():
    conn = conectar()
    mascotas = conn.execute('SELECT * FROM mascotas').fetchall()
    conn.close()
    return render_template('mascotas.html', mascotas=mascotas)

@app.route('/adoptantes')
def adoptantes_view():
    return render_template('adoptantes.html', adoptantes=adoptantes)

@app.route('/refugios')
def refugios_view():
    return render_template('refugios.html', refugios=refugios)

@app.route('/solicitudes')
def solicitudes_view():
    return render_template('solicitudes.html', solicitudes=solicitudes)

# ---------------------------------------------------------
# Rutas de formularios
# ---------------------------------------------------------
@app.route('/mascotas/agregar', methods=['GET', 'POST'])
def agregar_mascota():
    form = MascotaForm()
    if form.validate_on_submit():
        conn = conectar()
        conn.execute(
            'INSERT INTO mascotas (nombre, tipo, edad, estado) VALUES (?, ?, ?, ?)',
            (form.nombre.data, form.tipo.data, form.edad.data, form.estado.data)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('mascotas_view'))
    return render_template('formulario_mascota.html', form=form)

@app.route('/adoptantes/agregar', methods=['GET', 'POST'])
def agregar_adoptante():
    form = AdoptanteForm()
    if form.validate_on_submit():
        adoptantes.append({
            "nombre": form.nombre.data,
            "cedula": form.cedula.data,
            "telefono": form.telefono.data,
            "mascota_interes": form.mascota_interes.data
        })
        return redirect(url_for('adoptantes_view'))
    return render_template('formulario_adoptante.html', form=form)

@app.route('/refugios/agregar', methods=['GET', 'POST'])
def agregar_refugio():
    form = RefugioForm()
    if form.validate_on_submit():
        refugios.append({
            "nombre": form.nombre.data,
            "ciudad": form.ciudad.data,
            "contacto": form.contacto.data
        })
        return redirect(url_for('refugios_view'))
    return render_template('formulario_refugio.html', form=form)

@app.route('/solicitudes/agregar', methods=['GET', 'POST'])
def agregar_solicitud():
    form = SolicitudForm()
    if form.validate_on_submit():
        solicitudes.append({
            "solicitante": form.solicitante.data,
            "mascota": form.mascota.data,
            "fecha": form.fecha.data,
            "estado": form.estado.data
        })
        return redirect(url_for('solicitudes_view'))
    return render_template('formulario_solicitud.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    
    