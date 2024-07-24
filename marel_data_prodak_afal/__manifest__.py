# Buata Baru Addon BS
{
    'name': 'marel_data_prodak_afal ',
    'version': '11.1.0',
    'author': 'PT. MAREL SP',
    'license': 'OPL-1',
    'category': 'Modul',
    'website': 'http: //www.Orangpinggiran.com/',
    'summary': 'Custom-built Flectra',
    'description': ''' Modul BS
    ''',
    'depends': [
         'base',
         'product',
         'mail', # python
    ],
    'data': [
        'view/menu.xml',
        'view/marel_jenis_afal.xml',
        'view/marel_data_prodakafal.xml',
        'view/ir_sequence.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}