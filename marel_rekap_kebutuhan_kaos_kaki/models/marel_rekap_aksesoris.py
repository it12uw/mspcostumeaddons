from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import flectra.addons.decimal_precision as dp

class MarelListRekapAksesorisBarang(models.Model):

	_name = 'marel.listrekap.aksesorisbarang'
	_description = u'Marel List Rekap Aksesoris Barang'

	_rec_name = 'product_template_id'
	# _order = 'name ASC'
    # jenis_kerusakan_mesinmarel_id = fields.Many2one('jenis.kerusakan.mesinmarel', 'Jenis Kerusakan Mesin Marel')
		
	product_template_id = fields.Many2one('product.template',string=u'Nama Barang', required=True,)

	product_template_kaos_kaki_1 = fields.Many2one('product.template',string=u'Kaos Kaki 1',)
	
	product_template_kaos_kaki_2 = fields.Many2one('product.template',string=u'Kaos Kaki 2',)
	
	product_template_kaos_kaki_3 = fields.Many2one('product.template',string=u'Kaos Kaki 3',)
	
	product_template_kaos_kaki_4 = fields.Many2one('product.template',string=u'Kaos Kaki 4',)
	
	product_template_kaos_kaki_5 = fields.Many2one('product.template',string=u'Kaos Kaki 5',)
			
	marel_rekap_aksesoris_id = fields.Many2one('marel.rekap.aksesoris', 'Data Marel Rekap Aksesoris')

	jumlah_beli_1 = fields.Integer(string=u'Jumlah Artikel 1',)
	
	jumlah_beli_2 = fields.Integer(string=u'Jumlah Artikel 2',)
	
	jumlah_beli_3 = fields.Integer(string=u'Jumlah Artikel 3',)
	
	jumlah_beli_4 = fields.Integer(string=u'Jumlah Artikel 4',)
	
	jumlah_beli_5 = fields.Integer(string=u'Jumlah Artikel 5',)
	
	delivery_rekap_aksesoris_1 = fields.Date(string=u'Tgl Kirim Artikel 1',default=fields.Date.context_today,)
	
	delivery_rekap_aksesoris_2 = fields.Date(string=u'Tgl Kirim Artikel 2',default=fields.Date.context_today,)
	
	delivery_rekap_aksesoris_3 = fields.Date(string=u'Tgl Kirim Artikel 3',default=fields.Date.context_today,)
	
	delivery_rekap_aksesoris_4 = fields.Date(string=u'Tgl Kirim Artikel 4',default=fields.Date.context_today,)
	
	delivery_rekap_aksesoris_5 = fields.Date(string=u'Tgl Kirim Artikel 5',default=fields.Date.context_today,)
	
	total_beli = fields.Integer(string=u'Total',compute='_total_beli_barang',store=True,readonly=True)
	#compute='_total_beli_barang',store=True,
	
	@api.depends('jumlah_beli_1','jumlah_beli_2','jumlah_beli_3','jumlah_beli_4','jumlah_beli_5','total_beli')
	def _total_beli_barang (self):
    		for l in self:
    					if l.jumlah_beli_1 or l.jumlah_beli_2 or l.jumlah_beli_3 or l.jumlah_beli_4 or l.jumlah_beli_5 != 0:
    								l.total_beli = l.jumlah_beli_1 + l.jumlah_beli_2 + l.jumlah_beli_3 + l.jumlah_beli_4 + l.jumlah_beli_5
    					else:
    								l.total_beli == 0

	# @api.depends('point_1','point_2','point_3','point_4','total_point', 'product_qty') 
  #   def _total_semua_point(self):
  #       if self.point_1 or self.point_2 or self.point_3 or self.point_4 != 0:
  #               self.total_point = (self.point_1 + self.point_2 + self.point_3 + self.point_4)/self.product_qty
  #       else:
  #           self.total_point == 0
	
class MarelRekapAksesoris(models.Model):
	
	_name = 'marel.rekap.aksesoris'
	_description = u'Marel Rekap Aksesoris'

	# _rec_name = 'name'
	# _order = 'name ASC'

	# product_template_id = fields.Many2one('product.template',string=u'Nama Kaos Kaki',)	
	# sale_order_id = fields.Many2one('sale.order', 'Customer')

	marel_listrekap_aksesorisbarang_line = fields.One2many('marel.listrekap.aksesorisbarang','marel_rekap_aksesoris_id',string=u'List Rekap Aksesoris',required=True,)
		
	res_partner_id = fields.Many2one('res.partner',string=u'Customer',required=True,)
