{
    "name": "msp_buttonmulti_confirm_po",
    "description": "msp_buttonmulti_confirm_po",
    "version": "0.1",
    "author": "Demas",
    "website": "https://www.semarkoding.com",
    "license": "AGPL-3",
    "category": "msp_buttonmulti_confirm_po",
    "depends": ["purchase","marel_in_stock_picking",'marel_in_data_stock_picking',"stock","mrp"],
    "data": [
        "wizard/button_multi_confirm_po_view.xml",
        "wizard/button_multi_confirm_sr_view.xml",
        "wizard/button_multi_confirm_sp_view.xml",
        "wizard/button_multi_confirm_mo_view.xml",
        "wizard/button_multi_deleted_procurement_mo.xml",
        # report
        # "report/msp_menu_report.xml",
        # "report/msp_report_margin_so_doc.xml",
        # "report/report_rijek_mrp_doc.xml",
    ],
    "js": [],
    'installable': True,
    'application': True,
    'auto_install': False,
}