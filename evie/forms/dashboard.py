# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email, EqualTo, Length


class DashboardAccountForm(FlaskForm):
    """The dashboard account form"""

    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=3, max=20),
        ],
    )

    email = StringField(
        'E-Mail',
        validators=[
            DataRequired(),
            Email(),
        ],
    )

    save = SubmitField('Save')


class DashboardApplicationForm(FlaskForm):
    """The dashboard application form"""

    site_title = StringField(
        'Site Title',
        validators=[DataRequired()],
    )

    user_login_method = SelectField(
        'User Login-Method',
        choices=[
            ('email', 'E-Mail'),
            ('user', 'Username'),
            ('emus', 'E-Mail or Username'),
        ],
    )

    reg_enabled = BooleanField('Enable User-Registration')

    save = SubmitField('Save')


class DashboardDevelopmentForm(FlaskForm):
    """The dashboard development form"""

    debug_mode = BooleanField('Enable Debug-Mode')

    save = SubmitField('Save')
