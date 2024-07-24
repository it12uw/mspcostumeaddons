{
	"name": "msp_tanda_terima_tagihan",
	"version": "1.0", 
	"depends": ["product","mrp"],
	"author": "asrent345@gmail.com", 
	"category": "Education", 
	'website': 'http://www.vitraining.com',
	"description": """\

Manage
======================================================================

* this is my academic information system module
* created menu:
* created object
* created views
* logic:

""",
	"data": [
        # "security/ir.model.access.csv",
		"view/menu_2.xml",
		"view/msp_tanda_terima_tagihan.xml",		
		# report------		
		"report/msp_tanda_terima_tagihan_menu.xml",
		"report/msp_tanda_terima_tagihan_template.xml",
		# "report/report_marel_in_permintaan_benang_develop_doc.xml",
		#------- view report permintaan benang
		# "view/sample_report_permintaan_benang_template.xml",
		"view/ir_sequence.xml",
		# "view/marel_in_bom.xml",
		# "view/marelin_permintaan_develop.xml",
		# "view/bom_report_act.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}