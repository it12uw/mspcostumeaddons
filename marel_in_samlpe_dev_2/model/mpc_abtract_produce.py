from collections import defaultdict

from flectra import api, fields, models, _
from flectra.exceptions import UserError
from flectra.tools import float_compare, float_round, float_is_zero
from flectra.addons import decimal_precision as dp


class MpcAbstractProduce(models.AbstractModel):
    _name = "mpc.abstract.produce"
    _description = "Lot Produce"

    product_id = fields.Many2one('product.product', 'Product')
    product_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'), required=True)
    product_uom_id = fields.Many2one('product.uom', 'Unit of Measure')
    lot_id = fields.Many2one('stock.production.lot', domain="[('product_id', '=', product_id)]", string='Lot/Serial Number')
    production_id = fields.Many2one('mrp.production', 'Production')
    date_entry = fields.Datetime('Date', default=fields.Datetime.now)
    # net_weight = fields.Float(string='NW')
    # grade_id = fields.Char(string="Grade")
    # ket_grade = fields.Char(string='Keterangan Grade',)
    # justcut = fields.Char(string='Justcut',)
    # no_inspek = fields.Many2one ('mpc.inspek', string='No Inspek')
    
    # total_point = fields.Float(string='Total Point')
    # shift_inspek = fields.Char(string='Shift Inspek', )
    # jumlah_inspek = fields.Integer(string='Jumlah Inspek', )
    # inspek = fields.Char(string='Inspektor',)
    # p1 = fields.Integer(string='Point 1', default=0)
    # p2 = fields.Integer(string='Point 2', default=0)
    # p3 = fields.Integer(string='Point 3', default=0)
    # p4 = fields.Integer(string='Point 4', default=0)
    # pd = fields.Integer(string='PD', default=0)
    # no_potong = fields.Many2one('mpc.weaving', string='Id Potong')
    # no_beam_id = fields.Many2one('nomor.beam', string="No Beam")
    # potongke = fields.Char(string='No Potong')
    # tgl_potong = fields.Date(string='Tgl Potong')
    # no_mesin = fields.Many2one('mesin.produksi', string='No Mesin')
    # shift = fields.Char(string='Shift Potong', )
    # lbr_actual = fields.Float(string="Lebar Aktual")

    @api.onchange('product_qty')
    def _onchange_product_qty(self):
        lines = []
        qty_todo = self.product_uom_id._compute_quantity(self.product_qty, self.production_id.product_uom_id, round=False)
        for move in self.production_id.move_raw_ids.filtered(lambda m: m.state not in ('done', 'cancel') and m.bom_line_id):
            qty_to_consume = float_round(qty_todo * move.unit_factor, precision_rounding=move.product_uom.rounding)
            for move_line in move.move_line_ids:
                if float_compare(qty_to_consume, 0.0, precision_rounding=move.product_uom.rounding) <= 0:
                    break
                if move_line.lot_produced_id or float_compare(move_line.product_uom_qty, move_line.qty_done, precision_rounding=move.product_uom.rounding) <= 0:
                    continue
                to_consume_in_line = min(qty_to_consume, move_line.product_uom_qty)
                lines.append({
                    'move_id': move.id,
                    'qty_to_consume': to_consume_in_line,
                    'qty_done': to_consume_in_line,
                    'lot_id': move_line.lot_id.id,
                    'product_uom_id': move.product_uom.id,
                    'product_id': move.product_id.id,
                    'qty_reserved': min(to_consume_in_line, move_line.product_uom_qty),
                })
                qty_to_consume -= to_consume_in_line
            if float_compare(qty_to_consume, 0.0, precision_rounding=move.product_uom.rounding) > 0:
                if move.product_id.tracking == 'serial':
                    while float_compare(qty_to_consume, 0.0, precision_rounding=move.product_uom.rounding) > 0:
                        lines.append({
                            'move_id': move.id,
                            'qty_to_consume': 1,
                            'qty_done': 1,
                            'product_uom_id': move.product_uom.id,
                            'product_id': move.product_id.id,
                        })
                        qty_to_consume -= 1
                else:
                    lines.append({
                        'move_id': move.id,
                        'qty_to_consume': qty_to_consume,
                        'qty_done': qty_to_consume,
                        'product_uom_id': move.product_uom.id,
                        'product_id': move.product_id.id,
                    })

        self.produce_line_ids = [(5,)] + [(0, 0, x) for x in lines]

    # @api.onchange('lot_id','no_inspek')
    # def _onchange_lotid(self):
    #     self.net_weight=self.lot_id.nw_done
    #     self.grade_id=self.lot_id.grade_id_done
    #     self.ket_grade=self.lot_id.ket_grade
    #     self.justcut=self.lot_id.justcut
    #     self.no_inspek=self.lot_id.no_ins_done.id
    #     self.lbr_actual = self.lot_id.lbr_actual

    #     self.shift_inspek=self.no_inspek.shift_inspek
    #     self.jumlah_inspek=self.no_inspek.jumlah_inspek 
    #     self.inspek=self.no_inspek.inspek
    #     self.p1=self.no_inspek.p1
    #     self.p2=self.no_inspek.p1
    #     self.p3=self.no_inspek.p1
    #     self.p4=self.no_inspek.p1
    #     self.pd=self.no_inspek.p1
    #     self.no_potong=self.no_inspek.no_potong.id
    #     self.lbr_actual = self.no_inspek.lbr_actual

    #     self.potongke = self.no_potong.potongke
    #     self.tgl_potong = self.no_potong.tgl_potong
    #     self.no_mesin = self.no_potong.no_mesin.id
    #     self.no_beam_id = self.no_potong.no_beam_id.id
    #     self.shift = self.no_potong.shift

    # @api.onchange('no_potong')
    # def _onchange_nopot(self):
    #     self.potongke = self.no_potong.potongke
    #     self.tgl_potong = self.no_potong.tgl_potong
    #     self.no_mesin = self.no_potong.no_mesin.id
    #     self.no_beam_id = self.no_potong.no_beam_id.id
    #     self.shift = self.no_potong.shift

    @api.model
    def get_report_values(self, docids, data=None):
        # report_lines = self.get_data(data.get('form'))
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        return {'doc_ids': docids, 'doc_model': model, 'data': data,
                'docs': docs, 
                # 'get_data': report_lines
                }



