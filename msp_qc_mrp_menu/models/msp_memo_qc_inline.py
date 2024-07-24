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


class MspMemoQcInline(models.Model):
    _name = 'msp.memo.qc.inline'
    # _rec_name = 'nama_operator_id'
    # _inherit = 'mrp.workorder'

    def get_msp_memo_qc_inline_no(self):
        nama_baru = self.env['ir.sequence'].next_by_code('msp.memo.qc.inline.no')
        return nama_baru
    
    name = fields.Char(string='Id Memo',required=True,copy=False, default=get_msp_memo_qc_inline_no,readonly=True )
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,)
    shift = fields.Selection([
        ('A',_('A')),
        ('B',_('B')),
	    ('C',_('C')),], string="Shift",)
    
    line = fields.Char(string='Line',)
    nama_operator_id = fields.Many2one('marel.nama.operator',string=u'Nama Operator',)
    nama_teknisi_id = fields.Many2one('nama.teknisi',string=u'Nama Teknisi',)
    mrp_productioin_id = fields.Many2one('mrp.production', string=u'No MO',)
    keterangan = fields.Text(string='Keterangan',store=True,)
    # state = fields.Selection([
    #     ('draft', 'Open'),
    #     ('done','Done'),
    #     ('cancel','Canceled')
    #     ],string="Status", readonly=True, copy=False, default='draft')

    # @api.multi
    # def action_nilai_inline_qc(self):
    #     return {
    #             'name': 'Nilai Inline Qc',
    #             'view_type': 'form',
    #             'view_mode': 'form',
    #             'target': 'new',
    #             'res_model': 'msp.memoqc.inline.wizard',
    #             'type': 'ir.actions.act_window',
    #             'context':{},
    #         }