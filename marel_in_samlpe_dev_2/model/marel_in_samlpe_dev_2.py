from flectra.addons import decimal_precision as dp
from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from flectra.tools import float_round

class MarelInSamlpeDev2List(models.Model):
    _name = 'marelin.samlpe.dev2.list'
    #_rec_name = 'product_template_id'

    marel_in_samlpe_dev_id = fields.Many2one('marelin.samlpe.dev2',string=u'marel in samlpe_dev id',)
    #------------
    product_id = fields.Many2one('product.product',string=u'Nama Benang',)
    jumlah_ambil = fields.Float(string=u'Jmlah Ambil (C)',)
    qty_benang_kg = fields.Float(string=u'Qty Benang Per Pasang (kg)',digits=dp.get_precision('Custom 2'),)
    qty_benang_gr = fields.Float(string=u'Qty Benang Per Pasang (gr)',digits=dp.get_precision('Custom 2'),)
    qty_bom_reguler = fields.Float(string=u'Qty Bom (R)',digits=dp.get_precision('Custom 2'),)
    qty_bom_soccer = fields.Float(string=u'Qty Bom (S)',digits=dp.get_precision('Custom 2'),)
    partner_id = fields.Many2one('res.partner', string='Customer', )
    awal = fields.Float(string=u'Awal',digits=dp.get_precision('Custom 2'),)
    akhir = fields.Float(string=u'Akhir',digits=dp.get_precision('Custom 2'),)
    terpakai = fields.Float(string=u'Terpakai',digits=dp.get_precision('Custom 2'),)

    @api.multi
    def get_hitung_qty_bom_line(self):
        self.qty_bom_reguler = 0.0
        self.qty_bom_soccer = 0.0
        #mengconvert dari gr ke kg
        self.qty_benang_kg = (self.qty_benang_gr/1000)
        #perhitungan toleransi
        toleransi_qty_bom_r = (self.qty_benang_kg*0.07)
        toleransi_qty_bom_s = (self.qty_benang_kg*0.15)
        #qty bom kaos kaki
        self.qty_bom_reguler = (self.qty_benang_kg + toleransi_qty_bom_r)
        self.qty_bom_soccer = (self.qty_benang_kg + toleransi_qty_bom_s)
        return

class MarelInAksesorisSamlpeDev2List(models.Model):
    _name = 'marelin.aksesotis.samlpedev2.list'
    #_rec_name = 'product_template_id'

    marel_in_samlpe_dev_id = fields.Many2one('marelin.samlpe.dev2',string=u'marel_in_samlpe_dev_id',)
    #------------
    product_id = fields.Many2one('product.product',string=u'Nama Aksesoris',)
    jumlah_ambil = fields.Float(string=u'Jmlah Ambil',)


class OperatorMarelInSamlpeDev2List(models.Model):
    _name = 'operator.marelinsamlpe.dev2.list'

    marel_in_samlpe_dev_id = fields.Many2one('marelin.samlpe.dev2',string=u'marel_in_samlpe_dev_id',)

    
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, track_visibility='onchange', default=lambda self: self.env.user)
    nama_desain = fields.Char(string='Nama Desain',)
    berat = fields.Char(string='Berat',)
    waktu_produksi = fields.Char(string='Waktu Produksi',)
    tgl_buat = fields.Date(string='Tgl Buat',default=fields.Date.context_today,)
    nama_operator_id = fields.Many2one('marel.nama.operator',string=u'Nama Operator',)


    gum_stretch_x= fields.Char(string='Gum Stretch x ',)
    gum_stretch_y= fields.Char(string='Gum Stretch y ',)
    leg_gum_stretch_x= fields.Char(string='Leg Gum Stretch x ',)
    leg_gum_stretch_y= fields.Char(string='Leg Gum Stretch y ',)
    leg_gum_atas_stretch_x= fields.Char(string='Leg Gum Atas Stretch x ',)
    leg_gum_atas_stretch_y= fields.Char(string='Leg Gum Atas Stretch y ',)
    leg_gum_bawah_stretch_x= fields.Char(string='Leg Gum Bawah Stretch x ',)
    leg_gum_bawah_stretch_y= fields.Char(string='Leg Gum Bawah Stretch y ',)
    leg_stretch_x= fields.Char(string=' Leg Stretch x',)
    leg_stretch_y= fields.Char(string='Leg Stretch y ',)
    foot_stretch_x= fields.Char(string=' Foot Stretch x',)
    foot_stretch_y= fields.Char(string=' Foot Stretch y',)
    foot_gum_stretch_x= fields.Char(string='Foot Gum Stretch x ',)
    foot_gum_stretch_y= fields.Char(string='Foot Gum Stretch y ',)
    hell_stretch_x= fields.Char(string='Heel Stretch x ',)
    hell_stretch_y= fields.Char(string='Heel Stretch y ',)

    #tambhan 190820------------------------
    gum_atas_stretch_x = fields.Char(string='Gum Atas Stretch X',)
    gum_atas_stretch_y = fields.Char(string='Gum Atas Stretch Y',)

    gum_bawah_stretch_x = fields.Char(string='Gum Bawah Stretch X',)
    gum_bawah_stretch_y = fields.Char(string='Gum Bawah Stretch Y' ,)


    leg_gum_atas_stretch_x = fields.Char(string='Leg Gum Atas Stretch X',)
    leg_gum_atas_stretch_y = fields.Char(string='Leg Gum Atas Stretch Y',)
    
    leg_gum_bawah_stretch_x = fields.Char(string='Leg Gum Bawah Stretch X',)
    leg_gum_bawah_stretch_y= fields.Char(string='Leg Gum Bawah Stretch Y',)
    
    leg_gum_tengah_stretch_x = fields.Char(string='Leg Gum Tengah Stretch X',)
    leg_gum_tengah_stretch_y = fields.Char(string='Leg Gum Tengah Stretch Y',)

    # tutup tambhan 190820---------------------------------

    
    welt_inside_crc = fields.Char(string='Welt Inside CRC',)
    welt_inside_s = fields.Char(string='Welt Inside S',)
    welt_inside_e = fields.Char(string='Welt Inside E',)

    welt_outside_crc = fields.Char(string='Welt Outside CRC',)
    welt_outside_s = fields.Char(string='Welt Outside S',)
    welt_outside_e = fields.Char(string='Welt Outside E',)
    
    transfer_crc = fields.Char(string='Transfer CRC',)
    transfer_s = fields.Char(string='Transfer S',)
    transfer_e = fields.Char(string='Transfer E',)

    leg_gum_crc = fields.Char(string='Leg Gum CRC',)
    leg_gum_s = fields.Char(string='Leg Gum S',)
    leg_gum_e = fields.Char(string='Leg Gum E',)

    leg_crc = fields.Char(string='Leg CRC',)
    leg_s = fields.Char(string='Leg S',)
    leg_e = fields.Char(string='Leg E',)

    leg_band_elast_crc = fields.Char(string='Leg band Elast CRC',)
    leg_band_elast_s = fields.Char(string='Leg band Elast S',)
    leg_band_elast_e = fields.Char(string='Leg band Elast E',)

    ankle_crc = fields.Char(string='Ankle CRC',)
    ankle_s = fields.Char(string='Ankle S',)
    ankle_e = fields.Char(string='Ankle E',)

    heel_crc = fields.Char(string='Heel CRC',)
    heel_s = fields.Char(string='Heel S',)
    heel_e = fields.Char(string='Heel E',)

    foot_gum_crc = fields.Char(string='Foot Gum CRC',)
    foot_gum_s = fields.Char(string='Foot Gum S',)
    foot_gum_e = fields.Char(string='Foot Gum E',)

    foot_crc = fields.Char(string='Foot CRC',)
    foot_s = fields.Char(string='Foot S',)
    foot_e = fields.Char(string='Foot E',)

    begin_toe_crc = fields.Char(string='Begin Toe CRC',)
    begin_toe_s = fields.Char(string='Begin Toe S',)
    begin_toe_e = fields.Char(string='Begin Toe E',)

    toe_crc = fields.Char(string='Toe CRC',)
    toe_s = fields.Char(string='Toe S',)
    toe_e = fields.Char(string='Toe E',)

    rosso_crc = fields.Char(string='Rosso CRC',)
    rosso_s = fields.Char(string='Rosso S',)
    rosso_e = fields.Char(string='Rosso E',)

    lose_crc = fields.Char(string='Lose CRC',)
    lose_s = fields.Char(string='Lose S',)
    lose_e = fields.Char(string='Lose E',)

    lingking_crc = fields.Char(string='Lingking CRC',)
    lingking_s = fields.Char(string='Lingking S',)
    lingking_e = fields.Char(string='Lingking E',)

    
    feed_1 = fields.Char(string='Feed 1',)
    feed_1a = fields.Char(string='Feed 1A',)
    feed_1b = fields.Char(string='Feed 1B',)
    feed_1c = fields.Char(string='Feed 1C',)

    feed_2 = fields.Char(string='Feed 2',)
    feed_2a = fields.Char(string='Feed 2A',)
    feed_2b = fields.Char(string='Feed 2B',)
    feed_2c = fields.Char(string='Feed 2C',)

    feed_3_a = fields.Char(string='Feed 3.A',)
    feed_3a = fields.Char(string='Feed 3A',)
    feed_3_b = fields.Char(string='Feed 3.B',)
    feed_3b = fields.Char(string='Feed 3B',)
    feed_3c = fields.Char(string='Feed 3C',)

    feed_4_a = fields.Char(string='Feed 4.A',)
    feed_4a = fields.Char(string='Feed 4A',)
    feed_4_b = fields.Char(string='Feed 1',)
    feed_4b = fields.Char(string='Feed 4B',)

    feed_5 = fields.Char(string='Feed 5',)
    feed_5a = fields.Char(string='Feed 5A',)
    feed_5b = fields.Char(string='Feed 5B',)
    feed_5c = fields.Char(string='Feed 5C',)
    
    feed_6 = fields.Char(string='Feed 6',)
    feed_7 = fields.Char(string='Feed 7',)
    feed_8 = fields.Char(string='Feed 8',)
    #tambhan yang dev 3
    tgl_buat_operator = fields.Date(string='Tgl Buat Operator',)
    feed_4c = fields.Char(string='Feed 4C',)

# --------------------------JENIS KAOS KAKI ---------------------------------------
class MarelInSamlpeJenisKk(models.Model):
    _name = 'marel.sample.jenis.kk'
    
    name = fields.Char(string='Name',)
    

class MarelInSamlpeBom(models.Model):
    _inherit = ['mrp.bom']

    janis_kk_id = fields.Many2one('marel.sample.jenis.kk',string='Janis Kk',store=True,)
    
class MarelInSamlpeBomLine(models.Model):
    _inherit = ['mrp.bom.line']

    marel_in_samlpe_dev_id = fields.Many2one('marelin.samlpe.dev2',string=u'marel in samlpe_dev id',)
    jumlah_ambil = fields.Float(string=u'Jmlah Ambil (C)',)
    qty_benang_kg = fields.Float(string=u'Qty Benang Per Pasang (kg)',digits=dp.get_precision('Custom 2'),)
    qty_benang_gr = fields.Float(string=u'Qty Benang Per Pasang (gr)',digits=dp.get_precision('Custom 2'),)
    qty_bom_reguler = fields.Float(string=u'Qty Bom (R)',digits=dp.get_precision('Custom 2'),)
    qty_bom_soccer = fields.Float(string=u'Qty Bom (S)',digits=dp.get_precision('Custom 2'),)
    # partner_id = fields.Many2one('res.partner', string='Customer', )
    awal = fields.Float(string=u'Awal',digits=dp.get_precision('Custom 2'),)
    akhir = fields.Float(string=u'Akhir',digits=dp.get_precision('Custom 2'),)
    terpakai = fields.Float(string=u'Terpakai',compute='_compute_terpakai', digits=dp.get_precision('Custom 2'), store=True)


    @api.multi
    def get_hitung_qty_mrp_bom_line(self):
        self.qty_bom_reguler = 0.0
        self.qty_bom_soccer = 0.0
        # self.product_qty = 0.0
        #mengconvert dari gr ke kg
        self.qty_benang_kg = (self.qty_benang_gr/1000)
        #perhitungan toleransi
        toleransi_qty_bom_r = (self.qty_benang_kg*0.07)
        toleransi_qty_bom_s = (self.qty_benang_kg*0.15)
        #qty bom kaos kaki
        self.qty_bom_reguler = (self.qty_benang_kg + toleransi_qty_bom_r)
        self.qty_bom_soccer = (self.qty_benang_kg + toleransi_qty_bom_s)

        if (self.bom_id.janis_kk_id.id == 1):
            self.product_qty = self.qty_bom_reguler
        else :
            self.product_qty = self.qty_bom_soccer
        # else :
        #     self.product_qty = self.product_qty
        return

    @api.one
    @api.depends('awal','akhir')
    def _compute_terpakai(self):
        self.terpakai = self.awal - self.akhir


    @api.onchange('terpakai')
    def on_change_terpakai(self):
        res = {}
        if self.terpakai > 0:
            self.qty_benang_gr = self.terpakai    
        return res


