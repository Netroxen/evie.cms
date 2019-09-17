# -*- coding: utf-8 -*-

import os
import quart.flask_patch

from dynaconf import FlaskDynaconf
from dynaconf.loaders import toml_loader
from flask_caching import Cache
from quart import Quart

cache = Cache(config={'CACHE_TYPE': 'simple'})

ENVVAR_PREFIX = 'EVIE'
SETTINGS_FILES = ['env.toml', 'evie.toml']


def create_app(config=None):
    """Initializes the Evie application."""
    from . import auth, content, routes

    # App Instance
    app = Quart(__name__)

    FlaskDynaconf(
        app,
        ENVVAR_PREFIX_FOR_DYNACONF=ENVVAR_PREFIX,
        SETTINGS_FILE_FOR_DYNACONF=SETTINGS_FILES,
        SILENT_ERRORS_FOR_DYNACONF=False,
    )

    # Initialize Extensions
    auth.init_app(app)
    content.init_app(app)
    routes.init_app(app)

    # Initialize Caching
    cache.init_app(app)

    # Check Environment Variables
    if f'{ENVVAR_PREFIX}_CONF' in os.environ:
        app.config.from_envvar(f'{ENVVAR_PREFIX}_CONF')

    # Check Config Variable
    if config is not None:
        # Is a Dict
        if isinstance(config, dict):
            app.config.update(config)
        # Is a Python-File
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    return app
