from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class SolicitudForm(FlaskForm):
    id_adoptante = SelectField(
        'Adoptante',
        coerce=int,
        validators=[DataRequired(message="Selecciona un adoptante.")]
    )
    id_mascota = SelectField(
        'Mascota',
        coerce=int,
        validators=[DataRequired(message="Selecciona una mascota.")]
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
    enviar = SubmitField('Guardar solicitud')