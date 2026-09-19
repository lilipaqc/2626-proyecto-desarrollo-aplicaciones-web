from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from forms.mascota_form import MascotaForm
from forms.adoptante_form import AdoptanteForm
from forms.refugio_form import RefugioForm
from forms.solicitud_form import SolicitudForm
from forms.login_form import LoginForm
from forms.usuario_form import UsuarioForm

from conexion.conexion import get_db_connection
from models import Usuario

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-adoptaya-2026'  # necesaria para CSRF y sesiones

# ---------------------------------------------------------
# Configuración de Flask-Login
# ---------------------------------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Debes iniciar sesión para acceder a esta página."


@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    if data:
        return Usuario(data[0], data[1], data[2])
    return None

# ---------------------------------------------------------
# Datos de ejemplo (estáticos) para los módulos que aún no
# tienen persistencia en base de datos relacional
# ---------------------------------------------------------
adoptantes = [
    {"nombre": "María López", "cedula": "1712345678", "telefono": "0991234567", "mascota_interes": "Rocky"},
    {"nombre": "Carlos Pérez", "cedula": "1798765432", "telefono": "0987654321", "mascota_interes": "Luna"},
    {"nombre": "Andrea Torres", "cedula": "1755566677", "telefono": "0965544332", "mascota_interes": "Michi"},
]

refugios_lista = [
    {"nombre": "Refugio Huellitas", "ciudad": "Quito", "contacto": "huellitas@correo.com"},
    {"nombre": "Patitas Felices", "ciudad": "Ambato", "contacto": "patitasfelices@correo.com"},
    {"nombre": "Segunda Oportunidad", "ciudad": "Quito", "contacto": "segundaoportunidad@correo.com"},
]

solicitudes = [
    {"solicitante": "María López", "mascota": "Rocky", "fecha": "2026-08-10", "estado": "En revisión"},
    {"solicitante": "Carlos Pérez", "mascota": "Luna", "fecha": "2026-08-12", "estado": "Aprobada"},
    {"solicitante": "Andrea Torres", "mascota": "Michi", "fecha": "2026-08-14", "estado": "Pendiente"},
]


def obtener_refugios_choices():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id_refugio, nombre FROM refugios")
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()
    return [(r[0], r[1]) for r in resultado]


# ---------------------------------------------------------
# Rutas principales
# ---------------------------------------------------------
@app.route('/')
def index():
    fecha_actualizacion = "20 de septiembre de 2026"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM mascotas")
    total_mascotas = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    return render_template(
        'index.html',
        fecha_actualizacion=fecha_actualizacion,
        total_mascotas=total_mascotas
    )

@app.route('/adoptantes')
def adoptantes_view():
    return render_template('adoptantes.html', adoptantes=adoptantes)

@app.route('/refugios')
def refugios_view():
    return render_template('refugios.html', refugios=refugios_lista)

@app.route('/solicitudes')
def solicitudes_view():
    return render_template('solicitudes.html', solicitudes=solicitudes)

# ---------------------------------------------------------
# Autenticación: registro, login, logout
# ---------------------------------------------------------
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = UsuarioForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (usuario, password) VALUES (%s, %s)",
                (form.usuario.data, password_hash)
            )
            conn.commit()
            flash("Usuario registrado correctamente. Ahora puedes iniciar sesión.", "success")
            cursor.close()
            conn.close()
            return redirect(url_for('login'))
        except Exception:
            flash("Ese nombre de usuario ya existe. Elige otro.", "danger")
            cursor.close()
            conn.close()

    return render_template('registro.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (form.usuario.data,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()

        if data and check_password_hash(data[2], form.password.data):
            user = Usuario(data[0], data[1], data[2])
            login_user(user)
            flash(f"Bienvenido, {user.usuario}!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Usuario o contraseña incorrectos.", "danger")

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# ---------------------------------------------------------
# CRUD de Mascotas con MySQL (protegido con login)
# ---------------------------------------------------------
@app.route('/mascotas')
@login_required
def mascotas_view():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT m.id_mascota, m.nombre, m.tipo, m.edad, m.estado,
               r.nombre AS refugio_nombre
        FROM mascotas m
        LEFT JOIN refugios r ON m.id_refugio = r.id_refugio
    ''')
    mascotas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('mascotas.html', mascotas=mascotas)

@app.route('/mascotas/agregar', methods=['GET', 'POST'])
@login_required
def agregar_mascota():
    form = MascotaForm()
    form.id_refugio.choices = obtener_refugios_choices()

    if form.validate_on_submit():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mascotas (nombre, tipo, edad, estado, id_refugio) VALUES (%s, %s, %s, %s, %s)",
            (form.nombre.data, form.tipo.data, form.edad.data, form.estado.data, form.id_refugio.data)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('mascotas_view'))

    return render_template('formulario_mascota.html', form=form, titulo="Registrar Mascota")

@app.route('/mascotas/editar/<int:id_mascota>', methods=['GET', 'POST'])
@login_required
def editar_mascota(id_mascota):
    form = MascotaForm()
    form.id_refugio.choices = obtener_refugios_choices()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if form.validate_on_submit():
        cursor.execute(
            "UPDATE mascotas SET nombre = %s, tipo = %s, edad = %s, estado = %s, id_refugio = %s WHERE id_mascota = %s",
            (form.nombre.data, form.tipo.data, form.edad.data, form.estado.data, form.id_refugio.data, id_mascota)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('mascotas_view'))

    cursor.execute("SELECT * FROM mascotas WHERE id_mascota = %s", (id_mascota,))
    mascota = cursor.fetchone()
    cursor.close()
    conn.close()

    if mascota:
        form.nombre.data = mascota['nombre']
        form.tipo.data = mascota['tipo']
        form.edad.data = mascota['edad']
        form.estado.data = mascota['estado']
        form.id_refugio.data = mascota['id_refugio']

    return render_template('formulario_mascota.html', form=form, titulo="Editar Mascota")

@app.route('/mascotas/eliminar/<int:id_mascota>')
@login_required
def eliminar_mascota(id_mascota):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM mascotas WHERE id_mascota = %s", (id_mascota,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('mascotas_view'))

# ---------------------------------------------------------
# Formularios de otros módulos (siguen con listas en memoria)
# ---------------------------------------------------------
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
        refugios_lista.append({
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
    