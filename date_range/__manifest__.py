# © 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Date Range",
    "summary": "Manage all kind of date range",
    "version": "1.0.2.0.1",
    "category": "Uncategorized",
    "website": "https://gitlab.com/flectra-community/server-ux",
    "author": "ACSONE SA/NV, Flectra Community, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/date_range_security.xml",
        "views/assets.xml",
        "views/date_range_view.xml",
        "wizard/date_range_generator.xml",
    ],
    "qweb": [
        "static/src/xml/date_range.xml",
    ],
    'development_status': 'Mature',
    'maintainers': ['lmignon'],
}
