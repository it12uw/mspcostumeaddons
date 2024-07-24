{
    'name': 'Sale View Picking',
    'version': '11.1.0',
    'author': 'Taling Tarung',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'https: //www.talingtarung.com/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'sale_management', 
        'stock_account',
    ],
    'data': [
        'views/sale_order_view.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}