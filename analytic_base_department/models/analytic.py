# Copyright 2011-2016 Camptocamp SA
# Copyright 2013 Daniel Reis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from flectra import api, fields, models


class AnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    department_id = fields.Many2one(
        'hr.department',
        'Department')


class AnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    @api.model
    def _default_department(self):
        department_id = False
        employee = self.env.user.employee_ids
        if employee and employee[0].department_id:
            department_id = employee[0].department_id.id
        return department_id

    department_id = fields.Many2one(
        'hr.department',
        'Department',
        default=lambda self: self._default_department(),
        help="User's related department")
    account_department_id = fields.Many2one(
        comodel_name='hr.department',
        related='account_id.department_id',
        string='Account Department',
        store=True,
        readonly=True,
        help="Account's related department")
