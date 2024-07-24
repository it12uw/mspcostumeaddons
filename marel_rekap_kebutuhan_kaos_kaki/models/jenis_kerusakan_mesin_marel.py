# from flectra import models, fields, api, _
# from flectra.exceptions import UserError, ValidationError

# class JenisKerusakanMesinMarel(models.Model):
#     _name = 'jenis.kerusakan.mesinmarel'
#     _description = 'Jenis Kerusakan Mesin Marel'
# 	_rec_name = 'jenis_kerusakan_mesin'

#     # name = fields.Char(string='Name')
#     jenis_kerusakan_mesin = fields.Char(string="Jenis Keruskan Mesin", reqired = True,)


# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError


class JenisKerusakanMesinMarel(models.Model):
    """ The summary line for a class docstring should fit on one line.

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    _name = 'jenis.kerusakan.mesinmarel'
    _description = u'jenis kerusakan mesin marel'

    _rec_name = 'jenis_kerusakan'
    # _order = 'name ASC'

    
    jenis_kerusakan = fields.Char(string=u'jenis_kerusakan',)
    




