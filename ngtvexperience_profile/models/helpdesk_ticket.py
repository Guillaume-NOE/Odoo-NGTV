# -*- coding: utf-8 -*-
# Copyright 2022 Subteno (https://www.subteno.com).
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    first_category_id = fields.Many2one(
        string='First catgory',
        comodel_name='first.category',
        help='First category ID.'
    )
    second_category_id = fields.Many2one(
        string='Second catgory',
        comodel_name='second.category',
        domain=[('first_category_id', '=', first_category_id)],
        help='Second category ID.'
    )
    third_category_id = fields.Many2one(
        string='Third catgory',
        comodel_name='third.category',
        domain=[('second_category_id', '=', second_category_id)],
        help='Third category ID.'
    )

    @api.onchange('first_category_id', 'second_category_id')
    def onchange_category_ids(self):
        if self.first_category_id and self.second_category_id and self.second_category_id.first_category_id:
            if self.second_category_id.first_category_id != self.first_category_id:
                self.second_category_id = False
        if self.second_category_id and self.third_category_id and self.third_category_id.second_category_id:
            if self.third_category_id.second_category_id != self.second_category_id:
                self.third_category_id = False
