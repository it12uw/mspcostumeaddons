# -*- coding: utf-8 -*-
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flectra import api, fields, models, _
from flectra.exceptions import UserError


class ButtonMultiConfirmPo(models.TransientModel):
    """
    This wizard will confirm the all the selected draft invoices
    """

    _name = "purchase.order.confirm"
    _description = "Confirm the selected invoices"

    @api.multi
    def po_multi_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for record in self.env['purchase.order'].browse(active_ids):
            if record.state != 'draft':
                raise UserError(_("Selected Puchases(s) cannot be confirmed as they are not in 'Draft' state."))
            record.button_confirm()
        return {'type': 'ir.actions.act_window_close'}

class ButtonMultiDonePo(models.TransientModel):
    """
    This wizard will confirm the all the selected draft invoices
    """

    _name = "purchase.order.done"
    _description = "Done PO"

    @api.multi
    def po_multi_done(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for record in self.env['purchase.order'].browse(active_ids):
            if record.state != 'purchase':
                raise UserError(_("Selected Puchases(s) cannot be confirmed as they are not in 'Order' state."))
            record.button_done()
        return {'type': 'ir.actions.act_window_close'}