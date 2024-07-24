# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (https://akretion.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "msp_qc_mrp_menu",
    "summary": "msp_qc_mrp_menu",
    "version": "1.0.1.1.0",
    "author": "msp_qc_mrp_menu",
    "website": "https://github.com/akretion/flectra-usability",
    # "category": "Purchases",
    # "depends": ["stock","marel_in_data_stock_picking"],
    'depends': ["product", "barcodes", "stock", "marel_in_data_product","marel_in_mrp_production","marel_mesin_kerusakan","marel_in_work_order","mrp"],
    "data": [
        # 'views/msp_qc_mrp_menu.xml',
        'views/msp_memo_qc_inline.xml',
        'views/menu_qc.xml',
        'views/ir_sequence.xml',
        'wizard/msp_memoqc_inline_wizard.xml',
        'views/inherit_button_qc.xml',
        'views/msp_in_work_order.xml',
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
