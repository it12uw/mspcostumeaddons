# Copyright 2015 Anybox
# Copyright 2018 Camptocamp
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale product set',
    'category': 'Sale',
    'license': 'AGPL-3',
    'author': 'Anybox, Flectra Community, Odoo Community Association (OCA)',
    'version': '1.0.1.0.0',
    'website': 'https://gitlab.com/flectra-community/sale-workflow',
    'summary': "Sale product set",
    'depends': [
        'sale',
    ],
    'data': [
        'views/product_set.xml',
        'wizard/product_set_add.xml',
        'views/sale_order.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/product_set.xml',
        'demo/product_set_line.xml',
    ],
    'installable': True,
}
