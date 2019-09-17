# -*- coding: utf-8 -*-

from evie.tests import TestCase


class TestRender(TestCase):

    def test_index_renders_template(self):
        response = self.client.get('/')
        self.assertIn(b'<title>', response.data)
