# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from flectra import api, exceptions, fields, models, _
from flectra.exceptions import UserError
from flectra.addons import decimal_precision as dp


class StockMove(models.Model):
    _inherit = 'stock.move'

    bom_line_factor = fields.Float(string='Bom Unit', related='bom_line_id.product_qty', readonly=True)
    # bom_line_factor = fields.Float(string='Bom Unit', compute='_compute_bom_line', digits=dp.get_precision('BOM Unit of Measure'), readonly=True)

    # @api.depends('bom_line_id')
    # def _compute_bom_line (self):
    #     for move in self:
    #         bom_factor = self.env['mrp.bom.line'].search([('id','=',move.bom_line_id.id)])
    #         move.bom_line_factor = bom_factor.product_qty


class MRPBoMLine(models.Model):
    _inherit = 'mrp.bom.line'

    product_qty = fields.Float(
        'Product Quantity', default=1.0,
        digits=dp.get_precision('BOM Unit of Measure'), required=True)
