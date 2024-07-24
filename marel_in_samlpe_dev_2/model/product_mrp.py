# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
import math

from flectra import api, fields, models, _
from flectra.addons import decimal_precision as dp
from flectra.exceptions import AccessError, UserError
from flectra.tools import float_compare

class InheritMrpProduction(models.Model):
    _inherit = 'mrp.production'

    # @api.depends('product_id')
    # def data_bordir(self):
    #     import pdb; pdb.set_trace()
    #     bordir = self.env['sample.bordir'].search([('nama_produk','=',self.product_id.id)], limit = 1)
    #     bo = bordir.mapped('product_id')
    #     for b in bo:
    #         if b.id == self.product_id.id:
    #             self.stich = bo.stich
    

    stich = fields.Integer(related="product_id.stich",string="stich", store=True)