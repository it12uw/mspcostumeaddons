# Copyright 2016 Akretion (http://www.akretion.com/)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from flectra import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    payment_mode_id = fields.Many2one(
        'account.payment.mode',
        string='Payment Mode',
        domain="[('company_id', '=', company_id),('branch_id', '=', branch_id)]",
        ondelete='restrict',
        index=True,
    )
