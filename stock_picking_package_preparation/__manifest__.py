# Author: Guewen Baconnier
# Copyright 2015 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Stock Picking Package Preparation',
    'version': '1.0.1.0.0',
    'author': 'Camptocamp, Agile Business Group, '
              'Flectra Community, Odoo Community Association (OCA)',
    'maintainer': 'Camptocamp',
    'license': 'AGPL-3',
    'category': 'Warehouse Management',
    'depends': ['stock'],
    'website': 'https://gitlab.com/flectra-community/stock-logistics-workflow'
               '11.0/stock_picking_package_preparation',
    'data': [
        'security/ir.model.access.csv',
        'security/package_preparation_security.xml',
        'views/stock_picking_package_preparation_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
