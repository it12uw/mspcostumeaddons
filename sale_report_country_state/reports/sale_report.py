# Copyright 2020 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from flectra import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    state_id = fields.Many2one(
        comodel_name="res.country.state",
        string="Partner's State",
        readonly=True,
    )
    city_id = fields.Char(
        string="Partner's City",
        readonly=True,
    )
    street= fields.Char(string="Street",readonly=True,)
    street2= fields.Char(string="Street2",readonly=True,)
    mobile= fields.Char(string="Mobile",readonly=True,)
    phone= fields.Char(string="Phone",readonly=True,)

    def _select(self):
        select_str = super()._select()
        select_str += """,
            partner.state_id as state_id,
            partner.city as city_id,
            partner.street as street,
            partner.street2 as street2,
            partner.mobile as mobile,
            partner.phone as phone
        """
        return select_str

    def _group_by(self):
        group_by_str = super()._group_by()
        group_by_str += """,
            partner.state_id,
            partner.city,
            partner.street,
            partner.street2,
            partner.mobile,
            partner.phone
        """
        return group_by_str
