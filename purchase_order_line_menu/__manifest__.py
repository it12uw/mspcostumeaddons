# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (https://akretion.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Purchase Order Line menu",
    "summary": "Adds a menu to see purchase order lines",
    "version": "1.0.1.1.0",
    "author": "Akretion",
    "website": "https://github.com/akretion/flectra-usability",
    "category": "Purchases",
    "depends": ["purchase","marel_in_data_report_purchase_o","sale_margin","sale_report_cost","sale_report_country_state"],
    "data": [
        'views/purchase_order_line.xml',
        'views/sale_order_line.xml',
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
