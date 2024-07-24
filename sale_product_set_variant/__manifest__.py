# Copyright 2017-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Sale product set variant',
    'category': 'Sale',
    'license': 'AGPL-3',
    'author': 'Camptocamp, Flectra Community, Odoo Community Association (OCA)',
    'version': '1.0.1.0.0',
    'website': 'https://gitlab.com/flectra-community/sale-workflow',
    'summary': "Add variant management to sale product set.",
    'depends': [
        'sale_product_set',
    ],
    'data': [
        'views/product_set.xml',
        'wizard/product_set_add.xml',
    ],
    'demo': [
        'demo/product_set.xml',
    ],
}
