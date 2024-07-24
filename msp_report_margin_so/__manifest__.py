{
    "name": "msp_report_margin_so",
    "description": "msp_report_margin_so",
    "version": "0.1",
    "author": "Demas",
    "website": "https://www.semarkoding.com",
    "license": "AGPL-3",
    "category": "msp_report_margin_so",
    "depends": ["product","sale","mrp"],
    "data": [
        "view/so_report_act.xml",
        "view/report_jumlah_rijek_produksidoc.xml",
        # report
        "report/msp_menu_report.xml",
        "report/msp_report_margin_so_doc.xml",
        # "report/report_rijek_mrp_doc.xml",
    ],
    "js": [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
