from __init__ import *
from wtforms.validators import *

def validate_email(self, email):
    if Users.query.filter_by(email=email.data).first():
        raise ValidationError("Email already registered!")

def validate_uname(self, uname):
    if Users.query.filter_by(username=uname.data).first():
        raise ValidationError("Username already taken!")