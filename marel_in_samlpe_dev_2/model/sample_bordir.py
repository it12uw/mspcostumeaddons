from flectra import models, fields, api, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from flectra.exceptions import UserError, ValidationError

class SampleBordir(models.Model):
    _name = 'sample.bordir'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sample Bordir'
    _rec_name = 'nama_produk'

    def get_name_new(self):
         nama_baru = self.env['ir.sequence'].next_by_code('sample.bordir.app')
         return nama_baru

    product_tmpl_id = fields.Many2one(related='nama_produk.product_tmpl_id',string='Produck Template',store=True)
    jarum = fields.Integer(related='nama_produk.jarum',string='Jarum Baru',required=True, )
    nama_produk = fields.Many2one('product.product', string="Nama Produk",store=True,required=True,)
    no_doc = fields.Char(string='No Doc', default=get_name_new, readonly=True)
    nama_customer = fields.Char(string='Nama Customer',)
    name_cs = fields.Many2one('res.partner', string='Nama Customer',)
    nama_artikel = fields.Char(string='Nama Artikel')
    stich = fields.Integer(related="nama_produk.stich",string='Stich',)
    jenis_bordir = fields.Selection([
            ('badge', 'BEDGE'),
            ('frame', 'FRAME'),
            ('tempel', 'TEMPEL'),
        ], string='Jenis Bordir', copy=False,)
    ukuran_jenis_bordir = fields.Integer(string='Ukuran Frame',)
    aplikasi = fields.Boolean(string='Aplikasi',)
    time_bordir = fields.Integer(compute="hitung_waktu_standart_stich",string='Waktu Rumus/Menit') 
    waktu_bordir_real = fields.Integer(string="Waktu Bordir Real/Menit",)
    state = fields.Selection([
            ('draft','Open'),
            ('open','In Proses'),
            ('done','Di Setujui'),
            ('cancel','Di Cancel'),
        ], string='Status', readonly=True, copy=False, default='draft',track_visibility='onchange')
    posisi_bordir = fields.Char(string='Posisi Bordir',)
    jenis_kain = fields.Char(string='Jenis Kain',)
    heigth_bordir = fields.Integer(string='H',)
    weight_bordir = fields.Integer(string='W',)
    waktu_detik = fields.Integer(string='Waktu Real/Menit')
    # produck_benang_1 = fields.Many2one('product.product',string='Benang 1',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_2 = fields.Many2one('product.product',string='Benang 2',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]}) 
    # produck_benang_3 = fields.Many2one('product.product',string='Benang 3',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_4 = fields.Many2one('product.product',string='Benang 4',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_5 = fields.Many2one('product.product',string='Benang 5',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_6 = fields.Many2one('product.product',string='Benang 6',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_7 = fields.Many2one('product.product',string='Benang 7',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_8 = fields.Many2one('product.product',string='Benang 8',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_9 = fields.Many2one('product.product',string='Benang 9',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_10 = fields.Many2one('product.product',string='Benang 10',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_11 = fields.Many2one('product.product',string='Benang 11',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_12 = fields.Many2one('product.product',string='Benang 12',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    # produck_benang_13 = fields.Many2one('product.product',string='Benang 13',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    jumlah_pasang_benang = fields.Integer('Jumlah Benang',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    waktu_pasang_benang = fields.Integer('Waktu Pasang',states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})
    date_sample_bordir = fields.Date(string="Waktu Pembuatan")
    date_end_sample = fields.Datetime(string="Start Date Sample",readonly=True)
    date_start_sample = fields.Datetime(string="End Date Sample", readonly=True)


    @api.multi
    def action_confirm(self):
        waktu_create = fields.Datetime.now()
        # waktu_create = fields.Date.today()
        self.write({'state': 'open',
                    'date_start_sample':waktu_create,
                     })
    

    @api.multi
    def action_cancel(self):
        self.write({'state': 'cancel',
                    })

    
    @api.multi
    def action_done(self,vals):
        waktu_selesai = fields.Datetime.now()
        self.write({'state': 'done',
                    'date_end_sample':waktu_selesai,
                    })

    @api.depends()
    def hitung_waktu_standart_stich(self):
        for w in self:
            if w.stich > 1:
                w.time_bordir = w.stich / (25000/60)
            else:
                w.time_bordir = 0
    # buat perhitungan untuk membuat satu gambar diketahui lama waktu dan stich maka taget dalam 7 atau 8 jam kerja maka di dpat berapa stich
    # default stich adalah 25000 per jam atau 60 menit berati per menit 25000/60 nnti = 416,6666667 jmlh stich dikali standar per menit 
    # shift waktu real produksi jumlh kepala jalan nama operator 
    # jumlh benang  waktu pasang benang
    # time bordir di compute saja 

    # @api.model
    # def cange(self):




