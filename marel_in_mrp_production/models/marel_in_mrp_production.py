from psycopg2 import OperationalError, Error

from flectra import api, fields, models, _
from flectra.exceptions import UserError, ValidationError
from flectra.osv import expression
from flectra.tools.float_utils import float_compare, float_is_zero

class MarelNamaOperator(models.Model):
    _description = u'Marel In Manufacturing Orders'
    _inherit = 'mrp.production'

    type_kk = fields.Selection(string=u'Type KK',related='product_tmpl_id.type_kk')