class MpcAbstractProduceLine(models.AbstractModel):
    _name = "mpc.abstract.produce.line"
    _description = "Lot Produce Line"

    product_id = fields.Many2one('product.product', 'Product')
    product_tracking = fields.Selection(related="product_id.tracking")
    lot_id = fields.Many2one('stock.production.lot', 'Lot/Serial Number')
    qty_to_consume = fields.Float('To Consume', digits=dp.get_precision('Product Unit of Measure'))
    product_uom_id = fields.Many2one('product.uom', 'Unit of Measure')
    qty_done = fields.Float('Consumed', digits=dp.get_precision('Product Unit of Measure'))
    move_id = fields.Many2one('stock.move')
    qty_reserved = fields.Float('Reserved', digits=dp.get_precision('Product Unit of Measure'))

    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        """ When the user is encoding a produce line for a tracked product, we apply some logic to
        help him. This onchange will automatically switch `qty_done` to 1.0.
        """
        res = {}
        if self.product_id.tracking == 'serial':
            self.qty_done = 1
        return res

    @api.onchange('qty_done')
    def _onchange_qty_done(self):
        """ When the user is encoding a produce line for a tracked product, we apply some logic to
        help him. This onchange will warn him if he set `qty_done` to a non-supported value.
        """
        res = {}
        if self.product_id.tracking == 'serial' and self.qty_done:
            if float_compare(self.qty_done, 1.0, precision_rounding=self.move_id.product_id.uom_id.rounding) != 0:
                message = _('You can only process 1.0 %s of products with unique serial number.') % self.product_id.uom_id.name
                res['warning'] = {'title': _('Warning'), 'message': message}
        return res

    @api.onchange('product_id')
    def _onchange_product_id(self):
        self.product_uom_id = self.product_id.uom_id.id
