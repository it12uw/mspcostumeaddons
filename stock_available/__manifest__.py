# Copyright 2014 Numérigraphe
# Copyright 2016 Sodexis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Stock available to promise',
    'version': '1.0.1.1.0',
    "author": "Numérigraphe, Sodexis, Odoo Community Association (OCA)",
    'category': 'Warehouse',
    'depends': ['stock','product'],
    'license': 'AGPL-3',
    'data': [
        'views/product_template_view.xml',
        'views/product_product_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
}
