# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (https://akretion.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "marel_stock_picking_menu",
    "summary": "marel_stock_picking_menu",
    "version": "1.0.1.1.0",
    "author": "marel_stock_picking_menu",
    "website": "https://github.com/akretion/flectra-usability",
    # "category": "Purchases",
    # "depends": ["stock","marel_in_data_stock_picking"],
    'depends': ['product', 
                'barcodes', 
                'web_planner', 
                'base_branch_company',
                'stock',
                'marel_in_data_stock_picking',
                'account',
                'marel_in_stock_picking'],
    "data": [
        'views/marel_stock_picking_menu.xml',
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
