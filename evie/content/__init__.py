# -*- coding: utf-8 -*-

from flask_zodb import ZODB

db = ZODB()


def init_app(app):
    db.init_app(app)
