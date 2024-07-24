# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

{
    'name': 'marel_in_replace_report',
    'author': 'Odoo S.A.',
    'version': '1.2',
    'category': 'Sales',
    'depends' : ['base_setup', 'product','sale','stock','mrp','marel_in_so_ke_bom',],
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
        'view/marel_in_sale_order.xml',
        'report/report_product_template_custom.xml',
        'report/report_invoice_document_custom.xml',
        'report/report_invoice_document_group.xml',
        'report/account_report_payment_receipt_templates_custom.xml',
        'report/msp_inv_report_cutom.xml',
        'report/report_production_order_aksesoris_doc.xml',
        'report/marel_report.xml',
    ],
    'demo': [
    ],
	"installable": True,
	"auto_install": False,
    "application": True,
}
