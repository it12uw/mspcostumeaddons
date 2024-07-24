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

class MspWorkOrder(models.Model):
    _inherit = ['mrp.workorder']

    @api.multi
    def action_nilai_inline_qc(self):
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.memoqc.inline.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
            }
    
    
    total_yg_persen_selesai = fields.Float(string='Ttl Selesai (%)',compute='_get_total_yg_persen_selesai',store=True)
    # total_yg_persen_selesai = fields.Float(string='Total Selesai (%)',store=True)
    # TABAHAN TGL 6/6/20
    @api.one
    @api.depends('qty_produced','qty_production')
    def _get_total_yg_persen_selesai(self):
        if self.qty_production:
            self.total_yg_persen_selesai = ((self.qty_produced/self.qty_production)*100)
        else:
            self.total_yg_persen_selesai = 0