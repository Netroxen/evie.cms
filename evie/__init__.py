# -*- coding: utf-8 -*-

import os

import quart.flask_patch
from dynaconf import FlaskDynaconf
from flask_caching import Cache

from evie.app import EvieApp
from evie.content.core import ContentTypes
from evie.db import EvieDB

cache = Cache(config={'CACHE_TYPE': 'simple'})
database = EvieDB()
contenttypes = ContentTypes()

ENVVAR_PREFIX = 'EVIE'
SETTINGS_FILES = ['env.toml', 'evie.toml']


def create_app(config=None):
    """Initializes the Evie application."""
    from evie import auth, routes

    # App Instance
    app = EvieApp(__name__)

    FlaskDynaconf(
        app,
        ENVVAR_PREFIX_FOR_DYNACONF=ENVVAR_PREFIX,
        SETTINGS_FILE_FOR_DYNACONF=SETTINGS_FILES,
        SILENT_ERRORS_FOR_DYNACONF=False,
    )

    # Initialize Database
    database.init_app(app)

    # Initialize Modules
    auth.init_app(app)
    routes.init_app(app)

    contenttypes.init_app(app)

    # Initialize Caching
    cache.init_app(app)

    # Check Config Variable
    if config is not None:
        # Is a Dict
        if isinstance(config, dict):
            app.config.update(config)
        # Is a Python-File
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    # Check Environment Variables
    if f'{ENVVAR_PREFIX}_CONF' in os.environ:
        app.config.from_envvar(f'{ENVVAR_PREFIX}_CONF')

    return app
