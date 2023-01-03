# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_active = fields.Boolean(
        string='Active',
        readonly='_compute_is_readonly'
    )
    administrative_validation = fields.Boolean(
        string='Administrative Validation',
    )
    current_user_is_active = fields.Boolean(
        string='Current user is active',
        compute='_compute_current_user_is_active',
        help='Used to show or hide element in form view if the current user is active.'
    )
    has_administrative_validation = fields.Boolean(
        string='Current user has administrative validation',
        compute='_compute_current_user_validation',
        help='Used to show or hide element in form view if the current user has administrative validation.'
    )

    def _compute_current_user_is_active(self):
        """ Function to check if current user has access to group_active_res_partner. """
        for user in self:
            user.current_user_is_active = self.env.user.has_group('ngtvexperience_managment.group_active_res_partner')

    def _compute_current_user_validation(self):
        """ Function to check if current user has access to group_active_res_partner. """
        for user in self:
            user.has_administrative_validation = self.env.user.has_group('ngtvexperience_managment.group_administrative_res_partner')

