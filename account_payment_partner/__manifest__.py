# Copyright 2014 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# Copyright 2014 Tecnativa - Pedro M. Baeza
# Copyright 2018 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Payment Partner',
    'version': '1.0.1.4.0',
    'category': 'Banking addons',
    'license': 'AGPL-3',
    'summary': 'Adds payment mode on partners and invoices',
    'author': "Akretion, "
              "Tecnativa, "
              "Odoo Community Association (OCA)",
    'website': 'https://gitlab.com/flectra-community/bank-payment',
    'depends': ['account_payment_mode'],
    'data': [
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'views/account_move_line.xml',
        'views/account_payment_mode.xml',
        'views/report_invoice.xml',
    ],
    'demo': ['demo/partner_demo.xml'],
    'installable': True,
}
