from flectra import api, models, fields, tools


class MarelMesinKerusakanReport(models.Model):
    _name = "marel.mesin.kerusakan.report"
    _auto = False
    
    #field yang ada di nama.teknisi
    nama_teknisi = fields.Char(string='Nama Teknisi', readonly=True,)

    #field yang ada di nama.teknisi.mesin.list
    jam_mulai_perbaikan = fields.Datetime(string=u'Jam Mulai Perbaikan', readonly=True)
    jam_perbaikan_selesai = fields.Datetime(string=u'Jam Perbaikan Selesai',readonly=True)
    selesai = fields.Boolean(string=u'Selesai', readonly=True,)
    blm_selesai = fields.Boolean(string=u'Blm Selesai', readonly=True,)
    timer_duration = fields.Float(invisible=1, string='Time Duration (Minutes)',readonly=True)
    # nama_teknisi_ids = fields.Many2one('nama.teknisi',string=u'teknisi',readonly=True)
    # jenis_kerusakan_mesinmarel_list_id = fields.Many2one('jenis.kerusakan.mesinmarellist', 'Jenis Kerusakan Mesin List',readonly=True)

    # field jenis.kerusakan.mesinmarellist
    # jenis_kerusakan_mesinmarel_id = fields.Many2one('jenis.kerusakan.mesinmarel', 'Jenis Kerusakan Mesin Marel',readonly=True,)
    nama_teknisi_line = fields.One2many('nama.teknisi.mesin.list','jenis_kerusakan_mesinmarel_list_id',string=u'Nama Teknisi',readonly=True,)
    selesai = fields.Boolean(string=u'Selesai', readonly=True,)
    blm_selesai = fields.Boolean(string=u'Blm Selesai', readonly=True,)

    # field jenis.kerusakan.mesinmarel
    jenis_kerusakan = fields.Char(string=u'Jenis Kerusakan',readonly=True,)

    # fields kerusakan.list.mesin
    # mesin_produksi_id = fields.Many2one('mesin.marel.produksi',string=u'Nama/Blok Mesin',readonly=True,)
    jam_create = fields.Datetime(string=u'Jam Create', readonly=True)

    # felds mesin.marel.produksi
    nama_mesin_blok = fields.Char(string=u'Nama Mesin',readonly=True,)

    #marel.nama.operatorlist
    jumlah_yg_selesai = fields.Integer(string=u'Qty Yg Selesai',readonly=True,)
    jumlah_reject = fields.Integer(string=u'Jumlah Reject',readonly=True,)

    @api.model_cr
    def init(self):
        """ Marel Perbaikan Kerusakan Mesin """
        tools.drop_view_if_exists(self._cr, 'marel_mesin_kerusakan_report')
        self._cr.execute(""" CREATE VIEW marel_mesin_kerusakan_report AS (
                        SELECT
                            ntml.id as id,
                            ntml.jam_mulai_perbaikan as jam_mulai_perbaikan,
                            ntml.jam_perbaikan_selesai as jam_perbaikan_selesai,
                            ntml.selesai as selesai,
                            ntml.timer_duration as timer_duration,
                            ntml.blm_selesai as blm_selesai,
                            nt.nama_teknisi as nama_teknisi,
                            jkmm.jenis_kerusakan as jenis_kerusakan,
                            klm.jam_create as jam_create,
                            mmp.nama_mesin_blok as nama_mesin_blok,
                            mnol.jumlah_reject as jumlah_reject,
                            mnol.jumlah_yg_selesai as jumlah_yg_selesai
                        FROM
                            nama_teknisi_mesin_list ntml
                        JOIN
                            nama_teknisi nt ON (nt.id = ntml.nama_teknisi_ids)
                        JOIN
                            jenis_kerusakan_mesinmarellist jkmml ON (jkmml.id = ntml.jenis_kerusakan_mesinmarel_list_id)
                        JOIN
                            kerusakan_list_mesin klm ON (klm.id = jkmml.kerusakan_list_mesin_id)
                        JOIN
                            jenis_kerusakan_mesinmarel jkmm ON (jkmm.id = jkmml.jenis_kerusakan_mesinmarel_id)
						JOIN
							mesin_marel_produksi mmp ON (mmp.id = klm.mesin_produksi_id)
						JOIN
							marel_nama_operatorlist mnol ON (mmp.id = mnol.no_mesin_id)
                        GROUP BY
                            ntml.id,
                            ntml.jam_mulai_perbaikan,
                            ntml.jam_perbaikan_selesai,
                            ntml.selesai,
                            ntml.blm_selesai,
                            ntml.timer_duration,
                            nt.id,
                            jkmm.id,
                            klm.id,
                            mmp.id,
                            mnol.id
        )""")