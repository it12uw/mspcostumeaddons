# Copyright 2019 Marcelo Frare (Ass. PNLUG - Gruppo Odoo <http://flectra.pnlug.it>)
# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Odoo <http://flectra.pnlug.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name":     "Management System - Action Efficacy",
    "summary":  "Add information on the application of the Action.",
    "version":  "1.0.1.0.0",
    "development_status": "Production/Stable",

    "author":   "Associazione PNLUG - Gruppo Odoo, Odoo Community Association (OCA)",

    "website":  "https://gitlab.com/flectra-community/management-system"
                "11.0/mgmtsystem_extended",
    "license":  "AGPL-3",

    "category": "Management System",
    "depends": ['mgmtsystem_action',
                ],
    "data":    ['views/mgmtsystem_action_views.xml',
                ],
    'installable': True,
}
