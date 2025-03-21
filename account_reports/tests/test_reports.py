# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.
import time

from flectra.tests import common
from flectra.tools.misc import formatLang
from flectra import fields


class TestAccountReports(common.TransactionCase):
    def setUp(self):
        super(TestAccountReports, self).setUp()
        self.company = self.env.user.company_id

        self.partner_timmy_thomas = self.env['res.partner'].create({
            'name': 'Timmy Thomas',
        })

        #  Account types
        self.account_type_rcv = self.env['account.account.type'].create({
            'name': 'receivable',
            'type': 'receivable',
        })

        self.account_type_liq = self.env['account.account.type'].create({
            'name': 'liquidity',
            'type': 'liquidity',
        })

        self.account_type_other = self.env['account.account.type'].create({
            'name': 'other',
            'type': 'other',
        })

        # Accounts
        self.account_rcv = self.env['account.account'].create({
            'name': 'RCV',
            'code': '001',
            'user_type_id': self.account_type_rcv.id,
            'reconcile': True,
            'company_id': self.company.id,
        })

        self.account_sale = self.env['account.account'].create({
            'name': 'SALE',
            'code': '002',
            'user_type_id': self.account_type_other.id,
            'reconcile': False,
            'company_id': self.company.id,
        })

        self.account_expense = self.env['account.account'].create({
            'name': 'EXP',
            'code': '003',
            'user_type_id': self.account_type_other.id,
            'reconcile': False,
            'company_id': self.company.id,
        })

        self.account_pay = self.env['account.account'].create({
            'name': 'PAY',
            'code': '004',
            'user_type_id': self.account_type_liq.id,
            'reconcile': False,
            'company_id': self.company.id,
        })

        self.account_other = self.env['account.account'].create({
            'name': 'OTHER',
            'code': '005',
            'user_type_id': self.account_type_other.id,
            'reconcile': False,
            'company_id': self.company.id,
        })

        # Journals
        self.payment_journal = self.env['account.journal'].create({
            'name': 'payment',
            'code': 'PAY',
            'type': 'cash',
            'company_id': self.company.id,
            'default_debit_account_id': self.account_pay.id,
            'default_credit_account_id': self.account_pay.id,
        })

        self.sale_journal = self.env['account.journal'].create({
            'name': 'sale',
            'code': 'SALE',
            'type': 'sale',
            'company_id': self.company.id,
            'default_debit_account_id': self.account_sale.id,
            'default_credit_account_id': self.account_sale.id,
        })

        mock_date = time.strftime('%Y') + '-06-26'
        self.minimal_options = {
            'date': {
                'date_from': mock_date,
                'date_to': mock_date,
            },
        }
        self.minimal_options_general_ledger = dict(self.minimal_options)
        self.minimal_options_general_ledger['date']['date'] = mock_date
        self.minimal_options_general_ledger.update({
            'unfolded_lines': [],
            'journals': [],
            'comparison': {
                'periods': [],
            }
        })

    def test_00_financial_reports(self):
        for report in self.env['account.financial.html.report'].search([]):
            report.get_html(self.minimal_options)

    def test_01_custom_reports(self):
        report_models = [
            'account.bank.reconciliation.report',
            'account.general.ledger',
            'account.generic.tax.report',
        ]
        minimal_context = {
            'state': False,
        }

        for report_model in report_models:
            self.env[report_model].with_context(minimal_context).get_html(self.minimal_options_general_ledger)

    def test_02_followup_reports(self):
        self.minimal_options_general_ledger['partner_id'] = self.env.ref('base.res_partner_2').id
        self.env['account.followup.report'].get_html(self.minimal_options_general_ledger)

    def test_03_general_ledger(self):
        options = self.minimal_options_general_ledger
        GeneralLedger = self.env['account.general.ledger'].with_context(state='draft')
        GeneralLedger.with_context(GeneralLedger.set_context(options)).get_lines(options)

    def test_04_general_ledger_output_cashbasis0(self):
        def columns_get_numbers(columns_list):
            return [col.get('name') for col in columns_list]

        year = time.strftime('%Y')
        date_sale = year + '-06-26'
        date_payment = year + '-06-27'

        invoice_move = self.env['account.move'].create({
            'name': 'Invoice Move',
            'date': date_sale,
            'journal_id': self.sale_journal.id,
            'company_id': self.company.id,
        })

        # step sale
        sale_move_lines = self.env['account.move.line'].with_context(check_move_validity=False)
        sale_move_lines |= sale_move_lines.create({
            'name': 'receivable line',
            'account_id': self.account_rcv.id,
            'debit': 30.0,
            'move_id': invoice_move.id,
            'partner_id': self.partner_timmy_thomas.id,
        })
        sale_move_lines |= sale_move_lines.create({
            'name': 'product line',
            'account_id': self.account_sale.id,
            'credit': 30.0,
            'move_id': invoice_move.id,
            'partner_id': self.partner_timmy_thomas.id,
        })

        # step cost of product
        stock_move_lines = self.env['account.move.line'].with_context(check_move_validity=False)
        stock_move_lines |= stock_move_lines.create({
            'name': 'stock out line',
            'account_id': self.account_other.id,
            'credit': 5.0,
            'move_id': invoice_move.id,
            'partner_id': self.partner_timmy_thomas.id,
        })
        stock_move_lines |= stock_move_lines.create({
            'name': 'expense line',
            'account_id': self.account_expense.id,
            'debit': 5.0,
            'move_id': invoice_move.id,
            'partner_id': self.partner_timmy_thomas.id,
        })

        # step payment
        payment_move = self.env['account.move'].create({
            'name': 'payment move',
            'date': date_payment,
            'journal_id': self.payment_journal.id,
            'company_id': self.company.id,
        })

        payment_move_lines = self.env['account.move.line'].with_context(check_move_validity=False)
        payment_move_lines |= payment_move_lines.create({
            'name': 'receivable line',
            'credit': 30.0,
            'account_id': self.account_rcv.id,
            'partner_id': self.partner_timmy_thomas.id,
            'move_id': payment_move.id,
        })
        payment_move_lines |= payment_move_lines.create({
            'name': 'liquidity line',
            'debit': 30.0,
            'account_id': self.account_pay.id,
            'partner_id': self.partner_timmy_thomas.id,
            'move_id': payment_move.id,
        })

        invoice_move.post()
        payment_move.post()
        # reconcile
        aml_to_reconcile = (payment_move_lines | sale_move_lines).filtered(lambda l: not l.reconciled and l.account_id.internal_type == 'receivable')
        aml_to_reconcile.reconcile()
        partial_reconcile = self.env['account.partial.reconcile'].search([
            ('debit_move_id', 'in', aml_to_reconcile.ids),
            ('credit_move_id', 'in', aml_to_reconcile.ids)
        ])
        # Force reconcile at date
        self.env.cr.execute('UPDATE account_partial_reconcile SET create_date = %(date)s WHERE id in %(partial_ids)s',
            {'date': date_payment + ' 00:00:00',
             'partial_ids': tuple(partial_reconcile.ids)})

        # Build the report
        # With floats for numbers instead of currency formatted string
        GeneralLedger = self.env['account.general.ledger'].with_context(no_format=True, state='posted')
        journals_to_check = self.sale_journal + self.payment_journal
        options = {
            'date': {
                'date_from': date_sale,
                'date_to': date_sale,
            },
            'cash_basis': True,
            'unfolded_lines': [],
            'journals': [
                {'id': j.id, 'name': j.name, 'code': j.code, 'type': j.type, 'selected': True}
                for j in journals_to_check
            ],
        }

        # CASH BASIS TEST
        # Before Payment Date
        gl_lines_sale_cb = GeneralLedger.with_context(GeneralLedger.set_context(options)).get_lines(options)
        self.assertEqual(len(gl_lines_sale_cb), 0,
            'In cash basis, the general ledger before the payment date should be empty')

        # After Payment Date
        options['date']['date_to'] = date_payment
        gl_lines_pay_cb = GeneralLedger.with_context(GeneralLedger.set_context(options)).get_lines(options)
        self.assertEqual(len(gl_lines_pay_cb), 5,
            'In cash basis, the general ledger should contain 5 lines after payment date')

        for line in gl_lines_pay_cb:
            name = line['name']
            columns = columns_get_numbers(line['columns'][1:])  # just keep debit, credit and balance
            if name == '001 RCV':
                self.assertEqual(columns, [30.0, 30.0, 0.0])
            elif name == '002 SALE':
                self.assertEqual(columns, [0.0, 30.0, -30.0])
            elif name == '003 EXP':
                self.assertEqual(columns, [5.0, 0.0, 5.0])
            elif name == '004 PAY':
                self.assertEqual(columns, [30.0, 0.0, 30.0])
            elif name == '005 OTHER':
                self.assertEqual(columns, [0.0, 5.0, -5.0])

        # ACCRUAL TEST
        # Before Payment Date
        options['date']['date_to'] = date_sale
        options['cash_basis'] = False
        gl_lines_sale_acc = GeneralLedger.with_context(GeneralLedger.set_context(options)).get_lines(options)

        self.assertEqual(len(gl_lines_sale_acc), 4,
            'In accrual, the general ledger should contain 4 lines before payment date')

        for line in gl_lines_sale_acc:
            name = line['name']
            columns = columns_get_numbers(line['columns'][1:])
            if name == '001 RCV':
                self.assertEqual(columns, [30.0, 0.0, 30.0])
            elif name == '002 SALE':
                self.assertEqual(columns, [0.0, 30.0, -30.0])
            elif name == '003 EXP':
                self.assertEqual(columns, [5.0, 0.0, 5.0])
            elif name == '005 OTHER':
                self.assertEqual(columns, [0.0, 5.0, -5.0])

        # After payment Date
        options['date']['date_to'] = date_payment
        options['cash_basis'] = False
        gl_lines_pay_acc = GeneralLedger.with_context(GeneralLedger.set_context(options)).get_lines(options)

        self.assertEqual(len(gl_lines_pay_acc), 5,
            'In accrual, the general ledger should contain 5 lines after payment date')

        for line in gl_lines_pay_acc:
            name = line['name']
            columns = columns_get_numbers(line['columns'][1:])
            if name == '001 RCV':
                self.assertEqual(columns, [30.0, 30.0, 0.0])
            elif name == '002 SALE':
                self.assertEqual(columns, [0.0, 30.0, -30.0])
            elif name == '003 EXP':
                self.assertEqual(columns, [5.0, 0.0, 5.0])
            elif name == '004 PAY':
                self.assertEqual(columns, [30.0, 0.0, 30.0])
            elif name == '005 OTHER':
                self.assertEqual(columns, [0.0, 5.0, -5.0])

    def test_05_followup_multicompany(self):
        date_sale = fields.Date.today()

        # Company 0
        invoice_move = self.env['account.move'].create({
            'name': 'Invoice Move',
            'date': date_sale,
            'journal_id': self.sale_journal.id,
            'company_id': self.company.id,
        })

        sale_move_lines = self.env['account.move.line'].with_context(check_move_validity=False)
        sale_move_lines |= sale_move_lines.create({
            'name': 'receivable line',
            'account_id': self.account_rcv.id,
            'debit': 30.0,
            'move_id': invoice_move.id,
            'partner_id': self.partner_timmy_thomas.id,
        })
        sale_move_lines |= sale_move_lines.create({
            'name': 'product line',
            'account_id': self.account_sale.id,
            'credit': 30.0,
            'move_id': invoice_move.id,
            'partner_id': self.partner_timmy_thomas.id,
        })

        # Company 1
        company1 = self.env['res.company'].create({'name': 'company1'})
        self.env.user.write({
            'company_ids': [(4, company1.id, False)],
        })

        account_sale1 = self.account_sale.copy({'company_id': company1.id})
        sale_journal1 = self.sale_journal.copy({
            'company_id': company1.id,
            'default_debit_account_id': account_sale1.id,
            'default_credit_account_id': account_sale1.id,
        })
        account_rcv1 = self.account_rcv.copy({'company_id': company1.id})

        invoice_move1 = self.env['account.move'].create({
            'name': 'Invoice Move',
            'date': date_sale,
            'journal_id': sale_journal1.id,
            'company_id': company1.id,
        })

        sale_move_lines.create({
            'name': 'receivable line',
            'account_id': account_rcv1.id,
            'debit': 60.0,
            'move_id': invoice_move1.id,
            'partner_id': self.partner_timmy_thomas.id,
        })
        sale_move_lines.create({
            'name': 'product line',
            'account_id': account_sale1.id,
            'credit': 60.0,
            'move_id': invoice_move1.id,
            'partner_id': self.partner_timmy_thomas.id,
        })

        invoice_move.post()
        invoice_move1.post()

        # For company 0
        self.env.user.company_id = self.company
        currency = self.company.currency_id
        self.assertEqual(self.partner_timmy_thomas.credit, 30.0)

        options = dict(self.minimal_options)
        options['partner_id'] = self.partner_timmy_thomas.id

        lines = self.env['account.followup.report'].get_lines(options)

        # Title line + actual business line
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[1]['class'], 'total')
        self.assertEqual(len(lines[1]['columns']), 6)

        self.assertEqual(lines[1]['columns'][4]['name'], 'Total Due')
        self.assertEqual(lines[1]['columns'][5]['name'], formatLang(self.env, 30.00, currency_obj=currency))

        # For company 1
        self.env.user.company_id = company1
        currency = company1.currency_id
        self.env.cache.invalidate()
        self.assertEqual(self.partner_timmy_thomas.credit, 60.0)

        lines = self.env['account.followup.report'].get_lines(options)

        # Title line + actual business line
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[1]['class'], 'total')
        self.assertEqual(len(lines[1]['columns']), 6)

        self.assertEqual(lines[1]['columns'][4]['name'], 'Total Due')
        self.assertEqual(lines[1]['columns'][5]['name'], formatLang(self.env, 60.00, currency_obj=currency))
