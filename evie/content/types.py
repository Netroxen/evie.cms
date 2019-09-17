# -*- coding: utf-8 -*-

from flask_zodb import List, Object


class ContentType(Object):

    _title = ''
    _desc = ''

    async def __repr__(self):
        """
        Output:
            ContentType('Title')
        """
        return self.__class__.__name__ + '(\'{0}\')'.format(self._title)

    async def __init__(self, *args, **kwargs):
        if 'title' in kwargs:
            self._title = kwargs.pop('title')
        if 'desc' in kwargs:
            self._desc = kwargs.pop('desc')

    @property
    async def title(self):
        return self._title

    @title.setter
    async def set_title(self, value):
        self._title = value

    @property
    async def desc(self):
        return self._desc

    @desc.setter
    async def set_desc(self, value):
        self._desc = value


class Container(ContentType):

    _contents = List()

    async def __init__(self):
        super(Container, self).__init__
        if 'contents' in self.kwargs:
            self.update_contents(self.kwargs.pop('contents'))

    @property
    async def list_contents(self):
        return self._contents

    async def update_contents(self, contents):
        if contents:
            for item in contents:
                self._contents.append(item)
        return contents


class Item(ContentType):

    async def __init__(self):
        super(Item, self).__init__
