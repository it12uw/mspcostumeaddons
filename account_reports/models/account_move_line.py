# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.

from flectra import api, fields, models, _


class AccountMoveLine(models.Model):
    _name = "account.move.line"
    _inherit = "account.move.line"

    expected_pay_date = fields.Date('Expected Payment Date', help="Expected payment date as manually set through the customer statement (e.g: if you had the customer on the phone and want to remember the date he promised he would pay)")
    internal_note = fields.Text('Internal Note', help="Note you can set through the customer statement about a receivable journal item")
    next_action_date = fields.Date('Next Action Date', help="Date where the next action should be taken for a receivable item. Usually, automatically set when sending reminders through the customer statement.")

    @api.multi
    def write_blocked(self, blocked):
        """ This function is used to change the 'blocked' status of an aml.
            You need to be able to change it even if the aml is locked by the lock date
            (this function is used in the customer statements) """
        return self.with_context(check_move_validity=False).write({'blocked': blocked})

    def get_action_context(self):
        if self.invoice_id:
            return {
                'default_type': self.invoice_id.type,
                'default_journal_id': self.invoice_id.journal_id.id,
            }
        return {}
