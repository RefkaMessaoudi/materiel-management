# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Materiel Mangement',
    'version': '1.0.0',
    'category': 'Products',
    'description': """Materiel Management""",
    'depends': ['crm', 'stock'],
    'data': [
             'security/ir.model.access.csv',
             'views/menu_views.xml',
             'views/product_templete_views.xml',
             'views/res_country_views.xml',

             ],
    'images': [
               ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}

