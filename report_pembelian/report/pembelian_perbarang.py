from flectra import models, fields, api, _
from datetime import datetime
from flectra.exceptions import UserError

class PembelianBarang(models.Model):
    _name = 'pem.bar'

    name = fields.Char(string='Report', required=True, )
    date_start = fields.Datetime(string="Tanggal Awal", required=True, )
    date_end = fields.Datetime(string="Tanggal Akhir", required=True, )
    company_id = fields.Many2one('res.company')
    report_ids = fields.One2many('pembel.line', 'report_id', string="Headre Report")
    # produk = fields.Many2one('product.product', string='Produk')
    # categ_id = fields.Integer(string='Kategori Produk', )
    # kategory = fields.Many2many('product.category', string='Produk Kategori')
    
    # @api.onchange('kategory')
    # def _onchange_categ_id(self):
    #     if self.kategory:
    #         self.categ_id = self.kategory
    
    @api.multi
    def generate_report(self):
        sql = """select po.id,
                        po.name,
                        pt.name, 
                        pu.name, 
                        po.amount_total
                        from purchase_order po
                        join purchase_order_line pol on pol.order_id = po.id
                        join product_product pp on pol.product_id = pp.id
                        join product_template pt on pp.product_tmpl_id = pt.id
                        join product_uom pu on pt.uom_id = pu.id
                        where po.state = 'purchase' and po.create_date between %s and %s
                        GROUP BY po.id,pp.id, pt.id, pu.id
            """
        # qc = """Select pc.id 
        # form product_category pc
        # where pc.id in (%s)
        #     """
        # import pdb; pdb.set_trace()
        cr = self.env.cr

        cr.execute(sql,(self.date_start, self.date_end))
        result = cr.fetchall()

        sql = 'delete from pembel_line where report_id=%s'
        cr.execute(sql, (self.id,))

        for res in result:
            lis = self.env['pembel.line']
            lis.create({
                #isi field2 yang di line tapi disesuaikan dengan tabel atau querimya
                'report_id' : self.id,
                'po_name': res[1],
                'nama_produk': res[2],
                'uom': res[3],
                'tot_biaya': res[4],
                # 'selisih_date': res[6],
            })
    

    @api.multi
    def print_report(self):
        return self.env.ref('report_pembelian.qweb_pembelian_perbarang') .report_action(self)



class PembelianBarangLine(models.Model):
    _name = 'pembel.line'

    # report_id = fields.Many2one('rep.per', string="Report Line")
    #isiian dari report2
    report_id = fields.Many2one('pem.bar', string="Report Line")
    product_id = fields.Many2one('product.template',string="Nama Produk")
    po_name = fields.Char(string="No PO")
    nama_produk = fields.Char(string='Nama Produk')
    uom = fields.Char(string="Satuan")
    tot_biaya = fields.Float(string="Total Biaya", store=True)
    # date_po = fields.Date(string="Tgl PO")
    # date_request = fields.Date(string="Tgl Request")
    # selisih_date = fields.Integer(string="Waktu PO")
    # qty = fields.Float(string="Jumlah", store=True)
    # uom = fields.Char(string="Satuan")
    # br_rata = fields.Float(string='Biaya Rata-rata')
    # br_terakhir = fields.Float(string="Biaya Terakhir")
    # tot_biaya = fields.Float(string="Total Biaya", store=True)
    # complete_name = fields.Char(string="Categori")