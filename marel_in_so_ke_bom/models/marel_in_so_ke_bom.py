from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

class MarelBomDiSo(models.Model):
    _inherit = 'sale.order.line'
    
    bom_count = fields.Integer(string='BOM',related='product_id.bom_count',) #related='product_id.product_tmpl_id.bom_count',