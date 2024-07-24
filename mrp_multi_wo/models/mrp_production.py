from collections import defaultdict
import math

from flectra import api, fields, models, _
from flectra.addons import decimal_precision as dp
from flectra.exceptions import AccessError, UserError
from flectra.tools import float_compare

class MRPProduction(models.Model):
    _inherit = 'mrp.production'

    kkp_qty = fields.Integer('Capacity', default=96)

    @api.multi
    def button_plan_multi(self):
        """ Create work orders. And probably do stuff, like things. """
        orders_to_plan = self.filtered(lambda order: order.routing_id and order.state == 'confirmed')
        for order in orders_to_plan:
            for multi in range (1,int(order.product_qty),order.kkp_qty)[:-1]:
                quantity = order.product_uom_id._compute_quantity(order.product_qty, order.bom_id.product_uom_id) / order.bom_id.product_qty
                boms, lines = order.bom_id.explode(order.product_id, quantity, picking_type=order.bom_id.picking_type_id)
                order._generate_workorders_multi(boms)
            else:
                if order.product_qty % order.kkp_qty > 0:
                    left = order.product_qty % order.kkp_qty
                    quantity = order.product_uom_id._compute_quantity(order.product_qty, order.bom_id.product_uom_id) / order.bom_id.product_qty
                    boms, lines = order.bom_id.explode(order.product_id, quantity, picking_type=order.bom_id.picking_type_id)
                    order._generate_workorders_multi_modulo(boms)
                else:
                    quantity = order.product_uom_id._compute_quantity(order.product_qty, order.bom_id.product_uom_id) / order.bom_id.product_qty
                    boms, lines = order.bom_id.explode(order.product_id, quantity, picking_type=order.bom_id.picking_type_id)
                    order._generate_workorders_multi(boms)
        return orders_to_plan.write({'state': 'planned'})

    @api.multi
    def _generate_workorders_multi(self, exploded_boms):
        workorders = self.env['mrp.workorder']
        original_one = False
        for bom, bom_data in exploded_boms:
            # If the routing of the parent BoM and phantom BoM are the same, don't recreate work orders, but use one master routing
            if bom.routing_id.id and (not bom_data['parent_line'] or bom_data['parent_line'].bom_id.routing_id.id != bom.routing_id.id):
                temp_workorders = self._workorders_create_multi(bom, bom_data)
                workorders += temp_workorders
                if temp_workorders: # In order to avoid two "ending work orders"
                    if original_one:
                        temp_workorders[-1].next_work_order_id = original_one
                    original_one = temp_workorders[0]
        return workorders

    api.multi
    def _generate_workorders_multi_modulo(self, exploded_boms):
        workorders = self.env['mrp.workorder']
        original_one = False
        for bom, bom_data in exploded_boms:
            # If the routing of the parent BoM and phantom BoM are the same, don't recreate work orders, but use one master routing
            if bom.routing_id.id and (not bom_data['parent_line'] or bom_data['parent_line'].bom_id.routing_id.id != bom.routing_id.id):
                temp_workorders = self._workorders_create_multi_modulo(bom, bom_data)
                workorders += temp_workorders
                if temp_workorders: # In order to avoid two "ending work orders"
                    if original_one:
                        temp_workorders[-1].next_work_order_id = original_one
                    original_one = temp_workorders[0]
        return workorders


    def _workorders_create_multi(self, bom, bom_data):
        """
        :param bom: in case of recursive boms: we could create work orders for child
                    BoMs
        """
        workorders = self.env['mrp.workorder']
        bom_qty = bom_data['qty']

        quantity = self.kkp_qty
        for operation in bom.routing_id.operation_ids:
            # create workorder
            cycle_number = math.ceil(bom_qty / operation.workcenter_id.capacity)  # TODO: float_round UP
            duration_expected = (operation.workcenter_id.time_start +
                                operation.workcenter_id.time_stop +
                                cycle_number * operation.time_cycle * 100.0 / operation.workcenter_id.time_efficiency)
            workorder = workorders.create({
                'name': operation.name,
                'production_id': self.id,
                'workcenter_id': operation.workcenter_id.id,
                'operation_id': operation.id,
                'duration_expected': duration_expected,
                'state': len(workorders) == 0 and 'ready' or 'pending',
                'qty_producing': quantity,
                'qty_production': quantity,
                'capacity': operation.workcenter_id.capacity,
            })
            if workorders:
                workorders[-1].next_work_order_id = workorder.id
            workorders += workorder

            # assign moves; last operation receive all unassigned moves (which case ?)
            moves_raw = self.move_raw_ids.filtered(lambda move: move.operation_id == operation)
            if len(workorders) == len(bom.routing_id.operation_ids):
                moves_raw |= self.move_raw_ids.filtered(lambda move: not move.operation_id)
            moves_finished = self.move_finished_ids.filtered(lambda move: move.operation_id == operation) #TODO: code does nothing, unless maybe by_products?
            moves_raw.mapped('move_line_ids').write({'workorder_id': workorder.id})
            (moves_finished + moves_raw).write({'workorder_id': workorder.id})

            workorder._generate_lot_ids()
        return workorders

    def _workorders_create_multi_modulo(self, bom, bom_data):
        workorders = self.env['mrp.workorder']
        bom_qty = bom_data['qty']        
        quantity = self.product_qty % self.kkp_qty
        for operation in bom.routing_id.operation_ids:
            # create workorder
            cycle_number = math.ceil(bom_qty / operation.workcenter_id.capacity)  # TODO: float_round UP
            duration_expected = (operation.workcenter_id.time_start +
                                operation.workcenter_id.time_stop +
                                cycle_number * operation.time_cycle * 100.0 / operation.workcenter_id.time_efficiency)
            workorder = workorders.create({
                'name': operation.name,
                'production_id': self.id,
                'workcenter_id': operation.workcenter_id.id,
                'operation_id': operation.id,
                'duration_expected': duration_expected,
                'state': len(workorders) == 0 and 'ready' or 'pending',
                'qty_producing': quantity,
                'qty_production': quantity,
                'capacity': operation.workcenter_id.capacity,
            })
            if workorders:
                workorders[-1].next_work_order_id = workorder.id
            workorders += workorder

            # assign moves; last operation receive all unassigned moves (which case ?)
            moves_raw = self.move_raw_ids.filtered(lambda move: move.operation_id == operation)
            if len(workorders) == len(bom.routing_id.operation_ids):
                moves_raw |= self.move_raw_ids.filtered(lambda move: not move.operation_id)
            moves_finished = self.move_finished_ids.filtered(lambda move: move.operation_id == operation) #TODO: code does nothing, unless maybe by_products?
            moves_raw.mapped('move_line_ids').write({'workorder_id': workorder.id})
            (moves_finished + moves_raw).write({'workorder_id': workorder.id})

            workorder._generate_lot_ids()
        return workorders



