from flectra import api, fields, models, _
from flectra.exceptions import UserError

#--------------------------------- class baru -----------------------------------------------
class InHeaderPlanWarping(models.Model):
    _description = "Header Plan Warping"
    _name = "herader.planwarping"
    _rec_name = "name"

    kode_warping = fields.Char(string='Kode Plan Warping',required=True)
    name = fields.Many2one('mrp.production',string='No KP/MO')
    seri = fields.Char(string='Seri',)
    tarikan = fields.Char(string='Tarikan',)
    quantity = fields.Float(string='Quantity',)
    mesin = fields.Many2one('mesin.produksi',string='Mesin Warping')
    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)

#--------------------------------- class baru -----------------------------------------------
class InOperatorMengisiWarping(models.Model):
    _description = "Operator Mengisi Warping"
    _name = "operator.mengisiwarping"
    _rec_name = "name"

    no_kp = fields.Many2one('herader.planwarping',string='No KP/MO')
    seri = fields.Char(related='no_kp.seri',string='Seri',readonly=True,)
    tarikan = fields.Char(related='no_kp.tarikan',string='Tarikan',readonly=True,)
    quantity = fields.Float(related='no_kp.quantity',string='Quantity',readonly=True,)
    mesin = fields.Many2one(related='no_kp.mesin',string='Mesin Warping', readonly=True,)
    date_start = fields.Date(related='no_kp.date_start',string="Start Date",readonly=True,)
    date_end = fields.Date(related='no_kp.date_end',string="End Date",readonly=True,)
    #jumlah_benang_ppic = fields.Integer(string='Jumlah Benang PPIC', )
    name = fields.Char(string='Kode Plan Warping',required=True)
    operator = fields.One2many("pengisisan.operator.warping","operator_ids", "operator2",)
    operator1 = fields.One2many("pengisisan.operator.warping","operator_ids", "operator2",)
    kontrol_benang = fields.Boolean(String='Kontrol Benang',)
    pts_benang_rata = fields.Integer(string='Avg Benang/1 juta', )
    lebar_kain = fields.Integer(string='Lebar Kain', )
    lusi_pakan = fields.Char(string='Lusi/Pakan', )
    jumlah_benang_lusi = fields.Integer(string='Jumlah Benang Lusi/Pakan', )
    ne_benang_rata = fields.Char(string='NE Benang Rata2', )
    berat_neto1 = fields.Float(string="Total Berat Neto")

#----------------------------class one2many -----------------------#
class op_warping(models.Model):
    _description = "operator"
    _name = "pengisian.operator"
    _rec_name = "operator_mengisi_warping"

    operator_mengisi_warping = fields.Char(string="Operator")

class operator_mengisi(models.Model):
    _name = "pengisisan.operator.warping"
    _rec_name = "operator_ids"
    _description = "operator2"
     #-------------------------------- operator mngisi -------------------------------------
    #mulai dr urut k kanan
    pengisi = fields.Char("Nama Operator")
    operator_mengisi = fields.Many2one("pengisian.operator", "operator_mengisi",)
    operator_1 = fields.Many2one("operator.mengisiwarping", "Operator Mengisi Warping" )
    operator_ids = fields.Many2one("operator.mengisiwarping", "Operator Mengisi Warping" )
    jmlh_benang = fields.Integer(string='Jmlh Benang', ) #
    panjang_benang = fields.Integer(string='panjang benang', )
    no_beam = fields.Many2one("nomor.beam", string='No Beam', ) #op
    pts_benang = fields.Integer(string='Pts Benang', ) #op
    pts_persejuta = fields.Float(string='pts/1juta', ) #op
    berat_bruto = fields.Float(string='Berat Bruto', )
    berat_beam = fields.Float(string='Berat Beam', )
    berat_neto = fields.Float(string='Berat Neto', )
    #tgl = fields.Date(string='Tgl', required=True)
    jam_naik = fields.Char(string='Jam Naik')
    jam_turun = fields.Char(string='Jam Turun',)
    lama_proses_menit = fields.Integer(string='Lama Proses Menit',)
    rata_menit = fields.Float(string='Rata2 perMenit',)
    sebelum_dikanji_gram = fields.Char(string='Sebelum Dikanji Gram',)
    sebelum_dikanji_persen = fields.Char(string='Sebelum Dikanji %',)
    hns_kanan = fields.Char(string='HNS Kanan',)
    hns_tengah = fields.Char(string='HNS Tengah',)
    hns_kiri = fields.Char(string='HNS Kiri',)
    shift = fields.Selection(
        string=u'Shift',
        selection=[('A', 'A'), ("B", 'B'), ("C", 'C')]
    )
    
    #no = fields.Integer(string ="No", compute='_get_increment')

    #@api.one
    #def _get_increment(self):
    #    self.no = 1 + 1