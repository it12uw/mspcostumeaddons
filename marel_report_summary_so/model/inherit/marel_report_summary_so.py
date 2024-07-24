from flectra import models, fields, api, _
import logging
# _logger = logging.getLogger(__name__)


class MarelReportSummarySo(models.AbstractModel):
    """
    Class untuk Custom Data Report sebelum di render ke dalam template
    """
    _name = 'report.marel_report_summary_so.report_selisih_harga_kk'

    @api.model
    def get_report_values(self, docids, data=None):
        """
        Method default custom reporting odoo untuk custom data

        params:
            - docids = id record model yg akan digenerate didalam report
            - data = biasanya digunakan untuk custom report dengan data dari Wizard
        """
        # report_obj = self.env['report']
        # report = report_obj._get_report_from_name('manufacturing_bom_report.report_mrpbomorder')
        
        so = self.env['sale.order'].browse(docids)

        # Ambil data mo yg akan ditampilan di report, dimasukan ke dict dengan key id 
        # agar product dengan nama tidak tertumpuk
        # karena dikelompokkan oleh id
        data = {}
        for order in so:
            for record in order.order_line:
                if record.product_id.product_tmpl_id.categ_id.id==3:
                    if record.product_id.id in data:
                        data[record.product_id.id]['qty'] += record.product_uom_qty
                        data[record.product_id.id]['standard_price'] == record.product_id.standard_price
                        data[record.product_id.id]['price_unit'] == record.price_unit
                    else:
                        data[record.product_id.id] = {'name': record.product_id.name,'nomer_so': record.order_id.name,'standard_price':record.product_id.standard_price,'qty': record.product_uom_qty,'price_unit':record.price_unit}
        # masukkan ke dalam list tanpa key untuk mempermudah sorting
        # bisa di improve dengan library Pandas (untuk olah data) dan Jinja (templating report) agar lebih efektif
        data_without_key = []
        for key in data:
            data_without_key.append(data[key])


        #, 'delivery_date': record.production_id.
        docargs = {
            'so' : ", ".join(order.name for order in so),
            # 'nomer_so' : ", ".join(order.order_id.name for order in so),
            # 'no_so' : ", ".join(order.procurement_group_id.sale_id.name for order in mo),
            # 'kode_dokumen_bom' : ", ".join(order.kode_dokumen_bagian_id.kode_dokumen_bom for order in mo),
            # 'halaman_bom' : ", ".join(order.kode_dokumen_bagian_id.halaman_bom for order in mo),
            # 'no_revisi_bom' : ", ".join(order.kode_dokumen_bagian_id.no_revisi_bom for order in mo),
            # 'tgl_revisi_bom' : ", ".join(order.kode_dokumen_bagian_id.tgl_revisi_bom for order in mo),
            # 'tgl_efektif_bom' : ", ".join(order.kode_dokumen_bagian_id.tgl_efektif_bom for order in mo),
            'data': sorted(data_without_key, key=lambda key: key['name']) # sorting by name
        }

        # return self.env["report"].render('manufacturing_bom_report_new.so_report_act', docargs)
        return docargs