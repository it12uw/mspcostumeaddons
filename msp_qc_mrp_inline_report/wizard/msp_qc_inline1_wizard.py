from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime

# --------------------------- inline 20 ----------------------------------------------------
class MspQcInline1Wizard(models.TransientModel):
    _name = "msp.qc.inline1.wizard"

    def _default_mspmemo_qc_inline(self):
        return self.env['mrp.workorder'].browse(self._context.get('active_ids'))

    name = fields.Many2one('mrp.workorder',string="Name",default=_default_mspmemo_qc_inline, readonly=True, store=True,)
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,store=True,)
    mrp_productioin_id = fields.Many2one(string=u'No MO', related='name.production_id', readonly=True,store=True)
    keterangan = fields.Text(string='Keterangan',store=True,)
    # button_inline1 = fields.Boolean(string='Telah Di Tekan',store=True,)
    # drop down =======================================================
    handfeel = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ], string="Handfeel",)
    color = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ], string="Color",)

    aksesoris_1 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ], string="Benang",)

    aksesoris_2 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ], string="Bordir",)

    aksesoris_3 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ], string="Label",)
    
    aksesoris_4 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ], string="Hangtag",)
    
    aksesoris_5 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ], string="Barcode",)
    
    inspection_result = fields.Selection([
        ('Release',_('Release')),
        ('Reject',_('Reject')),
        ('Hold',_('Hold')),
        ('Under_guarantee',_('Under_guarantee')),
        ], string="Inspection Result",)


    sample_size_151_280 = fields.Integer(string='Sample Size (151-280)',default=32,readonly=True)
    mayor_151_280 = fields.Integer(string='Mayor (151-280)',default=2,readonly=True)
    minor_151_280 = fields.Integer(string='Minor (151-280)',default=3,readonly=True)

    sample_size_281_500 = fields.Integer(string='Sample Size (281-500)',default=50,readonly=True)
    mayor_281_500 = fields.Integer(string='Mayor (281-500)',default=3,readonly=True)
    minor_281_500 = fields.Integer(string='Minor (281-500)',default=5,readonly=True)

    sample_size_501_1200 = fields.Integer(string='Sample Size (501-1200)',default=80,readonly=True)
    mayor_501_1200 = fields.Integer(string='Mayor (501-1200)',default=5,readonly=True)
    minor_501_1200 = fields.Integer(string='Minor (501-1200)',default=7,readonly=True)
    
    sample_size_1201_3200 = fields.Integer(string='Sample Size (1201-32000)',default=125,readonly=True)
    mayor_1201_3200 = fields.Integer(string='Mayor (1201-32000)',default=7,readonly=True)
    minor_1201_3200 = fields.Integer(string='Minor (1201-32000)',default=10,readonly=True)

    sample_size_3201_10000 = fields.Integer(string='Sample Size (3201-10000)',default=200,readonly=True)
    mayor_3201_10000 = fields.Integer(string='Mayor (3201-10000)',default=10,readonly=True)
    minor_3201_10000 = fields.Integer(string='Minor (3201-10000)',default=14,readonly=True)

    prodak = fields.Selection([
        ('SOCK',_('SOCK')),
        ('BORDIR',_('BORDIR')),
        ('GARMENT',_('GARMENT')),
        ], string="Prodak",)

    
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
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 1",)

    rijek_2 = fields.Selection([
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 2",)

    rijek_3 = fields.Selection([
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 3",)

    rijek_4 = fields.Selection([
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 4",)

    rijek_5 = fields.Selection([
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 5",)

    rijek_6 = fields.Selection([
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 6",)

    rijek_7 = fields.Selection([
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 7",)

    rijek_8 = fields.Selection([
        ('bolong_lintoe',_('bolong_lintoe')),
        ('bolong_transfer',_('bolong_transfer')),
        ('bolong_leg',_('bolong_leg')),
        ('bolong_foot',_('bolong_foot')),
        ('vanice',_('vanice')),
        ('kotor',_('kotor')),
        ('tidak_loading_toe',_('tidak_loading_toe')),
        ('tidak_loading_pattern',_('tidak_loading_pattern')),
        ('gumpal',_('gumpal')),
        ('tidak_loading_heel',_('tidak_loading_heel')),
        ('tidak_loading_leg',_('tidak_loading_leg')),
        ('tidak_loading_foot',_('tidak_loading_foot')),
        ('tidak_jadi_terry',_('tidak_jadi_terry')),
        ('belang',_('belang')),
        ('loncat_heel',_('loncat_heel')),
        ('loncat_toe',_('loncat_toe')),
        ('loncat_leg',_('loncat_leg')),
        ('loncat_foot',_('loncat_foot')),
        ('keluar_terry',_('keluar_terry')),
        ('putus_benang',_('putus_benang')),
        ('jumpstitch',_('jumpstitch')),
        ('conti_tidak_center',_('conti_tidak_center')),
        ('conti_bergelombang',_('conti_bergelombang')),
        ('heel_toe_setting_tidak_center',_('heel_toe_setting_tidak_center')),
        ('elastik_kriting',_('elastik_kriting')),
        ('gum_keriting',_('gum_keriting')),
        ('renggang',_('renggang')),
        ('potongan_panjang',_('potongan_panjang')),
        ('tidak_jodoh',_('tidak_jodoh')),
        ('rosso_kelihatan',_('rosso_kelihatan')),
        ('lidah_seret',_('lidah_seret')),
        ('pecah,',_('pecah')),
        ('jarum_patah,',_('jarum_patah')),
        ('sinker,',_('sinker')),
        ], string="Rijek 8",)

    @api.multi
    def msp_qc_inline1_wizard(self, vals):
        obj_nilai = self.env['msp.qc.inline1'].create({
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
                                                    })
        return super(MspQcInline1Wizard, self).write(vals)

