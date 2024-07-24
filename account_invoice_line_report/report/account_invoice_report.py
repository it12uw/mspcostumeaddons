# Copyright 2018 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from flectra import api, fields, models, _


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    no_invoice = fields.Char('Invoice', readonly=True)
    origin = fields.Char('Origin', readonly=True)

    @api.model
    def _select(self):
        select_str = super(AccountInvoiceReport, self)._select()
        select_str += ", sub.no_invoice, sub.origin"
        return select_str

    @api.model
    def _sub_select(self):
        select_str = super(AccountInvoiceReport, self)._sub_select()
        select_str += ", ai.number as no_invoice, ai.origin as origin"
        return select_str

    @api.model
    def _group_by(self):
        group_by_str = super(AccountInvoiceReport, self)._group_by()
        group_by_str += ", ai.number, ai.origin"
        return group_by_str