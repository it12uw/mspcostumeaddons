# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from flectra import api, fields, models, tools, _

class CurrencyDP(models.Model):
    _inherit = "res.currency"

    rate = fields.Float(compute='_compute_current_rate', string='Current Rate', digits=(18, 16),
                        help='The rate of the currency to the currency of rate 1.')
    rate_ids = fields.One2many('res.currency.rate', 'currency_id', string='Rates')
    rounding = fields.Float(string='Rounding Factor', digits=(18, 16), default=0.01)

class CurrencyRateDP(models.Model):
    _inherit = "res.currency.rate"

    rate = fields.Float(digits=(18,16), default=1.0, help='The rate of the currency to the currency of rate 1')
