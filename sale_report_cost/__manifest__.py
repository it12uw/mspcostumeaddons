{
    'name': 'Sale Report Cost',
    'version': '11.0.0',
    'author': 'Taling Tarung',
    'license': 'OPL-1',
    'category': 'My-Custom',
    'website': 'https: //www.talingtarung.com/',
    'summary': 'Custom-built Flectra',
    'description': '''
    Add cost standard price in sale report
    ''',
    'depends': [
        # 'account',
        'sale'
    ],
    'data': [
        'reports/sale_report_view.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}