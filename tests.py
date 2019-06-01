# -*- coding: utf-8 -*-

import unittest

from evie import create_app


class TestPublic(unittest.TestCase):

    TESTING = True

    def setUp(self):
        self.app = create_app(self)
        self.client = self.app.test_client()

    def test_index_renders_template(self):
        response = self.client.get('/')
        self.assertIn(b'<title>', response.data)


if __name__ == '__main__':
    unittest.main()
