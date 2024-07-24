{
    'name': 'Rekap Aksesoris',
    'summary': 'Rekap Aksesoris',
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
        'base'
    ],
    # 'external_dependencies': {
    #     'python': [
    #     ],
    # },
    'data': [
        # 'views/marel_rekap_aksesoris.xml',
        'views/rekap_kebutuhan_aksesoris.xml',
        'views/menu.xml',
        #---------------
        'report/rekap_kebutuhan_aksesoris.xml',
        'report/report_rekap_kebutuhan_aksesoris_doc.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    # 'js': [
    # ],
    # 'css': [
    # ],
    # 'qweb': [
    # ],
    # 'images': [
    # ],
    # 'test': [
    # ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
