# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "msp_report_xlsx",
    "summary": "msp_report_xlsx",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Flectra Community, Odoo Community Association (OCA)",
    "category": "msp_report_xlsx",
    "website": "https://gitlab.com/art-in-heaven",
    "depends": ["mrp",
                "marel_in_work_order",
                "product",
                "stock_request"
                ],
    "data": [
        "report/report_mrp_sro.xml",
        'security/ir.model.access.csv',
        # "report/qweb_marel_wip_mo_report.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}