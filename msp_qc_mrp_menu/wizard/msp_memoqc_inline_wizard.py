from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime


class MspMemoqcInlineWizard(models.TransientModel):
    _name = "msp.memoqc.inline.wizard"

    def _default_mspmemo_qc_inline(self):
        return self.env['mrp.workorder'].browse(self._context.get('active_ids'))

    name = fields.Many2one('mrp.workorder',string="Name",default=_default_mspmemo_qc_inline, readonly=True, store=True,)
    
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,store=True,)
    shift = fields.Selection([
        ('A',_('A')),
        ('B',_('B')),
	    ('C',_('C')),], string="Shift",store=True,)
    
    line = fields.Char(string='Line',store=True,)
    nama_operator_id = fields.Many2one('marel.nama.operator',string=u'Nama Operator',store=True,)
    nama_teknisi_id = fields.Many2one(string='Nama Teknisi',comodel_name='nama.teknisi',store=True,)
    mrp_productioin_id = fields.Many2one(string=u'No MO', related='name.production_id', readonly=True,store=True)
    keterangan = fields.Text(string='Keterangan',store=True,)
    
    
    
    # state = fields.Selection([
    #     ('draft', 'Open'),
    #     ('done','Done'),
    #     ('cancel','Canceled')
    #     ],string="Status", readonly=True, copy=False, default='draft')
    
    @api.multi
    def line_qc(self, vals):
        obj_nilai = self.env['msp.memo.qc.inline'].create({
                                                    "mrp_productioin_id":self.mrp_productioin_id.id,
                                                    "tgl_create":self.tgl_create,
                                                    "shift":self.shift,
                                                    "line":self.line,
                                                    "keterangan":self.keterangan,
                                                    "nama_teknisi_id":self.nama_teknisi_id.id,
                                                    "nama_operator_id":self.nama_operator_id.id,
                                                    })
        return super(MspMemoqcInlineWizard, self).write(vals)


    # kebersihan = fields.Integer(string="Mc Bersih Dari Kapas", default=5)
    # rapi_benang = fields.Integer(string="Kerapian Lusi dan Sambungan", default=5)
    # tradle_bowl = fields.Integer(string="Tradle Lever dan BOWL Tidak Aus", default=5)
    # pengaman_kamran = fields.Integer(string="Pengaman Kamran Lengkap", default=4)
    # ril_gun = fields.Integer(string="Ril Gun Dikancing + Isolasi", default=2)
    # belt_kamran = fields.Integer(string="Belt Kamran", default=6)
    # tinggi_b_lusi = fields.Integer(string="Ketinggian B.Lusi ", default=5)
    # picking_stik = fields.Integer(string="PICKING STIK", default=5)
    # picker = fields.Integer(string="PICKER", default=5)
    # andong = fields.Integer(string="Andong", default=4)
    # belt_side_lever = fields.Integer(string="Belt Side Lever", default=3)
    # bowl_nok = fields.Integer(string="Bowl Nok", default=7)
    # duck_bill = fields.Integer(string="Duck Bill", default=5)
    # duck_bill_stop_finger = fields.Integer(string="Duck Bill + Stop Finger", default=5)
    # sisir = fields.Integer(string="Sisir", default=5)
    # gigi_beam = fields.Integer(string="Gigi Beam", default=4)
    # kancingan_beam = fields.Integer(string="Kancingan Beam", default=3)
    # pemisah_drofer = fields.Integer(string="Pemisah Drofer", default=3)
    # gigi_pick = fields.Integer(string="Gigi Pick", default=4)
    # ring_temple = fields.Integer(string="Ring Temple", default=5)
    # target_mc = fields.Integer(string="Target MC Jalan 2 Jam", default=10)
    # # coba = fields.Many2one("nomor.beam", string="beam")
    # order = fields.Selection([('cucuk',_('Naik Cuscuk')),('tying',_('Tying')),], related='name.order',string="Order Drawin", readonly=True)
    # seri_sizing = fields.Char(related="name.seri_sizing",string="Serian Kanji")
    # shif = fields.Selection([('A',_('A')),('B',_('B')),('C',_('C')),], string= "Shif", related="name.shif", readonly=True)
    # check = fields.Boolean(striing="Check", default=True)
    # tot_nilai = fields.Float(compute="tot_nil", string="Total Nilai", readonly=True, strore=True)
    # grade_op = fields.Selection(string="Grade Op", selection=[("a","A"),
    #                                                         ("b","B"),
    #                                                         ("c","C"),], compute="_grade_op", store=True, readonly=True)
