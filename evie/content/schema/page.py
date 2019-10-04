# -*- coding: utf-8 -*-

from wtforms import TextAreaField

from evie.content.schema import BaseForm
from evie.content.types import Item


class IPage(BaseForm):

    text = TextAreaField('Text')


class Page(Item):

    pass
