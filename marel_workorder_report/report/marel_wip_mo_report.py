from flectra import models, fields, api
from datetime import datetime, date
from flectra import http
from flectra.http import content_disposition, request
import io
import xlsxwriter
# from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT

class MarelWipMoReport(models.Model):
    _name = 'marel.wip.mo.report'
    _description = 'Marel Wip Mo Report'

    name = fields.Char(string='Report', default='Marel Wip Mo Report')
    date_start = fields.Datetime(string="Tanggal Awal", required=True, )
    date_end = fields.Datetime(string="Tanggal Akhir", required=True, )
    report_ids = fields.One2many('marel.wip.mo.report.line', 'report_id', string="Headre Report")

    # categ_id = fields.Integer(string='Kategori Produk', )
    # kategory = fields.Many2many('product.category', string='Produk Kategori')
    
    # @api.onchange('kategory')
    # def _onchange_categ_id(self):
    #     if self.kategory:
    #         self.categ_id = self.kategory


    # select 
    #                 sm.id,
    #                 mp.date_planned_start,
    #                 pt.name, 
    #                 sm.product_uom_qty
    
    def generate_report(self):
        sql = """select 
                    mnol.id,
                    mp.name,
                    mp.state,
                    mnol.tgl_kerja,
                    pt.name, 
 					mp.product_qty,
					mnol.jumlah_yg_selesai,
                    pu.name,
                    mnol.shift,
					mno.nama_operator,
					mnq.nama_qiusi,
					mmp.nama_mesin_blok,
                    mnol.krono_kk_menit
                from
                    marel_nama_operatorlist mnol
                    left join mrp_workorder mwo on mnol.nama_operator_work_order_id = mwo.id
                    join product_product pp on mwo.product_id = pp.id 
                    join product_template pt on pp.product_tmpl_id = pt.id
                    join product_category pc on pt.categ_id = pc.id
					join product_uom pu on pt.uom_id = pu.id
					left join mrp_production mp on mwo.production_id = mp.id
                    left join mesin_marel_produksi mmp on mnol.no_mesin_id = mmp.id
					left join marel_nama_operator mno on mnol.nama_operator_id = mno.id
					left join marel_nama_qiusi mnq on mnol.nama_qiusi_id = mnq.id
                where
                    mnol.tgl_kerja between %s and %s and mnol.workcenter_id = 1
                ORDER BY
                    mp.name ASC
                """
        # qc = """Select pc.id 
        # form product_category pc
        # where pc.id in (%s)
        #     """
        # import pdb; pdb.set_trace()

        # pt.categ_id = 36 or
        #             pt.categ_id = 5 or
        #             pt.categ_id = 70 or
        #             pt.categ_id = 105 or
        #             pt.categ_id = 106 or
        #             pt.categ_id = 109 and

        cr = self.env.cr

        cr.execute(sql,(self.date_start,self.date_end,))
        result = cr.fetchall()

        sql = 'delete from marel_wip_mo_report_line where report_id=%s'
        cr.execute(sql, (self.id,))

        for res in result:
            lis = self.env['marel.wip.mo.report.line']
            lis.create({
                #isi field2 yang di line tapi disesuaikan dengan tabel atau querimya
                'report_id' : self.id,
                'name': res[1],
                'state': res[2],
                'tgl_kerja': res[3],
                'product_id': res[4],
                'product_qty': res[5],
                'jumlah_yg_selesai': res[6],
                'uom_id': res[7],
                'shift': res[8],
                'nama_operator': res[9],
                'nama_qiusi': res[10],
                'nama_mesin_blok': res[11],
                'krono_kk_menit': res[12]
            })
    

    
    # def print_report(self):
    #     return self.env.ref('marel_workorder_report.marel_wip_mo_report_qweb') .report_action(self)

    def print_report_excel(self):
        return self.env.ref('marel_workorder_report.report_excel_marel_wip_mo_report') .report_action(self)




class MarelWipMoReportLine(models.Model):
    _name = 'marel.wip.mo.report.line'
    _description = 'Marel Wip Mo Report Line'


    report_id = fields.Many2one('marel.wip.mo.report', string="Report Line")

    name = fields.Char(string="MO")
    state = fields.Selection([
        ('confirmed', 'Confirmed'),
        ('planned', 'Planned'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='State',)
    tgl_kerja = fields.Date(string=u'tgl Kerja',default=fields.Date.context_today,)
    product_id = fields.Char(string='Nama Produk')
    product_qty = fields.Float('Quantity To Produce',)    
    jumlah_yg_selesai = fields.Integer(string=u'Qty Yg Selesai',)
    uom_id = fields.Char(string='UoM')
    shift = fields.Selection([
        ('A',('A')),
        ('B',('B')),
	    ('C',('C')),], string="Shift",)
    nama_operator = fields.Char(string=u'Nama Operator',)
    nama_qiusi = fields.Char(string=u'Nama Qiusi',)
    nama_mesin_blok = fields.Char(string=u'Nama Mesin',)
    krono_kk_menit = fields.Float(string=u'Krono KK (menit)')
