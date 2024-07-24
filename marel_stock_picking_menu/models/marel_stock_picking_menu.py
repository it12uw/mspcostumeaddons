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
    _inherit = 'stock.move'
    
    # picking_id_name = fields.Char(string="No WH",related='picking_id.name',store=True)
    no_bpb = fields.Char(string="No BPB",related='picking_id.no_bpb')
    no_spb = fields.Char(string="No SPB",related='picking_id.no_spb')
    no_sj = fields.Char(string="No SJ",related='picking_id.no_sj')
    tgl_transaksi = fields.Date(string="Tgl Kirim",related='picking_id.tgl_transaksi')