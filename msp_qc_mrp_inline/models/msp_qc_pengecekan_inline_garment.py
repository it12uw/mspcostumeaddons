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

class MspQcPengecekanInlineGarmen(models.Model):
    _name ='msp.qc.pengecekan.inlinegarmen'
    # _name ='msp.qc.pengecekan_inlinegarmen'

    def get_msp_qc_pengecekan_inlinegarmen_no(self):
        nama_baru = self.env['ir.sequence'].next_by_code('msp.qc.pengecekan.inlinegarmen.no')
        return nama_baru

    name = fields.Char(string='Id Inline 2',required=True,copy=False, default=get_msp_qc_pengecekan_inlinegarmen_no,readonly=True )
    tgl_create = fields.Datetime(string='Tanggal',default=fields.Datetime.now,readonly=True,)
    partner_id = fields.Many2one('res.partner','Partner',)
    style = fields.Char(string='Style',)
    description = fields.Char(string='Description',)
    defect_1  = fields.Char(string='Defect 1',)
    defect_2  = fields.Char(string='Defect 2',)
    defect_3  = fields.Char(string='Defect 3',)
    defect_4  = fields.Char(string='Defect 4',)
    defect_5  = fields.Char(string='Defect 5',)
    quantity_1  = fields.Integer(string='Quantity 1',)
    quantity_2  = fields.Integer(string='Quantity 2',)
    quantity_3  = fields.Integer(string='Quantity 3',)
    quantity_4  = fields.Integer(string='Quantity 4',)
    quantity_5  = fields.Integer(string='Quantity 5',)
    status_1 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Status", store=True,)
    status_2 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Status", store=True,)
    status_3 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Status", store=True,)
    status_4 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Status", store=True,)
    status_5 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Status", store=True,)