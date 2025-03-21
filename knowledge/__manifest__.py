# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Knowledge Management System",
    "version": "1.0.3.0.0",
    "author": "Flectra SA,"
              "MONK Software, "
              "Tecnativa, "
              "Eficent, "
              "Odoo Community Association (OCA)",
    "category": "Knowledge",
    "license": "AGPL-3",
    "website": "https://gitlab.com/flectra-community/knowledge",
    "depends": [
        "base",
    ],
    "data": [
        "data/ir_module_category.xml",
        "security/knowledge_security.xml",
        "views/knowledge.xml",
        "views/res_config.xml",
    ],
    "demo": [
        "demo/knowledge.xml",
    ],
    "installable": True,
    "application": True,
}
