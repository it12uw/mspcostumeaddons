# -*- coding: utf-8 -*-
# Part of Flectra. See LICENSE file for full copyright and licensing details.

import logging

from flectra import models, fields

_logger = logging.getLogger(__name__)

class SaleReport(models.Model):
    _inherit = 'sale.report'

    unit_cost = fields.Float('HPP', readonly=True)
    unit_price = fields.Float('Unit Price', readonly=True)
    discount = fields.Float('Discount', readonly=True)

    def _select(self):
        return super(SaleReport, self)._select() + ", ip.value_float as unit_cost, l.price_unit as unit_price, l.discount as discount"

    def _from(self):
        return super(SaleReport, self)._from() + "left join ir_property ip on ip.res_id='product.product,'||p.id"

    def _group_by(self):
        return super(SaleReport, self)._group_by() + ", ip.value_float, l.price_unit, l.discount"
