from flectra import api, fields, models, _
from flectra.exceptions import UserError


class InSerahTrimabenang(models.Model):
    _description = "Serah Trimabenang"
    _name = "serah.trimabenang"
    
    tgl_buat = fields.Date(string='Tanggal Buat',default=fields.Date.context_today,readonly=True,)
    #waktu_create =  fields.Date(string='Waktu Create', default=datetime.today()readonly=True,)
    no_kp = fields.Many2one('mrp.production',string='No KP/MO')
    kode = fields.Char(related='no_kp.product_tmpl_id.kode',string='Kode', store= True, readonly=True,)
    jenis_benang = fields.Char(related='no_kp.product_tmpl_id.jenis_benang',string='Jenis Benang',readonly=True,)
    #jenis_benang = fields.Char(related='no_kp.product_tmpl_id.jenis_benang',string='Jenis Benang',readonly=True,)
    #kode = fields.Char(related='no_kp.product_tmpl_id.kode',string='Kode Benang',readonly=True,)
    jumlah_bon = fields.Float(string='Jumlah Bon',)