class MarelInSamlpeDev2(models.Model):

    _name = 'marelin.samlpe.dev2'
    _rec_name = 'product_id'

    marel_in_samlpe_dev_list_line = fields.One2many('marelin.samlpe.dev2.list','marel_in_samlpe_dev_id',string=u'Samlpe Dev Line',)
    operator_marelinsamlpedev2_list = fields.One2many('operator.marelinsamlpe.dev2.list','marel_in_samlpe_dev_id',string=u'Oeprator Mengisi Sample',)
    marelin_aksesotis_samlpedev2_list = fields.One2many('marelin.aksesotis.samlpedev2.list','marel_in_samlpe_dev_id',string=u'Aksesoris Samlpe Dev Line',)
    # mrp bom
    bom_line_list = fields.One2many('mrp.bom.line','marel_in_samlpe_dev_id',string=u'BOM Line',related='product_id.bom_ids.bom_line_ids',)


    def get_marelin_samlpe_dev2_no(self):
        nama_baru = self.env['ir.sequence'].next_by_code('marelin.samlpe.dev2.no')
        return nama_baru
      
    name = fields.Char(string='Id Sample',required=True,copy=False, default=get_marelin_samlpe_dev2_no,readonly=True )
    #-------------------------------------
    tgl_masuk = fields.Date(string=u'Tgl Masuk',default=fields.Date.context_today,)
    tgl_selesai = fields.Datetime(string=u'Tgl Selesai',readonly=True)
    product_id = fields.Many2one('product.product',string=u'Nama Produk',)
    kode_dokumen = fields.Char(string=u'Kode Doc',)
    # ukuran_relaxed = fields.Float(string=u'Ukuran Relaxed',) 
    gambar_sample = fields.Binary(string='Gambar Sample',)
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, track_visibility='onchange', default=lambda self: self.env.user)

    kode_dokumen = fields.Char(string=u'Kode Doc',)
    penjerat_2 = fields.Many2one('product.product',string=u'Penjerat 2',)

    # steam
    size = fields.Float(string='Size',)
    waktu = fields.Float(string='Waktu Steam',)
    waktu_anti_slip = fields.Float(string='Waktu Anti Slip',)
    keterangan_anti_slip = fields.Text(string='keterangan AS',)


    no_mesin = fields.Float(string=u'No Mesin/Jarum',)
    warna = fields.Char(string=u'Warna',)
    keterangan = fields.Text(string='Keterangan',)
    
    # nama_kaoskaki = fields.Char(string=u'Nama Sample Kaos Kaki',required=True,)
    # waktu = fields.Integer(string=u'Waktu (menit)',)
    # berat_kaos_kaki = fields.Float(string=u'Berat KaosKaki (Kg)',digits=dp.get_precision('Product Unit of Measure'),)
    # status = fields.Boolean(string=u'Fix',)
    brand = fields.Char(string=u'Brand',)
    model_sample = fields.Char(string=u'Model',)
    # artikel = fields.Char(string=u'Artikel',)
    tipe = fields.Char(string=u'Type',)
    delivery = fields.Datetime(string=u'Delivery',)
    # style = fields.Char(string=u'Style',)
    # artikel = fields.Char(string=u'Artikel',)

    gum_relaxed_x= fields.Float(string='Gum Relaxed x ',)
    gum_relaxed_y= fields.Float(string='Gum Relaxed y ',)

    leg_gum_relaxed_x= fields.Float(string='Leg Gum Relaxed x ',)
    leg_gum_relaxed_y= fields.Float(string='Leg Gum Relaxed y ',)

    leg_gum_atas_relaxed_x= fields.Float(string='Leg Gum Atas Relaxed x ',)
    leg_gum_atas_relaxed_y= fields.Float(string='Leg Gum Atas Relaxed y ',)

    leg_gum_bawah_relaxed_x= fields.Float(string='Leg Gum Bawah Relaxed x ',)
    leg_gum_bawah_relaxed_y= fields.Float(string='Leg Gum Bawah Relaxed y ',)

    leg_relaxed_x= fields.Float(string=' Leg Relaxed x',)
    leg_relaxed_y= fields.Float(string='Leg Relaxed y ',)
    
    foot_relaxed_x= fields.Float(string=' Foot Relaxed x',)
    foot_relaxed_y= fields.Float(string=' Foot Relaxed y',)

    foot_gum_relaxed_x= fields.Float(string='Foot Gum Relaxed x ',)
    foot_gum_relaxed_y= fields.Float(string='Foot Gum Relaxed y ',)

    hell_relaxed_x= fields.Float(string='Heel Relaxed x ',)
    hell_relaxed_y= fields.Float(string='Heel Relaxed y ',)

    #tambhan 190820---------------------------------
    gum_atas_relaxed_x = fields.Float(string='Gum Atas Relaxed X',)
    gum_atas_relaxed_y = fields.Float(string='Gum Atas Relaxed Y',)

    gum_bawah_relaxed_x = fields.Float(string='Gum Bawah relaxed X',)
    gum_bawah_relaxed_y = fields.Float(string='Gum Bawah Relaxed Y' ,)
    
    leg_gum_tengah_relaxed_x = fields.Float(string='Leg Gum Tengah Relaxed X',)
    leg_gum_tengah_relaxed_y = fields.Float(string='Leg Gum Tengah Relaxed Y',)
    
    #Tambahan relaxedout 20230413
    gum_relaxed_out_x= fields.Float(string='Gum Relaxed Out X',)
    gum_relaxed_out_y= fields.Float(string='Gum Relaxed Out Y',)

    leg_gum_relaxed_out_x= fields.Float(string='Leg Gum Relaxed Out X',)
    leg_gum_relaxed_out_y= fields.Float(string='Leg Gum Relaxed Out Y',)

    leg_gum_atas_relaxed_out_x= fields.Float(string='Leg Gum Atas Relaxed Out X',)
    leg_gum_atas_relaxed_out_y= fields.Float(string='Leg Gum Atas Relaxed Out Y',)

    leg_gum_bawah_relaxed_out_x= fields.Float(string='Leg Gum Bawah Relaxed Out X',)
    leg_gum_bawah_relaxed_out_y= fields.Float(string='Leg Gum Bawah Relaxed Out Y',)

    leg_relaxed_out_x= fields.Float(string=' Leg Relaxed Out X',)
    leg_relaxed_out_y= fields.Float(string='Leg Relaxed Out Y',)

    foot_relaxed_out_x= fields.Float(string=' Foot Relaxed Out X',)
    foot_relaxed_out_y= fields.Float(string=' Foot Relaxed Out Y',)

    foot_gum_relaxed_out_x= fields.Float(string='Foot Gum Relaxed Out X',)
    foot_gum_relaxed_out_y= fields.Float(string='Foot Gum Relaxed Out Y',)

    hell_relaxed_out_x= fields.Float(string='Heel Relaxed Out X',)
    hell_relaxed_out_y= fields.Float(string='Heel Relaxed Out Y',)

    gum_atas_relaxed_out_x = fields.Float(string='Gum Atas Relaxed Out X',)
    gum_atas_relaxed_out_y = fields.Float(string='Gum Atas Relaxed Out Y',)

    gum_bawah_relaxed_out_x = fields.Float(string='Gum Bawah Relaxed Out X',)
    gum_bawah_relaxed_out_y = fields.Float(string='Gum Bawah Relaxed Out Y' ,)
    
    leg_gum_tengah_relaxed_out_x = fields.Float(string='Leg Gum Tengah Relaxed Out X',)
    leg_gum_tengah_relaxed_out_y = fields.Float(string='Leg Gum Tengah Relaxed Out Y',)

