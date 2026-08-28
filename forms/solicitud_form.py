from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class SolicitudForm(FlaskForm):
    solicitante = StringField(
        'Nombre del solicitante',
        validators=[DataRequired(message="El nombre del solicitante es obligatorio.")]
    )
    mascota = StringField(
        'Mascota solicitada',
        validators=[DataRequired(message="Indica la mascota solicitada.")]
    )
    fecha = StringField(
        'Fecha (AAAA-MM-DD)',
        validators=[DataRequired(message="La fecha es obligatoria.")]
    )
    estado = SelectField(
        'Estado de la solicitud',
        choices=[('', '-- Selecciona --'), ('Pendiente', 'Pendiente'), ('En revisión', 'En revisión'), ('Aprobada', 'Aprobada')],
        validators=[DataRequired(message="Selecciona el estado de la solicitud.")]
    )
    enviar = SubmitField('Registrar solicitud')
    