from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from flectra.addons import decimal_precision as dp


# -------------------------------- 25/10/21 table Operator rijek kaoskaki------------------------

class JenisRijekKaoskaki(models.Model):
    _name = 'jenis.rijek.kaoskaki'
    _description = u'Jenis Rijek Kaoskaki'
    # _rec_name = 'nama_operator_id'
    name = fields.Char(string='Jenis Rijek',)


class OperatorRijekKaoskaki(models.Model):
    _name = 'operator.rijek.kaoskaki'
    _description = u'Operator Rijek Kaoskaki'
    # _rec_name = 'nama_operator_id'

    marel_nama_operatorlist_id = fields.Many2one('marel.nama.operatorlist',string='Nama Operatorlist',)

    jenis_rijek_kaoskaki_id = fields.Many2one('jenis.rijek.kaoskaki',string='Jenis Rijek Kaoskaki',)
    keterangan = fields.Text(string='keterangan',)
    jumlah_rjk = fields.Integer( string='Jumlah Rijek', )
        
    
# ----------------------------------------------------------------

class MarelNamaOperator(models.Model):
    _name = 'marel.nama.operator'
    _description = u'Marel Nama Operator'
    _rec_name = 'nama_operator'
    
    nama_operator = fields.Char(string=u'Nama Operator',)

class MarelNamaQiusi(models.Model):
    _name = 'marel.nama.qiusi'
    _description = u'Marel Nama Qiusi'
    _rec_name = 'nama_qiusi'
    
    nama_qiusi = fields.Char(string=u'Nama Qiusi',)

    
# ---------------------------------------- beda data -----------------------

