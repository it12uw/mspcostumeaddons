from flectra import models, fields, api, _
from flectra.addons import decimal_precision as dp
from flectra.exceptions import UserError, ValidationError

class Product(models.Model):
    _inherit = 'product.product'

    qty_saleable = fields.Float(
        'Quantity Saleable', compute='_compute_saleable',
        digits=dp.get_precision('Product Unit of Measure'))

    def _compute_saleable(self):
        quantity = 0.0
        reserved = 0.0
        quant = self.env['stock.quant'].search([('product_id','in',[self.id]),('location_id','=',12)])
        for line in quant:
            quantity += line.quantity
            reserved += line.reserved_quantity
        self.qty_saleable = quantity - reserved


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    qty_saleable = fields.Float(
        'Quantity Saleable', compute='_compute_saleable',
        digits=dp.get_precision('Product Unit of Measure'))

    def _compute_saleable(self):
        for templates in self:
            product = self.env['product.product'].search([('product_tmpl_id','in',[templates.id])])
            quantity = 0.0
            reserved = 0.0
            for procode in product:
                quant = self.env['stock.quant'].search([('product_id','in',[procode.id]),('location_id','=',12)])
                for line in quant:
                    quantity += line.quantity
                    reserved += line.reserved_quantity
                templates.qty_saleable = quantity - reserved