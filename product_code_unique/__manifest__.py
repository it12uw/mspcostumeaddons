# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Unique Product Internal Reference",
    "summary": "Set Product Internal Reference as Unique",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "category": "Product",
    "website": "https://gitlab.com/flectra-community/product-attribute",
    "depends": ["product"],
    "data": [
    ],
    'demo': [
    ],
    "pre_init_hook": 'pre_init_product_code',
    "installable": True,
}
