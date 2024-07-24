# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from flectra import models, fields, api, _
from flectra.exceptions import ValidationError
from io import BytesIO
import xlwt
import base64
from datetime import datetime, date


class stock_jadi_wizard(models.TransientModel):
    _name = 'stock.jadi.wizard'
    _description = 'Stock Jadi Wizard'

    # @api.model
    # def send_inventory_report(self):
    #     ir_config_obj = self.env['ir.config_parameter']
    #     template_id = ir_config_obj.sudo().get_param('aspl_stock_jadi_report.stock_jadi_report_email_template_id')
    #     if template_id:
    #         email_template_id = self.env['mail.template'].search([('id', '=', int(template_id))])
    #         if ir_config_obj.sudo().get_param('aspl_stock_jadi_report.stock_jadi_report') and email_template_id:
    #             config_ids = self.env['res.config.settings'].search([], order="id desc", limit=1)
    #             for each in config_ids.inventory_report_user_ids.filtered(lambda l:l.email):
    #                 warehouse_ids = self.env['stock.warehouse'].search([('company_id', '=', each.company_id.id)])
    #                 inventory_wizard_id = self.create({
    #                                                    'company_id':each.company_id.id,
    #                                                    'start_date':date.today(),
    #                                                    'end_date':date.today(),
    #                                                    'warehouse_ids':[(6, 0, warehouse_ids.ids)],
    #                                                    'is_today_movement':True
    #                                                    })
    #                 inventory_wizard_id.generate_pdf_report()
    #                 email_subject = 'Stock Stock Report ' + str(date.today())
    #                 email_template_id.with_context({'user_email':each.email, 'email_subject':email_subject}).send_mail(inventory_wizard_id.id, force_send=True)

    start_date = fields.Date(string="Start Date", default=fields.Date.context_today)
    end_date = fields.Date(string="End Date", default=fields.Date.context_today)
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.user.company_id.id, required=True)
    warehouse_ids = fields.Many2many('stock.warehouse', 'warehouse_wizard_jadi_rel', string="Warehouse", required=True)
    location_id = fields.Many2one('stock.location', string="Location")
    filter_by = fields.Selection([('product', 'Product'), ('category', 'Category')], string="Filter By")
    group_by_categ = fields.Boolean(string="Category Group By")
    with_zero = fields.Boolean(string="With Zero Values")
    state = fields.Selection([('choose', 'choose'), ('get', 'get')], default='choose')
    name = fields.Char(string='File Name', readonly=True)
    data = fields.Binary(string='File', readonly=True)
    product_ids = fields.Many2many('product.product', 'product_jadi_inv_rel', string="Products")
    category_ids = fields.Many2many('product.category', 'product_categ_jadi_inv_rel', string="Categories")
    is_today_movement = fields.Boolean(string="Today Movement")

    @api.onchange('warehouse_ids')
    def onchange_warehouse_ids(self):
        if self.warehouse_ids:
            self.location_id = False

    @api.onchange('filter_by')
    def onchange_filter_by(self):
        self.product_ids = self.category_ids = False

    @api.onchange('company_id')
    def onchange_company_id(self):
        if self.company_id:
            self.warehouse_ids = self.location_id = False

    def check_date_range(self):
        if self.end_date < self.start_date:
            raise ValidationError(_('Enter proper date range'))

    def generate_pdf_report(self):
        self.check_date_range()
        datas = {'form':
                    {
                        'company_id': self.company_id.id,
                        'warehouse_ids': [y.id for y in self.warehouse_ids],
                        'location_id': self.location_id and self.location_id.id or False,
                        'start_date': date.today() if self.is_today_movement else self.start_date,
                        'end_date': date.today() if self.is_today_movement else self.end_date,
                        'id': self.id,
                        'product_ids': self.product_ids.ids,
                        'product_categ_ids': self.category_ids.ids
                    },
                }
        return self.env.ref('aspl_stock_jadi_report.action_report_stock_jadi').report_action(self, data=datas)

    def generate_xls_report(self):
        self.check_date_range()
        report_stock_inv_obj = self.env['report.aspl_stock_jadi_report.report_stock_jadi']
        workbook = xlwt.Workbook(encoding="utf-8")
        number_format = xlwt.easyxf(num_format_str = "#,##0.0000")

        for warehouse in self.warehouse_ids:
            header_style = xlwt.XFStyle()
            alignment = xlwt.Alignment()
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            font = xlwt.Font()
            fontP = xlwt.Font()
            font.bold = True
            font.height = 240
            font.colour_index = 2
            fontP.bold = True
            header_style.num_format_str = "#,##0.0000"

            # Cell Color
            pattern = xlwt.Pattern()
            pattern.pattern = xlwt.Pattern.SOLID_PATTERN
            pattern.pattern_fore_colour = 22

            header_style.font = fontP
            header_style.alignment = alignment
            header_style.pattern = pattern

            header_data = xlwt.XFStyle()
            alignment = xlwt.Alignment()
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            header_data.alignment = alignment
            

            total_value_style = xlwt.XFStyle()
            alignment = xlwt.Alignment()
            alignment.horz = xlwt.Alignment.HORZ_RIGHT
            total_value_style.alignment = alignment
            total_value_style.font = fontP
            total_value_style.num_format_str = "#,##0.0000"

            worksheet = workbook.add_sheet(warehouse.name, cell_overwrite_ok=True)
            worksheet.write_merge(0, 1, 0, 10, "Stock Report", style=header_style)


            for cols_width in range(0, 10):
                worksheet.col(cols_width).width = 4500

            # Excel Sheet Header Data 
            upper_header_lst = ['Company', 'Warehouse', 'Location', 'Start Date', 'End Date', 'Generated By', 'Generated Date']
            col = 0
            for header in upper_header_lst:
                worksheet.write(5, col, header, style=header_style)
                col += 1

            upper_header_lst_data = [self.company_id.name, warehouse.name, self.location_id.name if self.location_id else "All",
                                     self.start_date, self.end_date, self.env.user.name, str(datetime.today().date())]

            col = 0
            for header_value in upper_header_lst_data:
                worksheet.write(6, col, header_value, style=header_data)
                col += 1

            #worksheet.write_merge(9, 9, 0, 2, "Products", style=header_style)

            lower_header_lst = ['SKU', 'Product', 'Ne', 'Cost', 'Beginning', 'Received', 'Sales'
                                , 'Internal'
                                , 'Inspect', 'Production', 'Adjustments', 'Ending', 'Value']
            # row = 3
            row = 0
            for header in lower_header_lst:
                worksheet.write(9, row, header, style=header_style)
                row += 1
