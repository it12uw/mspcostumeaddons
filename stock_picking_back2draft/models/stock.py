# © 2016 Lorenzo Battistini - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from flectra import models, api, fields, _
from flectra.exceptions import UserError



class StockMove(models.Model):
    _inherit = 'stock.move'

    
    purchase_line_id = fields.Many2one('purchase.order.line',
        'Purchase Order Line', ondelete='set null', index=True, readonly=False)

    @api.multi
    def action_back_to_draft(self):
        if self.filtered(lambda m: m.state != 'cancel'):
            raise UserError(_("You can set to draft cancelled moves only"))
        self.write({'state': 'draft'})


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    purchase_id = fields.Many2one('purchase.order', related='move_lines.purchase_line_id.order_id',
        string="Purchase Orders", readonly=False)
    location_id = fields.Many2one(
        'stock.location', "Source Location",
        default=lambda self: self.env['stock.picking.type'].browse(self._context.get('default_picking_type_id')).default_location_src_id,
        readonly=False, required=True,
        states={})
    location_dest_id = fields.Many2one(
        'stock.location', "Destination Location",
        default=lambda self: self.env['stock.picking.type'].browse(self._context.get('default_picking_type_id')).default_location_dest_id,
        readonly=False, required=True,
        states={})

    @api.multi
    def action_back_to_draft(self):
        moves = self.mapped('move_lines')
        moves.action_back_to_draft()