class MarelNamaOperatorList(models.Model):
    
    _name = 'marel.nama.operatorlist'
    _description = u'Marel Nama Operator'
    _rec_name = 'nama_operator_id'

    nama_operator_work_order_id = fields.Many2one('mrp.workorder', 'Routing')
    workcenter_id = fields.Many2one('mrp.workcenter', 'Work Center', related='nama_operator_work_order_id.workcenter_id',store=True)

    @api.model
    def _default_no_mesin(self):
         return self.env['mesin.marel.produksi'].search([('id', '=',206)],limit=1)

    nama_operator_id = fields.Many2one('marel.nama.operator',string=u'Nama Operator',)
    nama_qiusi_id = fields.Many2one('marel.nama.qiusi',string=u'Nama qiusi',)
    no_mesin_id = fields.Many2one('mesin.marel.produksi',string=u'No Mesin', default=_default_no_mesin)
    shift = fields.Selection([
        ('A',_('A')),
        ('B',_('B')),
	    ('C',_('C')),
	    ('None',_('None Shift')),
        ], string="Shift",)
    no_kkp = fields.Char(string=u'No KKP',)
    jumlah_reject = fields.Integer(string=u'Jumlah Reject',compute='_get_jumlah_semua_rijek',store=True)
    tgl_kerja = fields.Date(string=u'tgl Kerja',default=fields.Date.context_today,)
    jumlah_yg_selesai = fields.Integer(string=u'Qty Yg Selesai',)
    # TABAHAN TGL 6/5/20
    jumlah_yg_selesai_sementara = fields.Integer(string=u'Qty Yg Selesai backUp',)
    krono_kk_menit = fields.Float(string=u'Krono KK (menit)',default=3.0)
    target_kk_operator = fields.Integer(string=u'Target KK Operator',store=True,)
    jam_kerja = fields.Float(string=u'Jam Kerja', default=480.0,readonly = True,)

    gread_d = fields.Integer(string="Gread D",)
    gum_putus_benang = fields.Integer(string=u'GUM PUTUS BENANG',store=True,)
    gum_bolong = fields.Integer(string=u'GUM BOLONG / SOBEK',store=True,)
    gum_vanise = fields.Integer(string=u'GUM VANISE',store=True,)
    gum_singker = fields.Integer(string=u'GUM SINGKER/ LIDAH SERET',store=True,)
    gum_kotor = fields.Integer(string=u'GUM KOTOR',store=True,)
    gum_terry = fields.Integer(string=u'GUM TERRY',store=True,)
    gum_jumpstich = fields.Integer(string=u'GUM JUMPSTICH',store=True,)
    gum_renggang = fields.Integer(string=u'GUM RENGGANG',store=True,)
    gum_tidak_loading = fields.Integer(string=u'GUM TIDAK LOADING',store=True,)
    gum_belang = fields.Integer(string=u'GUM BELANG',store=True,)
    gum_ukuran = fields.Integer(string=u'GUM UKURAN',store=True,)

    transfer_bolong = fields.Integer(string=u'TRANSFER BOLONG/ NYANGKOLY',store=True,)
    transfer_kotor = fields.Integer(string=u'TRANSFER KOTOR',store=True,)

    plainwelt_kotor = fields.Integer(string=u'PLAINWELT KOTOR',store=True,)
    plainwelt_vanise = fields.Integer(string=u'PLAINWELT VANISE',store=True,)
    plainwelt_tidak_loading = fields.Integer(string=u'PLAINWELT TIDAK LOADING',store=True,)
    

    leg_gum_ukuran_kerut = fields.Integer(string=u'LEG GUM UKURAN KERUT',store=True,)
    leg_gum_elastik_kerut = fields.Integer(string=u'LEG GUM ELASTIK KERUT',store=True,)
    leg_gum_sinker = fields.Integer(string=u'LEG GUM SINKER/ LIDAH SERET',store=True,)
    leg_gum_kotor = fields.Integer(string=u'LEG GUM KOTOR',store=True,)
    leg_gum_renggang = fields.Integer(string=u'LEG GUM RENGGANG',store=True,)


    leg_bolong = fields.Integer(string=u'LEG BOLONG',store=True,)
    leg_putus_benang = fields.Integer(string=u'LEG PUTUS BENANG',store=True,)
    leg_vanise = fields.Integer(string=u'LEG VANISE',store=True,)
    leg_singker = fields.Integer(string=u'LEG SINGKER',store=True,)
    leg_kotor = fields.Integer(string=u'LEG KOTOR',store=True,)
    leg_pecah = fields.Integer(string=u'LEG PECAH',store=True,)
    leg_loncat = fields.Integer(string=u'LEG LONCAT',store=True,)

    patern_vanise = fields.Integer(string=u'PATERN VANISE',store=True,)
    patern_putus_benang = fields.Integer(string=u'PATERN PUTUS BENANG',store=True,)
    patern_bolong = fields.Integer(string=u'PATERN SOBEK / BOLONG',store=True,)
    patern_kotor = fields.Integer(string=u'PATERN KOTOR',store=True,)
    patern_jumpstich = fields.Integer(string=u'PATERN JUMPSTICH',store=True,)
    patern_tidak_loading = fields.Integer(string=u'PATERN TIDAK LOADING',store=True,)

    hell_bolong = fields.Integer(string=u'HEEL BOLONG',store=True,)
    hell_putus_benang = fields.Integer(string=u'HEEL PUTUS BENANG',store=True,)
    hell_lidah_seret = fields.Integer(string=u'HEEL LIDAH SERET',store=True,)
    hell_kotor = fields.Integer(string=u'HEEL KOTOR',store=True,)
    hell_terry = fields.Integer(string=u'HEEL TERRY',store=True,)
    hell_loncat = fields.Integer(string=u'HEEL LONCAT',store=True,)
    hell_tidak_loading = fields.Integer(string=u'HEEL TIDAK LOADING',store=True,)
    hell_pecah = fields.Integer(string=u'HEEL PECAH',store=True,)
    hell_belang = fields.Integer(string=u'HEEL BELANG',store=True,)
    hell_kasar = fields.Integer(string=u'HEEL KASAR',store=True,)

    foot_bolong = fields.Integer(string=u'FOOT BOLONG',store=True,)
    foot_putus_benang = fields.Integer(string=u'FOOT PUTUS BENANG',store=True,)
    foot_vanise = fields.Integer(string=u'FOOT VANISE',store=True,)
    foot_jamur = fields.Integer(string=u'FOOT JARUM/ SINKER/ LIDAH SERET',store=True,)
    foot_kotor = fields.Integer(string=u'FOOT KOTOR',store=True,)
    foot_terry = fields.Integer(string=u'FOOT TERRY',store=True,)
    foot_loncat = fields.Integer(string=u'FOOT LONCAT',store=True,)
    foot_jumpstich = fields.Integer(string=u'FOOT JUMPSTICH',store=True,)
    foot_renggang = fields.Integer(string=u'FOOT RENGGANG',)
    foot_tidak_loading = fields.Integer(string=u'FOOT TIDAK LOADING',store=True,)
    foot_pecah = fields.Integer(string=u'FOOT PECAH',store=True,)
    foot_belang = fields.Integer(string=u'FOOT BELANG',store=True,)
    foot_ukuran = fields.Integer(string=u'FOOT UKURAN',store=True,)
    foot_kasar = fields.Integer(string=u'FOOT KASAR',store=True,)

    toe_putus_benang = fields.Integer(string=u'TOE PUTUS BENANG',store=True,)
    toe_bolong = fields.Integer(string=u'TOE BOLONG',store=True,)
    toe_vanise = fields.Integer(string=u'TOE VANISE',store=True,)
    toe_sinker = fields.Integer(string=u'TOE SINKER/ LIDAH SERET',store=True,)
    toe_kotor = fields.Integer(string=u'TOE KOTOR',store=True,)
    toe_terry = fields.Integer(string=u'TOE TERRY',store=True,)
    toe_loncat = fields.Integer(string=u'TOE LONCAT',store=True,)
    toe_tidak_loading = fields.Integer(string=u'TOE TIDAK LOADING',store=True,)
    toe_pecah = fields.Integer(string=u'TOE PECAH',store=True,)
    toe_belang = fields.Integer(string=u'TOE BELANG',store=True,)
    toe_kasar = fields.Integer(string=u'TOE KASAR',store=True,)
    
    lintoe_bolong = fields.Integer(string=u'LINTOE BOLONG',store=True,)
    lintoe_putus_benang = fields.Integer(string=u'LINTOE PUTUS BENANG',store=True,)
    lintoe_vanise = fields.Integer(string=u'LINTOE VANISE',store=True,)
    lintoe_renggang = fields.Integer(string=u'LINTOE RENGGANG',store=True,)
    lintoe_tidak_loading = fields.Integer(string=u'LINTOE TIDAK LOADING',store=True,)

    foot_gum_kotor = fields.Integer(string=u'FOOT GUM KOTOR',store=True,)
    foot_gum_kuran_kerut = fields.Integer(string=u'FOOT GUM UKURAN KERUT',store=True,)
    foot_gum_sinker = fields.Integer(string=u'FOOT GUM SINKER / LIDAH SERET',store=True,)
    foot_gum_pecah = fields.Integer(string=u'FOOT GUM PECAH',store=True,)
    foot_gum_tidak_loading = fields.Integer(string=u'FOOT GUM TIDAK LOADING',store=True,)
    foot_gum_ukuran = fields.Integer(string=u'FOOT GUM UKURAN',store=True,)
    
    
    
    # new rijek
    putus_benang = fields.Integer(string=u'Pts Benang',)
    bolong = fields.Integer(string=u' BOLONG / SOBEK',)
    vanise = fields.Integer(string=u' VANISE',)
    singker = fields.Integer(string=u' SINGKER/ LIDAH SERET',)
    kotor = fields.Integer(string=u' KOTOR',)
    terry = fields.Integer(string=u' TERRY',)
    jumpstich = fields.Integer(string=u' JUMPSTICH',)
    renggang = fields.Integer(string=u' RENGGANG',)
    tidak_loading = fields.Integer(string=u' TIDAK LOADING',)
    belang = fields.Integer(string=u' BELANG',)
    ukuran = fields.Integer(string=u' UKURAN',)

    lingtu = fields.Integer(string=u' LINGTU',)
    pecah = fields.Integer(string=u' PECAH',)
    loncat = fields.Integer(string=u' LONCAT',)
    transfer = fields.Integer(string=u' TRANSFER NYANGKOL',)
    gumpal = fields.Integer(string=u' GUMPAL',)
    kasar = fields.Integer(string=u' KASAR',)
    benang_gabung = fields.Integer(string=u' BENANG GABUNG',)
    bintik_bintik = fields.Integer(string=u' BINTIK BINTIK',)
    jam_kerja_buat_rijek = fields.Float(string=u'Jam Kerja', default=480.0,readonly = True,)
    jarum = fields.Integer(string=u'Jarum',)
    transfer_jebol = fields.Integer(string=u' TRANSFER Jebol',)
    # TABAHAN TGL 6/5/20
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done','Done'),
        ('cancel','Canceled')
        ],string="Status", readonly=True, copy=False, default='draft')


    target_conti = fields.Integer(string='Target Conti',)
    target_as = fields.Integer(string='Target Anti Slip',)
    target_sewing = fields.Integer(string='Target Sewing',)
    target_bordir = fields.Integer(string='Target Bordir',)
    target_setting = fields.Integer(string='Target Setting',)

    # 25/10/21
    @api.model
    def _default_no_box_packing (self):
        for l in self :
            if l.workcenter_id == 8 :
                l.no_box != 0
            else :
                l.no_box == 0

    no_box = fields.Integer(string='No Box', default=_default_no_box_packing, )
    operator_rijek_kaoskaki_ids = fields.One2many('operator.rijek.kaoskaki','marel_nama_operatorlist_id',string='Operator Rijek Kaoskaki',)
    
    

    # TABAHAN TGL 6/5/20
    @api.multi
    def unlink(self):
        if self.filtered(lambda x: x.status in ('marel_in_work_order', 'done')):
            raise UserError(_('You can not remove a Operator Mengisi Line.\nDiscard changes and try setting the quantity to 0.'))
        return super(MarelNamaOperatorList, self).unlink()

    # TABAHAN TGL 6/5/20
    @api.multi
    def action_confirm_value_fix(self):
        for l in self :
            if (l.nama_operator_work_order_id.product_uom_id.id == 21) & (l.nama_operator_work_order_id.workcenter_id.id != 8):
                if l.jumlah_yg_selesai_sementara != 0:
                    l.jumlah_yg_selesai = ((l.jumlah_yg_selesai_sementara)/2)
                l.write({'status': 'done'})
            else :
                if l.jumlah_yg_selesai_sementara != 0:
                    l.jumlah_yg_selesai = l.jumlah_yg_selesai_sementara
                l.write({'status': 'done'})
        self._action_ubah_data()
        self._get_mengisi_krono_kk()
        # self._get_mengisi_total_rijek()
        self._get_target_conti()
        self._get_target_as()
        self._get_target_sewing()
        self._get_target_bordir()
        self._get_target_setting()
    # TABAHAN TGL 6/5/20
    @api.multi
    def _action_ubah_data(self):
        for l in self :
            if l.status == 'done':
                l.jumlah_yg_selesai_sementara = 0

    # TABAHAN TGL 6/5/20
    @api.multi
    def _get_mengisi_krono_kk(self):
        for l in self :
            if l.jam_kerja > 0.0 and l.krono_kk_menit > 0:
                l.target_kk_operator = int(l.jam_kerja/l.krono_kk_menit)
            else:
                l.target_kk_operator = 12500
    

    # TABAHAN TGL 19/10/21
    @api.multi
    # @api.depends('nama_operator_line')
    def _get_target_conti(self):
        for l in self :
            if l.nama_operator_work_order_id.target_conti == 5000:
                l.target_conti = l.nama_operator_work_order_id.target_conti

    @api.multi
    # @api.depends('nama_operator_line')
    def _get_target_as(self):
        for l in self :
            if l.nama_operator_work_order_id.target_as > 0:
                l.target_as = l.nama_operator_work_order_id.target_as

    @api.multi
    # @api.depends('nama_operator_line')
    def _get_target_sewing(self):
        for l in self :
            if l.nama_operator_work_order_id.target_sewing > 0:
                l.target_sewing = l.nama_operator_work_order_id.target_sewing


    @api.multi
    # @api.depends('nama_operator_line')
    def _get_target_bordir(self):
        for l in self :
            if l.nama_operator_work_order_id.target_bordir > 0:
                l.target_bordir = l.nama_operator_work_order_id.target_bordir

    @api.multi
    # @api.depends('nama_operator_line')
    def _get_target_setting(self):
        for l in self :
            if l.nama_operator_work_order_id.target_setting == 12000:
                l.target_setting = l.nama_operator_work_order_id.target_setting

    # TABAHAN TGL 27/10/21
    @api.multi
    @api.depends('operator_rijek_kaoskaki_ids')
    def _get_jumlah_semua_rijek(self):
        for marel_nama_operatorlist_id in self:
            marel_nama_operatorlist_id.jumlah_reject = sum((line_id.jumlah_rjk) for line_id in marel_nama_operatorlist_id.operator_rijek_kaoskaki_ids)

                
