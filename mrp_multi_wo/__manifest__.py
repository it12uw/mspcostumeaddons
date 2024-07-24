{
   'name': 'MRP Multi WO',
   'version': '11.1.0',
   'author': 'Taling Tarung',
   'license': 'OPL-1',
   'category': 'Tailor-Made',
   'website': 'https: //www.talingtarung.com/',
   'summary': 'Custom-built Odoo',
   'description': '''
   ''',
   'depends': [
       'mrp', # python
       'stock', # python
   ],
   'data': [
       'views/mrp_production_views.xml',
   ],
   'qweb': [
   ],
   'auto_install': False,
   'installable': True,
   'application': True,
}