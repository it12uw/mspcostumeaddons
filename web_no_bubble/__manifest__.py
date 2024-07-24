# © 2016 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Web No Bubble',
    'version': '1.0.1.0.0',
    'author': 'Savoir-faire Linux, '
              'Flectra Community, Odoo Community Association (OCA)',
    'website': 'https://gitlab.com/flectra-community/web',
    'license': 'AGPL-3',
    'category': 'Web',
    'summary': 'Remove the bubbles from the web interface',
    'depends': ['web'],
    'data': [
        'views/web_no_bubble.xml',
    ],
    'installable': True,
    'application': False,
}
