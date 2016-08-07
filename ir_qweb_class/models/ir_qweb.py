# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class IrQweb(models.Model):
    _inherit = 'ir.qweb'

    def render_tag_class_add(self, element, template_attributes,
                             generated_attributes, qwebcontext
                             ):
        """ It adds a defined class to an element """
        expr = template_attributes['class-add']
        element.attr['class'] = element.attr.get('class', '') + ' %s' % expr
        return self.render_element(
            element, template_attributes, generated_attributes, qwebcontext
        )

    def render_tag_class_remove(self, element, template_attributes,
                             generated_attributes, qwebcontext
                             ):
        """ It removes a defined class to an element """
        expr = template_attributes['class-remove']
        cls = element.attr.get('class', '').replace(expr, '').strip()
        element.attr['class'] = cls
        return self.render_element(
            element, template_attributes, generated_attributes, qwebcontext
        )
