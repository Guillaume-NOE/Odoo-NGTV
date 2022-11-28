# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class SecondCategory(models.Model):
    _name = 'second.category'
    _description = 'Second Category'

    name = fields.Char(
        string='Name',
    )
    first_category_id = fields.Many2one(
        string='First category',
        comodel_name='first.category',
        help='First category ID.'
    )
