# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Manufacturing Production Control",
    "summary": "Penerimaan Produksi dan Inspekting",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Flectra Community, Odoo Community Association (OCA)",
    "category": "MPC",
    "website": "https://gitlab.com/art-in-heaven",
    "depends": ["mrp", "base", "stock", "product", "delivery",],
    "data": [
        "security/ir.model.access.csv",
        "report/mpc_produce_lot_report.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}