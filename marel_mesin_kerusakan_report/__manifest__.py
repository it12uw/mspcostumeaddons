# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "marel_mesin_kerusakan_report",
    "summary": "marel_mesin_kerusakan_report",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Flectra Community, Odoo Community Association (OCA)",
    "category": "marel_mesin_kerusakan_report",
    "website": "https://gitlab.com/art-in-heaven",
    "depends": ["marel_mesin_kerusakan","marel_in_work_order"],
    "data": [
        "report/marel_mesin_kerusakan_report.xml",
        # 'security/ir.model.access.csv',
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}