# -*- coding: utf-8 -*-

import os

import yaml

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def parse_config(path='config.yaml', flatten=False):
    """Return config from a provided YAML file."""
    file_path = os.path.join(APP_ROOT, path)
    # Try to open the file
    try:
        with open(file_path, 'r') as yaml_file:
            config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    except IOError:
        return
    # Flatten key, value dicts to single depth
    if flatten:
        flattened_config = dict()
        for key in config:
            values = config[key]
            for item in values:
                flattened_config[item] = values[item]
        return flattened_config
    return config
