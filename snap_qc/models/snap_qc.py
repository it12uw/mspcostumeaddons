from flectra import api, fields, models, _

class SnapQc(models.Model):
    _name='snap.qc'
    _description='Snap QC'


    date=fields.Date(string='Tanggal', default=fields.Date.context_today, readonly=True)
    blok=fields.Selection([
			('1',_('1')),
			('2',_('2')),
			('3',_('3')),
            ('4',_('4')),
			('5',_('5')),
			('6',_('6')),
            ('7',_('7')),
			('8',_('8')),
			('9',_('9')),
            ('10',_('10')),
			('11',_('11')),
			('12',_('12')),
            ('13',_('13')),
			], string= "Blok")
    total_mesin= fields.Integer(string="Total Mesin", compute='_compute_total_mesin',readonly=True,store=True ) 
    presentasi=fields.Float(compute='_compute_presentasi',string='Hasil Presentasi',readonly=True,store=True)
    total_mesin_jalan = fields.Float(string="Total Mesin Jalan", compute='_compute_total_mesin', readonly=True,store=True)     
    shift = fields.Selection([
        ('A',_('A')),
        ('B',_('B')),
        ('C',_('C')),
    ],string="Shift")

    @api.depends('blok')
    def _compute_total_mesin(self):
        for record in self:
            if record.blok == '1' or record.blok == '2' or record.blok == '3' or record.blok == '4' or record.blok == '5':
                record.total_mesin = 50
            elif record.blok == '6' or record.blok == '7' or record.blok == '8' or record.blok == '9' or record.blok == '10':
                record.total_mesin = 42
            elif record.blok == '11':
                record.total_mesin = 18
            elif record.blok == '12' or record.blok == '13':
                record.total_mesin = 36
            else:
                record.total_mesin = 550

    @api.depends('blok', 'shift', 'total_mesin_jalan')
    def _compute_presentasi(self):
        for record in self:
            if record.total_mesin_jalan:
                record.presentasi = record.total_mesin_jalan / record.total_mesin
            else:
                record.presentasi = 0
