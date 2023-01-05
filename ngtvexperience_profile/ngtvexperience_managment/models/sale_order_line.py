# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, api, _
from odoo.exceptions import ValidationError
from odoo.tools import float_compare, float_is_zero


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('discount')
    def _onchange_order_line_discount(self):
        """ Function to control if user has not repected maximun value of discount defined on current pricelist. """
        if self.order_id and self.order_id.pricelist_id:
            if not float_is_zero(self.order_id.pricelist_id.discount_max, precision_digits=3):
                if float_compare(self.discount, self.order_id.pricelist_id.discount_max, 3) > 0:
                    discount_max = self.order_id.pricelist_id.discount_max
                    raise ValidationError(_('The maximum value of discounts not to be exceeded is ' + str(discount_max)))
