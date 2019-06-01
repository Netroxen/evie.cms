# -*- coding: utf-8 -*-

from flask_login import UserMixin
from flask_zodb import List, Object
from slugify import slugify

from . import models


class User(Object, UserMixin):

    name = ''
    roles = List()

    async def __repr__(self):
        """
        Output:
            User('username', 'username@example.com')
        """
        return self.__class__.__name__ + '(\'{0}\', \'{1}\')'.format(
            self.username,
            self.email,
        )

    async def __init__(self, email, password, username, name=None, roles=None):
        self.email = email.lower()
        self.set_password(password)
        self.username = username
        self.name = name
        self.set_roles(roles)

    async def set_password(self, password):
        self.pass_hash = models.bcrypt.generate_password_hash(password)

    async def check_password(self, password):
        return await models.bcrypt.check_password_hash(self.pass_hash, password)

    async def set_roles(self, roles):
        for role in roles:
            self.roles.append(role)
        self.roles = set(self.roles)


class ContentType(Object):

    description = ''

    async def __repr__(self):
        """
        Output:
            ContentType('Title')
        """
        return self.__class__.__name__ + '(\'{0}\')'.format(self.title)

    async def __init__(self, title, description=None):
        self.slug = slugify(title)
        self.title = title
        self.description = description