from flectra import models, fields, api
from datetime import datetime, date, timedelta
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class AccountDuelateWiz(models.TransientModel):
    _name = 'account.duelate.wiz'

    date_start = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    date_end = fields.Date(string="End Date", required=True, default=fields.Date.today)
    

    def get_report(self):
        data = {
            'model': self._name,
            'ids': self.ids,
            'form': {
                'date_start': self.date_start, 'date_end': self.date_end,
            },
        }

        # ref `module_name.report_id` as reference.
        return self.env.ref('account_due_late_invoice.action_account_duelate_report').report_action(self,data=data)


class ReportAccountDuelateDoc(models.AbstractModel):
    _name = 'report.account_due_late_invoice.account_duelate_report_doc'

    @api.model
    def get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']

        start_date = datetime.strptime(date_start, DATE_FORMAT)
        end_date = datetime.strptime(date_end, DATE_FORMAT)
        delta = timedelta(days=1)

        docs = self.env['account.invoice'].search([('date', '>=', start_date.strftime(DATETIME_FORMAT)),
                ('date', '<', end_date.strftime(DATETIME_FORMAT))])

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }