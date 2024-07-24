from flectra import api, fields, models, _
from datetime import datetime

class MarelInResUser(models.Model):
    # _name = 'res.partner'
    _inherit = 'res.partner'    

    #product
    nik = fields.Char(string='NIK',)
    no_fak = fields.Char(string='No FAK',)
    attn = fields.Char(string='Attn',)