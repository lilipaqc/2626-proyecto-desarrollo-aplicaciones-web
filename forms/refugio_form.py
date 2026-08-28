from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RefugioForm(FlaskForm):
    nombre = StringField(
        'Nombre del refugio',
        validators=[DataRequired(message="El nombre del refugio es obligatorio."), Length(min=3, max=80)]
    )
    ciudad = StringField(
        'Ciudad',
        validators=[DataRequired(message="La ciudad es obligatoria.")]
    )
    contacto = StringField(
        'Correo de contacto',
        validators=[DataRequired(message="El correo de contacto es obligatorio."), Email(message="Ingresa un correo válido.")]
    )
    enviar = SubmitField('Registrar refugio')
    