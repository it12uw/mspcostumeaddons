# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "marel_summary_report",
    "summary": "marel_summary_report",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Flectra Community, Odoo Community Association (OCA)",
    "category": "marel_summary_report",
    "website": "https://gitlab.com/art-in-heaven",
    "depends": ["mrp", "stock", "product","sale","purchase"],
    "data": [
        "report/marel_summary_report.xml",
        # 'security/ir.model.access.csv',
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}