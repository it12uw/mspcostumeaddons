{
	"name": "marel_inherit_samlpe_dev_3",
	"version": "1.0", 
	"depends": [
		"base",
		"product",
		"marel_in_samlpe_dev_2",
		"marel_in_work_order",
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
		"view/marel_inherit_samlpe_dev_3.xml",	
		# report------		
		# "report/marel_inherit_samlpe_dev_2_menu.xml",
		"report/marel_inherit_samlpe_dev_3_doc.xml",
		#------/name
		# "view/ir_sequence.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}