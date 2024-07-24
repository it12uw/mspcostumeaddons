from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import flectra.addons.decimal_precision as dp

class MarelDataProdakAfal(models.Model):
    _name = 'marel.data.prodakafal'
    _inherit = ['mail.thread', 'mail.activity.mixin']
  
    def get_marel_data_prodak_afal_no(self):
      nama_baru = self.env['ir.sequence'].next_by_code('marel.data.prodakafal.no')
      return nama_baru
      
    name = fields.Char(string='Id Afal',required=True,copy=False, default=get_marel_data_prodak_afal_no,readonly=True )
    create_date = fields.Date(string='create_date',default=fields.Date.context_today,)
    product_id = fields.Many2one('product.product',string='Produk',)
    uom_id = fields.Char(string='Satuan',related='product_id.uom_id.name',)
    jenis_afal_id = fields.Many2one('marel.jenis.afal',string='Jenis Afal',)
    qty = fields.Float(string='Qty',)
    



class MarelJenisAfal(models.Model):
    _name = 'marel.jenis.afal'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Jenis Afal',)