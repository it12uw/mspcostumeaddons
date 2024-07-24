{
	"name": "Data MES PLAN",
	"version": "1.0", 
	"depends": [
		"product",
		"in_mrp_product_template",
		"mrp",
		"stock",
	],
	"author": "hendri&asrent345@gmail.com" , 
	"category": "Education", 
	'website': "https://gitlab.com/arsisra",
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
		"views/menu.xml",
		"views/in_plan_mes.xml",
		"views/in_serah_trima_barang.xml",
		"views/in_warping.xml",
		"views/in_laporan_harian_shift.xml",
		"views/in_sizing.xml",
	],
	"installable": True,
	"auto_install": False,
    "application": True,
}