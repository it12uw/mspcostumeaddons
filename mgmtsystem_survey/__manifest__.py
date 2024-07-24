# Copyright (C) 2010 Savoir-faire Linux (<https://gitlab.com/flectra-community/management-system>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Management System - Survey",
    "version": "1.0.1.0.0",
    "author": "Savoir-faire Linux,Odoo Community Association (OCA)",
    "website": "https://gitlab.com/flectra-community/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": [
        'mgmtsystem',
        'survey'
    ],
    "data": [
        'data/survey_stage.xml',
        'views/survey_survey.xml',
    ],
    "demo": [
    ],
    'installable': True,
}
