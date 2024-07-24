# -*- coding: utf-8 -*-
# Copyright 2028 Raphael Reverdy https://akretion.com
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

# class MspMayorMinor4(models.Model):
#     _name = "msp.mayor.minor4"

#     name = fields.Char(string='name',)

class MspQcInline4(models.Model):
    _name ='msp.qc.inline4'
    # _name = 'msp.qc.inline4'
    # _rec_name = 'nama_operator_id'

    def get_msp_qc_inline4_no(self):
        nama_baru = self.env['ir.sequence'].next_by_code('msp.qc.inline4.no')
        return nama_baru

    name = fields.Char(string='Id Inline 2',required=True,copy=False, default=get_msp_qc_inline4_no,readonly=True )
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,)
    inspection_date = fields.Datetime(string='Inspection Date',default=fields.Datetime.now,)
    # msp_qc_inline3_line_ids = fields.One3many('msp.qc.inline3.line','msp_qc_inline3_id',string=u'Defect Found',)
    keterangan = fields.Text(string='Keterangan',store=True,)
    name_workorder_id = fields.Many2one('mrp.workorder', string=u'No WO',store=True,)
    mrp_productioin_id = fields.Many2one('mrp.production', string=u'No MO',store=True,)
    # button_inline3 = fields.Integer(string='Telah Di Tekan',)
    
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
        ], string="Prodak",store=True,)

    
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

    keterangan_1 = fields.Char(string='keterangan 1',)
    keterangan_2 = fields.Char(string='keterangan 2',)
    keterangan_3 = fields.Char(string='keterangan 3',)
    keterangan_4 = fields.Char(string='keterangan 4',)
    keterangan_5 = fields.Char(string='keterangan 5',)
    keterangan_6 = fields.Char(string='keterangan 6',)
    keterangan_7 = fields.Char(string='keterangan 7',)
    keterangan_8 = fields.Char(string='keterangan 8',)
    # keterangan_9 = fields.Char(string='keterangan 9',)
    # keterangan_10 = fields.Char(string='keterangan 10',)

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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),        
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

    sugestion_1 = fields.Char(string='Sugestion 1',)
    sugestion_2 = fields.Char(string='Sugestion 2',)
    sugestion_3 = fields.Char(string='Sugestion 3',)
    sugestion_4 = fields.Char(string='Sugestion 4',)
    sugestion_5 = fields.Char(string='Sugestion 5',)
    sugestion_6 = fields.Char(string='Sugestion 6',)
    sugestion_7 = fields.Char(string='Sugestion 7',)
    sugestion_8 = fields.Char(string='Sugestion 8',)

    jumlah_kritikal_qc = fields.Integer(string='Jumlah Kritikal',)
    jumlah_mayor_qc = fields.Integer(string='Jumlah Mayor',)
    jumlah_minor_qc = fields.Integer(string='Jumlah Minor',)

    product_qty_inline = fields.Float('Quantity To Produce',)
    product_qty_inline_1 = fields.Float('Quantity 1',)
    comment = fields.Text(string='Comment',store=True)
    partner_id = fields.Many2one('res.partner', string='Customer', )
