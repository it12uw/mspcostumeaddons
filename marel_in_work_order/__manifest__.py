{
    'name': 'Inherit Mrp Work Order',
    'version': '11.1.0',
    'author': 'Aditya Demas',
    'license': 'OPL-1',
    'category': 'Inherit Mrp Work Order',
    'summary': 'Inherit Button and Field',
    'description': '''
    ''',
    'depends': ['mrp','stock'],
    'data': [
        'views/marel_nama_operator_template.xml',
        'views/marel_nama_qiusi.xml',
        'views/marel_in_work_order.xml',
        'views/marel_nama_operatorlist.xml',
        'views/marel_nama_operatorlist_packing.xml',
        'views/menu.xml',
        # 'views/ir_sequence.xml',
        'report/operator_rijek_kaoskaki_report.xml',
    ],
    'qweb': [
    ],
    'css': ['static/src/css/sale.css'],
    'auto_install': False,
    'installable': True,
    'application': True,
}