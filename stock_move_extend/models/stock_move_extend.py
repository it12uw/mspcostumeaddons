from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError


class StockMoveExtend(models.Model):
    _inherit = 'stock.move.line'

    product_move_tmpl = fields.Many2one(
        'product.template', 'Product Template',
        related='product_id.product_tmpl_id',
        help="Technical: used in views")
    categ_id = fields.Many2one('product.category','Category',related='product_move_tmpl.categ_id', store=True)
    group_id = fields.Many2one('procurement.group',string='SO', related='move_id.group_id')
    no_spb = fields.Char(string='SPB', related='picking_id.no_spb')
    no_bpb = fields.Char(string='BPB', related='picking_id.no_bpb')
    no_so = fields.Char(string='Origin', related='move_id.origin')
    no_sj = fields.Char(string='SJ', related='picking_id.no_sj')
    tgl_transaksi = fields.Date(string='Tgl Kirim', related='picking_id.tgl_transaksi')
    scheduled_date = fields.Datetime(string='Scheduled Date', related='picking_id.scheduled_date',store=True)
    partner_id = fields.Many2one('res.partner',string='Partner', related='picking_id.partner_id')
    price_unit = fields.Float(string='Cost', related='move_id.price_unit')
    sale_price = fields.Float(string='Price', related='move_id.sale_line_id.price_unit')



