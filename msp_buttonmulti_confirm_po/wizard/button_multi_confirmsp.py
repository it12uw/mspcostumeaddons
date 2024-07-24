# -*- coding: utf-8 -*-
from flectra import models, api, _
from flectra.exceptions import UserError


class ButtonMultiConfirmSp(models.TransientModel):
    """
    This wizard will confirm the all the selected draft invoices
    """

    _name = "stock.picking.confirm"
    _description = "Confirm the selected Stock Picking"

    @api.multi
    def sp_multi_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for record in self.env['stock.picking'].browse(active_ids):
            if record.state != 'assigned':
                raise UserError(_("Selected Stock Picking(s) cannot be confirmed as they are not in 'In Progress' state."))
            record.button_validate()
        return {'type': 'ir.actions.act_window_close'}