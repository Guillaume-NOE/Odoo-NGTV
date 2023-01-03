# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "NgtvExperience Management",
    'description': """Profile for NC2C OKDOM""",
    "version": "16.0.1.0.1",
    "author": "Abdelwahed Rihen",
    "depends": [
        'base',
        'product',
        'hr_expense',
        'sale',
        'project'
    ],
    "category": 'Sales',
    "license": "AGPL-3",
    "data": [
        # Security
        "security/res_groups.xml",

        # Views
        "views/hr_expense_view.xml",
        "views/product_pricelist_view.xml",
        "views/res_partner_view.xml",
    ],
    "installable": True,
    "auto_install": True,
}
