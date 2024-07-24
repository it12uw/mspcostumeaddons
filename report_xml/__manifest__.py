# Copyright (C) 2014-2015  Grupo ESOC <www.grupoesoc.es>
# License AGPL-3.0 or later (https://www.gnuorg/licenses/agpl.html).

{
    "name": "XML Reports",
    "version": "1.0.1.0.1",
    "category": "Reporting",
    "website": "https://gitlab.com/flectra-community/reporting-engine",
    "author": "Grupo ESOC Ingeniería de Servicios, "
              "Flectra Community, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "summary": "Allow to generate XML reports",
    "depends": [
        "web",
    ],
    "data": [
        "views/report_xml_templates.xml",
        "views/webclient_templates.xml",
    ],
    "demo": [
        "demo/report.xml",
    ]
}
