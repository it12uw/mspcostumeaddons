# Copyright 2017 Creu Blanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from flectra import api, fields, models, _
from flectra.exceptions import UserError


class ReportAction(models.Model):
    _inherit = 'ir.actions.report'

    report_type = fields.Selection(selection_add=[("fillpdf", "PDF Filler")])

    @api.model
    def render_fillpdf(self, docids, data):
        report_model_name = 'report.%s' % self.report_name
        report_model = self.env.get(report_model_name)
        if report_model is None:
            raise UserError(_('%s model was not found' % report_model_name))
        return report_model.with_context({
            'active_model': self.model
        }).fill_report(docids, data)

    @api.model
    def _get_report_from_name(self, report_name):
        res = super(ReportAction, self)._get_report_from_name(report_name)
        if res:
            return res
        report_obj = self.env['ir.actions.report']
        qwebtypes = ['fillpdf']
        conditions = [('report_type', 'in', qwebtypes),
                      ('report_name', '=', report_name)]
        context = self.env['res.users'].context_get()
        return report_obj.with_context(context).search(conditions, limit=1)
