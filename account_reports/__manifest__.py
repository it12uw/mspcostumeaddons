# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Accounting Reports',
    'summary': 'View and create reports',
    'category': 'Accounting',
    'description': """
Accounting Reports
==================
    """,
    'depends': ['account','account_hub',],
    'data': [
        'security/ir.model.access.csv',
        'data/account_financial_report_data.xml',
        'views/account_report_view.xml',
        'views/report_financial.xml',
        'views/search_template_view.xml',
        'views/report_followup.xml',
        'views/partner_view.xml',
        'views/account_journal_dashboard_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'qweb': [
        'static/src/xml/account_report_template.xml',
    ],
    'auto_install': True,
    
    
}
