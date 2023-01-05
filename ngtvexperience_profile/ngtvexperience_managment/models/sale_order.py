# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, api, _
from odoo.exceptions import ValidationError
from odoo.tools import float_compare, float_is_zero


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('pricelist_id')
    def _onchange_order_discount(self):
        """ Function to controle if user has depassed maximun value of dicount defined on current pricelist. """
        if self.pricelist_id and not float_is_zero(self.pricelist_id.discount_max, precision_digits=3):
            discount_max = self.pricelist_id.discount_max
            if self.order_line:
                for line in self.order_line:
                    if float_compare(line.discount, line.order_id.pricelist_id.discount_max, 3) > 0:
                        raise ValidationError(_('The maximum value of discounts not to be exceeded is ' + str(discount_max)))
