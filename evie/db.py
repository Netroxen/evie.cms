# -*- coding: utf-8 -*-

from pathlib import Path

import toml
import transaction
from quart import current_app

from evie.auth.user import Manager
from evie.content.schema.site import Site
from flask_zodb import ZODB, BTree, Dict


class EvieDB(object):

    zodb = ZODB()
    zodb_file = 'Data.fs'

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize a new ZODB database."""

        # Set Defaults
        self.app = app

        # Configure Path Defaults
        self._conf_db_defaults()
        self.zodb.init_app(app)

        # Prevent Event-Loop Blocking
        app.before_serving(self._init_db_defaults)

    def _conf_db_defaults(self) -> None:
        """Update common app config variables."""

        # Set Defaults
        db_dir = self.app.config['DB_DIR']
        zodb_storage = self.app.config['ZODB_STORAGE']
        zodb_blobs = self.app.config['ZODB_BLOBS']

        # Concatenate Paths
        self.storage = Path(db_dir, zodb_storage, self.zodb_file)
        self.blobs = Path(db_dir, zodb_blobs)

        # Update Configuration
        self.app.config['ZODB_STORAGE'] = self.storage.resolve().as_uri()
        self.app.config['ZODB_BLOBS'] = self.blobs.resolve().as_uri()

        if 'db' not in self.app.extensions:
            self.app.extensions['db'] = self

    def _init_db_defaults(self) -> None:
        """Create common database defaults."""

        # Open DB Connection
        cx = self.app.db.open()

        if not hasattr(cx.root, 'db_is_init'):

            # DB Default Tree Items
            zodb_contents = {'accounts': BTree(), 'catalog': BTree()}

            # Load Evie Config
            config_file = Path('config', 'evie.toml')
            config = toml.loads(config_file.read_text())

            # Copy Evie Config to DB
            cx.root.config = Dict(config['evie'])

            # Create Manager Account
            manager = Manager(
                email=self.app.config.ADMIN_EMAIL,
                password=self.app.config.ADMIN_PASSWORD,
                username=self.app.config.ADMIN_USERNAME,
                name=self.app.config.ADMIN_NAME,
            )
            zodb_contents['accounts'][manager.id] = manager

            # Create Site Object
            site = Site(
                title=self.app.config.SITE_TITLE,
                desc=self.app.config.SITE_DESC,
            )
            zodb_contents['catalog'][site.id] = site
            cx.root.config['SITE_ID'] = site.id

            for cat in zodb_contents:
                setattr(cx.root, cat, zodb_contents[cat])

            # Set DB As Initialized
            cx.root.db_is_init = True

            # Commit Changes
            transaction.commit()

        # Close DB Connection
        cx.close()

    async def insert_into(self, container: str, item: object) -> None:
        cat = current_app.zodb[container]
        if cat.has_key(item.id):
            raise KeyError('Item with ID \'%s\' already exists!' % (item.id))
        cat[item.id] = item
