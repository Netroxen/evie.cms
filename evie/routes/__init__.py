# -*- coding: utf-8 -*-

from flask_login import current_user, login_user
from quart import current_app, redirect, request, url_for

from evie.auth.user import ManagerUser

from . import admin, auth, base, errors


def init_app(app):
    # Blueprints
    app.register_blueprint(admin.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(errors.bp)
    app.register_blueprint(base.bp)
    # Methods
    app.before_request(app_before_request)


def app_before_request():
    if not current_app.app_is_init:
        pass
