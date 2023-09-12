from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from flask_wtf.file import FileRequired
from wtforms.validators import InputRequired, Email


class ClienteForm():
    username = StringField("Nombre: " ,validators = [InputRequired(message="Debe de ingresar el nombre")] )
    email = StringField("Email",  [InputRequired("Ingrese su correo"), Email("Debe ingresar un correo valido")])

class NewClient(FlaskForm, ClienteForm):
    password = PasswordField("Contraseña: " , validators=[InputRequired(message="Contraseña")])
    submit = SubmitField("Guardar")


class EditClient(FlaskForm, ClienteForm):
    password = PasswordField("Contraseña: " , validators=[InputRequired(message="Contraseña")])
    submit = SubmitField("Actualizar")
