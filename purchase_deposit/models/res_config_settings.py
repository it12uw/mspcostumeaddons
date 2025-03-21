# Copyright 2019 Elico Corp, Dominique K. <dominique.k@elico-corp.com.sg>
# Copyright 2019 Ecosoft Co., Ltd., Kitti U. <kittiu@ecosoft.co.th>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from flectra import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    default_purchase_deposit_product_id = fields.Many2one(
        comodel_name='product.product',
        string='Purchase Deposit Product',
        default_model='purchase.advance.payment.inv',
        domain=[('type', '=', 'service')],
        help="Default product used for payment advances.",
    )
