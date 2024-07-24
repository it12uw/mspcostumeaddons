# Copyright 2019 Marcelo Frare (Ass. PNLUG - Gruppo Flectra <http://flectra.pnlug.it>)
# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Flectra <http://flectra.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from flectra import fields, models


class MgmtsystemMgmProduct(models.Model):
    """
    Extend nonconformity adding fields for product
    """

    _inherit = ['mgmtsystem.nonconformity']

    # new fields
    # product reference
    product_id = fields.Many2one('product.product', 'Product')
