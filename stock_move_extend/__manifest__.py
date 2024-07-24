# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Moves Extent Search',
    'author': 'Art-In-Heaven',
    'version': '1.0',
    'summary': 'Inventory, Logistics, Warehousing',
    'description': "",
    'website': "https://gitlab.com/art-in-heaven",
    'depends': ['base','stock','product','account','sale_stock','marel_in_stock_picking'],
    'category': 'Warehouse',
    'data': [
        'views/stock_move_extend_view.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
