{
    'name': 'Invoice Subtotal',
    'version': '11.1.0',
    'author': '',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': '',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'account', 'sale', 'purchase',
    ],
    'data': [
        'views/purchase_views.xml',
        
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}