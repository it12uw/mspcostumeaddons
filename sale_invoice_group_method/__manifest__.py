# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Sale Invoice Group Method",
    "author": "Eficent, Flectra Community, Odoo Community Association (OCA)",
    "version": "1.0.1.1.1",
    "category": "Sale Workflow",
    "website": "https://gitlab.com/flectra-community/sale-workflow",
    "depends": [
        'sale_order_action_invoice_create_hook',
    ],
    "data": [
        'security/ir.model.access.csv',
        'view/res_partner_view.xml',
        'view/sale_order_view.xml',
        'view/sale_invoice_group_method_view.xml',
        'view/menu.xml',
    ],
    "license": 'LGPL-3',
    "installable": True
}
