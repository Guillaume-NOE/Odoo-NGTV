# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "NgtvExperience Profile",
    'description': """Profile for NgtvExperience""",
    "version": "15.0.1.0.0",
    "author": "Abdelwahed Rihen",
    "website": "https://ngtvexperience.com",
    "depends": [
        'base',
        'helpdesk'
    ],
    "category": "CRM",
    "license": "AGPL-3",
    "data": [
        # Data
        'data/datas.xml',

        # Security
        'security/res_groups.xml',
        'security/ir.model.access.csv',

        # Views
        "views/first_category_view.xml",
        "views/second_category_view.xml",
        "views/third_category_view.xml",
        "views/helpdesk_ticket_view.xml",
    ],
    "installable": True,
    "auto_install": True,
}
