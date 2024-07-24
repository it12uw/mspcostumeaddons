# Copyright 2017 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# Copyright 2018 Vicent Cubells - Tecnativa <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Line Report',
    'summary': 'New view to manage invoice lines information',
    'version': '1.0.1.0.0',
    'category': 'Account',
    'website': 'https://gitlab.com/flectra-community/account-invoice-reporting',
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'base',
        'product',
        'stock',
        'sale',
    ],
    'data': [
        'report/account_invoice_report_view.xml',
        'report/account_invoice_report_custom.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
