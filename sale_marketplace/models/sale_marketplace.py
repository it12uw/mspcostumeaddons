from flectra import api, fields, models, _
from flectra.exceptions import UserError
from flectra.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class SaleOrder(models.Model):
    _inherit = "sale.order"

    date_order = fields.Datetime(string='Order Date', required=True, readonly=False, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now, help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.")
    sale_marketplace = fields.Many2one ('market.place', 'Marketplace')
    # currency_rate = fields.Float("Currency Rate", compute='_compute_currency_rate', compute_sudo=True, store=True, digits=(12, 6), readonly=True, help='The rate of the currency to the currency of rate 1 applicable at the date of the order')

    # _sql_constraints = [
    #     ('customer_reference_unique_type', 'UNIQUE(client_order_ref)', 'This reference has been used.'),
    # ]

    @api.onchange('sale_marketplace')
    def _onchange_marketplace(self):
        if self.sale_marketplace:
            self.warehouse_id = self.sale_marketplace.warehouse_id.id
        else:
            company = self.env.user.company_id.id
            warehouse_ids = self.env['stock.warehouse'].search([('company_id', '=', company)], limit=1)
            self.warehouse_id = warehouse_ids

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['invoice_marketplace'] = self.sale_marketplace.id
        return invoice_vals

    # @api.depends('pricelist_id', 'date_order', 'company_id')
    # def _compute_currency_rate(self):
    #     for order in self:
    #         if not order.company_id:
    #             order.currency_rate = order.currency_id.with_context(date=order.date_order).rate or 1.0
    #             continue
    #         elif order.company_id.currency_id and order.currency_id:  # the following crashes if any one is undefined
    #             order.currency_rate = self.env['res.currency']._get_conversion_rate(order.company_id.currency_id, order.currency_id)
    #         else:
    #             order.currency_rate = 1.0


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    invoice_marketplace = fields.Many2one ('market.place', 'Marketplace')

    # @api.multi
    # def action_move_create(self):
    #     res = super(AccountInvoice, self).action_move_create
    #     move_vals = {
    #             'invoice_marketplace': inv.invoice_marketplace,
    #         }
    #     return res


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    invoice_marketplace = fields.Many2one ('market.place', string='Marketplace', related='invoice_id.invoice_marketplace', store=True)


class AccountMove(models.Model):
    _inherit = "account.move"

    invoice_marketplace = fields.Many2one ('market.place', 'Marketplace')


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    invoice_marketplace = fields.Many2one ('market.place', string='Marketplace', related='move_id.invoice_marketplace', store=True)


class SaleLine(models.Model):
    _inherit = "sale.order.line"

    analytic_account_id = fields.Many2one ('account.analytic.account', string='Analytic', related='order_id.analytic_account_id', store=True)