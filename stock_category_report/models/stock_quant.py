from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError


class StockCategoryQuant(models.Model):
    _inherit = 'stock.quant'


    categ_id = fields.Many2one(string='Category', related='product_id.product_tmpl_id.categ_id', store=True)