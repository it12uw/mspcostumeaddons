from flectra import models, fields, api, _
from flectra.exceptions import UserError, ValidationError

class InMarelKodeDokumenMrp(models.Model):
    _name = 'inmarel.kode.dokumen.mrp'
    _rec_name = 'kode_dokumen_bagian'

    kode_dokumen_bagian = fields.Char(string=u'Kode Dokumen', required=True)
    #------------------------ kkp ----------------------
    kode_dokumen_kkp = fields.Char(string=u'Kode Dokumen',)
    halaman_kkp = fields.Char(string=u'Halaman',)
    no_revisi_kkp = fields.Char(string=u'No Revisi',)
    tgl_revisi_kkp = fields.Date(string=u'Tgl Revisi',)
    tgl_efektif_kkp = fields.Date(string=u'Tgl Efektif',)
    # ----------------------- bom -----------------------
    kode_dokumen_bom = fields.Char(string=u'Kode Dokumen',)
    halaman_bom = fields.Char(string=u'Halaman',)
    no_revisi_bom = fields.Char(string=u'No Revisi',)
    tgl_revisi_bom = fields.Date(string=u'Tgl Revisi',)
    tgl_efektif_bom = fields.Date(string=u'Tgl Efektif',)
    # ----------------------- production order ------------------
    kode_dokumen_production_order_so = fields.Char(string=u'Kode Dokumen',)
    halaman_production_order_so = fields.Char(string=u'Halaman',)
    no_revisi_production_order_so = fields.Char(string=u'No Revisi',)
    tgl_revisi_production_order_so = fields.Date(string=u'Tgl Revisi',)
    tgl_efektif_production_order_so = fields.Date(string=u'Tgl Efektif',)

class InMarelKodeDokumenManufak(models.Model):
    _inherit = ['mrp.production']

    kode_dokumen_bagian_id = fields.Many2one('inmarel.kode.dokumen.mrp',string=u'Kode Dokumen',)

class MarelInKodeDokumenPo(models.Model):
    _name = 'inmarel.kode.dokumen.po'    
    _rec_name = 'kode_dokumen_bagian_po'

    kode_dokumen_bagian_po = fields.Char(string=u'Kode Dokumen', required=True)
    #------------------------ PO ----------------------
    kode_dokumen_po = fields.Char(string=u'Kode Dokumen',)
    halaman_po = fields.Char(string=u'Halaman',)
    no_revisi_po = fields.Char(string=u'No Revisi',)
    tgl_revisi_po = fields.Date(string=u'Tgl Revisi',)
    tgl_efektif_po = fields.Date(string=u'Tgl Efektif',)


class InMarelKodeDokumenPurchase(models.Model):
    _inherit = ['purchase.order']

    kode_dokumen_bagian_po_id = fields.Many2one('inmarel.kode.dokumen.po',string=u'Kode Dokumen',)

class MarelInKodeDokumenSj(models.Model):
    _name = 'inmarel.kode.dokumen.sj'    
    _rec_name = 'kode_dokumen_bagian_sj'

    kode_dokumen_bagian_sj = fields.Char(string=u'Kode Dokumen', required=True)
    #------------------------ SJ ----------------------
    kode_dokumen_sj = fields.Char(string=u'Kode Dokumen',)
    halaman_sj = fields.Char(string=u'Halaman',)
    no_revisi_sj = fields.Char(string=u'No Revisi',)
    tgl_revisi_sj = fields.Date(string=u'Tgl Revisi',)
    tgl_efektif_sj = fields.Date(string=u'Tgl Efektif',)


class InMarelKodeDokumenSuratJalan(models.Model):
    _inherit = ['stock.picking']

    kode_dokumen_bagian_sj_id = fields.Many2one('inmarel.kode.dokumen.sj',string=u'Kode Dokumen',)
    
    # --------------- kode invoice
class MarelInKodeDokumenInvoice(models.Model):
    _name = 'inmarel.kode.dokumen.invoice'    
    _rec_name = 'kode_dokumen_bagian_invoice'

    kode_dokumen_bagian_invoice = fields.Char(string=u'Kode Dokumen', required=True)
    #------------------------ invoice ----------------------
    kode_dokumen_invoice = fields.Char(string=u'Kode Dokumen',)
    halaman_invoice = fields.Char(string=u'Halaman',)
    no_revisi_invoice = fields.Char(string=u'No Revisi',)
    tgl_revisi_invoice = fields.Date(string=u'Tgl Revisi',)
    tgl_efektif_invoice = fields.Date(string=u'Tgl Efektif',)

class InMarelKodeDokumenInvoice(models.Model):
    _inherit = ['account.invoice']
    
    kode_dokumen_bagian_invoice_id = fields.Many2one('inmarel.kode.dokumen.invoice',string=u'Kode Dokumen',)
