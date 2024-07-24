from datetime import datetime
from dateutil.relativedelta import relativedelta

from flectra import api, fields, models, SUPERUSER_ID, _
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from flectra.tools.float_utils import float_is_zero, float_compare
from flectra.exceptions import UserError, AccessError, ValidationError
from flectra.tools.misc import formatLang
from flectra.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP
from flectra.addons import decimal_precision as dp

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # @api.multi
    # def action_confirm_po_admin(self):
    #     self.write({'state': 'sent'})
    
    confirm_price = fields.Boolean(string='Confirm Price',)
    is_confirm_price = fields.Boolean(string='Confirm Price')
    confirm_price_uid = fields.Many2one('res.users', 'Confirmed Price')
    
    def button_confirm_price_uid(self):
        self.write({'is_confirm_price':True,
                    'confirm_price_uid':self.env.user.id,})
        return True