# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Devintelle Solutions (<http://devintellecs.com/>).
#
##############################################################################

{
    'name': 'Dynamic Barcode Product Label Print',
    'version': '13.0.1.0',
    'category': 'Sales',
    'sequence':1,
    'summary': 'flectra app Print Dynamic Product Label - Barcode, Qrcode',
    'description': """
        flectra app Print Dynamic Product Label - Barcode, Qrcode
Dynamic Product label print 
flectra dynamic product label print 
Manage dynamic product label print 
flectra manage dynamic product label print 
Using this application you will print Product Label Based on your need
flectra Using this application you will print Product Label Based on your need
Dynamic page size 
flectra dynamic page size 
Manage dynamic page size 
flectra manage dynamic page size 
Dynamic Label Size
flectra Dynamic Label Size
Manage Dynamic Label Size
flectra manage Dynamic Label Size
Dynamic Font Size
flectra Dynamic Font Size
Manage Dynamic Font Size
flectra manage Dynamic Font Size
Multipal Barcode Type
flectra Multiple Barcode Type
Barcode print Based on default code or barcode
flectra Barcode print Based on default code or barcode
Print Number of label with number of products in single click
flectra Print Number of label with number of products in single click
Dynamic product label 
flectra dynamic product label
Manage dynamic product label
flectra manage dynamic product label 


            """,
    'author': 'DevIntelle  Consulting Service Pvt. Ltd',
    'website': 'http://devintellecs.com/',
    'depends': ['sale_management'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_lable_template_view.xml',
        'wizard/dev_product_label_view.xml',
        'report/header.xml',
        'report/product_label_report.xml',
        'report/report_menu.xml',
    ],
    'demo': [
        'demo/product_label_data.xml',
    ],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # author and support Details =============#
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':29.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