class MarelInWorkOrder(models.Model):
    _inherit = ['mrp.workorder']

    status = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'Progress'),
        ('done','Done'),
        ('cancel','Canceled')
        ],string="Status", readonly=True, copy=False, default='draft')

    qty_producing = fields.Float('Currently Produced Quantity', default=1.0,digits=dp.get_precision('Product Unit of Measure'),states={'done': [('readonly', True)], 'cancel': [('readonly', True)]}, compute='_get_jumlah_yg_selesai_producing',)

    jumlah_yg_dikurangi = fields.Integer(string='Jumlah Yg Dikurangi (Pair)',readonly=True,compute='_get_jumlah_yg_selesai_pair',)
    jumlah_yg_dikurangi_pcs = fields.Integer(string='Jumlah Yg Dikurangi (Pcs)',readonly=True,compute='_get_jumlah_yg_selesai_pcs',)
    nama_operator_line = fields.One2many('marel.nama.operatorlist','nama_operator_work_order_id',string=u'Nama Operator ',required=True,)
    nama_operator_packing_line = fields.One2many('marel.nama.operatorlist.packing','nama_operator_work_order_id',string=u'Nama Operator Packing',required=True,)
    no_so = fields.Char(related='production_id.origin',string=u'No So',)
# TABAHAN TGL 6/5/20
    qty_input_operator = fields.Float(string='Qty Input Operator', compute='_get_jumlah_yg_selesai', store=True)
    jumlah_yg_dikurangi_packing = fields.Integer(string='Jumlah Yg Dikurangi (Packing)',readonly=True,compute='_get_jumlah_yg_selesai_packing',)
