from flectra import _, api, fields, models
from flectra.exceptions import ValidationError


class StockLocation(models.Model):
    _inherit = "stock.location"


    is_wip = fields.Boolean (string='Is WIP', default=False)
    is_stock = fields.Boolean (string='Is Stock', default=False)


class StockPicking(models.Model):
    _inherit = "stock.picking"


    is_pinjam = fields.Boolean (string='Pinjam', default=False)
    is_makloon = fields.Boolean (string='Makloon', default=False)


class StockMove(models.Model):
    _inherit = "stock.move"


    is_pinjam = fields.Boolean (related='picking_id.is_pinjam', string='Pinjam')

    # @api.model
    # def compute_is_pinjam(self):
    #     for pinjam in self:
    #         pinjam.is_pinjam = pinjam.picking_id.is_pinjam if pinjam.picking_id.is_pinjam = True else False

class PickingType(models.Model):
    _inherit = "stock.picking.type"

    is_stock = fields.Boolean (string='Is Stock', default=False)
