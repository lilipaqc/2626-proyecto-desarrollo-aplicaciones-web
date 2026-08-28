from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AdoptanteForm(FlaskForm):
    nombre = StringField(
        'Nombre completo',
        validators=[DataRequired(message="El nombre es obligatorio."), Length(min=3, max=80)]
    )
    cedula = StringField(
        'Cédula',
        validators=[DataRequired(message="La cédula es obligatoria."), Length(min=10, max=10, message="La cédula debe tener 10 dígitos.")]
    )
    telefono = StringField(
        'Teléfono',
        validators=[DataRequired(message="El teléfono es obligatorio."), Length(min=7, max=15)]
    )
    mascota_interes = StringField(
        'Mascota de interés',
        validators=[DataRequired(message="Indica la mascota de interés.")]
    )
    enviar = SubmitField('Registrar adoptante')
    