# -*- coding: utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_zodb import ZODB

from . import content, forms, models

db = ZODB()
bcrypt = Bcrypt()


def init_app(app):
    db.init_app(app)
    bcrypt.init_app(app)
