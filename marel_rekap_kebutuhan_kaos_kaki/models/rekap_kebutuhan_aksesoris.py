from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
import flectra.addons.decimal_precision as dp

class RekapKebutuhanAksesoris(models.Model):
	_name = 'rekap.kebutuhan.aksesoris'
	_description = u'RekapKebutuhanAksesoris'
	_rec_name = 'mrp_production_id'
	
	rekap_kebutuhan_aksesoris_line = fields.One2many('rekap.kebutuhan.aksesoris.line','rekap_kebutuhan_aksesoris_id',string=u'Rekap Aksesoris Line',required=True,)
	tgl_pengajuan = fields.Date(string=u'Tgl Pengajuan',default=fields.Date.context_today,)
	mrp_production_id = fields.Many2one('mrp.production',string=u'No MO',)
	status_deskripsi = fields.Selection(string=u'Status Deskripsi',selection=[('Pengajuan Awal', 'Pengajuan Awal'), ('Revisi', 'Revisi')])
	partner_id = fields.Many2one('res.partner', string='Customer',)


class RekapKebutuhanAksesorisLine(models.Model):
	_name = 'rekap.kebutuhan.aksesoris.line'
	_description = u'RekapKebutuhanAksesorisLine'
	_rec_name = 'product_template_id'
	
	rekap_kebutuhan_aksesoris_id = fields.Many2one('rekap.kebutuhan.aksesoris',string=u'Rekap Aksesoris',)
	product_template_id = fields.Many2one('product.template',string=u'Nama Aksesoris',)
	jumlah = fields.Integer(string=u'jumlah',)

# class RekapKebutuhanAksesoris(models.Model):
#     _name = 'rekap.kebutuhan.aksesoris'
# 	_rec_name = 'mrp_production_id'
# 	_description = u'RekapKebutuhanAksesoris'
	
# 	rekap_kebutuhan_aksesoris_line = fields.One2many('rekap.kebutuhan.aksesoris.line','rekap_kebutuhan_aksesoris_id',string=u'Rekap Aksesoris Line',required=True,)
# 	tgl_pengajuan = fields.Date(string=u'Tgl Pengajuan',default=fields.Date.context_today,)
# 	mrp_production_id = fields.Many2one('mrp.production',string=u'No MO',)
# 	status_deskripsi = fields.Selection(string=u'Status Deskripsi',selection=[('Pengajuan Awal', 'Pengajuan Awal'), ('Revisi', 'Revisi')])
# 	partner_id = fields.Many2one('res.partner', string='Customer',)
		

# class RekapKebutuhanAksesorisLine(models.Model):
#     _name = 'rekap.kebutuhan.aksesoris.line'
# 	_description = u'RekapKebutuhanAksesorisLine'
# 	_rec_name = 'product_template_id'
	
# 	rekap_kebutuhan_aksesoris_id = fields.Many2one('rekap.kebutuhan.aksesoris',string=u'Rekap Aksesoris',)
# 	product_template_id = fields.Many2one('product.template',string=u'Nama Aksesoris',)
# 	jumlah = fields.Integer(string=u'jumlah',)