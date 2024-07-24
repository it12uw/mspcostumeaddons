from datetime import datetime
from dateutil.relativedelta import relativedelta

from flectra import api, fields, models, SUPERUSER_ID, _
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from flectra.tools.float_utils import float_is_zero, float_compare
from flectra.exceptions import UserError, AccessError, ValidationError
from flectra.tools.misc import formatLang
from flectra.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP
from flectra.addons import decimal_precision as dp
from flectra.tools import float_round

class MspStockPicking(models.Model):
    _inherit = ['stock.picking']
    
    purchase_id2 = fields.Many2one('purchase.order', 'No PO',store=True)
    
class MarelInStockPickingPo(models.Model):
    _inherit = ['purchase.order']
    
    picking_ids2 = fields.One2many('stock.picking','purchase_id2',string='NO Picking',)
    