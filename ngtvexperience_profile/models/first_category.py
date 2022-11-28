# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class FirstCategory(models.Model):
    _name = 'first.category'
    _description = 'First Category'

    name = fields.Char(
        string='Name',
    )
