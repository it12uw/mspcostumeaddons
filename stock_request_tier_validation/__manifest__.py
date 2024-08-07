# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Request Tier Validation",
    "summary": "Extends the functionality of Stock Requests to "
               "support a tier validation process.",
    "version": "1.0.1.2.0",
    "category": "Warehouse Management",
    "website": "https://gitlab.com/flectra-community/stock-logistics-warehouse",
    "author": "Eficent, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "stock_request",
        "base_tier_validation",
    ],
    "data": [
        "data/stock_request_tier_definition.xml",
        "views/stock_request_order_view.xml",
        "views/stock_request_view.xml",
    ],
}
