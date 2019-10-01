# -*- coding: utf-8 -*-

from flask_login import UserMixin

from evie.auth import bcrypt
from flask_zodb import Object


class User(Object, UserMixin):

    _name = ''
    _id = ''

    def __repr__(self):
        """
        Output:
            User('username')
        """
        return self.__class__.__name__ + '(\'{0}\')'.format(self.username)

    def __init__(self, email, password, username, *args, **kwargs):
        self._id = username
        # Mandatory
        self.email = email
        self.set_password(password)
        self.username = username
        # Optional
        if 'name' in kwargs:
            self._name = kwargs.pop('name')

    def set_password(self, password):
        self.pass_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.pass_hash, password)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def is_manager(self):
        return False


class Manager(User):
    """The manager is granted all privileges."""

    def is_manager(self):
        return True
