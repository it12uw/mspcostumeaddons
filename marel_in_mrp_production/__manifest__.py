{
    'name': 'Marel In Manufacturing Orders',
    'version': '11.1.0',
    'author': 'Aditya Demas',
    'license': 'OPL-1',
    'category': 'Marel In Manufacturing Orders',
    # 'website': 'http: //www.arkana.co.id/',
    'summary': 'Inherit Button and Field',
    'description': '''
    ''',
    'depends': ['mrp','marel_in_work_order'],
    'data': [
        # 'wizard/faktur_cancel_wizard.xml',
        'views/marel_in_mrp_production.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}