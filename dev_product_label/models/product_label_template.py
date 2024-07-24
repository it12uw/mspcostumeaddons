# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################

from flectra import models, fields, api, _
from flectra.exceptions import ValidationError
from datetime import datetime
from dateutil.relativedelta import relativedelta


class dev_product_label_template(models.Model):
    _name = 'dev.product.label.template'
    _description = 'Product Label Template'

    name = fields.Char('Name')
    page_height = fields.Float('Page Height', default=297)
    page_width = fields.Float('Page Width', default=210)
    
    label_height = fields.Integer('Label Height', default=50)
    label_width = fields.Integer('Label Width', default=30)
    
    margin_left= fields.Integer('Margin Left', default=5)
    margin_top= fields.Integer('Margin Top', default=5)
    barcode_height = fields.Integer('Barcode Height', default=50)
    barcode_width = fields.Integer('Barcode Width', default=250)
    
    product_name = fields.Boolean('Product Name', default=True)
    pro_name_bold= fields.Boolean('Bold Product Name')
    pro_font_size = fields.Integer('Font Size', default=18)
    attributes = fields.Boolean('Attributes', default=True)
    att_font_size = fields.Integer('Font Size', default=12)
    barcode_no = fields.Boolean('Barcode No', default=True)
    bar_font_size = fields.Integer('Font Size', default=12)
    default_code = fields.Boolean('Default Code', default=True)
    def_font_size = fields.Integer('Font Size', default=12)
    
    barcode_from = fields.Selection([('default_code','Default Code'),('barcode','Barcode')], default='barcode', required="1")
    barcode_type = fields.Selection([('Code128','Code128'),
                                     ('Code11','Code11'),
                                     ('Codabar','Codabar'),
                                     ('EAN13','EAN13'),
                                     ('EAN8','EAN8'),
                                     ('Extended39','Extended39'),
                                     ('Extended93','Extended93'),
                                     ('I2of5','I2of5'),
                                     ('QR','QR'),
                                     ('Standard39','Standard39'),
                                     ('Standard93','Standard93'),
                                     ('UPCA','UPCA')], string='Barcode Type', default='Code128', required="1")
                                     
    
    @api.constrains('pro_font_size', 'att_font_size', 'bar_font_size', 'def_font_size')        
    def check_font_size(self):
        for temp in self:
            if temp.product_name and temp.pro_font_size <= 0:
                raise ValidationError(_("Product Font Size must be positive"))
                
            if temp.attributes and temp.att_font_size <= 0:
                raise ValidationError(_("Attributes Font Size must be positive"))
                
            if temp.barcode_no and temp.bar_font_size <= 0:
                raise ValidationError(_("Barcode Font Size must be positive"))
            
            if temp.default_code and temp.def_font_size <= 0:
                raise ValidationError(_("Default Code Font Size must be positive"))
            
                
                
    @api.constrains('label_height', 'label_width')        
    def check_label_height_width(self):
        for temp in self:
            if temp.label_height <= 0:
                raise ValidationError(_("Label Height must be positive"))
            
            if temp.label_width <= 0:
                raise ValidationError(_("Label Width must be positive"))
                
                
    
    @api.constrains('margin_left', 'margin_top')        
    def check_margin(self):
        for temp in self:
            if temp.margin_left <= 0:
                raise ValidationError(_("Margin Left must be positive"))
            
            if temp.margin_top <= 0:
                raise ValidationError(_("Margin Top must be positive"))
                
                
    @api.constrains('page_height', 'page_width')        
    def check_page_height_width(self):
        for temp in self:
            if temp.page_height <= 0:
                raise ValidationError(_("Page Height must be positive"))
            
            if temp.page_width <= 0:
                raise ValidationError(_("Page Width must be positive"))
    
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
