from flectra import api, fields, models, _
from flectra.exceptions import UserError
from flectra.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class MarketPlace(models.Model):
    _name = "market.place"
    _description = "Market Place"

    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Reference')
    no_account = fields.Char(string='No Account')
    renewal = fields.Date(string='Tgl Renewal')
    warehouse_id = fields.Many2one('stock.warehouse', string='Warehouse')
