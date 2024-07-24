{
	"name": "marel_in_so",
	"version": "1.0", 
	"depends": [
		"base",
		"mrp",
		"purchase",
		"sale",
		"sale_order_dates",
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
		# "view/marel_mrp_production_tree_view_custom.xml",
		"view/marel_inherit_so.xml",
		# report
		"report/report_marel_list.xml",
		"report/report_marel_report_resume_so_doc.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}