# Copyright 2015 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "Base report xlsx",

    'summary': "Base module to create xlsx report",
    'author': 'ACSONE SA/NV,'
              'Creu Blanca,'
              'Flectra Community, Odoo Community Association (OCA)',
    'website': "https://gitlab.com/flectra-community/reporting-engine",
    'category': 'Reporting',
    'version': '1.0.1.0.3',
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': [
            'xlsxwriter',
            'xlrd',
        ],
    },
    'depends': [
        'base', 'web',
    ],
    'data': [
        'views/webclient_templates.xml',
    ],
    'demo': [
        'demo/report.xml',
    ],
    'installable': True,
}
