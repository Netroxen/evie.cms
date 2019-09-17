# -*- coding: utf-8 -*-

from evie import create_app, SETTINGS_FILES

app = create_app()

if __name__ == '__main__':
    app.run(extra_files=SETTINGS_FILES)
