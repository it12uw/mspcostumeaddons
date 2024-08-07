# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': "Stock Inventory Analytic",
    'summary': """
        Stock Inventory Analytic """,
    'author': 'Eficent, Odoo Community Association (OCA)',
    'website': "https://gitlab.com/flectra-community/account-analytic",
    'category': 'Warehouse Management',
    'version': '1.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'stock_analytic',
    ],
    'data': [
        'views/stock_inventory_line_view.xml',
        'wizard/stock_product_change_qty.xml',
    ],
    'installable': True,
}
