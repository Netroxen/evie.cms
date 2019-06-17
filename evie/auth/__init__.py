# -*- coding: utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_login import LoginManager

bcrypt = Bcrypt()
login_manager = LoginManager()


def init_app(app):
    bcrypt.init_app(app)
    login_manager.init_app(app)
