# Copyright 2014 Serv. Tec. Avanzados - Pedro M. Baeza
# Copyright 2018 Simone Rubino - Agile Business Group
# Copyright 2019 Andrii Skrypka
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from flectra import api, fields, models
from flectra.addons.quality_control.models.qc_trigger_line import\
    _filter_trigger_lines


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    qc_inspections_ids = fields.One2many(
        comodel_name='qc.inspection', inverse_name='picking_id', copy=False,
        string='Inspections', help="Inspections related to this picking.")
    created_inspections = fields.Integer(
        compute="_compute_count_inspections", string="Created inspections")
    done_inspections = fields.Integer(
        compute="_compute_count_inspections", string="Done inspections")
    passed_inspections = fields.Integer(
        compute="_compute_count_inspections", string="Inspections OK")
    failed_inspections = fields.Integer(
        compute="_compute_count_inspections", string="Inspections failed")

    @api.depends('qc_inspections_ids', 'qc_inspections_ids.state')
    def _compute_count_inspections(self):
        data = self.env['qc.inspection'].read_group([
            ('id', 'in', self.mapped('qc_inspections_ids').ids),
        ], ['picking_id', 'state'], ['picking_id', 'state'], lazy=False)
        picking_data = {}
        for d in data:
            picking_data.setdefault(d['picking_id'][0], {})\
                .setdefault(d['state'], 0)
            picking_data[d['picking_id'][0]][d['state']] += d['__count']
        for picking in self:
            count_data = picking_data.get(picking.id, {})
            picking.created_inspections = sum(count_data.values())
            picking.passed_inspections = count_data.get('success', 0)
            picking.failed_inspections = count_data.get('failed', 0)
            picking.done_inspections = \
                (picking.passed_inspections + picking.failed_inspections)

    @api.multi
    def action_done(self):
        res = super(StockPicking, self).action_done()
        inspection_model = self.env['qc.inspection']
        for operation in self.move_lines:
            qc_trigger = self.env['qc.trigger'].search(
                [('picking_type_id', '=', self.picking_type_id.id)])
            trigger_lines = set()
            for model in ['qc.trigger.product_category_line',
                          'qc.trigger.product_template_line',
                          'qc.trigger.product_line']:
                partner = (self.partner_id
                           if qc_trigger.partner_selectable else False)
                trigger_lines = trigger_lines.union(
                    self.env[model].get_trigger_line_for_product(
                        qc_trigger, operation.product_id, partner=partner))
            for trigger_line in _filter_trigger_lines(trigger_lines):
                inspection_model._make_inspection(operation, trigger_line)
        return res
