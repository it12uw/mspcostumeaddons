from flectra.addons import decimal_precision as dp
from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime
# from dateutil.relativedelta import relativedelta
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from flectra.tools import float_round

class MarelInheritSamlpeDev2(models.Model):
    # _name = 'marel.inherit.samlpe.dev2'
    _inherit = 'marelin.samlpe.dev2'
    
    kode_dokumen = fields.Char(string=u'Kode Doc',)
    penjerat_2 = fields.Many2one('product.product',string=u'Penjerat 2',)
    patter_6 = fields.Many2one('product.product',string=u'Pattern 6',)
    patter_7 = fields.Many2one('product.product',string=u'Pattern 7',)
    patter_8 = fields.Many2one('product.product',string=u'Pattern 8',)
    patter_9 = fields.Many2one('product.product',string=u'Pattern 9',)
    patter_10 = fields.Many2one('product.product',string=u'Pattern 10',)