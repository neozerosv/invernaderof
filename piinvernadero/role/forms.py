from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from flask_babel import _, lazy_gettext as _l
from piinvernadero.models import Role

class RoleCreateForm(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired(_l("Name is required"))])
    description = TextAreaField(_l('Description'), validators=[Length(min=0, max=200)])
    submit = SubmitField(_l('Add'))

    def validate_name(self, name):
        rolename = Role.query.filter_by(name=name.data).first()
        if rolename is not None:
            raise ValidationError(_l('Please use a different role name.'))

