# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Picking Purchase Order Link',
    'summary': """
        Link between picking and purchase order""",
    'version': '1.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Eficent Business and IT Consulting Services S.L.,'
              'Odoo Community Association (OCA)',
    'website': 'https://gitlab.com/flectra-community/stock-logistics-workflow',
    "application": False,
    "installable": True,
    'depends': [
        'purchase'
    ],
    'data': [
        'views/stock_picking_view.xml',
    ],
}
