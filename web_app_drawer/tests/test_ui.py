# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from openerp.tests import HttpCase


class TestUi(HttpCase):

    def test_web_app_drawer_tour(self):
        self.phantom_js(
            '/web',
            "openerp.Tour.run('test_web_app_drawer', 'test')",
            "openerp.Tour.tours.test_web_app_drawer",
            login="admin"
        )
