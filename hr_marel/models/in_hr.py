
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

class Employee(models.Model):
    _inherit = "hr.employee"


    nik = fields.Char(string="NIK")
    pendidikan = fields.Selection([
                        ("sd",_("SD")),
                        ("smp",_("SMP")),
                        ("sma_smk",_("SMA/SMK")),
                        ('d1',_("Sarjana D1")),
                        ('d2',_("Sarjana D2")),
                        ('d3',_("Sarjana D3")),
                        ("s1",_("Sarjana S1")),
                        ("s2",_("Sarjana S2")),], string= "Pendidikan")
    studi = fields.Char(string = "Program Studi")
    start_kerja = fields.Datetime(string="Mulai Kerja")
    jml_anak = fields.Integer(string="Jumlah Anak")
    ibu_kandung = fields.Char(string = "Ibu Kandung")
    religi = fields.Selection([
        ("islam",_("Islam")),
        ("kristen",_("Kristen")),
        ("khatolik",_("Khatolik")),
        ("hindu",_("Hindu")),
        ("budha",_("Budha")),
        ("other",_("Other")),], string="Agama")
    alamat = fields.Char(strig="Alamat")
    desa = fields.Char(string="Desa")
    rt_rw = fields.Char(string="Rt/Rw")
    kec = fields.Char(string="Kecamatan")
    kab = fields.Char(string="Kabupaten")