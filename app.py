from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------
# Datos de ejemplo (estáticos), todavía no hay base de datos
# ---------------------------------------------------------
mascotas = [
    {"nombre": "Rocky", "tipo": "Perro", "edad": "2 años", "estado": "Disponible"},
    {"nombre": "Michi", "tipo": "Gato", "edad": "1 año", "estado": "Disponible"},
    {"nombre": "Toby", "tipo": "Perro", "edad": "4 años", "estado": "Adoptado"},
    {"nombre": "Luna", "tipo": "Conejo", "edad": "8 meses", "estado": "Disponible"},
    {"nombre": "Simba", "tipo": "Gato", "edad": "3 años", "estado": "Adoptado"},
]

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
# Rutas
# ---------------------------------------------------------
@app.route('/')
def index():
    fecha_actualizacion = "23 de agosto de 2026"
    total_mascotas = len(mascotas)
    return render_template(
        'index.html',
        fecha_actualizacion=fecha_actualizacion,
        total_mascotas=total_mascotas
    )

@app.route('/mascotas')
def mascotas_view():
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

if __name__ == '__main__':
    app.run(debug=True)
    
    