# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from evie.content.types import Container


class BaseForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])

    desc = StringField('Description', validators=[DataRequired()])
