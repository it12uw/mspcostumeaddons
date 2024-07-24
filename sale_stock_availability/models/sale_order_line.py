##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from flectra import fields, models, api, _
from flectra.exceptions import Warning, UserError, ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    virtual_available = fields.Float(
        compute="_compute_virtual_available",
        string='Saldo Stock',
    )

    @api.depends(
        'product_id',
        'product_uom_qty',
        'product_uom')
    def _compute_virtual_available(self):
        for rec in self.filtered(
                lambda sol: sol.order_id.state in ['draft', 'sent']):
            product_uom = rec.product_id.uom_id
            virtual_available = rec.product_id.with_context(warehouse=rec.order_id.warehouse_id.id).qty_available_not_res
            if product_uom != rec.product_uom:
                virtual_available = product_uom._compute_quantity(virtual_available, rec.product_uom)
            rec.virtual_available = virtual_available - rec.product_uom_qty

    
    def create(self, values):
        line = super(SaleOrderLine, self).create(values)
        if line.virtual_available <= -1 and line.product_id.type == 'product' and not line.route_id:
            raise ValidationError(_("No Stock Check Available Stock in Warehouse"))
        return line
    