# tutup tambhan 190820-------------------------------------------


    style = fields.Char(string=u'Style',)
    artikel = fields.Char(string=u'Artikel',)
    body = fields.Many2one('product.product',string=u'Body',)
    wording_munich = fields.Many2one('product.product',string=u'Wording',)
    logo = fields.Many2one('product.product',string=u'Logo',)
    hell = fields.Many2one('product.product',string=u'Heel',)
    toe = fields.Many2one('product.product',string=u'Toe',)
    transfer = fields.Many2one('product.product',string=u'Transfer',)
    lintoe = fields.Many2one('product.product',string=u'Lintoe',)
    penjerat = fields.Many2one('product.product',string=u'Penjerat',)
    karet = fields.Many2one('product.product',string=u'Karet',)
    patter_1 = fields.Many2one('product.product',string=u'Pattern 1',)
    patter_2 = fields.Many2one('product.product',string=u'Pattern 2',)
    patter_3 = fields.Many2one('product.product',string=u'Pattern 3',)
    patter_4 = fields.Many2one('product.product',string=u'Pattern 4',)
    patter_5 = fields.Many2one('product.product',string=u'Pattern 5',)
    patter_6 = fields.Many2one('product.product',string=u'Pattern 6',)
    patter_7 = fields.Many2one('product.product',string=u'Pattern 7',)
    patter_8 = fields.Many2one('product.product',string=u'Pattern 8',)
    patter_9 = fields.Many2one('product.product',string=u'Pattern 9',)
    patter_10 = fields.Many2one('product.product',string=u'Pattern 10',)
    jumlah_pasang = fields.Integer(string='Jumlah Pasang',)

    #untuk BOM Benang
    needle = fields.Char(string=u'Needle',)
    nama_sample = fields.Char(string=u'Nama Sample',)
    tgl_bon = fields.Date(string=u'Tgl Permintaan BON',default=fields.Date.context_today,)

    partner_id = fields.Many2one('res.partner', string='Customer',)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done','Done'),
        ('cancel','Canceled')
        ],string="Status", readonly=True, copy=False, default='draft')

                            
    @api.multi
    def action_run(self):
        tgl_selesai = fields.Datetime.now()
        self.write({'state': 'done','tgl_selesai':tgl_selesai})
        # return True
    
    @api.multi
    def action_cancel(self):
		    self.write({'state': 'cancel'})
        # return True

    @api.multi
    def action_set_draft(self):
        self.write({'state': 'draft'})
        # return True

    # TOTAL BRUTO
    total_bruto = fields.Float(string='Total Bruto',compute='_get_jumlah_total_bruto',store=True)

    @api.multi
    @api.depends('bom_line_list')
    def _get_jumlah_total_bruto(self):
        for marel_in_samlpe_dev_id in self:
            marel_in_samlpe_dev_id.total_bruto = sum((line_id.terpakai) for line_id in marel_in_samlpe_dev_id.bom_line_list)
