# Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Document Management - Wiki - Procedures",
    "version": "1.0.1.0.0",
    "author": "Savoir-faire Linux,Odoo Community Association (OCA)",
    "website": "https://gitlab.com/flectra-community/management-system",
    "license": "AGPL-3",
    "category": "Generic Modules/Others",
    "depends": [
        'document_page_work_instruction'
    ],
    "data": [
        'data/document_page_procedure.xml',
        'views/document_page_procedure.xml',
    ],
    "demo": [
        'demo/document_page_procedure.xml',
    ],
    'installable': True,
}
