from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from flectra.addons import decimal_precision as dp

class SaleOrder(models.Model):
    _inherit = "sale.order"

# Ttd akuntan pk Wahyu
    @api.model
    def _default_confirmed_id_1(self):
        return self.env['res.users'].search([('id', '=',11)],limit=1)

    is_supervised = fields.Boolean(string='Supervised')
    supervise_uid = fields.Many2one('res.users', 'Supervise',default=_default_confirmed_id_1)
    is_approved = fields.Boolean(string='Approved')
    approval_uid = fields.Many2one('res.users', 'Approval')
    is_created = fields.Boolean(string='Created')
    created_uid = fields.Many2one('res.users', 'Created')


    @api.multi
    def _approval_action(self):
        if is_approved != 'True':
            is_approved = 'True'
            approval_uid = lambda self: self.env.uid

    @api.multi
    def _supervise_action(self):
        if is_supervised != 'True':
            is_supervised = 'True'
            supervise_uid = lambda self: self.env.uid

    @api.multi
    def _created_action(self):
        if is_created != 'True':
            is_created = 'True'
            created_uid = lambda self: self.env.uid

# Ttd akuntan Bu Wati
    # @api.model
    # def _default_akuntan_id(self):
    #     return self.env['res.users'].search([('id', '=',7)],limit=1)
    
    # akuntan_id = fields.Many2one('res.users',string='Akuntan',default=_default_akuntan_id)


# Ttd akuntan pk Tg
    @api.model
    def _default_confirmed_id_2(self):
        return self.env['res.users'].search([('id', '=',9)],limit=1)

    is_supervised_2 = fields.Boolean(string='Supervised')
    supervise_uid_2 = fields.Many2one('res.users', 'Supervise',default=_default_confirmed_id_2)


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_supervised = fields.Boolean(string='Supervised')
    supervise_uid = fields.Many2one('res.users', 'Supervise')
    is_approved = fields.Boolean(string='Approved')
    approval_uid = fields.Many2one('res.users', 'Approval')


    # @api.multi
    # def _approval_action(self):
    #     if is_approved != 'True':
    #         is_approved = 'True'
    #         approval_uid = lambda self: self.env.uid

    def button_approval_uid(self):
        self.write({'is_approved':True,
                    'approval_uid':self.env.user.id,})
        self.supervise_uid = self.create_uid
        self.button_confirm()
        return True
        

    @api.multi
    def _supervise_action(self):
        if is_supervised != 'True':
            is_supervised = 'True'
            supervise_uid = lambda self: self.env.uid

class StockPicking(models.Model):
    _inherit = "stock.picking"

    is_supervised = fields.Boolean(string='Adminitrasi')
    supervise_uid = fields.Many2one('res.users', 'Adminitrasi')
    is_approved = fields.Boolean(string='Pimpinan')
    approval_uid = fields.Many2one('res.users', 'Pimpinan')
    is_created = fields.Boolean(string='Penulis')
    created_uid = fields.Many2one('res.users', 'Penulis')


    @api.multi
    def _approval_action(self):
        if is_approved != 'True':
            is_approved = 'True'
            approval_uid = lambda self: self.env.uid

    @api.multi
    def _supervise_action(self):
        if is_supervised != 'True':
            is_supervised = 'True'
            supervise_uid = lambda self: self.env.uid

    @api.multi
    def _created_action(self):
        if is_created != 'True':
            is_created = 'True'
            created_uid = lambda self: self.env.uid


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

# Ttd akuntan Bu Wati
    @api.model
    def _default_akuntan_id(self):
        return self.env['res.users'].search([('id', '=',7)],limit=1)
    
    akuntan_id = fields.Many2one('res.users',string='Akuntan',default=_default_akuntan_id)
