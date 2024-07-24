from flectra import api, fields, models, _
from num2words import num2words


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    is_approved = fields.Boolean(string='Approved')
    approval_uid = fields.Many2one('res.users', 'Approval')
   
    @api.multi
    def numtoword_s(self, amount_total):
        return (num2words(amount_total, lang='id')).title()+" rupiah"

    @api.multi
    def _approval_action(self):
        if is_approved != 'True':
            is_approved = 'True'
            approval_uid = lambda self: self.env.uid