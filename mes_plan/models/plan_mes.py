from flectra import api, fields, models, _
from flectra.exceptions import UserError

#--------------------------------- class baru -----------------------------------------------
class InPlanMes(models.Model):
    _description = "Plan MES "
    _name = "plan.mes"
    #_rec_name = "no_mo"

    kode_plan_mesin = fields.Char(string='Kode Plan Mesin',required=True)
    no_kp = fields.Many2one('mrp.production',string='No KP/MO')
    nama_template = fields.Many2one(related='no_kp.product_tmpl_id',string='Nama Barang', readonly=True,)
    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)
    real_date_start = fields.Date(string="Real Start Date",)
    real_date_end = fields.Date(string="Real End Date",)
