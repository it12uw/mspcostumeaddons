# Copyright 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Report QWeb Parameter",
    "version": "1.0.1.0.0",
    "license": "AGPL-3",
    "summary": """
        Add new parameters for qweb templates in order to reduce field length
        and check minimal length
    """,
    "author": "Creu Blanca,"
              "Flectra Community, Odoo Community Association (OCA)",
    "website": "https://gitlab.com/flectra-community/reporting-engine",
    "category": "Technical Settings",
    "depends": [
        "web",
    ],
    "demo": [
        "demo/test_report_field_length.xml"
    ],
    "installable": True,
}
