# -*- coding: utf-8 -*-
# Copyright 2018 Akretion (https://akretion.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "msp_qc_mrp_inline",
    "summary": "msp_qc_mrp_inline",
    "version": "1.0.1.1.0",
    "author": "msp_qc_mrp_inline",
    "website": "https://github.com/akretion/flectra-usability",
    # "category": "Purchases",
    # "depends": ["stock","marel_in_data_stock_picking"],
    'depends': ['msp_qc_mrp_menu','product', 'barcodes', 'stock', 'marel_in_data_product','marel_in_mrp_production','marel_mesin_kerusakan','marel_in_work_order','mrp'],
    "data": [
        # ------------------------- view inline menu ----------------------------
        'views/msp_qc_inline1.xml',
        'views/msp_qc_inline2.xml',
        'views/msp_qc_inline3.xml',
        'views/msp_qc_inline4.xml',
        'views/menu_msp_qc_inline.xml',
        'views/msp_qc_inline_garment.xml',
        'views/msp_qc_endline_garment.xml',
        # -----------------------------------------------------------------------------
        'views/ir_sequence.xml',
        # 'views/menu_msp_qc_mrp_inline.xml',
        # 'views/msp_qc_defect.xml',
        'views/msp_in_work_order.xml',
        'views/inherit_button_qc_inline1.xml',
        # ---------------------------------------------- wizard------------------------
        'wizard/msp_qc_inline1_wizard.xml',
        'wizard/msp_qc_inline2_wizard.xml',
        'wizard/msp_qc_inline3_wizard.xml',
        'wizard/msp_qc_inline4_wizard.xml',
        'wizard/msp_qc_inline_garment_wizard.xml',
        'wizard/msp_qc_endline_garment_wizard.xml',
    ],
    "js": [
        # 'static/src/js/buttons_hide.js',
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
