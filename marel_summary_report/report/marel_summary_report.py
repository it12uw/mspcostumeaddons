from flectra import api, models, fields, tools


class MarelSummaryReport(models.Model):
    _name = "marel.summary.report"
    _auto = False

    #field yang ada di sale order line
    num_productions = fields.Integer(string="Num Production",readonly=True)
    analytic_account_id = fields.Many2one(comodel_name='account.analytic.account', string='Analytic Account',readonly=True)
    amount_total_so = fields.Float(string='Total + Tax', readonly=True,)
    product_id_sol = fields.Many2one('product.product', string="Product Sale",readonly=True)
    product_uom_qty = fields.Integer(string='Quantity Order', required=True, readonly=True)
    product_uom_so = fields.Many2one('product.uom', string='Unit of Measure', readonly=True)
    price_unit_so = fields.Float('Unit Price', required=True,readonly=True)
    tax_id = fields.Many2many('account.tax', string='Taxes',readonly=True)
    price_subtotal_so = fields.Float(string='Subtotal Sale Order', readonly=True, store=True)
    #field yang ada di purchase order
    product_pol = fields.Many2one('product.product',string="Product Purchase",readonly=True)
    product_qty = fields.Float(string='Quantity', readonly=True)
    account_analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account',readonly=True)
    qty_received = fields.Integer(string="Quantyti Received",readonly=True)
    qty_invoiced = fields.Integer(string="Quantyti Invoice",readonly=True)
    product_uom_po = fields.Char(string="Product Unit Of Measure",readonly=True)
    price_unit_po = fields.Float(string="Price Unit Purchase",readonly=True)
    price_subtotal_po = fields.Float(string="Price Subtotal Purchase",readonly=True, store= True)
    amount_total_po = fields.Float(string='Total + Tax', readonly=True,)
    # field totalhitung Provit
    pov_tex = fields.Float(string="Provit + Tax",readonly=True)
    tot_prov = fields.Float(string="Provit",readonly=True,)
    # hpp_pick = fields.Float(string="HPP/PICK",readonly=True,)
    hpp_tex = fields.Float(string="HPP/PICK  + Tax", readonly=True,)
    sale_price = fields.Float(string="Harga Pokok", readonly=True,)
    bom_comp = fields.Char(string="Komponen Produk",readonly=True)
    bom_cost = fields.Float(string="Harga Komponen", readonly=True,)


    #field yang ada di Mo
    name = fields.Char('Reference', copy=False, readonly=True, default=lambda x: _('New'))
    product_mo = fields.Char(string="Product MO",readonly=True,)
    origin = fields.Char('Source', copy=False,help="Reference of the document that generated this production order request.",readonly=True)
    product_tmpl_id = fields.Many2one('product.template', 'Product Template', readonly=True)
    # pakan = fields.Integer(string='Pakan',readonly=True)
    # lusi = fields.Integer(string='Lusi',readonly=True)
    product_id = fields.Many2one('product.product', 'Product',domain=[('type', 'in', ['product', 'consu'])], readonly=True,)
    analytic_account_id_mo = fields.Many2one(comodel_name='account.analytic.account', string='Analytic Account',readonly=True)

    #Field yang ada di product
    # rego_price = fields.Float(string="Standart Cost", readonly=True)
    harga_price = fields.Float(string="Standart Cost", readonly=True)

    @api.model_cr
    def init(self):
        """ Summray """
        tools.drop_view_if_exists(self._cr, 'marel_summary_report')
        self._cr.execute(""" CREATE VIEW marel_summary_report AS (
                        SELECT
                            mr.id as id,
                            mr.name as name,
                            mr.product_id as product_id,
                            pt.default_code as product_tmpl_id,
                            sol.price_unit as price_unit_so,
                            sol.price_subtotal as price_subtotal_so,
                            sol.product_uom_qty as product_uom_qty,
                            sol.product_id as product_id_sol,
                            so.amount_total as amount_total_so,
                            pol.product_id as product_pol,
                            pol.price_unit as price_unit_po,
                            pol.price_subtotal as price_subtotal_po,
                            po.amount_total as amount_total_po,
                            (sol.price_subtotal - pol.price_subtotal) as tot_prov,
                            (so.amount_total - po.amount_total) as pov_tex,
                            ((so.amount_total - po.amount_total)/sol.product_uom_qty) as hpp_tex,
                            ip.value_float as sale_price,
                            ptb.name as bom_comp,
                            ip2.value_float as bom_cost

                        FROM
                            mrp_production mr
                        LEFT JOIN
                            product_product pp ON (pp.id = mr.product_id)
                        LEFT JOIN
                            product_template pt ON (pt.id = pp.product_tmpl_id)
                        JOIN
                            product_category pc ON (pc.id = pt.categ_id)
                        JOIN
                            account_analytic_account ac ON (ac.id = mr.analytic_account_id)
                        LEFT JOIN
							ir_property ip ON (ip.name='standard_price' AND ip.res_id= 'product.product,'||pp.id)
						JOIN
							mrp_bom mb ON (mb.id = mr.bom_id)
						JOIN
							mrp_bom_line mbl ON (mbl.bom_id = mb.id)
						JOIN
							product_product ppb ON (ppb.id = mbl.product_id)
						JOIN
							product_template ptb ON (ptb.id = ppb.product_tmpl_id)
						LEFT JOIN
							ir_property ip2 ON (ip2.name='standard_price' AND ip2.res_id= 'product.product,'||ppb.id)
                        JOIN
                            sale_order so ON (so.analytic_account_id = ac.id)
                        JOIN
                            sale_order_line sol ON (sol.order_id = so.id)
                        JOIN
                            product_product ppsol ON (sol.product_id = ppsol.id)
                        JOIN
                            purchase_order_line pol ON (pol.account_analytic_id = ac.id)
                        JOIN
                            product_product pppol ON (pol.product_id = pppol.id)
                        JOIN
                            product_template ptpol ON (ptpol.id = pppol.product_tmpl_id)
                        JOIN
                            purchase_order po ON (po.id = pol.order_id)
                        
        )""")