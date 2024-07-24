# -*- coding: utf-8 -*-
# Copyright 2018 Raphael Reverdy https://akretion.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import datetime
from dateutil import relativedelta
from itertools import groupby
from operator import itemgetter

from flectra import api, fields, models, _
from flectra.addons import decimal_precision as dp
from flectra.exceptions import UserError
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from flectra.tools.float_utils import float_compare, float_round, float_is_zero

# class MspQcDefect(models.Model):
#     _name = 'msp.qc.defect'
    
#     name = fields.Char( string='Nama',)

class MspQcInline1(models.Model):
    _name = 'msp.qc.inline1'
    # _rec_name = 'nama_operator_id'

    def get_msp_qc_inline1_no(self):
        nama_baru = self.env['ir.sequence'].next_by_code('msp.qc.inline1.no')
        return nama_baru

    name = fields.Char(string='Id Inline 1',required=True,copy=False, default=get_msp_qc_inline1_no,readonly=True )
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,)
    # msp_qc_inline1_line_ids = fields.One2many('msp.qc.inline1.line','msp_qc_inline1_id',string=u'Defect Found',)
    keterangan = fields.Text(string='Keterangan',store=True,)
    name_workorder_id = fields.Many2one('mrp.workorder', string=u'No WO',store=True,)
    mrp_productioin_id = fields.Many2one('mrp.production', string=u'No MO',store=True,)
    # button_inline1 = fields.Boolean(string='Telah Di Tekan',)
    
    # drop down =======================================================
    handfeel = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ('NA',_('NA')),
        ], string="Handfeel",)
    color = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ('NA',_('NA')),
        ], string="Color",)

    aksesoris_1 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ('NA',_('NA')),
        ], string="Benang",)

    aksesoris_2 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ('NA',_('NA')),
        ], string="Bordir",)

    aksesoris_3 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ('NA',_('NA')),
        ], string="Label",)
    
    aksesoris_4 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ('NA',_('NA')),
        ], string="Hangtag",)
    
    aksesoris_5 = fields.Selection([
        ('G',_('G')),
        ('NG',_('NG')),
        ('NA',_('NA')),
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
