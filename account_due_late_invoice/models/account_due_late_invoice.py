from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from flectra.addons import decimal_precision as dp
from datetime import datetime


class AccountDueLateInvoice (models.Model):
    _inherit = 'account.invoice'

    pay_date = fields.Date('Tgl Payment Real', compute="get_last_payment")
    # days = fields.Integer(related='payment_term_id.line_ids.days', string='Term Days')
    days = fields.Integer(related='real_term.line_ids.days', string='Term Days')
    due_late = fields.Integer('Late Payment', compute="_compute_days_duelate", group_operator='avg', store=True)
    date_due2 = fields.Date(string='Tgl Real Term')
    real_term = fields.Many2one(related='partner_id.real_term', string='Term Bay', store=True)
    date_doc = fields.Date(string='Doc Date')
    
    def get_last_payment(self):
        for invoice in self:
            payments_ids = self.env['account.payment'].search([('invoice_ids', '=', invoice.id), ('state', '=', 'posted')])
            expected_ids = self.env['account.move.line'].search([('invoice_id', '=', invoice.id),('account_id', 'in', (7,13))])
            payment = payments_ids and max(payments_ids)
            expected = expected_ids and max(expected_ids)
            if payment:
                invoice.pay_date = payment.payment_date
            elif expected:
                invoice.pay_date = expected.expected_pay_date
        
    @api.onchange ('pay_date')
    def _compute_days_duelate(self):
        for line in self:
            if line.pay_date is None:
                pay_date = fields.Date.from_string(
                    line.pay_date)
                #reference ke term bayangan di partner_id
                # date_due = fields.Date.from_string(
                #     line.date_due)
                # due_late = (pay_date - date_due).days
                # line.due_late = due_late
                date_due2 = fields.Date.from_string(
                    line.date_due2)
                due_late = (pay_date - date_due2).days
                line.due_late = due_late

    @api.onchange('real_term', 'date_doc')
    def _onchange_payment_term_real_term(self):
        date_doc = self.date_doc
        if not date_doc:
            date_doc = fields.Date.context_today(self)
        if self.real_term:
            rterm = self.real_term
            rterm_list = rterm.with_context(currency_id=self.company_id.currency_id.id).compute(value=1, date_ref=date_doc)[0]
            self.date_due2 = max(line[0] for line in rterm_list)
            self.date_due = max(line[0] for line in rterm_list)
        elif self.date_due2 and (date_doc > self.date_due2):
            self.date_due2 = date_doc
            self.date_due = date_doc

class AccountDueLateInvoice (models.Model):
    _inherit = 'res.partner'

    real_term = fields.Many2one('account.payment.term', string='Payment Real Terms')
    