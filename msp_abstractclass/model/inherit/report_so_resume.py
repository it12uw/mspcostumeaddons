from flectra import models, fields, api, _
import logging
# _logger = logging.getLogger(__name__)


class ReportSoResume(models.AbstractModel):
    """
    Class untuk Custom Data Report sebelum di render ke dalam template
    """
    _name = 'report.msp_abstractclass.marelreport_abstractclass'

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
                # if record.product_id.product_tmpl_id.categ_id.id==61 or record.product_id.product_tmpl_id.categ_id.id==3 or record.product_id.product_tmpl_id.categ_id.id==72 :
                if record.order_id.id in data:
                    data[record.order_id.id]['product_uom_qty'] == record.product_uom_qty
                    data[record.order_id.id]['price_unit'] == record.price_unit
                    data[record.order_id.id]['purchase_price'] == record.purchase_price
                else:
                        # data[record.product_id.id] = {'name': record.product_id.name, 'qty': record.product_uom_qty,'qty_pair': record.product_uom_qty,'stock': record.product_id.qty_available}
                    data[record.order_id.id] = {'name': record.order_id.name}

        # data = {}
        # for order in so:
        #     for record in order.order_line:
        #         if record.product_id.product_tmpl_id.categ_id.id==61 or record.product_id.product_tmpl_id.categ_id.id==3 or record.product_id.product_tmpl_id.categ_id.id==72 :
        #             if record.order_id.id in data:
        #                 data[record.order_id.id]['product_uom_qty'] += record.product_uom_qty
        #                 data[record.order_id.id]['price_unit'] += record.price_unit
        #                 data[record.order_id.id]['purchase_price'] += record.purchase_price
        #             else:
        #                 data[record.order_id.id] = {'name': record.order_id.name}

        # masukkan ke dalam list tanpa key untuk mempermudah sorting
        # bisa di improve dengan library Pandas (untuk olah data) dan Jinja (templating report) agar lebih efektif
        data_without_key = []
        for key in data:
            data_without_key.append(data[key])


        #, 'delivery_date': record.production_id.
        docargs = {
            'so' : ", ".join(order.name for order in so),
            # 'delivery_date' : ", ".join(order.procurement_group_id.sale_id.delivery_date for order in mo),
            # 'no_so' : ", ".join(order.procurement_group_id.sale_id.name for order in mo),
            # 'kode_dokumen_bom' : ", ".join(order.kode_dokumen_bagian_id.kode_dokumen_bom for order in mo),
            # 'halaman_bom' : ", ".join(order.kode_dokumen_bagian_id.halaman_bom for order in mo),
            # 'no_revisi_bom' : ", ".join(order.kode_dokumen_bagian_id.no_revisi_bom for order in mo),
            # 'tgl_revisi_bom' : ", ".join(order.kode_dokumen_bagian_id.tgl_revisi_bom for order in mo),
            # 'tgl_efektif_bom' : ", ".join(order.kode_dokumen_bagian_id.tgl_efektif_bom for order in mo),
            'data': sorted(data_without_key, key=lambda key: key['name']) # sorting by name
        }

        # return self.env["report"].render('manufacturing_bom_report_rekap.report_mrpbomorder_new', docargs)
        return docargs
            