# Part of Flectra See LICENSE file for full copyright and licensing details.

from flectra import api, fields, models, _
from flectra.tools.misc import formatLang
from flectra.exceptions import Warning


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    @api.depends('order_line')
    def _get_total_cost(self):
        for order_id in self:
            order_id.total_cost = sum(
                [order_id.pricelist_id.currency_id.round(line_id.purchase_price) for line_id in order_id.order_line])
    @api.multi
    @api.depends('order_line')
    def _get_margin(self):
        for order_id in self:
            order_id.margin_sale =(order_id.amount_total-order_id.total_cost)

    total_cost = fields.Float(string="Total Cost",
                                compute='_get_total_cost', store=True)

    margin_sale = fields.Float(string="Margin/Untung",
                                compute='_get_margin', store=True)