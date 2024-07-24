from flectra import api, fields, models, _

class TemuanOption(models.Model):
    _name = 'temuan.option'
    _description = 'Opsi Temuan'

    name = fields.Char(string='Jenis Temuan', required=True)

class PengecekanSample(models.Model):
    _name = 'pengecekan.sample'
    _description = 'Pengecekan Sample'    

    product_id = fields.Many2one('product.product', compute='_compute_product_id', store=True)

    pengecekan_sample_line = fields.One2many('pengecekan.sample.line', 'pengecekan_sample_id')

    manufacturing_order = fields.Many2one('mrp.production', string='Manufacturing Order')
    
    marel_sample_id = fields.Many2one('marelin.samlpe.dev2', string='Sample Development')

    timestamp = fields.Datetime(string='Timestamp', default=fields.Datetime.now, readonly=True)
    tgl_buat = fields.Date(string='Tanggal', default=fields.Date.context_today)
    tgl_mulai = fields.Date(string='Tanggal Mulai')
    tgl_selesai = fields.Datetime(string=u'Tanggal Selesai',readonly=True)
    nama_operator_id = fields.Many2one('marel.nama.qiusi', string='Inspector')
    temuan = fields.Char(string='Temuan')
    no_mesin = fields.Many2one('mesin.marel.produksi', string='Mesin')

    style = fields.Char(string='Style', related='marel_sample_id.style')
    warna = fields.Char(string='Warna', related='marel_sample_id.warna')
    
    keterangan = fields.Text(string='Keterangan')
    
    state = fields.Selection(
        [('draft', 'Draft'),
         ('ready', 'Ready'),
         ('waiting', 'Waiting For Approval'),
         ('success', 'Check success'),
         ('failed', 'Check failed'),
         ('canceled', 'Canceled')],
        string='State', readonly=True, default='draft',
        track_visibility='onchange',
        widget='statusbar',
        statusbar_colors='{"success": "green", "failed": "red", "canceled": "red"}',
        )
    success_header = fields.Boolean(
        compute="_compute_success_header", string='Status',
        help='This field will be marked if all tests have succeeded.',
        store=True)

    gum_relaxed_x= fields.Float(string='Gum Relaxed x ', related='marel_sample_id.gum_relaxed_x')
    gum_relaxed_y= fields.Float(string='Gum Relaxed y ', related='marel_sample_id.gum_relaxed_y')

    leg_gum_relaxed_x= fields.Float(string='Leg Gum Relaxed x ', related='marel_sample_id.leg_gum_relaxed_x')
    leg_gum_relaxed_y= fields.Float(string='Leg Gum Relaxed y ', related='marel_sample_id.leg_gum_relaxed_y')

    leg_gum_atas_relaxed_x= fields.Float(string='Leg Gum Atas Relaxed x ',related='marel_sample_id.leg_gum_atas_relaxed_x')
    leg_gum_atas_relaxed_y= fields.Float(string='Leg Gum Atas Relaxed y ',related='marel_sample_id.leg_gum_atas_relaxed_y')

    leg_gum_bawah_relaxed_x= fields.Float(string='Leg Gum Bawah Relaxed x ',related='marel_sample_id.leg_gum_bawah_relaxed_x')
    leg_gum_bawah_relaxed_y= fields.Float(string='Leg Gum Bawah Relaxed y ',related='marel_sample_id.leg_gum_bawah_relaxed_y')

    leg_relaxed_x= fields.Float(string=' Leg Relaxed x',related='marel_sample_id.leg_relaxed_x')
    leg_relaxed_y= fields.Float(string='Leg Relaxed y ',related='marel_sample_id.leg_relaxed_y')

    foot_relaxed_x= fields.Float(string=' Foot Relaxed x',related='marel_sample_id.foot_relaxed_x')
    foot_relaxed_y= fields.Float(string=' Foot Relaxed y',related='marel_sample_id.foot_relaxed_y')

    foot_gum_relaxed_x= fields.Float(string='Foot Gum Relaxed x ',related='marel_sample_id.foot_gum_relaxed_x')
    foot_gum_relaxed_y= fields.Float(string='Foot Gum Relaxed y ',related='marel_sample_id.foot_gum_relaxed_y')

    hell_relaxed_x= fields.Float(string='Heel Relaxed x ',related='marel_sample_id.hell_relaxed_x')
    hell_relaxed_y= fields.Float(string='Heel Relaxed y ',related='marel_sample_id.hell_relaxed_y')

    #tambhan 190820---------------------------------
    gum_atas_relaxed_x = fields.Float(string='Gum Atas Relaxed X',related='marel_sample_id.gum_atas_relaxed_x')
    gum_atas_relaxed_y = fields.Float(string='Gum Atas Relaxed Y',related='marel_sample_id.gum_atas_relaxed_y')

    gum_bawah_relaxed_x = fields.Float(string='Gum Bawah relaxed X',related='marel_sample_id.gum_bawah_relaxed_x')
    gum_bawah_relaxed_y = fields.Float(string='Gum Bawah Relaxed Y' ,related='marel_sample_id.gum_bawah_relaxed_y')
    
    leg_gum_tengah_relaxed_x = fields.Float(string='Leg Gum Tengah Relaxed X',related='marel_sample_id.leg_gum_tengah_relaxed_x')
    leg_gum_tengah_relaxed_y = fields.Float(string='Leg Gum Tengah Relaxed Y',related='marel_sample_id.leg_gum_tengah_relaxed_y')
    
    #Tambahan relaxedout 20230413
    gum_relaxed_out_x= fields.Float(string='Gum Relaxed Out X',related='marel_sample_id.gum_relaxed_out_x')
    gum_relaxed_out_y= fields.Float(string='Gum Relaxed Out Y',related='marel_sample_id.gum_relaxed_out_y')

    leg_gum_relaxed_out_x= fields.Float(string='Leg Gum Relaxed Out X',related='marel_sample_id.leg_gum_relaxed_out_x')
    leg_gum_relaxed_out_y= fields.Float(string='Leg Gum Relaxed Out Y',related='marel_sample_id.leg_gum_relaxed_out_y')

    leg_gum_atas_relaxed_out_x= fields.Float(string='Leg Gum Atas Relaxed Out X',related='marel_sample_id.leg_gum_atas_relaxed_out_x')
    leg_gum_atas_relaxed_out_y= fields.Float(string='Leg Gum Atas Relaxed Out Y',related='marel_sample_id.leg_gum_atas_relaxed_out_y')

    leg_gum_bawah_relaxed_out_x= fields.Float(string='Leg Gum Bawah Relaxed Out X',related='marel_sample_id.leg_gum_bawah_relaxed_out_x')
    leg_gum_bawah_relaxed_out_y= fields.Float(string='Leg Gum Bawah Relaxed Out Y',related='marel_sample_id.leg_gum_bawah_relaxed_out_y')

    leg_relaxed_out_x= fields.Float(string=' Leg Relaxed Out X',related='marel_sample_id.leg_relaxed_out_x')
    leg_relaxed_out_y= fields.Float(string='Leg Relaxed Out Y',related='marel_sample_id.leg_relaxed_out_y')

    foot_relaxed_out_x= fields.Float(string=' Foot Relaxed Out X',related='marel_sample_id.foot_relaxed_out_x')
    foot_relaxed_out_y= fields.Float(string=' Foot Relaxed Out Y',related='marel_sample_id.foot_relaxed_out_y')

    foot_gum_relaxed_out_x= fields.Float(string='Foot Gum Relaxed Out X',related='marel_sample_id.foot_gum_relaxed_out_x')
    foot_gum_relaxed_out_y= fields.Float(string='Foot Gum Relaxed Out Y',related='marel_sample_id.foot_gum_relaxed_out_y')

    hell_relaxed_out_x= fields.Float(string='Heel Relaxed Out X',related='marel_sample_id.hell_relaxed_out_x')
    hell_relaxed_out_y= fields.Float(string='Heel Relaxed Out Y',related='marel_sample_id.hell_relaxed_out_y')

    gum_atas_relaxed_out_x = fields.Float(string='Gum Atas Relaxed Out X',related='marel_sample_id.gum_atas_relaxed_out_x')
    gum_atas_relaxed_out_y = fields.Float(string='Gum Atas Relaxed Out Y',related='marel_sample_id.gum_atas_relaxed_out_y')

    gum_bawah_relaxed_out_x = fields.Float(string='Gum Bawah Relaxed Out X',related='marel_sample_id.gum_bawah_relaxed_out_x')
    gum_bawah_relaxed_out_y = fields.Float(string='Gum Bawah Relaxed Out Y' ,related='marel_sample_id.gum_bawah_relaxed_out_y')
    
    leg_gum_tengah_relaxed_out_x = fields.Float(string='Leg Gum Tengah Relaxed Out X', related='marel_sample_id.leg_gum_tengah_relaxed_out_x')
    leg_gum_tengah_relaxed_out_y = fields.Float(string='Leg Gum Tengah Relaxed Out Y', related='marel_sample_id.leg_gum_tengah_relaxed_out_y')


    @api.depends('marel_sample_id.state')
    def _compute_state_data(self):
        for record in self:
            if record.marel_sample_id.state == 'done':
                
                record.style=record.marel_sample_id.style
                record.warna=record.marel_sample_id.warna

                gum_relaxed_x=record.marel_sample_id.gum_relaxed_x
                gum_relaxed_y=record.marel_sample_id.gum_relaxed_y

                leg_gum_relaxed_x=record.marel_sample_id.leg_gum_relaxed_x
                leg_gum_relaxed_y=record.marel_sample_id.leg_gum_relaxed_y

                leg_gum_atas_relaxed_x=record.marel_sample_id.leg_gum_atas_relaxed_x
                leg_gum_atas_relaxed_y=record.marel_sample_id.leg_gum_atas_relaxed_y

                leg_gum_bawah_relaxed_x=record.marel_sample_id.leg_gum_bawah_relaxed_x
                leg_gum_bawah_relaxed_y=record.marel_sample_id.leg_gum_bawah_relaxed_y

                leg_relaxed_x=record.marel_sample_id.leg_relaxed_x
                leg_relaxed_y=record.marel_sample_id.leg_relaxed_y

                foot_relaxed_x=record.marel_sample_id.foot_relaxed_x
                foot_relaxed_y=record.marel_sample_id.foot_relaxed_y

                foot_gum_relaxed_x=record.marel_sample_id.foot_gum_relaxed_x
                foot_gum_relaxed_y=record.marel_sample_id.foot_gum_relaxed_y

                hell_relaxed_x=record.marel_sample_id.hell_relaxed_x
                hell_relaxed_y=record.marel_sample_id.hell_relaxed_y

                gum_atas_relaxed_x=record.marel_sample_id.gum_atas_relaxed_x
                gum_atas_relaxed_y=record.marel_sample_id.leg_gum_atas_relaxed_y

                gum_bawah_relaxed_x=record.marel_sample_id.gum_bawah_relaxed_x
                gum_bawah_relaxed_y=record.marel_sample_id.gum_bawah_relaxed_y

                leg_gum_tengah_relaxed_x=record.marel_sample_id.leg_gum_tengah_relaxed_x
                leg_gum_tengah_relaxed_y=record.marel_sample_id.leg_gum_tengah_relaxed_y

                gum_relaxed_out_x=record.marel_sample_id.gum_relaxed_out_x
                gum_relaxed_out_y=record.marel_sample_id.gum_relaxed_out_y

                leg_gum_relaxed_out_x=record.marel_sample_id.leg_gum_relaxed_out_x
                leg_gum_relaxed_out_y=record.marel_sample_id.leg_gum_relaxed_out_y

                leg_gum_atas_relaxed_out_x=record.marel_sample_id.leg_gum_atas_relaxed_out_x
                leg_gum_atas_relaxed_out_y=record.marel_sample_id.leg_gum_atas_relaxed_out_y

                leg_gum_bawah_relaxed_out_x=record.marel_sample_id.leg_gum_bawah_relaxed_out_x
                leg_gum_bawah_relaxed_out_y=record.marel_sample_id.leg_gum_bawah_relaxed_out_y

                leg_relaxed_out_x=record.marel_sample_id.leg_relaxed_out_x
                leg_relaxed_out_y=record.marel_sample_id.leg_relaxed_out_y

                foot_relaxed_out_x=record.marel_sample_id.foot_relaxed_out_x
                foot_relaxed_out_y=record.marel_sample_id.foot_relaxed_out_y

                foot_gum_relaxed_out_x=record.marel_sample_id.foot_gum_relaxed_out_x
                foot_gum_relaxed_out_y=record.marel_sample_id.foot_gum_relaxed_out_y

                hell_relaxed_out_x=record.marel.marel_sample_id.hell_relaxed_out_x
                hell_relaxed_out_y=record.marel_sample_id.hell_relaxed_out_y

                gum_atas_relaxed_out_x = record.marel_sample_id.gum_atas_relaxed_out_x
                gum_atas_relaxed_out_y = record.marel_sample_id.gum_atas_relaxed_out_y

                gum_bawah_relaxed_out_x = record.marel_sample_id.gum_bawah_relaxed_out_x
                gum_bawah_relaxed_out_y = record.marel_sample_id.gum_bawah_relaxed_out_y
                
                leg_gum_tengah_relaxed_out_x = record.marel_sample_id.leg_gum_tengah_relaxed_out_x
                leg_gum_tengah_relaxed_out_y = record.marel_sample_id.leg_gum_tengah_relaxed_out_y


            else :
                record.style=False
                record.warna=False

                record.gum_relaxed_x=False                
                record.gum_relaxed_y=False

                record.leg_gum_relaxed_x=False
                record.leg_gum_relaxed_y=False

                record.leg_gum_atas_relaxed_x=False
                record.leg_gum_atas_relaxed_y=False

                record.leg_gum_bawah_relaxed_x=False
                record.leg_gum_bawah_relaxed_y=False

                record.leg_relaxed_x=False                
                record.leg_relaxed_y=False

                record.foot_relaxed_x=False
                record.foot_relaxed_y=False

                record.foot_gum_relaxed_x=False
                record.foot_gum_relaxed_y=False

                record.hell_relaxed_x=False
                record.hell_relaxed_y=False

                record.gum_atas_relaxed_x=False
                record.gum_atas_relaxed_y=False

                record.gum_bawah_relaxed_x=False
                record.gum_bawah_relaxed_y=False

                record.leg_gum_tengah_relaxed_x=False
                record.leg_gum_tengah_relaxed_y=False

                record.gum_relaxed_out_x=False
                record.gum_relaxed_out_y=False

                record.leg_gum_relaxed_out_x=False
                record.leg_gum_relaxed_out_y=False

                record.leg_gum_atas_relaxed_out_x=False
                record.leg_gum_atas_relaxed_out_y=False

                record.leg_gum_bawah_relaxed_out_x=False
                record.leg_gum_bawah_relaxed_out_y=False

                record.leg_relaxed_out_x=False
                record.leg_relaxed_out_y=False

                record.foot_relaxed_out_x=False
                record.foot_relaxed_out_y=False

                record.foot_gum_relaxed_out_x=False
                foot_gum_relaxed_out_y=False

                record.hell_relaxed_out_x=False
                record.hell_relaxed_out_y=False

                record.gum_atas_relaxed_out_x =False 
                record.gum_atas_relaxed_out_y = False

                record.gum_bawah_relaxed_out_x = False
                record.gum_bawah_relaxed_out_y = False
                
                record.leg_gum_tengah_relaxed_out_x = False
                record.leg_gum_tengah_relaxed_out_y = False

    @api.depends('manufacturing_order')
    def _compute_product_id(self):
        for record in self:
            record.product_id = record.manufacturing_order.product_id if record.manufacturing_order else False
    
    @api.multi
    def _update_success_header(self):
        for pengecekan in self:
            pengecekan.success_header = all(line.success for line in pengecekan.pengecekan_sample_line)

    @api.multi
    def action_approve(self):
        for pengecekan in self:
            pengecekan.success_header = True
            pengecekan.state = 'success'
            pengecekan.tgl_selesai=fields.Datetime.now()

    @api.multi
    def action_cancel(self):
        for pengecekan in self:
            pengecekan.success_header = False
            pengecekan.state = 'canceled'

    @api.multi
    def action_set_to_draft(self):
        for pengecekan in self:
            pengecekan.success_header=False
            pengecekan.state='draft'        

