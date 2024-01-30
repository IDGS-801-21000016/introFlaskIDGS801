
from flask_wtf import Form
from wtforms import StringField, IntegerField, EmailField
# importamos los validadores de WTForms
from wtforms.validators import DataRequired, Email



class UserForm(Form):
    nombre = StringField('nombre')
    a_paterno = StringField('Apaterno')
    a_materno = StringField('Amaterno')
    edad = IntegerField('edad')
    email = EmailField('email')