from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime

# --------------------------- inline 20 ----------------------------------------------------
# class MspMayorMinor2Wizard(models.TransientModel):
#     _name = "msp.mayor.minor2"

#     name = fields.Char(string='name',)


class MspQcInline2Wizard(models.TransientModel):
    _name = "msp.qc.inline2.wizard"

    def _default_mspmemo_qc_inline(self):
        return self.env['mrp.workorder'].browse(self._context.get('active_ids'))

    name = fields.Many2one('mrp.workorder',string="Name",default=_default_mspmemo_qc_inline, readonly=True, store=True,)
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,store=True,)
    mrp_productioin_id = fields.Many2one(string=u'No MO', related='name.production_id', readonly=True,store=True)
    keterangan = fields.Text(string='Keterangan',store=True,)
    # button_inline2 = fields.Integer(string='Telah Di Tekan',store=True,)
    # drop down =======================================================
    handfeel = fields.Selection([
        ('g',_('Good')),
        ('ng',_('Not Good')),
        ('na',_('Not Aplicable')),
        ], string="Handfeel",store=True,)
    color = fields.Selection([
        ('g',_('Good')),
        ('ng',_('Not Good')),
        ('na',_('Not Aplicable')),
        ], string="Color",store=True,)
    aksesoris_1 = fields.Selection([
        ('g',_('Good')),
        ('ng',_('Not Good')),
        ('na',_('Not Aplicable')),
        ], string="Benang",store=True,)

    aksesoris_2 = fields.Selection([
        ('g',_('Good')),
        ('ng',_('Not Good')),
        ('na',_('Not Aplicable')),
        ], string="Bordir",store=True,)

    aksesoris_3 = fields.Selection([
        ('g',_('Good')),
        ('ng',_('Not Good')),
        ('na',_('Not Aplicable')),
        ], string="Label",store=True,)
    
    aksesoris_4 = fields.Selection([
        ('g',_('Good')),
        ('ng',_('Not Good')),
        ('na',_('Not Aplicable')),
        ], string="Hangtag",store=True,)
    
    aksesoris_5 = fields.Selection([
        ('g',_('Good')),
        ('ng',_('Not Good')),
        ('na',_('Not Aplicable')),
        ], string="Barcode",store=True,)
    
    inspection_result = fields.Selection([
        ('release',_('Release')),
        ('reject',_('Reject')),
        ('hold',_('Hold')),
        ('under_guarantee',_('Under Guarantee')),
        ], string="Inspection Result",store=True,)


    sample_size_2_8 = fields.Integer(string='Sample Size (2-8)',default=2,readonly=True)
    mayor_2_8 = fields.Integer(string='Mayor (2-8)',default=0,readonly=True)
    minor_2_8 = fields.Integer(string='Minor (2-8)',default=1,readonly=True)

    sample_size_9_15 = fields.Integer(string='Sample Size (9-15)',default=3,readonly=True)
    mayor_9_15 = fields.Integer(string='Mayor (9-15)',default=0,readonly=True)
    minor_9_15 = fields.Integer(string='Minor (9-15)',default=1,readonly=True)

    sample_size_16_25 = fields.Integer(string='Sample Size (6-25)',default=5,readonly=True)
    mayor_16_25 = fields.Integer(string='Mayor (6-25)',default=1,readonly=True)
    minor_16_25 = fields.Integer(string='Minor (6-25)',default=2,readonly=True)

    sample_size_26_50 = fields.Integer(string='Sample Size (26-50)',default=8,readonly=True)
    mayor_26_50 = fields.Integer(string='Mayor (26-50)',default=2,readonly=True)
    minor_26_50 = fields.Integer(string='Minor (26-50)',default=1,readonly=True)

    sample_size_51_90 = fields.Integer(string='Sample Size (51-90)',default=13,readonly=True)
    mayor_51_90 = fields.Integer(string='Mayor (51-90)',default=2,readonly=True)
    minor_51_90 = fields.Integer(string='Minor (51-90)',default=2,readonly=True)

    sample_size_91_150 = fields.Integer(string='Sample Size (91-150)',default=32,readonly=True)
    mayor_91_150 = fields.Integer(string='Mayor (91-150)',default=2,readonly=True)
    minor_91_150 = fields.Integer(string='Minor (91-150)',default=3,readonly=True)
    # --
    sample_size_151_280 = fields.Integer(string='Sample Size (151-280)',default=32,readonly=True)
    mayor_151_280 = fields.Integer(string='Mayor (151-280)',default=2,readonly=True)
    minor_151_280 = fields.Integer(string='Minor (151-280)',default=3,readonly=True)

    sample_size_281_500 = fields.Integer(string='Sample Size (281-500)',default=50,readonly=True)
    mayor_281_500 = fields.Integer(string='Mayor (281-500)',default=3,readonly=True)
    minor_281_500 = fields.Integer(string='Minor (281-500)',default=4,readonly=True)

    sample_size_501_1200 = fields.Integer(string='Sample Size (501-1200)',default=80,readonly=True)
    mayor_501_1200 = fields.Integer(string='Mayor (501-1200)',default=5,readonly=True)
    minor_501_1200 = fields.Integer(string='Minor (501-1200)',default=6,readonly=True)
    
    sample_size_1201_3200 = fields.Integer(string='Sample Size (1201-32000)',default=125,readonly=True)
    mayor_1201_3200 = fields.Integer(string='Mayor (1201-32000)',default=7,readonly=True)
    minor_1201_3200 = fields.Integer(string='Minor (1201-32000)',default=8,readonly=True)

    sample_size_3201_10000 = fields.Integer(string='Sample Size (3201-10000)',default=200,readonly=True)
    mayor_3201_10000 = fields.Integer(string='Mayor (3201-10000)',default=10,readonly=True)
    minor_3201_10000 = fields.Integer(string='Minor (3201-10000)',default=11,readonly=True)

    sample_size_10001_35000 = fields.Integer(string='Sample Size (10000-35000)',default=315,readonly=True)
    mayor_10001_35000 = fields.Integer(string='Mayor (10000-35000)',default=14,readonly=True)
    minor_10001_35000 = fields.Integer(string='Minor (10000-35000)',default=15,readonly=True)

    sample_size_35001 = fields.Integer(string='Sample Size (35001)',default=500,readonly=True)
    mayor_35001 = fields.Integer(string='Mayor (35001)',default=21,readonly=True)
    minor_35001 = fields.Integer(string='Minor (35001)',default=22,readonly=True)

    prodak = fields.Selection([
        ('sock',_('SOCK')),
        ('bordir',_('BORDIR')),
        ('garment',_('GARMENT')),
        ], string="Produk",store=True,)

    
    no_carton_inspected_1 = fields.Integer(string='No Carton Inspected 1',)
    no_carton_inspected_2 = fields.Integer(string='No Carton Inspected 2',)
    no_carton_inspected_3 = fields.Integer(string='No Carton Inspected 3',)
    no_carton_inspected_4 = fields.Integer(string='No Carton Inspected 4',)
    no_carton_inspected_5 = fields.Integer(string='No Carton Inspected 5',)
    no_carton_inspected_6 = fields.Integer(string='No Carton Inspected 6',)
    no_carton_inspected_7 = fields.Integer(string='No Carton Inspected 7',)
    no_carton_inspected_8 = fields.Integer(string='No Carton Inspected 8',)
    no_carton_inspected_9 = fields.Integer(string='No Carton Inspected 9',)
    no_carton_inspected_10 = fields.Integer(string='No Carton Inspected 10',)


    rijek_1 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 1",store=True,)

    rijek_2 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 2",store=True,)

    rijek_3 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 3",store=True,)

    rijek_4 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 4",store=True,)

    rijek_5 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 5", store=True,)
    rijek_6 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 6", store=True,)

    rijek_7 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 7",store=True,)

    rijek_8 = fields.Selection([
        ('bolong_lintoe',_('Bolong Lintoe')),
        ('bolong_transfer',_('Bolong Transfer')),
        ('bolong_leg',_('Bolong Leg')),
        ('bolong_foot',_('BBlong Foot')),
        ('vanice',_('Vanice')),
        ('kotor',_('Kotor')),
        ('tidak_loading_toe',_('Tidak Loading Toe')),
        ('tidak_loading_pattern',_('Tidak Loading Pattern')),
        ('gumpal',_('Gumpal')),
        ('tidak_loading_heel',_('Tidak Loading Heel')),
        ('tidak_loading_leg',_('Tidak Loading Leg')),
        ('tidak_loading_foot',_('Tidak Loading Foot')),
        ('tidak_jadi_terry',_('Tidak Jadi Terry')),
        ('belang',_('Belang')),
        ('loncat_heel',_('Loncat Heel')),
        ('loncat_toe',_('Loncat Toe')),
        ('loncat_leg',_('Loncat Teg')),
        ('loncat_foot',_('Loncat Foot')),
        ('keluar_terry',_('Keluar Terry')),
        ('putus_benang',_('Putus Benang')),
        ('jumpstitch',_('Jumpstitch')),
        ('conti_tidak_center',_('Conti Tidak Center')),
        ('conti_bergelombang',_('Conti Bergelombang')),
        ('heel_toe_setting_tidak_center',_('Heel Toe Setting Tidak Center')),
        ('elastik_kriting',_('Elastik Kriting')),
        ('gum_keriting',_('Gum Keriting')),
        ('renggang',_('Renggang')),
        ('potongan_panjang',_('Potongan Panjang')),
        ('tidak_jodoh',_('Tidak Jodoh')),
        ('rosso_kelihatan',_('Rosso Kelihatan')),
        ('lidah_seret',_('Lidah Seret')),
        ('pecah,',_('Pecah')),
        ('jarum_patah,',_('Jarum Patah')),
        ('sinker,',_('Sinker')),
        ], string="Rijek 8",store=True,)
    
    
    # bentuk_rijek_1 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_1 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_1 = fields.Integer(string='Nilai 1',)

    # bentuk_rijek_2 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_2 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_2 = fields.Integer(string='Nilai 2',)

    # bentuk_rijek_3 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_3 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_3 = fields.Integer(string='Nilai 3',)

    # bentuk_rijek_4 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_4 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_4 = fields.Integer(string='Nilai 4',)

    # bentuk_rijek_5 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_5 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_5 = fields.Integer(string='Nilai 5',)

    # bentuk_rijek_6 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_6 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_6 = fields.Integer(string='Nilai 6',)

    # bentuk_rijek_7 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_7 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_7 = fields.Integer(string='Nilai 7',)

    # bentuk_rijek_8 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_8 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_8 = fields.Integer(string='Nilai 8',)

    jumlah_kritikal_qc = fields.Integer(string='Jumlah Kritikal',)
    jumlah_mayor_qc = fields.Integer(string='Jumlah Mayor',)
    jumlah_minor_qc = fields.Integer(string='Jumlah Minor',)

    product_qty_inline = fields.Float('Quantity To Produce',readonly=True,related='mrp_productioin_id.product_qty')
    product_qty_inline_1 = fields.Float('Quantity 1',readonly=True,related='mrp_productioin_id.product_qty')
    comment = fields.Text(string='Comment',store=True)

    sugestion_1 = fields.Char(string='Sugestion 1',)
    sugestion_2 = fields.Char(string='Sugestion 2',)
    sugestion_3 = fields.Char(string='Sugestion 3',)
    sugestion_4 = fields.Char(string='Sugestion 4',)
    sugestion_5 = fields.Char(string='Sugestion 5',)
    sugestion_6 = fields.Char(string='Sugestion 6',)
    sugestion_7 = fields.Char(string='Sugestion 7',)
    sugestion_8 = fields.Char(string='Sugestion 8',)

    # product_qty_inline_2 = fields.Float('Quantity 2',readonly=True,related='mrp_productioin_id.product_qty')
    # product_qty_inline_3 = fields.Float('Quantity 3',readonly=True,related='mrp_productioin_id.product_qty')
    # product_qty_inline_4 = fields.Float('Quantity 4',readonly=True,related='mrp_productioin_id.product_qty')

    # @api.multi
    # @api.depends('mrp_productioin_id')
    # def _get_mengisi_jumlah_mayor_qc(self):
    #     for l in self :
    #         l.jumlah_mayor_qc = l.rijek_minor_1 + l.rijek_minor_2 + l.rijek_minor_3 + l.rijek_minor_4 + l.rijek_minor_5 + l.rijek_minor_6 + l.rijek_minor_7 + l.rijek_minor_8
    #         l.jumlah_mayor_qc = sum(l.rijek_minor_1 + l.rijek_minor_2 + l.rijek_minor_3 + l.rijek_minor_4 + l.rijek_minor_5 + l.rijek_minor_6 + l.rijek_minor_7 + l.rijek_minor_8)
    #     self._get_mengisi_jumlah_minor_qc()
    #     self._get_mengisi_jumlah_kritikal_qc()

        # for nama_operator_work_order_id in self:
            # nama_operator_work_order_id.total_bolong = sum((line_id.bolong) for line_id in nama_operator_work_order_id.nama_operator_line)

    # @api.multi
    # def _get_mengisi_jumlah_mayor_qc(self):
    #     for l in self :
    #         if l.mrp_productioin_id != "":
    #             l.jumlah_mayor_qc = l.rijek_minor_1 + l.rijek_minor_2 + l.rijek_minor_3 + l.rijek_minor_4 + l.rijek_minor_5 + l.rijek_minor_6 + l.rijek_minor_7 + l.rijek_minor_8
        # self._get_mengisi_jumlah_minor_qc()
        # self._get_mengisi_jumlah_kritikal_qc()
        # self._get_mengisi_jumlah_mayor_qc()

    # @api.multi
    # def _get_mengisi_jumlah_minor_qc(self):
    #     for l in self :
    #         if l.mrp_productioin_id != "":
    #             l.jumlah_minor_qc = l.rijek_mayor_1 + l.rijek_mayor_2 + l.rijek_mayor_3 + l.rijek_mayor_4 + l.rijek_mayor_5 + l.rijek_mayor_6 + l.rijek_mayor_7 + l.rijek_mayor_8

    # @api.multi
    # def _get_mengisi_jumlah_kritikal_qc(self):
    #     for l in self :
    #         if l.mrp_productioin_id != "":
    #             l.jumlah_kritikal_qc = l.kritikal_1 + l.kritikal_2 + l.kritikal_3 + l.kritikal_4 + l.kritikal_5 + l.kritikal_6 + l.kritikal_7 + l.kritikal_8


    @api.multi
    def msp_qc_inline2_wizard(self, vals):
        # self._get_mengisi_jumlah_minor_qc()
        # self._get_mengisi_jumlah_kritikal_qc()
        # self._get_mengisi_jumlah_mayor_qc()
        obj_nilai = self.env['msp.qc.inline2'].create({
                                                    "name_workorder_id":self.name.id,
                                                    "mrp_productioin_id":self.mrp_productioin_id.id,
                                                    "tgl_create":self.tgl_create,
                                                    "keterangan":self.keterangan,
                                                    "handfeel":self.handfeel,
                                                    "color":self.color,
                                                    "aksesoris_1":self.aksesoris_1,
                                                    "aksesoris_2":self.aksesoris_2,
                                                    "aksesoris_3":self.aksesoris_3,
                                                    "aksesoris_4":self.aksesoris_4,
                                                    "aksesoris_5":self.aksesoris_5,
                                                    "inspection_result":self.inspection_result,
                                                    "sample_size_151_280":self.sample_size_151_280,
                                                    "mayor_151_280":self.mayor_151_280,
                                                    "minor_151_280":self.minor_151_280,
                                                    "sample_size_281_500":self.sample_size_281_500,
                                                    "mayor_281_500":self.mayor_281_500,
                                                    "minor_281_500":self.minor_281_500,
                                                    "sample_size_501_1200":self.sample_size_501_1200,
                                                    "mayor_501_1200":self.mayor_501_1200,
                                                    "minor_501_1200":self.minor_501_1200,
                                                    "sample_size_1201_3200":self.sample_size_1201_3200,
                                                    "mayor_1201_3200":self.mayor_1201_3200,
                                                    "minor_1201_3200":self.minor_1201_3200,
                                                    "sample_size_3201_10000":self.sample_size_3201_10000,
                                                    "mayor_3201_10000":self.mayor_3201_10000,
                                                    "minor_3201_10000":self.minor_3201_10000,
                                                    "prodak":self.prodak,
                                                    "no_carton_inspected_1":self.no_carton_inspected_1,
                                                    "no_carton_inspected_2":self.no_carton_inspected_2,
                                                    "no_carton_inspected_3":self.no_carton_inspected_3,
                                                    "no_carton_inspected_4":self.no_carton_inspected_4,
                                                    "no_carton_inspected_5":self.no_carton_inspected_5,
                                                    "no_carton_inspected_6":self.no_carton_inspected_6,
                                                    "no_carton_inspected_7":self.no_carton_inspected_7,
                                                    "no_carton_inspected_8":self.no_carton_inspected_8,
                                                    "no_carton_inspected_9":self.no_carton_inspected_9,
                                                    "no_carton_inspected_10":self.no_carton_inspected_10,
                                                    "rijek_1":self.rijek_1,
                                                    "rijek_2":self.rijek_2,
                                                    "rijek_3":self.rijek_3,
                                                    "rijek_4":self.rijek_4,
                                                    "rijek_5":self.rijek_5,
                                                    "rijek_6":self.rijek_6,
                                                    "rijek_7":self.rijek_7,
                                                    "rijek_8":self.rijek_8,
                                                    "sugestion_1":self.sugestion_1,
                                                    "sugestion_2":self.sugestion_2,
                                                    "sugestion_3":self.sugestion_3,
                                                    "sugestion_4":self.sugestion_4,
                                                    "sugestion_5":self.sugestion_5,
                                                    "sugestion_6":self.sugestion_6,
                                                    "sugestion_7":self.sugestion_7,
                                                    "sugestion_8":self.sugestion_8,
                                                    "bentuk_rijek_1":self.bentuk_rijek_1,
                                                    "bentuk_rijek_2":self.bentuk_rijek_2,
                                                    "bentuk_rijek_3":self.bentuk_rijek_3,
                                                    "bentuk_rijek_4":self.bentuk_rijek_4,
                                                    "bentuk_rijek_5":self.bentuk_rijek_5,
                                                    "bentuk_rijek_6":self.bentuk_rijek_6,
                                                    "bentuk_rijek_7":self.bentuk_rijek_7,
                                                    "bentuk_rijek_8":self.bentuk_rijek_8,
                                                    "nilai_rijek_1":self.nilai_rijek_1,
                                                    "nilai_rijek_2":self.nilai_rijek_2,
                                                    "nilai_rijek_3":self.nilai_rijek_3,
                                                    "nilai_rijek_4":self.nilai_rijek_4,
                                                    "nilai_rijek_5":self.nilai_rijek_5,
                                                    "nilai_rijek_6":self.nilai_rijek_6,
                                                    "nilai_rijek_7":self.nilai_rijek_7,
                                                    "nilai_rijek_8":self.nilai_rijek_8,
                                                    # "rijek_3":self.rijek_3,
                                                    # "rijek_4":self.rijek_4,
                                                    # "rijek_5":self.rijek_5,
                                                    # "rijek_6":self.rijek_6,
                                                    # "rijek_7":self.rijek_7,
                                                    # "rijek_8":self.rijek_8,
                                                    # "rijek_minor_1":self.rijek_minor_1,
                                                    # "rijek_mayor_1":self.rijek_mayor_1,
                                                    # "nilai_rijek_1":self.nilai_rijek_1,
                                                    # "rijek_minor_2":self.rijek_minor_2,
                                                    # "rijek_mayor_2":self.rijek_mayor_2,
                                                    # "nilai_rijek_2":self.nilai_rijek_2,
                                                    # "rijek_minor_3":self.rijek_minor_3,
                                                    # "rijek_mayor_3":self.rijek_mayor_3,
                                                    # "nilai_rijek_3":self.nilai_rijek_3,
                                                    # "rijek_minor_4":self.rijek_minor_4,
                                                    # "rijek_mayor_4":self.rijek_mayor_4,
                                                    # "nilai_rijek_4":self.nilai_rijek_4,
                                                    # "rijek_minor_5":self.rijek_minor_5,
                                                    # "rijek_mayor_5":self.rijek_mayor_5,
                                                    # "nilai_rijek_5":self.nilai_rijek_5,
                                                    # "rijek_minor_6":self.rijek_minor_6,
                                                    # "rijek_mayor_6":self.rijek_mayor_6,
                                                    # "nilai_rijek_6":self.nilai_rijek_6,
                                                    # "rijek_minor_7":self.rijek_minor_7,
                                                    # "rijek_mayor_7":self.rijek_mayor_7,
                                                    # "nilai_rijek_7":self.nilai_rijek_7,
                                                    # "rijek_minor_8":self.rijek_minor_8,
                                                    # "rijek_mayor_8":self.rijek_mayor_8,
                                                    # "nilai_rijek_8":self.nilai_rijek_8,
                                                    # "kritikal_1":self.kritikal_1,
                                                    # "kritikal_2":self.kritikal_2,
                                                    # "kritikal_3":self.kritikal_3,
                                                    # "kritikal_4":self.kritikal_4,
                                                    # "kritikal_5":self.kritikal_5,
                                                    # "kritikal_6":self.kritikal_6,
                                                    # "kritikal_7":self.kritikal_7,
                                                    # "kritikal_8":self.kritikal_8,
                                                    "product_qty_inline":self.product_qty_inline,
                                                    "product_qty_inline_1":self.product_qty_inline_1,
                                                    "comment":self.comment,
                                                    # "product_qty_inline_2":self.product_qty_inline_2,
                                                    # "product_qty_inline_3":self.product_qty_inline_3,
                                                    # "product_qty_inline_4":self.product_qty_inline_4,
                                                    "jumlah_mayor_qc":self.jumlah_mayor_qc,
                                                    "jumlah_minor_qc":self.jumlah_minor_qc,
                                                    "jumlah_kritikal_qc":self.jumlah_kritikal_qc,
                                                    })
            # self._get_mengisi_jumlah_minor_qc()
            # self._get_mengisi_jumlah_kritikal_qc()
            # self._get_mengisi_jumlah_mayor_qc()
        return super(MspQcInline2Wizard, self).write(vals)

