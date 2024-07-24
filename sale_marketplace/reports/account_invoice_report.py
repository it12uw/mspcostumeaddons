# Copyright 2018 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from flectra import api, fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    market_place_id = fields.Many2one(comodel_name="market.place", string="Market")

    

    def _select(self):
        return super(AccountInvoiceReport, self)._select() + ", sub.market_place_id"
    
    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select() + ", ai.invoice_marketplace as market_place_id"

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + ", ai.invoice_marketplace"
