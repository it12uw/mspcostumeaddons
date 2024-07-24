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

class MspQcIEndlineGarment(models.Model):
    _name= "msp.qc.endline.garment"
    # _name = 'msp.qc.inlinefinishing'
    # _rec_name = 'nama_operator_id'


    def get_msp_qc_inline_garment_no(self):
        nama_baru = self.env['ir.sequence'].next_by_code('msp.qc.endline.garment.no')
        return nama_baru

    name = fields.Char(string='Id Endline Garment',required=True,copy=False, default=get_msp_qc_inline_garment_no,readonly=True )
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,store=True,)
    inspection_date = fields.Datetime(string='Data Inspection',store=True,)
    # msp_qc_inline1_line_ids = fields.One2many('msp.qc.inline1.line','msp_qc_inline1_id',string=u'Defect Found',)
    keterangan = fields.Text(string='Keterangan',store=True,)
    name_workorder_id = fields.Many2one('mrp.workorder', string=u'No WO',store=True,)
    mrp_productioin_id = fields.Many2one('mrp.production', string=u'No MO',store=True,)
    
    # drop down =======================================================
    # handfeel = fields.Selection([
    #     ('g',_('Good')),
    #     ('ng',_('Not Good')),
    #     ('na',_('Not Aplicable')),
    #     ], string="Handfeel",store=True,)
    # color = fields.Selection([
    #     ('g',_('Good')),
    #     ('ng',_('Not Good')),
    #     ('na',_('Not Aplicable')),
    #     ], string="Color",store=True,)
    # aksesoris_1 = fields.Selection([
    #     ('g',_('Good')),
    #     ('ng',_('Not Good')),
    #     ('na',_('Not Aplicable')),
    #     ], string="Benang",store=True,)

    # aksesoris_2 = fields.Selection([
    #     ('g',_('Good')),
    #     ('ng',_('Not Good')),
    #     ('na',_('Not Aplicable')),
    #     ], string="Bordir",store=True,)

    # aksesoris_3 = fields.Selection([
    #     ('g',_('Good')),
    #     ('ng',_('Not Good')),
    #     ('na',_('Not Aplicable')),
    #     ], string="Label",store=True,)
    
    # aksesoris_4 = fields.Selection([
    #     ('g',_('Good')),
    #     ('ng',_('Not Good')),
    #     ('na',_('Not Aplicable')),
    #     ], string="Hangtag",store=True,)
    
    # aksesoris_5 = fields.Selection([
    #     ('g',_('Good')),
    #     ('ng',_('Not Good')),
    #     ('na',_('Not Aplicable')),
    #     ], string="Barcode",store=True,)
    
    # inspection_result = fields.Selection([
    #     ('release',_('Release')),
    #     ('reject',_('Reject')),
    #     ('hold',_('Hold')),
    #     ('under_guarantee',_('Under Guarantee')),
    #     ], string="Inspection Result",store=True,)


    # sample_size_151_280 = fields.Integer(string='Sample Size (151-280)',default=32,readonly=True)
    # mayor_151_280 = fields.Integer(string='Mayor (151-280)',default=2,readonly=True)
    # minor_151_280 = fields.Integer(string='Minor (151-280)',default=3,readonly=True)

    # sample_size_281_500 = fields.Integer(string='Sample Size (281-500)',default=50,readonly=True)
    # mayor_281_500 = fields.Integer(string='Mayor (281-500)',default=3,readonly=True)
    # minor_281_500 = fields.Integer(string='Minor (281-500)',default=5,readonly=True)

    # sample_size_501_1200 = fields.Integer(string='Sample Size (501-1200)',default=80,readonly=True)
    # mayor_501_1200 = fields.Integer(string='Mayor (501-1200)',default=5,readonly=True)
    # minor_501_1200 = fields.Integer(string='Minor (501-1200)',default=7,readonly=True)
    
    # sample_size_1201_3200 = fields.Integer(string='Sample Size (1201-32000)',default=125,readonly=True)
    # mayor_1201_3200 = fields.Integer(string='Mayor (1201-32000)',default=7,readonly=True)
    # minor_1201_3200 = fields.Integer(string='Minor (1201-32000)',default=10,readonly=True)

    # sample_size_3201_10000 = fields.Integer(string='Sample Size (3201-10000)',default=200,readonly=True)
    # mayor_3201_10000 = fields.Integer(string='Mayor (3201-10000)',default=10,readonly=True)
    # minor_3201_10000 = fields.Integer(string='Minor (3201-10000)',default=14,readonly=True)

    # prodak = fields.Selection([
    #     ('sock',_('SOCK')),
    #     ('bordir',_('BORDIR')),
    #     ('garment',_('GARMENT')),
    #     ], string="Prodak",store=True,)


    rijek_1 = fields.Selection([
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
    
    rijek_9 = fields.Selection([
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
        ], string="Rijek 9",store=True,)
    
    rijek_10 = fields.Selection([
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
        ], string="Rijek 10",store=True,)


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

    bentuk_rijek_9 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_9 = fields.Integer(string='Nilai 9',)

    bentuk_rijek_10 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_10 = fields.Integer(string='Nilai 10',)


    sugestion_1 = fields.Char(string='Sugestion 1',)
    sugestion_2 = fields.Char(string='Sugestion 2',)
    sugestion_3 = fields.Char(string='Sugestion 3',)
    sugestion_4 = fields.Char(string='Sugestion 4',)
    sugestion_5 = fields.Char(string='Sugestion 5',)
    sugestion_6 = fields.Char(string='Sugestion 6',)
    sugestion_7 = fields.Char(string='Sugestion 7',)
    sugestion_8 = fields.Char(string='Sugestion 8',)
    sugestion_9 = fields.Char(string='Sugestion 8',)
    sugestion_10 = fields.Char(string='Sugestion 8',)

    keterangan_1 = fields.Char(string='keterangan 1',)
    keterangan_2 = fields.Char(string='keterangan 2',)
    keterangan_3 = fields.Char(string='keterangan 3',)
    keterangan_4 = fields.Char(string='keterangan 4',)
    keterangan_5 = fields.Char(string='keterangan 5',)
    keterangan_6 = fields.Char(string='keterangan 6',)
    keterangan_7 = fields.Char(string='keterangan 7',)
    keterangan_8 = fields.Char(string='keterangan 8',)
    keterangan_9 = fields.Char(string='keterangan 9',)
    keterangan_10 = fields.Char(string='keterangan 10',)


    jumlah_kritikal_qc = fields.Integer(string='Jumlah Kritikal',)
    jumlah_mayor_qc = fields.Integer(string='Jumlah Mayor',)
    jumlah_minor_qc = fields.Integer(string='Jumlah Minor',)

    product_qty_inline = fields.Float('Quantity To Produce',)
    product_qty_inline_1 = fields.Float('Quantity 1',)
    comment = fields.Text(string='Comment',store=True)
    partner_id = fields.Many2one('res.partner', string='Customer', )
    
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

