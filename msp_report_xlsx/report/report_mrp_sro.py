from flectra import models, fields, api
from datetime import datetime, date
from flectra import http
from flectra.http import content_disposition, request
import io
import xlsxwriter
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from flectra import tools

class ReportMrpSro(models.Model):
    _name = "report.mrp.sro"
    # _inherit = ['mrp.production']
    _auto = False
    _rec_name = 'origin'
    _order = 'origin desc'


    date_planned_start = fields.Datetime(string="Deadline Start",readonly=True)
    name = fields.Char('Reference', copy=False, readonly=True)
    origin = fields.Char(string="No Sr",readonly=True)
    product_id = fields.Many2one('product.product', 'Product', readonly=True)
    categ_id = fields.Many2one('product.category', 'Product', readonly=True)
    picking_type_id = fields.Many2one('stock.picking.type', 'Type Picking', readonly=True)
    product_qty = fields.Float('Qty Order',readonly=True)
    total_qty_done = fields.Float('Qty Done',readonly=True)
    qty_kekurangan = fields.Float(string=u'Qty Kekurangan',readonly=True)
    state = fields.Selection([
        ('confirmed', 'Confirmed'),
        ('planned', 'Planned'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='State',)

    @api.model_cr
    def init(self):
        """ Report Mrp Sro """
        tools.drop_view_if_exists(self._cr, 'report_mrp_sro')
        self._cr.execute(""" CREATE VIEW report_mrp_sro AS (
            SELECT
                min(mp.id) as id,
                mp.date_planned_start as date_planned_start,
                mp.name as name,
				mp.origin as origin,
				mp.product_id as product_id,
				pt.categ_id as categ_id,
				mp.product_qty as product_qty,
 				mp.total_qty_done as total_qty_done,
 				mp.qty_kekurangan as qty_kekurangan,
 				mp.state as state
            FROM
                mrp_production mp
                join product_product pp on mp.product_id = pp.id
                join product_template pt on pp.product_tmpl_id = pt.id
            WHERE
				mp.origin like '%SR/%' or
 				mp.origin like '%SRO/%' or
 				mp.origin like '%Request2MSP%' or
 				mp.origin like '%Request > WH2M%'
            GROUP BY
                mp.id,
                mp.date_planned_start,
                mp.name,
				mp.origin,
				mp.product_id,
                pt.categ_id,
				mp.product_qty,
 				mp.total_qty_done,
 				mp.qty_kekurangan,
 				mp.state
        )""")