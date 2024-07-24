# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

{
    'name': 'Marel In Report MO',
    'author': 'Odoo S.A.',
    'version': '1.2',
    'category': 'Sales',
    'depends': ['base', 'mrp','barcodes','account'],
    'description': """
This is the base module for managing products and pricelists in Odoo, Flectra.
==============================================================================

Products support variants, different pricing methods, vendors information,
make to stock/order, different units of measure, packaging and properties.

Pricelists support:
-------------------
    * Multiple-level of discount (by product, category, quantities)
    * Compute price based on different criteria:
        * Other pricelist
        * Cost price
        * List price
        * Vendor price

Pricelists preferences by product and/or partners.

Print product labels with barcode.
    """,
    'data': [
        'report/marel_report_kkp.xml',
        #------------------48 pair k pcs
        # 'report/report_marel_in_report_mo_doc.xml',
        # 'report/report_marel_in_report_mo_48_short_doc.xml',
        #----------------- 24 pair k pcs
        # 'report/report_marel_in_report_mo_24_doc.xml',
        # 'report/report_marel_in_report_mo_24_short_new_doc.xml',
        #------------------ sisaa
        # 'report/report_marel_in_report_mo_sisa_doc.xml',
        # 'report/report_marel_in_report_mo_sisa_doc_24.xml',
        # 'report/report_marel_in_report_kkp_headband_sisa_doc.xml',
        # 'report/report_marel_in_report_mo_120_sisa_doc.xml',
        'report/kwitansi_ship.xml',
        'report/kwitansi_ship_multi.xml',
        # 'report/report_marel_in_report_kkp_headband_120_doc.xml',
        # 'report/report_marel_in_report_mo_60_sisa_doc.xml',
        # 'report/report_marel_in_report_kkp_headband_96_sisa_doc.xml',
        'report/report_marel_in_report_kkp_headband_96_doc.xml',
        #-----------pcs 48 pcs
        # 'report/report_marel_in_report_kkp_headband_doc.xml',
        # 'report/report_marel_in_report_kkp_headband_very_short_doc.xml',
        # ---------- very short pair k pcs
        # 'report/report_marel_in_report_mo_24_very_short_doc.xml',
        # 'report/report_marel_in_report_mo_48_very_short_doc.xml',

        #------------- 48 pair ke pcs
        # 'report/report_marel_in_report_mo_doc.xml',
        # ------------- 24 pair k pcs
        # 'report/report_marel_in_report_mo_24_doc.xml',
        # ------------- pcs headband
        # 'report/report_marel_in_report_kkp_headband_doc.xml',
        #-------------- 120 pcs
        # 'report/report_marel_in_report_mo_120_doc.xml',
        # ------------- 120 headband
        # 'report/report_marel_in_report_kkp_headband_sisa_120_doc.xml',        
        # ------------- 60 pair k pcs
        'report/report_marel_in_report_mo_60_doc.xml',     
        # ------------- 60 pair k pcs
        # 'report/report_marel_in_report_mo_96_doc.xml',     
        # 'report/report_marel_in_report_mo_96_sisa_doc.xml',
        'view/marel_in_mrp_production.xml'     


    ],
    'demo': [
    ],
	"installable": True,
	"auto_install": False,
    "application": True,
}
