# -*- coding: utf-8 -*-

from . import errors, public


def init_app(app):
    app.register_blueprint(errors.bp)
    app.register_blueprint(public.bp)
