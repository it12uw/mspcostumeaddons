# Copyright 2015 Anybox S.A.S
# Copyright 2016-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from flectra import fields, models
from flectra.addons import decimal_precision as dp


class ProductSetLine(models.Model):
    _name = 'product.set.line'
    _description = 'Product set line'
    _rec_name = 'product_id'
    _order = 'sequence'

    product_id = fields.Many2one(
        comodel_name='product.product',
        domain=[('sale_ok', '=', True)],
        string='Product',
        required=True
    )
    quantity = fields.Float(
        string='Quantity',
        digits=dp.get_precision('Product Unit of Measure'),
        required=True,
        default=1
    )
    product_set_id = fields.Many2one(
        'product.set',
        string='Set',
        ondelete='cascade',
    )
    sequence = fields.Integer(
        string='Sequence',
        required=True,
        default=0,
    )
