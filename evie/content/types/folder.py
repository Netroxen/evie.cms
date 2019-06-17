# -*- coding: utf-8 -*-

from evie.content.types import Container
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class IFolder(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])


class Folder(Container):

    pass