# TABAHAN TGL 8/5/20
    total_putus_benang = fields.Integer(string=u'Total Pts Benang',compute='_get_jumlah_yg_selesai_total_putus_benang',store=True)
    total_bolong = fields.Integer(string=u'Total BOLONG / SOBEK',compute='_get_jumlah_yg_selesai_total_bolong',store=True)
    total_vanise = fields.Integer(string=u'Total VANISE',compute='_get_jumlah_yg_selesai_total_vanise',store=True)
    total_singker = fields.Integer(string=u' SINGKER/ LIDAH SERET',compute='_get_jumlah_yg_selesai_total_singker',store=True)
    total_kotor = fields.Integer(string=u'Total KOTOR',compute='_get_jumlah_yg_selesai_total_kotor',store=True)
    total_terry = fields.Integer(string=u'Total TERRY',compute='_get_jumlah_yg_selesai_total_terry',store=True)
    total_jumpstich = fields.Integer(string=u'Total JUMPSTICH',compute='_get_jumlah_yg_selesai_total_jumpstich',store=True)
    total_renggang = fields.Integer(string=u'Total RENGGANG',compute='_get_jumlah_yg_selesai_total_renggang',store=True)
    total_tidak_loading = fields.Integer(string=u'Total TIDAK LOADING',compute='_get_jumlah_yg_selesai_total_tidak_loading',store=True)
    total_belang = fields.Integer(string=u'Total BELANG',compute='_get_jumlah_yg_selesai_total_belang',store=True)
    total_ukuran = fields.Integer(string=u'Total UKURAN',compute='_get_jumlah_yg_selesai_total_ukuran',store=True)

    total_lingtu = fields.Integer(string=u'Total LINGTU',compute='_get_jumlah_yg_selesai_total_lingtu',store=True)
    total_pecah = fields.Integer(string=u'Total PECAH',compute='_get_jumlah_yg_selesai_total_pecah',store=True)
    total_loncat = fields.Integer(string=u'Total LONCAT',compute='_get_jumlah_yg_selesai_total_loncat',store=True)
    total_transfer = fields.Integer(string=u'Total TRANSFER NYANGKOL',compute='_get_jumlah_yg_selesai_total_transfer',store=True)
    total_gumpal = fields.Integer(string=u'Total GUMPAL',compute='_get_jumlah_yg_selesai_total_gumpal',store=True)
    total_kasar = fields.Integer(string=u'Total KASAR',compute='_get_jumlah_yg_selesai_total_kasar',store=True)
    total_benang_gabung = fields.Integer(string=u'Total BENANG GABUNG',compute='_get_jumlah_yg_selesai_total_benang_gabung',store=True)
    total_bintik_bintik = fields.Integer(string=u'Total BINTIK BINTIK',compute='_get_jumlah_yg_selesai_total_bintik_bintik',store=True)
    total_jarum = fields.Integer(string=u'Total Jarum',compute='_get_jumlah_yg_selesai_total_jarum',store=True)
    total_transfer_jebol = fields.Integer(string=u'Total TRANSFER Jebol',compute='_get_jumlah_yg_selesai_total_transfer_jebol',store=True)
    
    target_conti = fields.Integer(string='Target Conti', default=5000)
    target_as = fields.Integer(string='Target Anti Slip',)
    target_sewing = fields.Integer(string='Target Sewing',)
    target_bordir = fields.Integer(string='Target Bordir',)
    target_setting = fields.Integer(string='Target Setting',default=12000)

