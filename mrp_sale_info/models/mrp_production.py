# Copyright 2016 Antiun Ingenieria S.L. - Javier Iniesta
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from flectra import fields, models, api, _


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    sale_id = fields.Many2one(
        comodel_name='sale.order', string='Sale order', readonly=True,
        store=True, related='procurement_group_id.sale_id')
    partner_id = fields.Many2one(
        comodel_name='res.partner', related='sale_id.partner_id',
        string='Customer', store=True)
    commitment_date = fields.Datetime(
        related='sale_id.commitment_date', string='Commitment Date',
        store=True)
    sale_id2 = fields.Many2one('sale.order', 'Ref SO',store=True)


# class ProcurementGroup(models.Model):
#     _inherit = 'procurement.group'

#     @api.multi
#     def write(self, values):
#         res = super(ProcurementGroup, self).write(values)
#         if not self.sale_id:
#             mrp_sale_id = self.env['mrp.production'].search([('procurement_group_id', '=', self.id)])
#             for line in mrp_sale_id:
#                 self.sale_id = line.sale_id2
#         return res



class ProcurementRule(models.Model):
    _inherit = 'procurement.rule'

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, values, bom):
        res=super()._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, values, bom)
        res.update ({
            'sale_id2': values.get('group_id').sale_id.id if values.get('group_id', False) else False,
        })
        return res