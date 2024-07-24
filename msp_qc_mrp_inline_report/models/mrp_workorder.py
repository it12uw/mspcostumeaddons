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

class MspWorkOrder1(models.Model):
    _inherit = ['mrp.workorder']
    
    status_button_1 = fields.Boolean(string='Status Button 20%',store=True,default=False,)
    status_button_2 = fields.Boolean(string='Status Button 50%',store=True,default=False,)
    status_button_3 = fields.Boolean(string='Status Button 90%',store=True,default=False,)
    
    # hidden button inline
    @api.multi
    def action_telah_diinline1(self):
        self.write({'status_button_1' : 'yes',})

    @api.multi
    def action_nilai_inline_1_qc(self):
        self.action_telah_diinline1()
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qc.inline1.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
            }

    # ------------------------------------ inline 50 -----------------------------------
    @api.multi
    def action_telah_diinline2(self):
        self.write({'status_button_2' : 'yes',})

    @api.multi
    def action_nilai_inline_2_qc(self):
        self.action_telah_diinline2()
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qc.inline2.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
            }
    # ------------------------------------ inline 90 -----------------------------------
    @api.multi
    def action_telah_diinline3(self):
        self.write({'status_button_3' : 'yes',})

    @api.multi
    def action_nilai_inline_3_qc(self):
        self.action_telah_diinline3()
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qc.inline3.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
            }