{
    'name': 'Account Due Late',
    'version': '11.1.0',
    'author': 'Taling Tarung',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'https: //www.talingtarung.com/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'account', 
        'account_payment',
        'base', 
    ],
    'data': [
        'views/account_due_late_invoice.xml',
        'views/account_duelate_menu.xml',
        'views/in_partner.xml',
        'report/account_duelate_report.xml',
        'wizards/account_duelate_wiz.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
