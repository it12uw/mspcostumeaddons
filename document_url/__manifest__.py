# Copyright 2014 Serv. Tecnol. Avanzados (https://gitlab.com/flectra-community/knowledge)
#                       Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
{
    'name': 'URL attachment',
    'version': '1.0.1.0.0',
    'category': 'Tools',
    'author': "Tecnativa,"
              "Odoo Community Association (OCA)",
    'website': 'https://gitlab.com/flectra-community/knowledge',
    'license': 'AGPL-3',
    'depends': [
        'document',
    ],
    'data': [
        'view/document_url_view.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/url.xml',
    ],
    'installable': True,
}
