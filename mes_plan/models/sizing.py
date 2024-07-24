from flectra import api, fields, models, _
from flectra.exceptions import UserError

class InHeaderPlanSizing(models.Model):
    _description = "Header Plan Sizing"
    _name = "herader.plansizing"
    _rec_name = "name"


    mo_warping = fields.Many2one('herader.planwarping',string='MO Warping',)
    kode_warping = fields.Char(related='mo_warping.kode_warping',string='Kode Warping',readonly=True,)
    kode_sizing = fields.Char(string='Kode Sizing',)
    name = fields.Many2one('mrp.production',string='No KP/MO')
    seri = fields.Char(string='Seri',)
    tarikan = fields.Char(string='Tarikan',)
    quantity = fields.Float(string='Quantity',)
    mesin = fields.Many2one('mesin.produksi',string='Mesin Warping')
    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)


#--------------------------------- class baru -----------------------------------------------
class InOperatorSizing_Depan(models.Model):
    _description = "Operator Sizing Depan"
    _name = "operator.sizingdepan"


    #ubah fields
    name = fields.Many2one('herader.plansizing',string='No KP/MO')
    kode_sizing = fields.Char(related='name.kode_sizing',string='Seri',readonly=True,)
    seri = fields.Char(related='name.seri',string='Seri',readonly=True,)
    tarikan = fields.Char(related='name.tarikan',string='Tarikan',readonly=True,)
    quantity = fields.Float(related='name.quantity',string='Quantity',readonly=True,)
    mesin = fields.Many2one(related='name.mesin',string='Mesin Warping', readonly=True,)
    date_start = fields.Date(related='name.date_start',string="Start Date",readonly=True,)
    date_end = fields.Date(related='name.date_end',string="End Date",readonly=True,)

    tgl = fields.Date(string='Tgl', required=True)
    grade = fields.Char(string='Grade',)
    seri = fields.Char(string='Seri',)
    #------------------ beda ------------------------------------
    warping = fields.Char(string='Warping')
    mc_szg = fields.Many2one(string="MC Szg",comodel_name="mesin.produksi",ondelete='set null',)
    mc_wvp = fields.Many2one(string="MC WVP",comodel_name="mesin.produksi",ondelete='set null',)
    #---------------------------------- operator
    asal_benang = fields.Char(string='Asal Benang', )
    elg = fields.Integer(string='ELG', )
    stg = fields.Integer(string='STG', )
    pts_benang = fields.Char(string='Pts Benang', )
    te = fields.Char(string='TE', )
    pjg = fields.Integer(string='Pjg', )
    
    no_beam = fields.Char(string='no Beam', )
    panjang_benang = fields.Integer(string='Panjang Benang', )
    bruto = fields.Float(string='Berat Bruto', )
    beam = fields.Float(string='Berat Beam', )
    netto = fields.Float(string='Berat Netto', )
    spu = fields.Float(string='SPU', )
    visco_1 = fields.Integer(string='Visco 1', )
    visco_2 = fields.Integer(string='Visco 2', )
    suhu_1 = fields.Integer(string='Suhu 1', )
    suhu_2 = fields.Integer(string='Suhu 2', )
    ref = fields.Char(string='REF', )    
    jam_naik = fields.Char(string='Jam Naik', )
    jam_turun = fields.Char(string='Jam Turun', )
    hasil_menit = fields.Char(string='Hasil Menit', )
    #tambahan
    hasil_shift = fields.Char(string='Hasil Shift', )
    speed = fields.Integer(string='Speed', )
    press_dp_blk = fields.Char(string='Press Dp Blk', )
    temp_cyl_1 = fields.Char(string='Temp Cyl 1', )
    temp_cyl_2 = fields.Char(string='Temp Cyl 2', )
    temp_cyl_3 = fields.Char(string='Temp cyl 3', )
    operator_db_blk = fields.Char(string='Operator Db Blk', )
    #tambahan
    leader = fields.Integer(string='Leader', )
    leadery = fields.Integer(string='Putus Benang Creel', )
    putus_benang_size_box = fields.Integer(string='Putus Benang Size Box', )
    putus_benang_sisir = fields.Integer(string='Putus Benang Sisir', )
    
    #----------------------------------------------------------------------------------------
        #era bawah
    informasi = fields.Text(string='Informasi', )
    keterangan = fields.Text(string='Keterangan', )
    
    afal_setting_m = fields.Integer(string='Afal Setting M', )
    afal_setting_kg = fields.Float(string='Afal Setting KG', )

    alfa_terkaji_awal = fields.Float(string='Alfa Terkaji Awal KG', )
    alfa_terkaji_akhir = fields.Float(string='Alfa Terkaji Akhir KG', )
    alfa_terkaji_total = fields.Float(string='Alfa Terkaji Total KG', )    
    
    alfa_belum_awal = fields.Float(string='Alfa Belum Awal KG', )
    alfa_belum_akhir = fields.Float(string='Alfa Belum Akhir KG', )
    alfa_belum_total = fields.Float(string='Alfa Belum Total KG', )

    pesiapan_size_box_finish = fields.Float(string='Pesiapan Size Box Finish', )
    pesiapan_size_box_start = fields.Float(string='Pesiapan Size Box Start', )
    pesiapan_size_box_total = fields.Float(string='Pesiapan Size Box Total', )

    #--------------------------------------------------------------------------------------------
    pesiapan_cyl_finish = fields.Float(string='Pesiapan Cyl Finish', )
    pesiapan_cyl_start = fields.Float(string='Pesiapan Cyl Start', )
    pesiapan_cyl_total = fields.Float(string='Pesiapan Cyl Total', )

    pesiapan_head_finish = fields.Float(string='Pesiapan Head Finish', )
    pesiapan_head_start = fields.Float(string='Pesiapan Head Start', )
    pesiapan_head_total = fields.Float(string='Pesiapan Head Total', )

    pesiapan_pesankan_finish = fields.Float(string='Pesiapan Pesankan Finish', )
    pesiapan_pesankan_start = fields.Float(string='Pesiapan Pesankan Start', )
    pesiapan_pesankan_total = fields.Float(string='Pesiapan Pesankan Total', )
    

