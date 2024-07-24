from flectra.addons import decimal_precision as dp
from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime
from flectra.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from flectra.tools import float_round

class MarelInSamlpeBom1(models.Model):
    _inherit = ['mrp.bom']

    toleransi_antislip = fields.Float(string='Toleransi Antislip (%)',)
    
    
class MarelInSamlpeBomLine1(models.Model):
    _inherit = ['mrp.bom.line']

    @api.multi
    def get_hitung_qty_mrp_bom_line(self):
        self.qty_bom_reguler = 0.0
        self.qty_bom_soccer = 0.0
        #mengconvert dari gr ke kg
        self.qty_benang_kg = (self.qty_benang_gr/1000)
        #perhitungan toleransi
        toleransi_qty_bom_r = (self.qty_benang_kg*0.07)
        toleransi_qty_bom_s = (self.qty_benang_kg*0.15)
        #qty bom kaos kaki
        self.qty_bom_reguler = (self.qty_benang_kg + toleransi_qty_bom_r)
        self.qty_bom_soccer = (self.qty_benang_kg + toleransi_qty_bom_s)

        if (self.bom_id.janis_kk_id.id == 1 and self.operation_id.workcenter_id.id != 5):
            self.product_qty = self.qty_bom_reguler
        elif (self.bom_id.janis_kk_id.id == 2 and self.operation_id.workcenter_id.id != 5):
            self.product_qty = self.qty_bom_soccer
        elif (self.operation_id.workcenter_id.id == 5):
            self.product_qty = (self.qty_benang_gr + (((self.bom_id.toleransi_antislip)/100)*self.qty_benang_gr))/1000
