{
    'name': 'Cost Custom',
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
        'product',
        'stock',
        'stock_account',
        'product_extended',
        'mrp',
        'base'
    ],
    'data': [
        'product_views.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}