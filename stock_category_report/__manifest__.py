{
    'name': 'Stock Category Group',
    'version': '11.1.0',
    'author': 'Taling Tarung',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'https: //www.talingtarung.com/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'stock',
        'product',
        'base', 
    ],
    'data': [
        'views/stock_quant.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}