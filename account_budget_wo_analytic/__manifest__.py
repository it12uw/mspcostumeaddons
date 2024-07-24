{
   'name': 'Account Budget WO Analytic',
   'version': '11.1.0',
   'author': 'Taling Tarung',
   'license': 'OPL-1',
   'category': '',
   'website': 'https: //www.talingtarung.com/',
   'summary': 'Custom-built Odoo',
   'description': '''
   ''',
   'depends': [
       'account', # python
       'account_budget', # python
   ],
   'data': [
       'views/account_budget_view.xml',
   ],
   'qweb': [
   ],
   'auto_install': False,
   'installable': True,
   'application': False,
}