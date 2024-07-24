from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

class MarelPlanMesinPpic(models.Model):
    _name = 'marel.plan.mesinppic'
    _description = u'Marel Plan Mesin Ppic'
    _rec_name = 'mrp_production_ppic_id'

    mrp_production_ppic_id = fields.Many2one('mrp.production', 'Plan Mesin Ppic')
    target_per_hari = fields.Integer(string=u'Target Per Hari',)
    no_mesin_id = fields.Many2one('mesin.marel.produksi',string=u'No Mesin',)
    
    
class MarelMrpProductionPpicMesin(models.Model):
    _inherit = ['mrp.production']
    mrp_production_ppic_line = fields.One2many('marel.plan.mesinppic','mrp_production_ppic_id',string=u'Mesin Per MO/Artikel ',required=True,)