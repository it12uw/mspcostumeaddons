# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payments Due list',
    'version': '1.0.2.0.0',
    'category': 'Generic Modules/Payment',
    'author': 'Flectra Community, Odoo Community Association (OCA)',
    'summary': 'Check printing commons',
    'website': 'https://gitlab.com/flectra-community/account-payment',
    'license': 'LGPL-3',
    'depends': ['account'],
    'data': [
        'views/payment_view.xml',
    ],
    'pre_init_hook': 'pre_init_hook',
    'installable': True,
    'auto_install': False,
}
