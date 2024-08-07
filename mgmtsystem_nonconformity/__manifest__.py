# Copyright (C) 2010 Savoir-faire Linux (<https://gitlab.com/flectra-community/management-system>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Management System - Nonconformity",
    "version": "1.0.1.1.2",
    "author": "Savoir-faire Linux,Odoo Community Association (OCA)",
    "website": "https://gitlab.com/flectra-community/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        'mgmtsystem_action',
        'document_page_procedure',
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/mgmtsystem_nonconformity_security.xml',
        'views/mgmtsystem_nonconformity.xml',
        'views/mgmtsystem_origin.xml',
        'views/mgmtsystem_cause.xml',
        'views/mgmtsystem_severity.xml',
        'views/mgmtsystem_action.xml',
        'views/mgmtsystem_nonconformity_stage.xml',
        'data/sequence.xml',
        'data/mgmtsystem_nonconformity_severity.xml',
        'data/mgmtsystem_nonconformity_origin.xml',
        'data/mgmtsystem_nonconformity_cause.xml',
        'data/mgmtsystem_nonconformity_stage.xml',
        'data/mail_message_subtype.xml',
        'reports/mgmtsystem_nonconformity_report.xml',
    ],
    "demo": [
        "demo/mgmtsystem_nonconformity_origin.xml",
        "demo/mgmtsystem_nonconformity_cause.xml",
        "demo/mgmtsystem_nonconformity.xml",
    ],
    'installable': True,
}
