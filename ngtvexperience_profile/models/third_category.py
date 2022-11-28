# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class ThirdCategory(models.Model):
    _name = 'third.category'
    _description = 'Third Category'

    name = fields.Char(
        string='Name',
    )
    second_category_id = fields.Many2one(
        string='Second category',
        comodel_name='second.category',
        help='Second category ID.'
    )
