# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2015 John Walsh
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MRP MTO with Stock",
    "summary": "Fix Manufacturing orders to pull from stock until qty is "
               "zero, and then create a procurement for them.",
    "author": "John Walsh, Eficent, Odoo Community Association (OCA)",
    "website": "https://gitlab.com/flectra-community/manufacture",
    "category": "Manufacturing",
    "version": "1.0.2.0.1",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock",
        "mrp",
        "stock_available_unreserved",
    ],
    "data": [
        'views/product_template_view.xml',
        'views/stock_warehouse.xml',
    ],
    "demo": ['demo/product.xml'],
}
