from dataclasses import dataclass
from flask_wtf import Form
from wtforms import StringField, TelField, EmailField



@dataclass
class UserForm(Form):
    nombre = StringField('nombre')
    email = EmailField('email')
    a_paterno = StringField('a_paterno')