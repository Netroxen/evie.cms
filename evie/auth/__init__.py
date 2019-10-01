# -*- coding: utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from quart import current_app

bcrypt = Bcrypt()

# LoginManager Configuration

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    user = current_app.get_user(user_id)
    return user


def init_app(app):
    bcrypt.init_app(app)
    login_manager.init_app(app)
