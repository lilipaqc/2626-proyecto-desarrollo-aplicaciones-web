from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class MascotaForm(FlaskForm):
    nombre = StringField(
        'Nombre de la mascota',
        validators=[DataRequired(message="El nombre es obligatorio."), Length(min=2, max=50)]
    )
    tipo = SelectField(
        'Tipo de animal',
        choices=[('', '-- Selecciona --'), ('Perro', 'Perro'), ('Gato', 'Gato'), ('Conejo', 'Conejo'), ('Otro', 'Otro')],
        validators=[DataRequired(message="Selecciona un tipo de animal.")]
    )
    edad = StringField(
        'Edad',
        validators=[DataRequired(message="La edad es obligatoria."), Length(max=20)]
    )
    estado = SelectField(
        'Estado',
        choices=[('', '-- Selecciona --'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')],
        validators=[DataRequired(message="Selecciona el estado de la mascota.")]
    )
    enviar = SubmitField('Registrar mascota')
    