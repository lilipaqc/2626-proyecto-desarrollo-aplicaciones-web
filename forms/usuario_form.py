from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class UsuarioForm(FlaskForm):
    usuario = StringField(
        'Usuario',
        validators=[DataRequired(message="El usuario es obligatorio."), Length(min=3, max=50)]
    )
    password = PasswordField(
        'Contraseña',
        validators=[DataRequired(message="La contraseña es obligatoria."), Length(min=4, message="Mínimo 4 caracteres.")]
    )
    confirmar = PasswordField(
        'Confirmar contraseña',
        validators=[DataRequired(message="Confirma tu contraseña."), EqualTo('password', message="Las contraseñas no coinciden.")]
    )
    enviar = SubmitField('Registrarse')