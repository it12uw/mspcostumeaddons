# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (https://akretion.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "msp_qc_mrp_inline_report",
    "summary": "msp_qc_mrp_inline_report",
    "version": "1.0.1.1.0",
    "author": "msp_qc_mrp_inline_report",
    "website": "https://github.com/akretion/flectra-usability",
    # "category": "Purchases",
    # "depends": ["stock","marel_in_data_stock_picking"],
    'depends': ['msp_qc_mrp_menu','product', 'barcodes', 'stock', 'marel_in_data_product','marel_in_mrp_production','marel_mesin_kerusakan','marel_in_work_order','mrp'],
    "data": [
        'report/menu_report.xml',
        'report/msp_qc_mrp_inline1_report_template.xml',
        'report/msp_qc_mrp_inline2_report_template.xml',
        'report/msp_qc_mrp_inline3_report_template.xml',
        'report/msp_qc_mrp_inline4_report_template.xml',
        'report/msp_qc_inline_garment_report_template.xml',
        'report/msp_qc_endline_garment_report_template.xml',    ],
    "js": [
        # 'static/src/js/buttons_hide.js',
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
