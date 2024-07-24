# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.

from flectra import api, fields, models, _

class CrossoveredBudgetLines(models.Model):
    _inherit = "crossovered.budget.lines"

    @api.multi
    def _compute_practical_amount(self):
        for line in self:
            result = 0.0
            acc_ids = line.general_budget_id.account_ids.ids
            date_to = self.env.context.get('wizard_date_to') or line.date_to
            date_from = self.env.context.get('wizard_date_from') or line.date_from
            if line.analytic_account_id.id:
                self.env.cr.execute("""
                    SELECT SUM(amount)
                    FROM account_analytic_line
                    WHERE account_id=%s
                        AND (date between to_date(%s,'yyyy-mm-dd') AND to_date(%s,'yyyy-mm-dd'))
                        AND general_account_id=ANY(%s)""",
                (line.analytic_account_id.id, date_from, date_to, acc_ids,))
                result = self.env.cr.fetchone()[0] or 0.0
            else:
                self.env.cr.execute("""
                    SELECT sum(credit)-sum(debit)
                    FROM account_move_line aml
                    JOIN account_move am ON am.id = aml.move_id
                    WHERE am.state = 'posted'
                        AND (aml.date between to_date(%s,'yyyy-mm-dd') AND to_date(%s,'yyyy-mm-dd'))
                        AND account_id IN %s""",
                (date_from, date_to, tuple(acc_ids),))
                result = self.env.cr.fetchone()[0] or 0.0
            line.practical_amount = result
        # for line in self:
        #     acc_ids = line.general_budget_id.account_ids.ids
        #     date_to = line.date_to
        #     date_from = line.date_from
        #     if line.analytic_account_id.id:
        #         analytic_line_obj = self.env['account.analytic.line']
        #         domain = [('account_id', '=', line.analytic_account_id.id),
        #                   ('date', '>=', date_from),
        #                   ('date', '<=', date_to),
        #                   ]
        #         if acc_ids:
        #             domain += [('general_account_id', 'in', acc_ids)]

        #         where_query = analytic_line_obj._where_calc(domain)
        #         analytic_line_obj._apply_ir_rules(where_query, 'read')
        #         from_clause, where_clause, where_clause_params = where_query.get_sql()
        #         select = "SELECT SUM(amount) from " + from_clause + " where " + where_clause

        #     else:
        #         aml_obj = self.env['account.move.line']
        #         domain = [('account_id', 'in',
        #                    line.general_budget_id.account_ids.ids),
        #                   ('date', '>=', date_from),
        #                   ('date', '<=', date_to),
        #                   ('move_id.state', '=', 'posted')
        #                   ]
        #         where_query = aml_obj._where_calc(domain)
        #         aml_obj._apply_ir_rules(where_query, 'read')
        #         from_clause, where_clause, where_clause_params = where_query.get_sql()
        #         select = "SELECT sum(credit)-sum(debit) from " + from_clause + " where " + where_clause

        #     self.env.cr.execute(select, where_clause_params)
        #     line.practical_amount = self.env.cr.fetchone()[0] or 0.0
    