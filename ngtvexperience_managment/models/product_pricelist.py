# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    discount_max = fields.Float(
        string='Discount Max',
    )
