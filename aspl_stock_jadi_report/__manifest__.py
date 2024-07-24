# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
{
    'name': 'Odoo Stock Jadi Report',
    'version': '1.0',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'summary': 'This module allows you to generate Stock Inventory Report with PDF and XLS format.',
    'description' :"""This module allows you to generate Stock Inventory Report with PDF and XLS format.""",
    'category': 'Stock',
    'website': 'http://www.acespritech.com',
    'depends': ['base', 'stock','aspl_stock_inventory_report'],
    'price': 35,
    'currency': 'EUR',
    'images': [
        'static/description/main_screenshot.png',
    ],
    'data': [
            'wizard/wizard_stock_jadi_report_view.xml',
            'report/report.xml',
            # 'data/inventory_mail_template.xml',
            'report/report_stock_jadi.xml',
            # 'views/res_config_setting.xml',
            # 'views/stock_location.xml',
            'security/ir.model.access.csv',
        ],
    'installable': True,
    'auto_install': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: