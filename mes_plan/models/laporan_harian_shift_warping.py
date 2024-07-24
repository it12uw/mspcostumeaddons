from flectra import api, fields, models, _
from flectra.exceptions import UserError

#--------------------------------- class baru -----------------------------------------------
class InLaporanHarianShiftWarping(models.Model):
    _description = "Laporan Harian Shift Warping"
    _name = "laporanharian.shiftwarping"
    #_rec_name = "name"

    no_kp = fields.Many2one('herader.planwarping',string='No KP/MO')
    seri = fields.Char(related='no_kp.seri',string='Seri',readonly=True,)
    tarikan = fields.Char(related='no_kp.tarikan',string='Tarikan',readonly=True,)
    quantity = fields.Float(related='no_kp.quantity',string='Quantity',readonly=True,)
    mesin = fields.Many2one(related='no_kp.mesin',string='Mesin Warping', readonly=True,)
    date_start = fields.Date(related='no_kp.date_start',string="Start Date",readonly=True,)
    date_end = fields.Date(related='no_kp.date_end',string="End Date",readonly=True,)
#------------------------- operator ------------------------------------------------------
    tgl = fields.Date(string='Tgl', required=True)
    operator = fields.Char(string='Operator',)
    waktu = fields.Char(string='waktu/jam',)
    panjang_tiap_beam = fields.Char(string='Panjang Tiap Beam', )
    hasil_perbeam = fields.Char(string='Hasil  Per Beam', )
    pts_persejuta = fields.Float(string='pts/1juta', )
    provit = fields.Integer(string='Provit', )
    ttl_lost_time = fields.Char(string='TTL Lost Time', )
    eff = fields.Char(string='EFF', )
    keterangan = fields.Text(tring='Keterangan',)
#--------------------------------- class baru -----------------------------------------------