# 
            rows = 10
            prod_beginning_qty = prod_qty_in = prod_qty_out = prod_qty_int = prod_qty_ins = prod_qty_pjmin = prod_qty_pjmout = prod_qty_rpro = prod_qty_pro = prod_qty_adjust = prod_ending_qty = val_ending_qty = 0.00
 
            if not self.group_by_categ:
                product_ids = report_stock_inv_obj._get_products(self)
                for product in product_ids:
                    beginning_qty = report_stock_inv_obj._get_beginning_inventory(self, product)
                    product_val = report_stock_inv_obj.get_product_sale_qty(self, product)
                    today_movment_qty = product_val.get('product_qty_in') + product_val.get('product_qty_out')\
                        + product_val.get('product_qty_inspect') + product_val.get('product_qty_mrp')\
                        + product_val.get('product_qty_adjustment') + product_val.get('product_qty_internal')

                    ending_qty = beginning_qty + product_val.get('product_qty_in') + product_val.get('product_qty_out')\
                        + product_val.get('product_qty_inspect') + product_val.get('product_qty_mrp')\
                        + product_val.get('product_qty_adjustment') + product_val.get('product_qty_internal')
                    if not self.with_zero and beginning_qty == 0.0 and product_val.get('product_qty_in') == 0.0 and product_val.get('product_qty_out') == 0.0 and \
                        product_val.get('product_qty_inspect') == 0.0 and product_val.get('product_qty_internal') == 0.0 and \
                        product_val.get('product_qty_mrp') == 0.0 and product_val.get('product_qty_adjustment') == 0:
                        continue
                    elif today_movment_qty == 0.00 and self.is_today_movement:
                        continue
                    val_qty =  ending_qty*product.standard_price
                    # + product_val.get('product_qty_internal')
                    # worksheet.write_merge(rows, rows, 0, 2, product.name_get()[0][1])
                    worksheet.write(rows, 0, product.default_code)
                    worksheet.write(rows, 1, product.name)
                    worksheet.write(rows, 2, product.product_tmpl_id.list_price)
                    worksheet.write(rows, 3, product.product_tmpl_id.standard_price, number_format)
                    worksheet.write(rows, 4, beginning_qty, number_format)
                    worksheet.write(rows, 5, product_val.get('product_qty_in'), number_format)
                    worksheet.write(rows, 6, abs(product_val.get('product_qty_out')), number_format)
                    worksheet.write(rows, 7, product_val.get('product_qty_internal'), number_format)
                    worksheet.write(rows, 8, product_val.get('product_qty_inspect'), number_format)
                    worksheet.write(rows, 9, product_val.get('product_qty_mrp'), number_format)
                    worksheet.write(rows, 10, product_val.get('product_qty_adjustment'), number_format)
                    worksheet.write(rows, 11, ending_qty, number_format)
                    worksheet.write(rows, 12, val_qty, number_format)
                    prod_qty_in += product_val.get('product_qty_in')
                    prod_qty_out += product_val.get('product_qty_out')
                    prod_qty_int += product_val.get('product_qty_internal')
                    prod_qty_ins += product_val.get('product_qty_inspect')
                    prod_qty_pro += product_val.get('product_qty_mrp')
                    prod_qty_adjust += product_val.get('product_qty_adjustment')
                    prod_ending_qty += ending_qty
                    prod_beginning_qty += beginning_qty
                    val_ending_qty += val_qty
                    rows += 1
                worksheet.write_merge(rows + 1, rows + 1, 0, 3, 'Total', style=header_style)
                worksheet.write(rows + 1, 4, prod_beginning_qty, style=header_style)
                worksheet.write(rows + 1, 5, prod_qty_in, style=header_style)
                worksheet.write(rows + 1, 6, abs(prod_qty_out), style=header_style)
                worksheet.write(rows + 1, 7, prod_qty_int, style=header_style)
                worksheet.write(rows + 1, 8, prod_qty_ins, style=header_style)
                worksheet.write(rows + 1, 9, prod_qty_pro, style=header_style)
                worksheet.write(rows + 1, 10, prod_qty_adjust, style=header_style)
                worksheet.write(rows + 1, 11, prod_ending_qty, style=header_style)
                worksheet.write(rows + 1, 12, val_ending_qty, style=header_style)
            else:
                rows += 1
                product_val = report_stock_inv_obj.get_product_sale_qty(self)
                for categ, product_value in product_val.items():
                    categ_prod_beginning_qty = categ_prod_qty_in = categ_prod_qty_out = categ_prod_qty_ins = categ_prod_qty_int = categ_prod_qty_pro = categ_prod_qty_adjust = categ_prod_ending_qty = categ_val_ending_qty = 0.00
                    worksheet.write_merge(rows, rows, 0, 10, self.env['product.category'].browse(categ).name, style=header_style)
                    rows += 1
                    for product in product_value:
                        product_id = self.env['product.product'].browse(product['product_id'])
                        beginning_qty = report_stock_inv_obj._get_beginning_inventory(self, product_id.id)
                        ending_qty = beginning_qty + product.get('product_qty_in') + product.get('product_qty_out') \
                            + product.get('product_qty_inspect') + product.get('product_qty_mrp') \
                            + product.get('product_qty_adjustment') + product.get('product_qty_internal')
                        if not self.with_zero and beginning_qty == 0.0 and product.get('product_qty_in') == 0.0 and product.get('product_qty_out') == 0.0 and \
                            product.get('product_qty_internal') == 0.0 and product.get('product_qty_inspect') == 0.0 and \
                            product.get('product_qty_mrp') == 0.0 and product.get('product_qty_adjustment') == 0:
                            continue
                        val_qty =  ending_qty*product_id.standard_price
                        # + product.get('product_qty_internal') 
                        # worksheet.write_merge(rows, rows, 0, 2, product_id.name_get()[0][1])
                        worksheet.write(rows, 0, product_id.default_code)
                        worksheet.write(rows, 1, product_id.name)
                        worksheet.write(rows, 2, product_id.product_tmpl_id.list_price)
                        worksheet.write(rows, 3, product_id.standard_price, number_format)
                        worksheet.write(rows, 4, beginning_qty, number_format)
                        worksheet.write(rows, 5, product.get('product_qty_in'), number_format)
                        worksheet.write(rows, 6, abs(product.get('product_qty_out')), number_format)
                        worksheet.write(rows, 7, product.get('product_qty_internal'), number_format)
                        worksheet.write(rows, 8, product.get('product_qty_inspect'), number_format)
                        worksheet.write(rows, 9, product.get('product_qty_mrp'), number_format)
                        worksheet.write(rows, 10, product.get('product_qty_adjustment'), number_format)
                        worksheet.write(rows, 11, ending_qty, number_format)
                        worksheet.write(rows, 12, val_qty, number_format)
                        categ_prod_qty_in += product.get('product_qty_in')
                        categ_prod_qty_out += product.get('product_qty_out')
                        categ_prod_qty_int += product.get('product_qty_internal')
                        categ_prod_qty_ins += product.get('product_qty_inspect')
                        categ_prod_qty_pro += product.get('product_qty_mrp')
                        categ_prod_qty_adjust += product.get('product_qty_adjustment')
                        categ_prod_ending_qty += ending_qty
                        categ_prod_beginning_qty += beginning_qty
                        categ_val_ending_qty += val_qty
                        rows += 1
                    worksheet.write_merge(rows, rows, 0, 3, 'Total', style=total_value_style)
                    worksheet.write(rows, 4, categ_prod_beginning_qty, style=total_value_style)
                    worksheet.write(rows, 5, categ_prod_qty_in, style=total_value_style)
                    worksheet.write(rows, 6, abs(categ_prod_qty_out), style=total_value_style)
                    worksheet.write(rows, 7, categ_prod_qty_int, style=total_value_style)
                    worksheet.write(rows, 8, categ_prod_qty_ins, style=total_value_style)
                    worksheet.write(rows, 9, categ_prod_qty_pro, style=total_value_style)
                    worksheet.write(rows, 10, categ_prod_qty_adjust, style=total_value_style)
                    worksheet.write(rows, 11, categ_prod_ending_qty, style=total_value_style)
                    worksheet.write(rows, 12, categ_val_ending_qty, style=header_style)
                    prod_qty_in += categ_prod_qty_in
                    prod_qty_out += categ_prod_qty_out
                    prod_qty_int += categ_prod_qty_int
                    prod_qty_ins += categ_prod_qty_ins
                    prod_qty_pro += categ_prod_qty_pro
                    prod_qty_adjust += categ_prod_qty_adjust
                    prod_ending_qty += categ_prod_ending_qty
                    prod_beginning_qty += categ_prod_beginning_qty
                    val_ending_qty += categ_val_ending_qty
                    rows += 1
                worksheet.write_merge(rows + 1, rows + 1, 0, 3, "Grand Total", style=header_style)
                worksheet.write(rows + 1, 4, prod_beginning_qty, style=header_style)
                worksheet.write(rows + 1, 5, prod_qty_in, style=header_style)
                worksheet.write(rows + 1, 6, abs(prod_qty_out), style=header_style)
                worksheet.write(rows + 1, 7, prod_qty_int, style=header_style)
                worksheet.write(rows + 1, 8, prod_qty_ins, style=header_style)
                worksheet.write(rows + 1, 9, prod_qty_pro, style=header_style)
                worksheet.write(rows + 1, 10, prod_qty_adjust, style=header_style)
                worksheet.write(rows + 1, 11, prod_ending_qty, style=header_style)
                worksheet.write(rows + 1, 12, val_ending_qty, style=header_style)

        file_data = BytesIO()
        workbook.save(file_data)
        self.write({
            'state': 'get',
            'data': base64.encodestring(file_data.getvalue()),
            'name': 'stock_jadi.xlsx'
        })
        return {
            'name': 'Stock Jadi Report',
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target': 'new'
        }


class stock_location(models.Model):
    _inherit = 'stock.location'

    @api.model
    def name_search(self, name, args, operator='ilike', limit=100):
        if self._context.get('company_id'):
            domain = [('company_id', '=', self._context.get('company_id')), ('usage', '=', 'internal')]
            if self._context.get('warehouse_ids') and self._context.get('warehouse_ids')[0][2]:
                warehouse_ids = self._context.get('warehouse_ids')[0][2]
                stock_ids = []
                for warehouse in self.env['stock.warehouse'].browse(warehouse_ids):
                    stock_ids.append(warehouse.view_location_id.id)
                domain.append(('location_id', 'child_of', stock_ids))
            args += domain
        return super(stock_location, self).name_search(name, args, operator, limit)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
