# -*- coding: utf-8 -*-

from flectra import api, fields, models, _
from datetime import datetime

class PreProductionMeetingReport(models.AbstractModel):
    _name = 'report.report_meeting.report_template'
    _description = 'Pre Production Meeting Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['mrp.production'].browse(docids)
        
        return {
            'doc_ids': docids,
            'doc_model': 'mrp.production',
            'docs': docs,
            'data': data,
            'current_date': fields.Date.today(),
            'get_sale_order': self._get_sale_order,
        }
    
    def _get_sale_order(self, production):
        """Get related sale order from production"""
        sale_order = False
        if production.origin:
            sale_order = self.env['sale.order'].search([
                ('name', '=', production.origin)
            ], limit=1)
        return sale_order