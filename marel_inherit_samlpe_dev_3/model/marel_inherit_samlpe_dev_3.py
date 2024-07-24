from flectra.addons import decimal_precision as dp
from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime
# from dateutil.relativedelta import relativedelta
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from flectra.tools import float_round

class MarelInherit3OperatorMengisi(models.Model):
    
    _inherit = 'operator.marelinsamlpe.dev2.list'
    
    tgl_buat_operator = fields.Date(string='Tgl Buat Operator',)
    feed_4c = fields.Char(string='Feed 4C',)