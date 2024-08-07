# Copyright 2017 ACSONE SA/NV
# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Pack Operation Auto Fill',
    'summary': "Stock pack operation auto fill",
    'version': '1.0.2.0.1',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV,'
              'Tecnativa,'
              'Flectra Community, Odoo Community Association (OCA)',
    'website': 'https://gitlab.com/flectra-community/stock-logistics-workflow',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock_picking.xml',
        'views/stock_picking_type_views.xml',
    ],
}
