# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.

from flectra import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    days_between_two_followups = fields.Integer(related='company_id.days_between_two_followups', string='Minimum days between two follow-ups')
