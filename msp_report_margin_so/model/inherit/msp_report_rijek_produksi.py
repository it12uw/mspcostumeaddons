from flectra import models, fields, api, _
import logging
# _logger = logging.getLogger(__name__)


class MspReportRijekProduksiReport(models.AbstractModel):
    """
    Class untuk Custom Data Report sebelum di render ke dalam template
    """
    _name = 'report.msp_report_margin_so.report_jumlah_rijek_produksi'

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
        
        mo = self.env['mrp.production'].browse(docids)

        # Ambil data mo yg akan ditampilan di report, dimasukan ke dict dengan key id 
        # agar product dengan nama tidak tertumpuk
        # karena dikelompokkan oleh id

# ---------------------------------------------------------------------------------work center 1
        data = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 1:
                    if record.workcenter_id.id in data:
                        data[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data[record.workcenter_id.id]['singker'] += record.total_singker
                        data[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data[record.workcenter_id.id]['terry'] += record.total_terry
                        data[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data[record.workcenter_id.id]['belang'] += record.total_belang
                        data[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
        # masukkan ke dalam list tanpa key untuk mempermudah sorting
        # bisa di improve dengan library Pandas (untuk olah data) dan Jinja (templating report) agar lebih efektif
        data_without_key = []
        for key in data:
            data_without_key.append(data[key])
# ---------------------------------------------------------------------------------work center 2
        data_2 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 2:
                    if record.workcenter_id.id in data_2:
                        data_2[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_2[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_2[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_2[record.workcenter_id.id]['singker'] += record.total_singker
                        data_2[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_2[record.workcenter_id.id]['terry'] += record.total_terry
                        data_2[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_2[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_2[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_2[record.workcenter_id.id]['belang'] += record.total_belang
                        data_2[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_2[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_2[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_2[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_2[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_2[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_2[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_2[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_2[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_2[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_2[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
#                     #     data[record.workcenter_id.id] = {'name': record.workcenter_id.name, 'qty': record.product_uom_qty,'qty_pair': record.product_uom_qty,'stock': record.workcenter_id.qty_available}
#         # masukkan ke dalam list tanpa key untuk mempermudah sorting
#         # bisa di improve dengan library Pandas (untuk olah data) dan Jinja (templating report) agar lebih efektif
        data_without_key_2 = []
        for key in data_2:
            data_without_key_2.append(data_2[key])

# # ---------------------------------------------------------------------------------work center 3
        data_3 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 3:
                    if record.workcenter_id.id in data_3:
                        data_3[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_3[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_3[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_3[record.workcenter_id.id]['singker'] += record.total_singker
                        data_3[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_3[record.workcenter_id.id]['terry'] += record.total_terry
                        data_3[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_3[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_3[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_3[record.workcenter_id.id]['belang'] += record.total_belang
                        data_3[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_3[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_3[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_3[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_3[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_3[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_3[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_3[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_3[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_3[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_3[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
        # masukkan ke dalam list tanpa key untuk mempermudah sorting
        # bisa di improve dengan library Pandas (untuk olah data) dan Jinja (templating report) agar lebih efektif
        data_without_key_3 = []
        for key in data_3:
            data_without_key_3.append(data_3[key])

# # ---------------------------------------------------------------------------------work center 4
        data_4 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 4:
                    if record.workcenter_id.id in data_4:
                        data_4[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_4[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_4[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_4[record.workcenter_id.id]['singker'] += record.total_singker
                        data_4[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_4[record.workcenter_id.id]['terry'] += record.total_terry
                        data_4[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_4[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_4[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_4[record.workcenter_id.id]['belang'] += record.total_belang
                        data_4[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_4[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_4[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_4[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_4[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_4[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_4[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_4[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_4[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_4[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_4[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
        data_without_key_4 = []
        for key in data_4:
            data_without_key_4.append(data_4[key])

# ---------------------------------------------------------------------------------work center 5
        data_5 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 5:
                    if record.workcenter_id.id in data_5:
                        data_5[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_5[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_5[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_5[record.workcenter_id.id]['singker'] += record.total_singker
                        data_5[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_5[record.workcenter_id.id]['terry'] += record.total_terry
                        data_5[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_5[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_5[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_5[record.workcenter_id.id]['belang'] += record.total_belang
                        data_5[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_5[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_5[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_5[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_5[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_5[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_5[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_5[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_5[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_5[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_5[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
        data_without_key_5 = []
        for key in data_5:
            data_without_key_5.append(data_5[key])
# ---------------------------------------------------------------------------------work center 6
        data_6 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 6:
                    if record.workcenter_id.id in data_6:
                        data_6[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_6[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_6[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_6[record.workcenter_id.id]['singker'] += record.total_singker
                        data_6[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_6[record.workcenter_id.id]['terry'] += record.total_terry
                        data_6[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_6[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_6[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_6[record.workcenter_id.id]['belang'] += record.total_belang
                        data_6[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_6[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_6[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_6[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_6[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_6[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_6[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_6[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_6[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_6[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_6[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
        data_without_key_6 = []
        for key in data_6:
            data_without_key_6.append(data_6[key])
# ---------------------------------------------------------------------------------work center 7
        data_7 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 7:
                    if record.workcenter_id.id in data_7:
                        data_7[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_7[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_7[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_7[record.workcenter_id.id]['singker'] += record.total_singker
                        data_7[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_7[record.workcenter_id.id]['terry'] += record.total_terry
                        data_7[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_7[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_7[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_7[record.workcenter_id.id]['belang'] += record.total_belang
                        data_7[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_7[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_7[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_7[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_7[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_7[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_7[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_7[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_7[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_7[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_7[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}

        data_without_key_7 = []
        for key in data_7:
            data_without_key_7.append(data_7[key])

# # ---------------------------------------------------------------------------------work center 8
        data_8 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 8:
                    if record.workcenter_id.id in data_8:
                        data_8[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_8[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_8[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_8[record.workcenter_id.id]['singker'] += record.total_singker
                        data_8[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_8[record.workcenter_id.id]['terry'] += record.total_terry
                        data_8[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_8[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_8[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_8[record.workcenter_id.id]['belang'] += record.total_belang
                        data_8[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_8[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_8[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_8[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_8[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_8[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_8[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_8[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_8[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_8[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_8[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
        data_without_key_8 = []
        for key in data_8:
            data_without_key_8.append(data_8[key])

# ---------------------------------------------------------------------------------work center 9
        data_9 = {}
        for order in mo:
            for record in order.workorder_ids:
                if record.workcenter_id.id == 9:
                    if record.workcenter_id.id in data_9:
                        data_9[record.workcenter_id.id]['putus_benang'] += record.total_putus_benang
                        data_9[record.workcenter_id.id]['bolong'] += record.total_bolong
                        data_9[record.workcenter_id.id]['vanise'] += record.total_vanise
                        data_9[record.workcenter_id.id]['singker'] += record.total_singker
                        data_9[record.workcenter_id.id]['kotor'] += record.total_kotor
                        data_9[record.workcenter_id.id]['terry'] += record.total_terry
                        data_9[record.workcenter_id.id]['jumpstich'] += record.total_jumpstich
                        data_9[record.workcenter_id.id]['renggang'] += record.total_renggang
                        data_9[record.workcenter_id.id]['tidak_loading'] += record.total_tidak_loading
                        data_9[record.workcenter_id.id]['belang'] += record.total_belang
                        data_9[record.workcenter_id.id]['ukuran'] += record.total_ukuran
                        data_9[record.workcenter_id.id]['lingtu'] += record.total_lingtu
                        data_9[record.workcenter_id.id]['pecah'] += record.total_pecah
                        data_9[record.workcenter_id.id]['loncat'] += record.total_loncat
                        data_9[record.workcenter_id.id]['gumpal'] += record.total_gumpal
                        data_9[record.workcenter_id.id]['kasar'] += record.total_kasar
                        data_9[record.workcenter_id.id]['benang_gabung'] += record.total_benang_gabung
                        data_9[record.workcenter_id.id]['bintik_bintik'] += record.total_bintik_bintik
                        data_9[record.workcenter_id.id]['jarum'] += record.total_jarum
                        data_9[record.workcenter_id.id]['transfer_jebol'] += record.total_transfer_jebol
                    else:
                        data_9[record.workcenter_id.id] ={'name': record.workcenter_id.name,'putus_benang': record.total_putus_benang,'bolong': record.total_bolong,'vanise': record.total_vanise,'singker': record.total_singker,'kotor': record.total_kotor,'terry': record.total_terry,'jumpstich': record.total_jumpstich,'renggang': record.total_renggang,'tidak_loading': record.total_tidak_loading,'belang': record.total_belang,'ukuran': record.total_ukuran,'lingtu': record.total_lingtu,'pecah': record.total_pecah,'loncat': record.total_loncat,'gumpal': record.total_gumpal,'kasar': record.total_kasar,'benang_gabung': record.total_benang_gabung,'bintik_bintik': record.total_bintik_bintik,'jarum': record.total_jarum,'transfer_jebol': record.total_transfer_jebol}
        data_without_key_9 = []
        for key in data_9:
            data_without_key_9.append(data_9[key])

        docargs = {
            'mo' : ", ".join(order.name for order in mo),
            # 'delivery_date' : ", ".join(order.procurement_group_id.sale_id.delivery_date for order in mo),
            # 'no_so' : ", ".join(order.procurement_group_id.sale_id.name for order in mo),
            # 'kode_dokumen_bom' : ", ".join(order.kode_dokumen_bagian_id.kode_dokumen_bom for order in mo),
            # 'halaman_bom' : ", ".join(order.kode_dokumen_bagian_id.halaman_bom for order in mo),
            # 'no_revisi_bom' : ", ".join(order.kode_dokumen_bagian_id.no_revisi_bom for order in mo),
            # 'tgl_revisi_bom' : ", ".join(order.kode_dokumen_bagian_id.tgl_revisi_bom for order in mo),
            # 'tgl_efektif_bom' : ", ".join(order.kode_dokumen_bagian_id.tgl_efektif_bom for order in mo),
            'data': sorted(data_without_key, key=lambda key: key['name']), # sorting by name
            'data_2': sorted(data_without_key_2, key=lambda key: key['name']), # sorting by name
            'data_3': sorted(data_without_key_3, key=lambda key: key['name']), # sorting by name
            'data_4': sorted(data_without_key_4, key=lambda key: key['name']), # sorting by name
            'data_5': sorted(data_without_key_5, key=lambda key: key['name']), # sorting by name
            'data_6': sorted(data_without_key_6, key=lambda key: key['name']), # sorting by name
            'data_7': sorted(data_without_key_7, key=lambda key: key['name']), # sorting by name
            'data_8': sorted(data_without_key_8, key=lambda key: key['name']), # sorting by name
            'data_9': sorted(data_without_key_9, key=lambda key: key['name']) # sorting by name
        }

        # return self.env["report"].render('manufacturing_bom_report_new.report_mrpbomorder_new', docargs)
        return docargs
            