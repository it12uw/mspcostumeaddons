# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Add Report Order',
    'author': 'Art in Heaven',
    'version' : '1.1',
    'summary': 'Order Confirmation',
    'sequence': 30,
    'description': """
Add Report Order
    """,
    'category': 'Sales',
    'website': '',
    'images' : [''],
    'depends' : [
        'sale',
        'stock',
        'purchase',
        'account',
        'web_digital_sign',
    ],
    'data': [
        'report/report_confirmation.xml',
        'report/marel_report_menu.xml',
        # 'report/purchase_order_templates.xml',
        # 'report/purchase_order_templates_tax.xml',
        # 'report/purchase_reports.xml',
        'views/purchase_views.xml',
        'views/sale_views.xml',
        'views/stock_picking_form_views_approval.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
