# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from flectra import api, fields, models, tools

class MPCproducelotreport(models.Model):
    _name = "mpc.produce.lot.report"
    _auto = False

    
    # lot_id = fields.Many2one('stock.production.lot', 'Barcode', readonly=True)
    date = fields.Datetime(string='Date', readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    product_tmpl_id = fields.Many2one('product.template', string='Product Template', related='product_id.product_tmpl_id', readonly=True)
    kode_lot = fields.Char('Kode Lot', readonly=True)
    qty_done = fields.Float('Qty', readonly=True)
    avg_qty = fields.Float('Rata Mtr', readonly=True, group_operator = 'avg')
    percentage = fields.Float('Percent%', readonly=True,)
    production_id = fields.Many2one('mrp.production', 'MO/KP', readonly=True)
    reference = fields.Char('Ref MO/KP', readonly=True)
    categ_id = fields.Many2one('product.category', 'Category', readonly=True)
    

    @api.model_cr
    def init(self):
        """ MPC Produce Lot Report """
        tools.drop_view_if_exists(self._cr, 'mpc_produce_lot_report')
        self._cr.execute(""" CREATE VIEW mpc_produce_lot_report AS (
            SELECT
                sml.id as id,
                sml.create_date as date,
                sml.product_id as product_id,
                pt.default_code as kode_lot,
                sum(sml.qty_done) as qty_done,
                sml.production_id as production_id,
                sml.reference as reference,
                pc.id as categ_id,
                sum(sml.qty_done) as avg_qty,
                sum(sml.qty_done) as percentage
                
            FROM
                stock_move_line sml
            LEFT JOIN
                product_product pp ON (sml.product_id = pp.id)
            LEFT JOIN
                product_template pt ON (pp.product_tmpl_id = pt.id)
            LEFT JOIN
                product_category pc ON (pt.categ_id = pc.id)
            LEFT JOIN
                mrp_production mrp ON (sml.production_id = mrp.id)
            
            
            WHERE
                sml.location_id=7 and (sml.location_dest_id in (12,31))
            
            GROUP BY
                sml.id, sml.product_id, sml.create_date, pt.default_code, 
                sml.production_id,
                sml.reference,
                sml.qty_done,
                pc.id
        )""")