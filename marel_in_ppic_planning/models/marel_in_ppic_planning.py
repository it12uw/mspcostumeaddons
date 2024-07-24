from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

class MarelInPpicPlanning(models.Model):
    _name = 'marel.in.ppic.planning'
    _description = u'Marel In Ppic Planning'
    _rec_name = 'no_mo_id'


    no_mesin_id = fields.Many2one('mesin.marel.produksi','No Mesin',)
    no_mo_id = fields.Many2one('mrp.workorder',string=u'No MO',)
    product_id = fields.Many2one(related='no_mo_id.product_id',string=u'Nama Artikel',readonly=True,)
    total_yg_telah_jadi = fields.Float(related='no_mo_id.qty_produced',string=u'Qty Finish',readonly=True,)
    total_yg_blm_selesai = fields.Float(related='no_mo_id.qty_producing',string=u'Qty Blm Selesai',readonly=True,)
    total_orderan = fields.Float(related='no_mo_id.qty_production',string=u'Qty Orderan',readonly=True,)
    product_uom_id = fields.Many2one('product.uom', 'Unit of Measure',related='no_mo_id.product_uom_id', readonly=True,help='Technical: used in views only.')
    tgl_mulai = fields.Date(string=u'Tgl Mulai',)
    tgl_akhir = fields.Date(string=u'Tgl Akhir',)        