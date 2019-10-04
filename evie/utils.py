# -*- coding: utf-8 -*-


def class_from_str(path: str):
    path_list = list(filter(None, path.split('.')))
    klass = path_list[-1]
    module_import = __import__('.'.join(path_list[:-1]), fromlist=[klass])
    return getattr(module_import, klass)
