from flectra import api, models, fields, tools

class MarelWorkOrderReport(models.Model):
    _name = "marel.workorder.report"
    _auto = False

    #work.order
    total_qty = fields.Float(string='Total Qty',readonly=True)
    duration = fields.Float(string='duration',readonly=True)
    qty_producing = fields.Float(string='Qty',readonly=True)
    qty_produced = fields.Float(string='Qty yg Selesai',readonly=True)
    product_id = fields.Many2one('product.product', string="Product Sale",readonly=True)
    name = fields.Char(string='Work Order',readonly=True)
    # product.product
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', readonly=True)
    # product_id = fields.Char(string='Product',readonly=True)
    # product.template
    # product_tmpl_id = fields.Char(string='Product Template',readonly=True)
    #other
    # total_qty = fields.Float('Total Qty', readonly=True,)

    @api.model_cr
    def init(self):
        """ marel_workorder_report """
        tools.drop_view_if_exists(self._cr, 'marel_workorder_report')
        self._cr.execute(""" CREATE VIEW marel_workorder_report AS (
                        SELECT
                            mwo.id as id,
                            mwo.name as name,
                            mwo.duration as duration,
                            mwo.qty_producing as qty_producing,
                            mwo.qty_produced as qty_produced,
                            mwo.product_id as product_id,
                            (mwo.qty_producing+mwo.qty_produced) as total_qty
                        FROM
                            mrp_workorder mwo
                        JOIN
                            product_product pp ON (pp.id = mwo.product_id)
                        JOIN
                            product_template pt ON (pt.id = pp.product_tmpl_id)
        )""")