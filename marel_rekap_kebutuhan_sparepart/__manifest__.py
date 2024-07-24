{
    'name': 'marel_rekap_kebutuhan_sparepart',
    'summary': 'marel_rekap_kebutuhan_sparepart',
    'version': '1.0',

    'description': """
Human readable name Module Project.
==============================================


    """,

    'author': 'asrent',
    # 'maintainer': 'TM_FULLNAME',
    # 'contributors': ['TM_FULLNAME <TM_FULLNAME@gmail.com>'],

    'website': 'asrent',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        # 'ms_base',
        'base',
        'product',
    ],
    # 'external_dependencies': {
    #     'python': [
    #     ],
    # },
    'data': [
        'views/ir_sequence.xml',
        'views/marel_pengambilan_sparepart.xml',
        'views/menu.xml',
        #---------------
        'report/marel_report_sparepart.xml',
        'report/report_marel_pengambilan_sparepart_doc.xml',
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
