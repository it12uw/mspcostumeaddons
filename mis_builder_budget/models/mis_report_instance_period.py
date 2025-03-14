# Copyright 2017-2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from flectra import api, fields, models


SRC_MIS_BUDGET = 'mis_budget'


class MisReportInstancePeriod(models.Model):

    _inherit = 'mis.report.instance.period'

    source = fields.Selection(
        selection_add=[
            (SRC_MIS_BUDGET, 'MIS Budget'),
        ],
    )
    source_mis_budget_id = fields.Many2one(
        comodel_name='mis.budget',
        string='Budget',
        oldname='source_mis_budget',
    )

    @api.multi
    def _get_additional_budget_item_filter(self):
        """ Prepare a filter to apply on all budget items

        This filter is applied with a AND operator on all
        budget items. This hook is intended
        to be inherited, and is useful to implement filtering
        on analytic dimensions or operational units.

        The default filter is built from a ``mis_report_filters context``
        key, which is a list set by the analytic filtering mechanism
        of the mis report widget::

          [(field_name, {'value': value, 'operator': operator})]

        This default filter is the same as the one set by
        _get_additional_move_line_filter on mis.report.instance, so
        a budget.item is expected to have the same analytic fields as
        a move line.

        Returns an Flectra domain expression (a python list)
        compatible with mis.budget.item."""
        self.ensure_one()
        filters = self._get_filter_domain_from_context()
        return filters
