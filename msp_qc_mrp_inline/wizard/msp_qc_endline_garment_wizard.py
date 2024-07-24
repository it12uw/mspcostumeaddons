from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError
from datetime import date, datetime

# --------------------------- inline 20 ----------------------------------------------------
# class MspMayorMinor1Wizard(models.TransientModel):
#     _name = "msp.mayor.minor1"

    # name = fields.Char(string='name',)
    

class MspQcIEndlineGarmentWizard(models.TransientModel):
    _name = "msp.qcendline.garment.wizard"

    def _default_msp_qcendline_garment_wizard(self):
        return self.env['mrp.workorder'].browse(self._context.get('active_ids'))

    name = fields.Many2one('mrp.workorder',string="Name",default=_default_msp_qcendline_garment_wizard, readonly=True, store=True,)
    tgl_create = fields.Datetime(string='Tgl Create',default=fields.Datetime.now,readonly=True,store=True,)
    inspection_date = fields.Datetime(string='Data Inspection',store=True,)
    # msp_qc_inline1_line_ids = fields.One2many('msp.qc.inline1.line','msp_qc_inline1_id',string=u'Defect Found',)
    keterangan = fields.Text(string='Keterangan',store=True,)
    name_workorder_id = fields.Many2one('mrp.workorder', string=u'No WO',store=True,)
    mrp_productioin_id = fields.Many2one(string=u'No MO', related='name.production_id', readonly=True,store=True)

    rijek_1 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 1",store=True,)

    rijek_2 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 2",store=True,)

    rijek_3 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 3",store=True,)

    rijek_4 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 4",store=True,)

    rijek_5 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 5", store=True,)

    rijek_6 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 6", store=True,)

    rijek_7 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 7",store=True,)

    rijek_8 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 8",store=True,)
    
    rijek_9 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 9",store=True,)
    
    rijek_10 = fields.Selection([
        ('collar',_('COLLAR (KRAH)')),
        ('label',_('LABEL')),
        ('front_placket',_('Front Placket (Plaket Depan)')),
        ('front',_('Front (Depan)')),
        ('pocket',_('Pocket (Kantong)')),
        ('yoke',_('Yoke (bahu)')),
        ('sleeve',_('Sleeve (lengan)')),
        ('sleeve_placket',_('Sleeve Placket (Placket Tangan)')),
        ('armhole',_('Armhole (Lingkar Lengan)')),
        ('side_seam',_('Side Seam (Klim Samping)')),
        ('cuff',_('Cuff (Manset)')),
        ('bottom_hem',_('Bottom Hem (Klim Bawah)')),
        ('bottom_hole',_('Button Hole (Lubang Kancing)')),
        ('bottom',_('Button(kancing)')),
        ('embroidery',_('Embroidery (Bordir)')),
        ('finishing',_('Finishing')),
        ], string="Rijek 10",store=True,)


    # bentuk_rijek_1 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_1 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_1 = fields.Integer(string='Nilai 1',store=True)

    # bentuk_rijek_2 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_2 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_2 = fields.Integer(string='Nilai 2',store=True)

    # bentuk_rijek_3 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_3 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_3 = fields.Integer(string='Nilai 3',store=True)

    # bentuk_rijek_4 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_4 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_4 = fields.Integer(string='Nilai 4',store=True)

    # bentuk_rijek_5 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_5 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_5 = fields.Integer(string='Nilai 5',store=True)

    # bentuk_rijek_6 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_6 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_6 = fields.Integer(string='Nilai 6',store=True)

    # bentuk_rijek_7 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_7 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_7 = fields.Integer(string='Nilai 7',store=True)

    # bentuk_rijek_8 = fields.Many2one('msp.mayor.minor1', string='bentuk_rijek')
    bentuk_rijek_8 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_8 = fields.Integer(string='Nilai 8',store=True)

    bentuk_rijek_9 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_9 = fields.Integer(string='Nilai 9',store=True)

    bentuk_rijek_10 = fields.Selection([('mayor',_('Mayor')),('minor',_('Minor')),('kritikal',_('Kritikal')),], string="Rijek", store=True,)
    nilai_rijek_10 = fields.Integer(string='Nilai 10',store=True)


    sugestion_1 = fields.Char(string='Sugestion 1',)
    sugestion_2 = fields.Char(string='Sugestion 2',)
    sugestion_3 = fields.Char(string='Sugestion 3',)
    sugestion_4 = fields.Char(string='Sugestion 4',)
    sugestion_5 = fields.Char(string='Sugestion 5',)
    sugestion_6 = fields.Char(string='Sugestion 6',)
    sugestion_7 = fields.Char(string='Sugestion 7',)
    sugestion_8 = fields.Char(string='Sugestion 8',)
    sugestion_9 = fields.Char(string='Sugestion 8',)
    sugestion_10 = fields.Char(string='Sugestion 8',)
    
    keterangan_1 = fields.Char(string='keterangan 1',)
    keterangan_2 = fields.Char(string='keterangan 2',)
    keterangan_3 = fields.Char(string='keterangan 3',)
    keterangan_4 = fields.Char(string='keterangan 4',)
    keterangan_5 = fields.Char(string='keterangan 5',)
    keterangan_6 = fields.Char(string='keterangan 6',)
    keterangan_7 = fields.Char(string='keterangan 7',)
    keterangan_8 = fields.Char(string='keterangan 8',)
    keterangan_9 = fields.Char(string='keterangan 9',)
    keterangan_10 = fields.Char(string='keterangan 10',)


    jumlah_kritikal_qc = fields.Integer(string='Jumlah Kritikal',store=True)
    jumlah_mayor_qc = fields.Integer(string='Jumlah Mayor',store=True)
    jumlah_minor_qc = fields.Integer(string='Jumlah Minor',store=True)

    product_qty_inline = fields.Float('Quantity To Produce',readonly=True,related='mrp_productioin_id.product_qty')
    product_qty_inline_1 = fields.Float('Quantity 1',readonly=True,related='mrp_productioin_id.product_qty')
    comment = fields.Text(string='Comment',store=True)
    partner_id = fields.Many2one('res.partner', string='Customer', )

    # inspection_result = fields.Selection([
    #     ('release',_('Release')),
    #     ('reject',_('Reject')),
    #     ('hold',_('Hold')),
    #     ('under_guarantee',_('Under Guarantee')),
    #     ], string="Inspection Result",store=True,)
    

    @api.multi
    def msp_qc_endline_garment_wizard(self, vals):
        obj_nilai = self.env['msp.qc.endline.garment'].create({
                                                    "name_workorder_id":self.name.id,
                                                    "mrp_productioin_id":self.mrp_productioin_id.id,
                                                    "tgl_create":self.tgl_create,
                                                    "inspection_date":self.inspection_date,
                                                    "keterangan":self.keterangan,
                                                    "rijek_1":self.rijek_1,
                                                    "rijek_2":self.rijek_2,
                                                    "rijek_3":self.rijek_3,
                                                    "rijek_4":self.rijek_4,
                                                    "rijek_5":self.rijek_5,
                                                    "rijek_6":self.rijek_6,
                                                    "rijek_7":self.rijek_7,
                                                    "rijek_8":self.rijek_8,
                                                    "rijek_9":self.rijek_9,
                                                    "rijek_10":self.rijek_10,
                                                    "sugestion_1":self.sugestion_1,
                                                    "sugestion_2":self.sugestion_2,
                                                    "sugestion_3":self.sugestion_3,
                                                    "sugestion_4":self.sugestion_4,
                                                    "sugestion_5":self.sugestion_5,
                                                    "sugestion_6":self.sugestion_6,
                                                    "sugestion_7":self.sugestion_7,
                                                    "sugestion_8":self.sugestion_8,
                                                    "sugestion_9":self.sugestion_9,
                                                    "sugestion_10":self.sugestion_10,
                                                    "keterangan_1":self.keterangan_1,
                                                    "keterangan_2":self.keterangan_2,
                                                    "keterangan_3":self.keterangan_3,
                                                    "keterangan_4":self.keterangan_4,
                                                    "keterangan_5":self.keterangan_5,
                                                    "keterangan_6":self.keterangan_6,
                                                    "keterangan_7":self.keterangan_7,
                                                    "keterangan_8":self.keterangan_8,
                                                    "keterangan_9":self.keterangan_9,
                                                    "keterangan_10":self.keterangan_10,
                                                    "bentuk_rijek_1":self.bentuk_rijek_1,
                                                    "bentuk_rijek_2":self.bentuk_rijek_2,
                                                    "bentuk_rijek_3":self.bentuk_rijek_3,
                                                    "bentuk_rijek_4":self.bentuk_rijek_4,
                                                    "bentuk_rijek_5":self.bentuk_rijek_5,
                                                    "bentuk_rijek_6":self.bentuk_rijek_6,
                                                    "bentuk_rijek_7":self.bentuk_rijek_7,
                                                    "bentuk_rijek_8":self.bentuk_rijek_8,
                                                    "bentuk_rijek_9":self.bentuk_rijek_9,
                                                    "bentuk_rijek_10":self.bentuk_rijek_10,
                                                    "nilai_rijek_1":self.nilai_rijek_1,
                                                    "nilai_rijek_2":self.nilai_rijek_2,
                                                    "nilai_rijek_3":self.nilai_rijek_3,
                                                    "nilai_rijek_4":self.nilai_rijek_4,
                                                    "nilai_rijek_5":self.nilai_rijek_5,
                                                    "nilai_rijek_6":self.nilai_rijek_6,
                                                    "nilai_rijek_7":self.nilai_rijek_7,
                                                    "nilai_rijek_8":self.nilai_rijek_8,
                                                    "nilai_rijek_9":self.nilai_rijek_9,
                                                    "nilai_rijek_10":self.nilai_rijek_10,
                                                    "product_qty_inline":self.product_qty_inline,
                                                    "product_qty_inline_1":self.product_qty_inline_1,
                                                    "comment":self.comment,
                                                    "jumlah_mayor_qc":self.jumlah_mayor_qc,
                                                    "jumlah_minor_qc":self.jumlah_minor_qc,
                                                    "jumlah_kritikal_qc":self.jumlah_kritikal_qc,
                                                    # "inspection_result":self.inspection_result,
                                                    })
        return super(MspQcIEndlineGarmentWizard, self).write(vals)

