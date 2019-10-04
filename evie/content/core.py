# -*- coding: utf-8 -*-

from pathlib import Path

import toml

from evie.utils import class_from_str

content_path = Path(__file__).parent


class ContentTypes(object):

    config_file = content_path / 'types.toml'
    items = dict()

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Register ContentType Definitions
        self.load_config(app)
        # Register Extension
        if 'types' not in app.extensions:
            app.extensions['types'] = self

    def get_config(self):
        file_output = self.config_file.read_text()
        return toml.loads(file_output)

    def load_config(self, app):
        config = self.get_config()
        for item in config:
            cx = ContentType(id=item, **config[item])
            self.items[item] = cx
            setattr(self, item, cx)


class ContentType(object):

    id = ''
    title = ''
    desc = ''

    _template = ''
    _schema = None
    _klass = None

    access_perm = ''
    allowed_types = list()

    def __repr__(self):
        return '<ContentType {0}>'.format(self.title)

    def __init__(self, id: str,
                 title: str, template: str,
                 schema: str, klass: str,
                 *args, **kwargs):
        # Mandatory
        self.id = id
        self.title = title
        self.template = template
        # Classes
        self._schema = schema
        self._klass = klass
        # Optional
        if 'desc' in kwargs:
            self.desc = kwargs.pop('desc')
        if 'access_perm' in kwargs:
            self.access_perm = kwargs.pop('access_perm')
        if 'allowed_types' in kwargs:
            self.allowed_types = kwargs.pop('allowed_types')

    @property
    def schema(self):
        return class_from_str(self._schema)

    @property
    def klass(self):
        return class_from_str(self._klass)
