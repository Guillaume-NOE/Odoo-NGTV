# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import models, fields


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project ID',
        help="Project ID"
    )
