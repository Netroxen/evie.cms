# -*- coding: utf-8 -*-

from pathlib import Path

import toml
import transaction
from quart import copy_current_request_context, current_app

from flask_zodb import ZODB, BTree, Dict


class EvieDB(object):

    zodb = ZODB()
    zodb_file = 'Data.fs'

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize a new ZODB database."""

        self._update_common(app)
        self.zodb.init_app(app)
        self._create_common(app)

    def _update_common(self, app):
        """Update common app config variables."""

        # Set Defaults
        db_dir = app.config['DB_DIR']
        zodb_storage = app.config['ZODB_STORAGE']
        zodb_blobs = app.config['ZODB_BLOBS']

        # Concatenate Paths
        self.storage = Path(db_dir, zodb_storage, self.zodb_file)
        self.blobs = Path(db_dir, zodb_blobs)

        # Update Configuration
        app.config['ZODB_STORAGE'] = self.storage.resolve().as_uri()
        app.config['ZODB_BLOBS'] = self.blobs.resolve().as_uri()

        if 'db' not in app.extensions:
            app.extensions['db'] = self

    def _create_common(self, app):
        """Create common database defaults."""

        zodb = app.extensions['zodb']
        data = zodb.db

        # Open DB Connection
        cx = data.open()

        if not hasattr(cx.root, 'db_is_init'):

            zodb_contents = {'accounts': BTree(), 'catalog': BTree()}

            config_file = Path('config', 'evie.toml')
            config = toml.loads(config_file.read_text())

            # Copy Config
            cx.root.config = Dict(config['evie'])

            for cat in zodb_contents:
                setattr(cx.root, cat, zodb_contents[cat])

            # Set DB As Initialized
            cx.root.db_is_init = True

            # Commit Changes
            transaction.commit()

        # Close DB Connection
        cx.close()

    def insert_into(self, container, item):
        cat = current_app.zodb[container]
        if cat.has_key(item.id):
            raise KeyError(
                'Item with ID \'{0}\' already exists!'.format(item.id)
            )
        cat[item.id] = item
