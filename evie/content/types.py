# -*- coding: utf-8 -*-

from slugify import slugify

from flask_zodb import List, Object


class ContentType(Object):

    _id = ''
    _title = ''
    _desc = ''

    def __repr__(self):
        """
        Input:
            ContentType(title='Item Title')
        Output:
            ContentType('item-title')
        """
        return self.__class__.__name__ + '(\'{0}\')'.format(self._id)

    def __init__(self, title, *args, **kwargs):
        # Mandatory
        self._id = slugify(title)
        self._title = title
        # Optional
        if 'desc' in kwargs:
            self._desc = kwargs.pop('desc')

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value


class Container(ContentType):

    _contents = List()

    @property
    def list_contents(self):
        return self._contents


class Site(Container):

    pass


class Item(ContentType):

    pass
