from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

class MarelInMrpProduction(models.Model):
    _inherit = 'mrp.production'

    kkp_div = fields.Integer(string='KKP Div', default=1)

