# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    """The registration form"""

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

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
        ],
    )

    confirm_password = PasswordField(
        'Confirm password',
        validators=[
            DataRequired(),
            EqualTo('password'),
        ],
    )

    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    """The login form"""

    username = StringField(
        'Username',
        validators=[
            DataRequired(),
        ],
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
        ],
    )

    remember = BooleanField('Remember me')

    submit = SubmitField('Log in')
