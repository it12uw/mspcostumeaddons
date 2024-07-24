from datetime import datetime
from dateutil.relativedelta import relativedelta

from flectra import api, fields, models, SUPERUSER_ID, _
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from flectra.tools.float_utils import float_is_zero, float_compare
from flectra.exceptions import UserError, AccessError, ValidationError
from flectra.tools.misc import formatLang
from flectra.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP
from flectra.addons import decimal_precision as dp


class MarelIAaccountInvoice(models.Model):
    _inherit = "account.invoice"
    
    receive_date  = fields.Date(string=u'Receive Date',)
    reference = fields.Char(string='Vendor Reference', copy=False, help="The partner reference of this invoice.", readonly=True, states={'draft': [('readonly', False)],'open':[('readonly',False)]})