# -*- coding: utf-8 -*-

import os

from flask_caching import Cache
from quart import Quart

cache = Cache(config={'CACHE_TYPE': 'simple'})


def create_app(config=None):
    """Initializes the Evie application."""
    from . import models, routes, utils

    # App Instance
    app = Quart(__name__)

    # Parse Config (config.yaml)
    app.config.from_mapping(utils.parse_config(app))

    # Initialize Extensions
    models.init_app(app)
    routes.init_app(app)

    # Initialize Caching
    cache.init_app(app)

    # Check Environment Variables
    if 'FLASK_CONF' in os.environ:
        app.config.from_envvar('FLASK_CONF')

    # Check Config Variable
    if config is not None:
        # Is a Dict
        if isinstance(config, dict):
            app.config.update(config)
        # Is a Python-File
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    return app
