# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from lxml import etree

from openerp.tests.common import TransactionCase


class TestIrQweb(TransactionCase):

    def setUp(self):
        self.engine = self.env['ir.qweb']

    def _test_element(self, attr, value):
        return etree.Element('span', {
            attr: value,
            'class': 'this-class',
        })

    def test_render_tag_class_add(self):
        el = self._test_element('t-class-add', 'that-class')
        res = self.engine.render_node(el)
        self.assertEqual(
            '<span class="this-class that-class"></span>', res,
        )

    def test_render_tag_class_add(self):
        el = self._test_element('t-class-remove', 'this-class')
        res = self.engine.render_node(el)
        self.assertEqual(
            '<span class=""></span>', res,
        )
