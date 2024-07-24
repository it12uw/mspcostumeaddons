# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Add Report Kwitansi',
    'author': 'Art in Heaven',
    'version' : '1.1',
    'summary': 'Kwitansi',
    'sequence': 30,
    'description': """
Add Report Kwitansi
    """,
    'category': 'Accounting',
    'website': '',
    'images' : [''],
    'depends' : ['account','web','web_digital_sign'],
    'data': [
        'views/account_report.xml',
        'report/report_invoice_inherit.xml',
        'views/kwitansi_ship.xml',
        # 'views/report_template_financeinfo_inherit.xml',
        # 'views/account_invoice_view.xml',

    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
