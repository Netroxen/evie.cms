# -*- coding: utf-8 -*-

import unittest

from evie import create_app


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(self)
        self.client = self.app.test_client()
