# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.

from flectra import fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    days_between_two_followups = fields.Integer(string='Number of days between two follow-ups', default=14)
