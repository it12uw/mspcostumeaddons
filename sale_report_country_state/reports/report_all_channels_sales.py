# Copyright 2020 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from flectra import fields, models


class ReportAllChannelsSales(models.Model):
    _inherit = "report.all.channels.sales"

    state_id = fields.Many2one(
        comodel_name="res.country.state",
        string="Partner's State",
        readonly=True,
    )
    city_id = fields.Char(
        string="Partner's City",
        readonly=True,
    )

    def _so(self):
        so_str = super()._so()
        so_str = so_str.replace(
            "rp.country_id AS country_id,",
            """rp.country_id AS country_id,
               rp.state_id AS state_id,
               rp.city AS city_id,
            """, 1)
        return so_str

    def get_main_request(self):
        request_str = super().get_main_request()
        request_str = request_str.replace(
            "country_id,",
            """country_id,
               state_id,
               city_id,
            """, 1)
        return request_str

    def _pos(self):
        pos_str = super()._pos()
        pos_str = pos_str.replace(
            "rp.country_id AS country_id,",
            """rp.country_id AS country_id,
               rp.state_id AS state_id,
               rp.city AS city_id,
            """, 1)
        return pos_str
