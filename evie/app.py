# coding: utf-8

from quart import Quart

from evie.auth.user import User


class EvieApp(Quart):

    # Database Properties

    @property
    def zodb(self):
        """Returns the ZODB object instance."""
        zodb = self.extensions.get('zodb', None)
        if zodb is not None:
            return zodb.zodb
        raise RuntimeError('Nothing Set!')

    @property
    def db(self):
        """Returns the ZODB object database."""
        zodb = self.extensions.get('zodb', None)
        if zodb is not None:
            return zodb.db
        raise RuntimeError('Nothing Set!')

    @property
    def content(self):
        """Returns the EvieDB class instance."""
        db = self.extensions.get('db', None)
        if db is not None:
            return db
        raise RuntimeError('Nothing Set!')

    # Helper Methods

    def get_user(self, username):
        """Return an account item."""
        return self.zodb['accounts'].get(username, None)

    def create_user(self, *args, **kwargs):
        """Create a new account item."""
        self.content.insert_into('accounts', User(*args, **kwargs))