# 25/10/21
    boolean_pcs = fields.Boolean(string='Pair',)

    jumlah_reject_wo = fields.Integer(string=u'Jumlah Rijek WO',compute='_get_jumlah_semua_rijek_wo',store=True)
    jumlah_selesai_wo = fields.Integer(string=u'Jumlah Selesai WO',compute='_get_jumlah_semua_selesai_wo',store=True)


    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_semua_rijek_wo(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.jumlah_reject_wo = sum((line_id.jumlah_reject) for line_id in nama_operator_work_order_id.nama_operator_line)

    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_semua_selesai_wo(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.jumlah_selesai_wo = sum((line_id.jumlah_yg_selesai) for line_id in nama_operator_work_order_id.nama_operator_line)


    # TABAHAN TGL 6/5/20
    @api.multi
    def write(self, values):
        if ('date_planned_start' in values or 'date_planned_finished' in values):
            raise UserError(_('You can not change the finished work order.'))
        return super(MarelInWorkOrder, self).write(values)


    @api.multi
    def get_kurangi_jumlah_kkp(self):
        self.qty_producing = 0
        kurang_kkp = (self.qty_producing + self.jumlah_yg_dikurangi)/2
        self.qty_producing = kurang_kkp
        return
    
    @api.multi
    def get_kurangi_jumlah_kkp_pcs(self):
        self.qty_producing = 0
        kurang_kkp = self.qty_producing + self.jumlah_yg_dikurangi_pcs
        self.qty_producing = kurang_kkp
        return

    # TABAHAN TGL 6/5/20
    @api.multi
    def get_kurangi_packing(self):
        self.qty_producing = 0
        kurang_kkp = self.qty_producing + self.jumlah_yg_dikurangi_packing
        self.qty_producing = kurang_kkp
        return

    # TABAHAN TGL 6/5/20
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.qty_input_operator = sum((line_id.jumlah_yg_selesai_sementara) for line_id in nama_operator_work_order_id.nama_operator_line)


    # TABAHAN TGL 6/5/20 ----------------------
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_pcs(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.jumlah_yg_dikurangi_pcs = sum((line_id.jumlah_yg_selesai_sementara) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 6/5/20
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_pair(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.jumlah_yg_dikurangi = sum((line_id.jumlah_yg_selesai_sementara) for line_id in nama_operator_work_order_id.nama_operator_line)


    # TABAHAN TGL 6/5/20
    @api.multi
    @api.depends('nama_operator_packing_line')
    def _get_jumlah_yg_selesai_packing(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.jumlah_yg_dikurangi_packing = sum((line_id.qty_perbox_sementara) for line_id in nama_operator_work_order_id.nama_operator_packing_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_putus_benang(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_putus_benang = sum((line_id.putus_benang) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_bolong(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_bolong = sum((line_id.bolong) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_vanise(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_vanise = sum((line_id.vanise) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_singker(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_singker = sum((line_id.singker) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_kotor(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_kotor = sum((line_id.kotor) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_terry(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_terry = sum((line_id.terry) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_jumpstich(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_jumpstich = sum((line_id.jumpstich) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_renggang(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_renggang = sum((line_id.renggang) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_tidak_loading(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_tidak_loading = sum((line_id.tidak_loading) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_belang(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_belang = sum((line_id.belang) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_ukuran(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_ukuran = sum((line_id.ukuran) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_lingtu(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_lingtu = sum((line_id.lingtu) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_pecah(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_pecah = sum((line_id.pecah) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_loncat(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_loncat = sum((line_id.loncat) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_transfer(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_transfer = sum((line_id.transfer) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_gumpal(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_gumpal = sum((line_id.gumpal) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_kasar(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_kasar = sum((line_id.kasar) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_benang_gabung(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_benang_gabung = sum((line_id.benang_gabung) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_bintik_bintik(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_bintik_bintik = sum((line_id.bintik_bintik) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_jarum(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_jarum = sum((line_id.jarum) for line_id in nama_operator_work_order_id.nama_operator_line)

    # TABAHAN TGL 8/5/20 Rijek
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_total_transfer_jebol(self):
        for nama_operator_work_order_id in self:
            nama_operator_work_order_id.total_transfer_jebol = sum((line_id.transfer_jebol) for line_id in nama_operator_work_order_id.nama_operator_line)


    # TABAHAN TGL 15/10/21 ----------------------
    @api.multi
    @api.depends('nama_operator_line')
    def _get_jumlah_yg_selesai_producing(self):
        # if (self.boolean_pcs == True):
        # di gunakan ke odoo jika produksi tetap pcs
        if (self.product_uom_id.id == 21) & (self.workcenter_id.id != 8):
            self.boolean_pcs = True
            for nama_operator_work_order_id in self:
                nama_operator_work_order_id.qty_producing = sum(((line_id.jumlah_yg_selesai_sementara)/2) for line_id in nama_operator_work_order_id.nama_operator_line)
        else:
            for nama_operator_work_order_id in self:
                nama_operator_work_order_id.qty_producing = sum((line_id.jumlah_yg_selesai_sementara) for line_id in nama_operator_work_order_id.nama_operator_line)

    @api.multi
    def record_production_2(self):
        # self.ensure_one()
        if self.qty_producing <= 0:
            raise UserError(_('Please set the quantity you are currently producing. It should be different from zero.'))

        # if (self.production_id.product_id.tracking != 'none') and not self.final_lot_id and self.move_raw_ids:
        #     raise UserError(_('You should provide a lot/serial number for the final product'))
        
        self.record_production()
        self.nama_operator_line.action_confirm_value_fix()



    # @api.onchange('status')
    # def _onchange_status(self):
    #     for line in self.nama_operator_line:
    #         line.status = line.nama_operator_work_order_id.status

    # def write(self, vals):
    #     res = super().write(vals)
    #     if 'status' in vals:
    #         lines = self.mapped('nama_operator_line').filtered(
    #             lambda l: l.status != vals['status'])
    #         lines.write({'status': vals['status']})
        # return res

    # TABAHAN TGL 18/10/21 ----------------------
    # @api.multi
    # def _get_update_status2_progress_wo(self):
    #     for l in self :
    #         if l.qty_produced >= 0 and l.qty_produced < l.qty_production:
    #             l.write({'status': 'progress'})

    # @api.multi
    # def _get_update_status2_done_wo(self):
    #     for l in self :
    #         if l.qty_produced >= l.qty_production:
    #             l.write({'status': 'done'})
# ---------------------------------------- beda data -----------------------
class MarelNamaOperatorListPacking(models.Model):
    
    _name = 'marel.nama.operatorlist.packing'
    _description = u'Marel Data Packing'
    _rec_name = 'nama_operator_id'

    nama_operator_work_order_id = fields.Many2one('mrp.workorder', 'Routing')

    tgl_kerja = fields.Date(string=u'tgl Kerja',default=fields.Date.context_today,)
    nama_operator_id = fields.Many2one('marel.nama.operator',string=u'Nama Operator',)
    no_kkp = fields.Char(string=u'No KKP',)
    qty_perbox = fields.Integer(string='Qty Perbox',readonly=True,)
    no_box = fields.Char(string='No Box',)    
    # TABAHAN TGL 6/5/20
    status = fields.Selection([
        ('draft', 'Draft'),
        ('done','Done'),
        ('cancel','Canceled')
        ],string="Status", readonly=True, copy=False, default='draft')
    qty_perbox_sementara = fields.Integer(string='Qty Perbox Sementara',)

    # TABAHAN TGL 6/5/20
    @api.multi
    def unlink(self):
        if self.filtered(lambda x: x.status in ('marel_in_work_order', 'done')):
            raise UserError(_('You can not remove a Operator Packing Mengisi Line.\nDiscard changes and try setting the quantity to 0.'))
        return super(MarelNamaOperatorListPacking, self).unlink()

    # TABAHAN TGL 6/5/20
    @api.multi
    def action_confirm_value_packing_fix(self):
        for l in self :
            if l.qty_perbox_sementara != 0:
                l.qty_perbox = l.qty_perbox_sementara
            l.write({'status': 'done'})
        self._action_ubah_data_packing()
    # TABAHAN TGL 6/5/20
    @api.multi
    def _action_ubah_data_packing(self):
        for l in self :
            if l.status == 'done':
                l.qty_perbox_sementara = 0


