# -*- coding: utf-8 -*-
from flectra import models, api, _
from flectra.exceptions import UserError


class ButtonMultiConfirmSr(models.TransientModel):
    """
    This wizard will confirm the all the selected draft invoices
    """

    _name = "stock.request.confirm"
    _description = "Confirm the selected Stock Request"

    @api.multi
    def sr_multi_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for record in self.env['stock.request'].browse(active_ids):
            if record.state != 'open':
                raise UserError(_("Selected Stock Request(s) cannot be confirmed as they are not in 'In Progress' state."))
            record.action_done()
        return {'type': 'ir.actions.act_window_close'}