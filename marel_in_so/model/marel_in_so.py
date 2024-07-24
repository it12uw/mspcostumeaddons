from datetime import datetime
from dateutil.relativedelta import relativedelta

from flectra import api, fields, models, SUPERUSER_ID, _
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from flectra.tools.float_utils import float_is_zero, float_compare
from flectra.exceptions import UserError, AccessError, ValidationError
from flectra.tools.misc import formatLang
from flectra.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP
from flectra.addons import decimal_precision as dp


class MarelInSaleOrderButton(models.Model):
    # _description = u'MarelInSaleOrderButton'
    _inherit = "sale.order"
    
    delivery_date = fields.Date(string=u'delivery date',required=True, default=fields.Date.context_today,)

    @api.multi
    def action_confirm_mm(self):
        self.write({'state': 'sent'}) 
        
class MarelInSaleOrderLine(models.Model):
    # _description = u'MarelInSaleOrderButton'
    _inherit = "sale.order.line"
    
    categ_id = fields.Many2one('product.category',string='Ketegori',related='product_id.categ_id',store=True)
    commitment_date = fields.Datetime(string='Commitment Date', related='order_id.commitment_date',store=True)
    requested_date = fields.Datetime(string='Requested Date', related='order_id.requested_date',store=True)
    

class SaleOrder(models.Model):
    # _description = u'MarelInSaleOrderButton'
    _inherit = "sale.order"
    
    date_order = fields.Datetime(string='Order Date', required=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
