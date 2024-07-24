# © 2015-2016 Akretion (https://gitlab.com/flectra-community/stock-logistics-workflow)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Stock Disallow Negative',
    'version': '1.0.1.2.1',
    'category': 'Inventory, Logistic, Storage',
    'license': 'AGPL-3',
    'summary': 'Disallow negative stock levels by default',
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'https://gitlab.com/flectra-community/stock-logistics-workflow',
    'depends': ['stock'],
    'data': [
        'views/product_product_views.xml',
        'views/stock_location_views.xml',
    ],
    'installable': True,
}
