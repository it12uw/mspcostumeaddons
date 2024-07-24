{
	"name": "marel_in_sample_marketing",
	"version": "1.0", 
	"depends": [
		"base",
		"product",
		"sale",
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
		"view/menu_2.xml",
		"view/marel_in_sample_marketing.xml",	
		# report------		
		# "report/marel_form_pengajuan_sample.xml",
		# "report/marel_in_sample_marketing_menu.xml",
        "report/pengajuan_sample_menu.xml",
        "report/pengajuan_sample_report.xml",
		#------/name
		"view/ir_sequence.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}