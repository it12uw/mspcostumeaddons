{
	"name": "marel_inherit_samlpe_dev_2",
	"version": "1.0", 
	"depends": [
		"base",
		"product",
		"marel_in_samlpe_dev_2",
	],
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
		# "view/menu_2.xml",
		# "view/marel_inherit_samlpe_dev_2.xml",	
		# report benang sample	
		"view/bom_report_act.xml",
		"view/sample_report_permintaan_benang_template.xml",
		"view/sample_report_permintaan_aksesoris_template.xml",
		# report------		
		"report/marel_inherit_samlpe_dev_2_menu.xml",
		"report/marel_in_samlpe_dev_2_template.xml",
		"report/report_marel_in_permintaan_benang_develop_doc.xml",
		#------/name
		# "view/ir_sequence.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}