from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

class InMarelKodeDokumenSuratJalan(models.Model):
    _inherit = 'stock.picking'
    
    tgl_kirim = fields.Date(string=u'Tgl Kirim',store=True)

class MarelInStockMove(models.Model):
    _inherit = 'stock.move'
    
    keterangan_move = fields.Text(string=u'Keterangan',store=True)
    rb= fields.Integer(string=u'RB',store=True)
    rk= fields.Integer(string=u'RK',store=True)
    rijek= fields.Integer(string=u'Rijek',store=True)
    noorder = fields.Char('No Order',store=True)
    

class MarelInStockMove(models.Model):
    _inherit = 'stock.move.line'
    
    keterangan_move_line = fields.Text(string=u'Keterangan',store=True)