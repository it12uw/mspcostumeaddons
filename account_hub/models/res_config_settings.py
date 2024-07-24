# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.

from flectra import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_account_reports = fields.Boolean("Dynamic Reports")
    module_account_reports_followup = fields.Boolean("Follow-up Levels")