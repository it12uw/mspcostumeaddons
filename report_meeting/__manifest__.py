# -*- coding: utf-8 -*-
{
    'name': 'Pre Production Meeting Report',
    'version': '2.0',
    'category': 'Manufacturing',
    'summary': 'Form Pre Production Meeting for Manufacturing Orders',
    'description': """
Pre Production Meeting Report
=============================
This module adds a detailed pre-production meeting report for manufacturing orders,
enabling better planning and preparation before production starts.
    """,
    'author': 'Marel Sukses Pratama',
    'website': 'https://marelsp.com/',
    'depends': ['mrp', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'report/pre_production_report_templates.xml',
        'views/pre_production_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}