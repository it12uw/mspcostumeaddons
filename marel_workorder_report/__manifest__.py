# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "marel_workorder_report",
    "summary": "marel_workorder_report",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Flectra Community, Odoo Community Association (OCA)",
    "category": "marel_workorder_report",
    "website": "https://gitlab.com/art-in-heaven",
    "depends": ["mrp",
                "marel_in_work_order",
                "product"],
    "data": [
        "report/marel_wip_mo_report.xml",
        "report/wip_mo_report_conti.xml",
        # "report/qweb_marel_wip_mo_report.xml",
        # 'security/ir.model.access.csv',
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}