class PengecekanSampleLine(models.Model):    
    _name = 'pengecekan.sample.line'
    _description = 'Pengecekan Sample Line'

    pengecekan_sample_id = fields.Many2one('pengecekan.sample', string='Sample Reference', ondelete='cascade', index=True, copy=False)
    tgl_buat = fields.Date(string='Tanggal', default=fields.Date.context_today)
    nama_operator_id = fields.Many2one('marel.nama.qiusi', string='Inspector')
    no_mesin = fields.Many2one('mesin.marel.produksi', string='No Mesin')
    temuan = fields.Many2one('temuan.option', string='Temuan', required=True)
    keterangan = fields.Char(string='Keterangan')
    tgl_selesai = fields.Datetime(string=u'Tgl Selesai', readonly=True)

    stretch_gum_x = fields.Char(string='Gum X')
    stretch_gum_y = fields.Char(string='Gum Y')

    stretch_leg_x = fields.Char(string='Leg X')
    stretch_leg_y = fields.Char(string='Leg Y')

    stretch_leg_gum_x = fields.Char(string='Leg Gum X')
    stretch_leg_gum_y = fields.Char(string='Leg Gum Y')

    stretch_leg_gum_bawah_x = fields.Char(string='Leg Gum Bawah X')
    stretch_leg_gum_bawah_y = fields.Char(string='Leg Gum Bawah Y')

    stretch_foot_x = fields.Char(string='Foot x')
    stretch_foot_y = fields.Char(string='Foot y')

    stretch_foot_gum_x = fields.Char(string='Foot Gum X')
    stretch_foot_gum_y = fields.Char(string='Foot Gum Y')

    @api.depends('temuan', 'keterangan')
    def _compute_quality_test_check(self):
        for line in self:
            line.success = line.temuan and line.keterangan
            if line.success:
                line.pengecekan_sample_id._update_success_header()