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
        return self.extensions.get('db', None)

    # Helper Methods

    def get_site(self) -> None:
        """Return the site root."""
        id = self.zodb['config'].get('SITE_ID', None)
        return self.zodb['catalog'].get(id, None)

    def get_user(self, username: str) -> User:
        """Return an account item."""
        return self.zodb['accounts'].get(username, None)

    async def create_user(self, *args, **kwargs) -> None:
        """Create a new account item."""
        await self.content.insert_into('accounts', User(*args, **kwargs))
