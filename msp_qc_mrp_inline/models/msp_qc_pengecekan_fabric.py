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

class MspQcPengecekanFabric(models.Model):
    _name ='msp.qc.pengecekan.fabric'
    # _name = 'msp.qc.inline4'

    def get_msp_qc_inline4_no(self):
        nama_baru = self.env['ir.sequence'].next_by_code('msp.qc.inline4.no')
        return nama_baru

    name = fields.Char(string='Id Inline 2',required=True,copy=False, default=get_msp_qc_inline4_no,readonly=True )
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,)
    style_no = fields.Char(string='Style No',)
    surat_jalan = fields.Char(string='Surat jalan',)
    lebar_kain_sesuai_tag = fields.Integer(string='Lebar kain sesuai tag',)
    panjang_kain_sesuai_tag = fields.Integer(string='Panjang kain sesuai tag',)
    aktual_lebar_kain_sesuai_tag = fields.Integer(string='Aktual lebar kain sesuai tag',required=True)
    aktual_panjang_kain_sesuai_tag = fields.Integer(string='Aktual panjang kain sesuai tag',required=True)
    keterangan = fields.Text(string='Keterangan',store=True,)
