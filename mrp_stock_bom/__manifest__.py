# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "MRP Stock BOM",
    "summary": "Show BOM line qty",
    "version": "1.0.1.0.0",
    "category": "Manufacturing",
    "website": "https://gitlab.com/flectra-community/manufacture",
    "author": "Flectra Community, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "mrp",
        "stock",
    ],
    "data": [
        "views/mrp_stock_bom.xml",
        "data/product_data.xml",
    ]
}