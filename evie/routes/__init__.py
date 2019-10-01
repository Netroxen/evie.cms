# -*- coding: utf-8 -*-

from . import admin, auth, base, errors


def init_app(app):
    # Blueprints
    app.register_blueprint(admin.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(errors.bp)
    app.register_blueprint(base.bp)
