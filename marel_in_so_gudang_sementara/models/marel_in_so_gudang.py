
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError


class MarelInSoGudang(models.Model): 
    _inherit = 'stock.picking'

    
    # so_sementara = fields.Many2one('sale.order',string=u'No SO',)
    
    so_sementara = fields.Many2one('sale.order',string=u'No SO',)