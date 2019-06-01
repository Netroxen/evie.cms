# -*- coding: utf-8 -*-

from flask_zodb import List

from . import models


class Folder(models.ContentType):

    contents = List()

    async def __init__(self, contents=None):
        super(Folder, self).__init__
        self.update_contents(contents)

    async def update_contents(self, contents):
        for item in contents:
            self.contents.append(item)


class Page(models.ContentType):

    text = ''

    async def __init__(self, text=None):
        super(Page, self).__init__
        self.text = text
