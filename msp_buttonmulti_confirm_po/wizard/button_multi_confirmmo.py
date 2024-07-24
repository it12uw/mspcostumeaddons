# -*- coding: utf-8 -*-
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from flectra import api, fields, models, _
from flectra.exceptions import UserError


class ButtonMultiConfirmMo(models.TransientModel):
    """
    This wizard will confirm the all the selected draft Manufactur
    """

    _name = "mrp.production.confirm"
    _description = "Confirm the selected Manufactur"

    @api.multi
    def mo_multi_confirm(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []

        for record in self.env['mrp.production'].browse(active_ids):
            if record.state != 'draft':
                raise UserError(_("Selected Manufactur(s) cannot be confirmed as they are not in 'Draft' state."))
            record.action_confirm()
        return {'type': 'ir.actions.act_window_close'}


class ButtonMultiConfirmMo(models.TransientModel):
    _name = "mrp.procurement.reset"
    _description = "Reset Procurement the selected Manufactur"

    @api.multi
    def mo_multi_deleted_procurement_group_id(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        obj_line = self.env['mrp.production'].browse(active_ids)

        for record in obj_line:
            if record.state != 'draft':
                raise UserError(_("Selected Manufactur(s) cannot be confirmed as they are not in 'Draft' state."))
            record.write({'procurement_group_id':''})
            record.action_confirm()
        return {'type': 'ir.actions.act_window_close'}
