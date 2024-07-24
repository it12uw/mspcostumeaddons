# -*- coding: utf-8 -*-
# Copyright 2018 Raphael Reverdy https://akretion.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import datetime
from dateutil import relativedelta
from itertools import groupby
from operator import itemgetter

from flectra import api, fields, models, _
from flectra.addons import decimal_precision as dp
from flectra.exceptions import UserError
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from flectra.tools.float_utils import float_compare, float_round, float_is_zero


class StockMove(models.Model):
    _inherit = 'mrp.production'

        # TABAHAN TGL 3/6/20
    mrp_total_putus_benang = fields.Integer(string=u'Total Pts Benang',compute='_get_jumlah_yg_selesai_total_putus_benang',store=True)
    mrp_total_bolong = fields.Integer(string=u'Total BOLONG / SOBEK',compute='_get_jumlah_yg_selesai_total_bolong',store=True)
    mrp_total_vanise = fields.Integer(string=u'Total VANISE',compute='_get_jumlah_yg_selesai_total_vanise',store=True)
    mrp_total_singker = fields.Integer(string=u' SINGKER/ LIDAH SERET',compute='_get_jumlah_yg_selesai_total_singker',store=True)
    mrp_total_kotor = fields.Integer(string=u'Total KOTOR',compute='_get_jumlah_yg_selesai_total_kotor',store=True)
    mrp_total_terry = fields.Integer(string=u'Total TERRY',compute='_get_jumlah_yg_selesai_total_terry',store=True)
    mrp_total_jumpstich = fields.Integer(string=u'Total JUMPSTICH',compute='_get_jumlah_yg_selesai_total_jumpstich',store=True)
    mrp_total_renggang = fields.Integer(string=u'Total RENGGANG',compute='_get_jumlah_yg_selesai_total_renggang',store=True)
    mrp_total_tidak_loading = fields.Integer(string=u'Total TIDAK LOADING',compute='_get_jumlah_yg_selesai_total_tidak_loading',store=True)
    mrp_total_belang = fields.Integer(string=u'Total BELANG',compute='_get_jumlah_yg_selesai_total_belang',store=True)
    mrp_total_ukuran = fields.Integer(string=u'Total UKURAN',compute='_get_jumlah_yg_selesai_total_ukuran',store=True)

    mrp_total_lingtu = fields.Integer(string=u'Total LINGTU',compute='_get_jumlah_yg_selesai_total_lingtu',store=True)
    mrp_total_pecah = fields.Integer(string=u'Total PECAH',compute='_get_jumlah_yg_selesai_total_pecah',store=True)
    mrp_total_loncat = fields.Integer(string=u'Total LONCAT',compute='_get_jumlah_yg_selesai_total_loncat',store=True)
    mrp_total_transfer = fields.Integer(string=u'Total TRANSFER NYANGKOL',compute='_get_jumlah_yg_selesai_total_transfer',store=True)
    mrp_total_gumpal = fields.Integer(string=u'Total GUMPAL',compute='_get_jumlah_yg_selesai_total_gumpal',store=True,)
    mrp_total_kasar = fields.Integer(string=u'Total KASAR',compute='_get_jumlah_yg_selesai_total_kasar',store=True)
    mrp_total_benang_gabung = fields.Integer(string=u'Total BENANG GABUNG',compute='_get_jumlah_yg_selesai_total_benang_gabung',store=True)
    mrp_total_bintik_bintik = fields.Integer(string=u'Total BINTIK BINTIK',compute='_get_jumlah_yg_selesai_total_bintik_bintik', store=True)
    mrp_total_jarum = fields.Integer(string=u'Total Jarum',compute='_get_jumlah_yg_selesai_total_jarum',store=True)
    mrp_total_transfer_jebol = fields.Integer(string=u'Total TRANSFER Jebol',compute='_get_jumlah_yg_selesai_total_transfer_jebol',store=True)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_putus_benang(self):
        for production_id in self:
            production_id.mrp_total_putus_benang = sum((line_id.total_putus_benang) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_bolong(self):
        for production_id in self:
            production_id.mrp_total_bolong = sum((line_id.total_bolong) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_vanise(self):
        for production_id in self:
            production_id.mrp_total_vanise = sum((line_id.total_vanise) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_singker(self):
        for production_id in self:
            production_id.mrp_total_singker = sum((line_id.total_singker) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_kotor(self):
        for production_id in self:
            production_id.mrp_total_kotor = sum((line_id.total_kotor) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_terry(self):
        for production_id in self:
            production_id.mrp_total_terry = sum((line_id.total_terry) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_jumpstich(self):
        for production_id in self:
            production_id.mrp_total_jumpstich = sum((line_id.total_jumpstich) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_renggang(self):
        for production_id in self:
            production_id.mrp_total_renggang = sum((line_id.total_renggang) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_tidak_loading(self):
        for production_id in self:
            production_id.mrp_total_tidak_loading = sum((line_id.total_tidak_loading) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_belang(self):
        for production_id in self:
            production_id.mrp_total_belang = sum((line_id.total_belang) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_ukuran(self):
        for production_id in self:
            production_id.mrp_total_ukuran = sum((line_id.total_ukuran) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_lingtu(self):
        for production_id in self:
            production_id.mrp_total_lingtu = sum((line_id.total_lingtu) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_pecah(self):
        for production_id in self:
            production_id.mrp_total_pecah = sum((line_id.total_pecah) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_loncat(self):
        for production_id in self:
            production_id.mrp_total_loncat = sum((line_id.total_loncat) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_transfer(self):
        for production_id in self:
            production_id.mrp_total_transfer = sum((line_id.total_transfer) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_gumpal(self):
        for production_id in self:
            production_id.mrp_total_gumpal = sum((line_id.total_gumpal) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_kasar(self):
        for production_id in self:
            production_id.mrp_total_kasar = sum((line_id.total_kasar) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_benang_gabung(self):
        for production_id in self:
            production_id.mrp_total_benang_gabung = sum((line_id.total_benang_gabung) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_bintik_bintik(self):
        for production_id in self:
            production_id.mrp_total_bintik_bintik = sum((line_id.total_bintik_bintik) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_jarum(self):
        for production_id in self:
            production_id.mrp_total_jarum = sum((line_id.total_jarum) for line_id in production_id.workorder_ids)

    # TABAHAN TGL 3/6/20 Rijek
    @api.multi
    @api.depends('workorder_ids')
    def _get_jumlah_yg_selesai_total_transfer_jebol(self):
        for production_id in self:
            production_id.mrp_total_transfer_jebol = sum((line_id.total_transfer_jebol) for line_id in production_id.workorder_ids)
