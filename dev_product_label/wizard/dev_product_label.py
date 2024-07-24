 # -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Devintelle Solutions (<http://devintellecs.com/>).
#
##############################################################################

from flectra import api, fields, models, _

class dev_product_label(models.TransientModel):
    _name = "dev.product.label"
    
    template_id = fields.Many2one('dev.product.label.template', string='Template')
                                     
    pro_line_ids = fields.One2many('dev.product.line', 'pro_label_id', string='Product Label Lines')
    
    
    
    def get_attribute(self,product):
        att_name = ''
        for att in product.attribute_line_ids:
            if att_name:
                att_name = att_name + ', '+att.attribute_id.name
            else:
                att_name= att.attribute_id.name
        return att_name
            
    
    def set_paper_size(self):
        paper_ids = self.env['report.paperformat'].sudo().search([('name','=','Product Label A4')])
        if paper_ids:
            for paper in paper_ids:
                paper.page_height = self.template_id.page_height
                paper.page_width = self.template_id.page_width
        
        else:
            report_pool = self.env['ir.actions.report']
            report_id = report_pool.search([('name','=', 'Product Label')], limit=1)
            if report_id:
                vals = {
                    'name':'Product Label A4',
                    'default':True,
                    'format':'custom',
                    'page_height':297,
                    'page_width':210,
                    'orientation':'Portrait',
                    'margin_top':7,
                    'margin_bottom':7,
                    'margin_left':0,
                    'margin_right':0,
                    'header_line':False,
                    'header_spacing':7,
                    'dpi':90
                }
                paper_id = self.env['report.paperformat'].sudo().create(vals)
                if paper_id:
                    paper_id.page_height = self.template_id.page_height
                    paper_id.page_width = self.template_id.page_width
                    report_id.paperformat_id = paper_id and paper_id.id or False
        
    
    
    
    def get_vals(self):
        self.set_paper_size()
        vals=[]
        for line in self.pro_line_ids:
            count=0
            while (count < line.label):
                att_name = self.get_attribute(line.product_id)
                barcode_label = ''
                if self.template_id.barcode_from == 'default_code':
                    barcode_label = line.product_id.default_code
                else:
                    barcode_label = line.product_id.barcode
                vals.append({
                    'name':line.product_id.name,
                    'attribute':att_name,
                    'barcode':line.product_id.barcode,
                    'default_code':line.product_id.default_code,
                    'barcode_label':barcode_label or '',
                    'barcode_type':self.template_id.barcode_type,
                })
                
                count +=1
        return vals
        
        
    
#    @api.multi
#    def get_vals(self):
#        vals=[]
#        count=0
#        while (count <= self.label):
#            val = []
#            for i in range(0, self.row):
#                count +=1
#                if count <= self.label:
#                    val.append({
#                        'name':self.product_id.name,
#                    })
#            vals.append(val)
#        return vals
            

    def print_pdf(self):
        data={}
        data['form'] = self.read()[0]
        return self.env.ref('dev_product_label.dev_print_product_label').report_action(self, data=None)
        
class dev_product_line(models.TransientModel):
    _name = "dev.product.line"
    
    product_id = fields.Many2one('product.product', string='Product', required="1")
    label = fields.Integer(string='No of Label', required="1", default=5)
    pro_label_id = fields.Many2one('dev.product.label', string='Product Label')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
