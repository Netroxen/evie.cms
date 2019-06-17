# -*- coding: utf-8 -*-

from evie.content.types import Item
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class IPage(FlaskForm):

    title = StringField('Title', validators=[DataRequired()])


class Page(Item):

    pass
