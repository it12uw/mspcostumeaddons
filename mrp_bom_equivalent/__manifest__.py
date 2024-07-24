# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MRP BoM Equivalences",
    "summary": "Specify non-equivalent products to a part on a BOM",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Flectra Community, Odoo Community Association (OCA)",
    "category": "MRP",
    "website": "https://gitlab.com/flectra-community/manufacture",
    "depends": ["mrp", "product_priority"],
    "data": [
        "views/mrp_view.xml",
    ],
    "installable": True,
}
