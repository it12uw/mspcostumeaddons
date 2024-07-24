from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import flectra.addons.decimal_precision as dp

class marel_pengambilan_sparepart(models.Model):
	_name="marel.pengambilan.sparepart"
	_description = "Pengambilan Sparepart"
	_order = "name desc"
	
	# def get_no_pengambilan_sparepart(self):
	# 	nama_baru = self.env['ir.sequence'].next_by_code('marel.pengambilan.sparepart.no')
	# 	return nama_baru

	@api.model
	def create(self, vals):
		if vals.get('name', 'New') == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('marel.pengambilan.sparepart.no') or 'New'
			result = super(marel_pengambilan_sparepart, self).create(vals)
		return result

	name = fields.Char('Id',readonly=True, required=True, copy=False, default='New')
	# name = fields.Char('Id',readonly=True,copy=False,default=get_no_pengambilan_sparepart,)
	shift = fields.Selection(string=u'Shift',selection=[('A', 'A'),('B', 'B'), ('C', 'C')],)
	marel_pengambilan_sparepart_line = fields.One2many('marel.pengambilan.sparepart.line','marel_pengambilan_sparepart_id',string=u'Rekap Aksesoris Line',required=True,)
	tgl_pengambilan = fields.Date(string=u'Tgl Pengambilan',default=fields.Date.context_today,)
	partner_id = fields.Many2one('res.partner', string='Customer',)
	state = fields.Selection([
         ('draft','Draft'),
         ('confirm','Confirmed'),
         ('cancel','Cancelled')
    ], string='State', default='draft')	
		
	@api.multi
	def action_confirm(self):
		self.write({'state': 'confirm'})	

	@api.multi
	def action_cancel(self):
		self.write({'state': 'cancel'})	
    
	@api.multi
	def unlink(self):
		for me_id in self :
			if me_id.state != 'draft' :
				raise Warning("Tidak bisa menghapus data pendaftaran yang bukan draft !")
		return super(marel_pengambilan_sparepart, self).unlink()

class marel_pengambilan_sparepart_line(models.Model):
	_name = 'marel.pengambilan.sparepart.line'
	_rec_name = 'product_id'
	
	product_id = fields.Many2one('product.product',string=u'Nama Barang',)
	jumlah_pengambilan = fields.Float(string=u'Jumlah Pengambilan',required=True,)
	no_mesin_id = fields.Many2one('mesin.marel.produksi',string=u'No Mesin',)
	keterangan = fields.Text(string=u'Keterangan',)
	marel_pengambilan_sparepart_id = fields.Many2one('marel.pengambilan.sparepart',string=u'Pengambilan Sparepart',)
	