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

class MspWorkOrder1(models.Model):
    _inherit = ['mrp.workorder']
    
    status_button_1 = fields.Boolean(string='Status Button 20%',store=True,default=False,)
    status_button_2 = fields.Boolean(string='Status Button 40%',store=True,default=False,)
    status_button_3 = fields.Boolean(string='Status Button 80%',store=True,default=False,)
    status_button_4 = fields.Boolean(string='Status Button 100%',store=True,default=False,)
    status_button_inline_garment = fields.Boolean(string='Status Button Inline garment',store=True,default=False,)
    status_button_endline_garment = fields.Boolean(string='Status Button Endline garment',store=True,default=False,)
    
    # hidden button inline
    @api.multi
    def action_telah_diinline1(self):
        self.write({'status_button_1' : 'yes',})

    @api.multi
    def action_nilai_inline_1_qc(self):
        self.ensure_one()
        self.action_telah_diinline1()
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qc.inline1.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
                'target': 'new',
            }

    @api.multi
    def action_pending_diinline1(self):
        self.status_button_1 = False

    @api.multi
    def action_nilai_pending_inline_1_qc(self):
        self.ensure_one()
        self.action_pending_diinline1()
    # ------------------------------------ inline 40 -----------------------------------
    @api.multi
    def action_telah_diinline2(self):
        self.write({'status_button_2' : 'yes',})

    @api.multi
    def action_nilai_inline_2_qc(self):
        self.ensure_one()
        self.action_telah_diinline2()
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qc.inline2.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
                'target': 'new',
            }

    @api.multi
    def action_pending_diinline2(self):
        self.status_button_2 = False

    @api.multi
    def action_nilai_pending_inline_2_qc(self):
        self.ensure_one()
        self.action_pending_diinline2()
    # ------------------------------------ inline 80 -----------------------------------
    @api.multi
    def action_telah_diinline3(self):
        self.write({'status_button_3' : 'yes',})

    @api.multi
    def action_nilai_inline_3_qc(self):
        self.ensure_one()
        self.action_telah_diinline3()
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qc.inline3.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
                'target': 'new',
            }

    @api.multi
    def action_pending_diinline3(self):
        self.status_button_3 = False

    @api.multi
    def action_nilai_pending_inline_3_qc(self):
        self.ensure_one()
        self.action_pending_diinline3()
    # ------------------------------------ inline 100 -----------------------------------
    @api.multi
    def action_telah_diinline4(self):
        self.write({'status_button_4' : 'yes',})

    @api.multi
    def action_nilai_inline_4_qc(self):
        self.ensure_one()
        self.action_telah_diinline4()
        return {
                'name': 'Nilai Inline Qc',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qc.inline4.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
                'target': 'new',
            }

    @api.multi
    def action_pending_diinline4(self):
        self.status_button_4 = False

    @api.multi
    def action_nilai_pending_inline_4_qc(self):
        self.ensure_one()
        self.action_pending_diinline4()
    # ------------------------------------ inline Garment -----------------------------------
    @api.multi
    def action_telah_diinline_garment(self):
        self.write({'status_button_inline_garment' : 'yes',})

    @api.multi
    def action_nilai_inline_garment_qc(self):
        self.ensure_one()
        self.action_telah_diinline_garment()
        return {
                'name': 'Nilai Inline Qc Garment',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qcinline.garment.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
                'target': 'new',
            }

    @api.multi
    def action_pending_status_button_inline_garment(self):
        self.status_button_inline_garment = False

    @api.multi
    def action_nilai_pending_status_button_inline_garment_qc(self):
        self.ensure_one()
        self.action_pending_status_button_inline_garment()
    # ------------------------------------ Endline Garment -----------------------------------
    @api.multi
    def action_telah_diendline_garment(self):
        self.write({'status_button_endline_garment' : 'yes',})

    @api.multi
    def action_nilai_endline_garment_qc(self):
        self.ensure_one()
        self.action_telah_diendline_garment()
        return {
                'name': 'Nilai Endline Qc Garment',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_model': 'msp.qcendline.garment.wizard',
                'type': 'ir.actions.act_window',
                'context':{},
                'target': 'new',
            }

    @api.multi
    def action_pending_status_button_endline_garment(self):
        self.status_button_endline_garment = False

    @api.multi
    def action_nilai_pending_status_button_endline_garment_qc(self):
        self.ensure_one()
        self.action_pending_status_button_endline_garment()


    # @api.multi
    # def record_production(self):
    #     self.ensure_one()
    #     if self.qty_producing <= 0:
    #         raise UserError(_('Please set the quantity you are currently producing. It should be different from zero.'))

    #     if (self.production_id.product_id.tracking != 'none') and not self.final_lot_id and self.move_raw_ids:
    #         raise UserError(_('You should provide a lot/serial number for the final product'))

    #     # Update quantities done on each raw material line
    #     # For each untracked component without any 'temporary' move lines,
    #     # (the new workorder tablet view allows registering consumed quantities for untracked components)
    #     # we assume that only the theoretical quantity was used
    #     for move in self.move_raw_ids:
    #         if move.has_tracking == 'none' and (move.state not in ('done', 'cancel')) and move.bom_line_id\
    #                     and move.unit_factor and not move.move_line_ids.filtered(lambda ml: not ml.done_wo):
    #             rounding = move.product_uom.rounding
    #             if self.product_id.tracking != 'none':
    #                 qty_to_add = float_round(self.qty_producing * move.unit_factor, precision_rounding=rounding)
    #                 move._generate_consumed_move_line(qty_to_add, self.final_lot_id)
    #             elif len(move._get_move_lines()) < 2:
    #                 move.quantity_done += float_round(self.qty_producing * move.unit_factor, precision_rounding=rounding)
    #             else:
    #                 move._set_quantity_done(move.quantity_done + float_round(self.qty_producing * move.unit_factor, precision_rounding=rounding))

    #     # Transfer quantities from temporary to final move lots or make them final
    #     for move_line in self.active_move_line_ids:
    #         # Check if move_line already exists
    #         if move_line.qty_done <= 0:  # rounding...
    #             move_line.sudo().unlink()
    #             continue
    #         if move_line.product_id.tracking != 'none' and not move_line.lot_id:
    #             raise UserError(_('You should provide a lot/serial number for a component'))
    #         # Search other move_line where it could be added:
    #         lots = self.move_line_ids.filtered(lambda x: (x.lot_id.id == move_line.lot_id.id) and (not x.lot_produced_id) and (not x.done_move) and (x.product_id == move_line.product_id))
    #         if lots:
    #             lots[0].qty_done += move_line.qty_done
    #             lots[0].lot_produced_id = self.final_lot_id.id
    #             move_line.sudo().unlink()
    #         else:
    #             move_line.lot_produced_id = self.final_lot_id.id
    #             move_line.done_wo = True

    #     # One a piece is produced, you can launch the next work order
    #     if self.next_work_order_id.state == 'pending':
    #         self.next_work_order_id.state = 'ready'

    #     self.move_line_ids.filtered(
    #         lambda move_line: not move_line.done_move and not move_line.lot_produced_id and move_line.qty_done > 0
    #     ).write({
    #         'lot_produced_id': self.final_lot_id.id,
    #         'lot_produced_qty': self.qty_producing
    #     })

    #     # If last work order, then post lots used
    #     # TODO: should be same as checking if for every workorder something has been done?
    #     if not self.next_work_order_id:
    #         production_move = self.production_id.move_finished_ids.filtered(
    #                             lambda x: (x.product_id.id == self.production_id.product_id.id) and (x.state not in ('done', 'cancel')))
    #         if production_move.product_id.tracking != 'none':
    #             move_line = production_move.move_line_ids.filtered(lambda x: x.lot_id.id == self.final_lot_id.id)
    #             if move_line:
    #                 move_line.product_uom_qty += self.qty_producing
    #                 move_line.qty_done += self.qty_producing
    #             else:
    #                 move_line.create({'move_id': production_move.id,
    #                          'product_id': production_move.product_id.id,
    #                          'lot_id': self.final_lot_id.id,
    #                          'product_uom_qty': self.qty_producing,
    #                          'product_uom_id': production_move.product_uom.id,
    #                          'qty_done': self.qty_producing,
    #                          'workorder_id': self.id,
    #                          'location_id': production_move.location_id.id,
    #                          'location_dest_id': production_move.location_dest_id.id,
    #                 })
    #         else:
    #             production_move.quantity_done += self.qty_producing

    #     if not self.next_work_order_id:
    #         for by_product_move in self.production_id.move_finished_ids.filtered(lambda x: (x.product_id.id != self.production_id.product_id.id) and (x.state not in ('done', 'cancel'))):
    #             if by_product_move.has_tracking != 'serial':
    #                 values = self._get_byproduct_move_line(by_product_move, self.qty_producing * by_product_move.unit_factor)
    #                 self.env['stock.move.line'].create(values)
    #             elif by_product_move.has_tracking == 'serial':
    #                 qty_todo = by_product_move.product_uom._compute_quantity(self.qty_producing * by_product_move.unit_factor, by_product_move.product_id.uom_id)
    #                 for i in range(0, int(float_round(qty_todo, precision_digits=0))):
    #                     values = self._get_byproduct_move_line(by_product_move, 1)
    #                     self.env['stock.move.line'].create(values)

    #     # Update workorder quantity produced
    #     self.qty_produced += self.qty_producing

    #     if self.final_lot_id:
    #         self.final_lot_id.use_next_on_work_order_id = self.next_work_order_id
    #         self.final_lot_id = False

    #     # Set a qty producing
    #     rounding = self.production_id.product_uom_id.rounding
    #     if float_compare(self.qty_produced, self.production_id.product_qty, precision_rounding=rounding) >= 0:
    #         self.qty_producing = 0
    #     elif self.production_id.product_id.tracking == 'serial':
    #         self._assign_default_final_lot_id()
    #         self.qty_producing = 1.0
    #         self._generate_lot_ids()
    #     else:
    #         self.qty_producing = float_round(self.production_id.product_qty - self.qty_produced, precision_rounding=rounding)
    #         self._generate_lot_ids()

    #     if self.next_work_order_id and self.production_id.product_id.tracking != 'none':
    #         self.next_work_order_id._assign_default_final_lot_id()

    #     # if float_compare(self.qty_produced, self.production_id.product_qty, precision_rounding=rounding) >= 0:
    #     #     self.button_finish()
    #     return True
