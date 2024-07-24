# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

import re

from flectra import api, fields, models, tools, _
from flectra.exceptions import ValidationError
from flectra.osv import expression

from flectra.addons import decimal_precision as dp

from flectra.tools import float_compare, pycompat


class InheritProductProductSample(models.Model):
    _inherit = "product.product"

    jarum = fields.Integer(string='Jarum')
    stich = fields.Integer(string="Stich", store=True)
    time_bordir = fields.Integer(compute="hitung_waktu_standart_stich",string='Waktu Rumus/Menit',store=True) 


    @api.depends()
    def hitung_waktu_standart_stich(self):
        for w in self:
            if w.stich > 1:
                w.time_bordir = w.stich / (25000/60)
            else:
                w.time_bordir = 0