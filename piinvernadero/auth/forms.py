from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from piinvernadero.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired(_l("Username is required"))])
    password = PasswordField(_l('Password'), validators=[DataRequired(_l("Password is required"))])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired(_l("Username is required"))])
    email = StringField(_l('Email'), validators=[DataRequired(_l("Email is required")), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired(_l("Password is required"))])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(_l("Password confirmation is required")), EqualTo('password',_l('Passwords must match'))])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different email address.'))
