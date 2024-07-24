# -*- coding: utf-8 -*-
# Copyright (c) 2015-Present TidyWay Software Solution. (<https://tidyway.in/>)

import pytz
import time
from operator import itemgetter
from itertools import groupby
from flectra import models, fields, api, _
from flectra.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, date


class aspl_stock_jadi_report(models.AbstractModel):
    _name = 'report.aspl_stock_jadi_report.report_stock_jadi'
    _description = 'Report Stock Stock'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name('aspl_stock_jadi_report.report_stock_jadi')
        record_id = data['form']['id'] if data and data['form'] and data['form']['id'] else docids[0]
        records = self.env['stock.jadi.wizard'].browse(record_id)
        return {
            'doc_model': report.model,
            'docs': records,
            'data': data,
            'get_beginning_inventory': self._get_beginning_inventory,
            'get_products':self._get_products,
            'get_product_sale_qty':self.get_product_sale_qty,
            'get_location':self.get_location(records),
        }

    def get_location(self, records):
        stock_ids = []
        location_obj = self.env['stock.location']
        domain = [('company_id', '=', records.company_id.id), ('usage', '=', 'internal')]
        if records.warehouse_ids:
            for warehouse in records.warehouse_ids:
                stock_ids.append(warehouse.view_location_id.id)
            domain.append(('location_id', 'child_of', stock_ids))
        final_stock_ids = location_obj.search(domain).ids
        return final_stock_ids

    def get_parent_location(self, records):
        stock_ids = []
        location_obj = self.env['stock.location']
        domain = [('company_id', '=', records.company_id.id)]
        if records.location_id:
            for locations in records.location_id:
                stock_ids.append(locations.id)
            domain.append(('id', 'child_of', stock_ids))
        final_stock_ids = location_obj.search(domain).ids
        return final_stock_ids


    def convert_withtimezone(self, userdate):
        user_date = datetime.strptime(userdate, DEFAULT_SERVER_DATETIME_FORMAT)
        tz_name = self.env.context.get('tz') or self.env.user.tz
        if tz_name:
            utc = pytz.timezone('UTC')
            context_tz = pytz.timezone(tz_name)
            user_datetime = user_date
            local_timestamp = context_tz.localize(user_datetime, is_dst=False)
            user_datetime = local_timestamp.astimezone(utc)
            return user_datetime.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        return user_date.strftime(DEFAULT_SERVER_DATETIME_FORMAT)

    def _get_products(self, record):
        product_product_obj = self.env['product.product']
        domain = [('type', '=', 'product')]
        product_ids = False
        if record.category_ids:
            domain.append(('categ_id', 'in', record.category_ids.ids))
            product_ids = product_product_obj.search(domain)
        if record.product_ids:
            product_ids = record.product_ids
        if not product_ids:
             product_ids = product_product_obj.search(domain)
        return product_ids

    def _get_beginning_inventory(self, record, product):
        locations = self.get_parent_location(record) if record.location_id else self.get_location(record)
        # locations = [record.location_id.id] if record.location_id else self.get_location(record)
        # if record.location_id:
        #     for loc in record.location_id:
        #         locations = []
        #         for locs in loc:
        #             parents = self.env['stock.location'].search([('parent_path', '=like', locs.parent_path + '%')])
        #         locations.append(parents.id)
        # else:
        #     self.get_location(record)

        if isinstance(product, int):
            product_data = product
        else:
            product_data = product.id

        start_date = str(date.today()) if record.is_today_movement else str(record.start_date)
        from_date = self.convert_withtimezone(start_date + ' 00:00:00')
        # from_date = (start_date + ' 00:00:00')
        self._cr.execute(''' 
                        SELECT id as product_id,coalesce(sum(qty), 0.0) as qty
                        FROM
                            ((
                            SELECT pp.id, pp.default_code,m.date,
                                CASE when pt.uom_id = m.product_uom 
                                THEN u.name 
                                ELSE (select name from product_uom where id = pt.uom_id) 
                                END AS name,

                                CASE when pt.uom_id = m.product_uom
                                THEN coalesce(sum(-m.product_qty)::decimal, 0.0)
                                ELSE coalesce(sum(-m.product_qty * pu.factor / u.factor )::decimal, 0.0) 
                                END AS qty

                            FROM product_product pp 
                            LEFT JOIN stock_move m ON (m.product_id=pp.id)
                            LEFT JOIN product_template pt ON (pp.product_tmpl_id=pt.id)
                            LEFT JOIN stock_location l ON (m.location_id=l.id)    
                            LEFT JOIN stock_picking p ON (m.picking_id=p.id)
                            LEFT JOIN product_uom pu ON (pt.uom_id=pu.id)
                            LEFT JOIN product_uom u ON (m.product_uom=u.id)
                            WHERE m.date <  %s AND (m.location_id in %s) AND m.state='done' AND pp.active=True AND pp.id = %s 
                            GROUP BY  pp.id, pt.uom_id , m.product_uom ,pp.default_code,u.name,m.date
                            ) 
                            UNION ALL
                            (
                            SELECT pp.id, pp.default_code,m.date,
                                CASE when pt.uom_id = m.product_uom 
                                THEN u.name 
                                ELSE (select name from product_uom where id = pt.uom_id) 
                                END AS name,
                                CASE when pt.uom_id = m.product_uom 
                                THEN coalesce(sum(m.product_qty)::decimal, 0.0)
                                ELSE coalesce(sum(m.product_qty * pu.factor / u.factor )::decimal, 0.0) 
                                END  AS qty
                            FROM product_product pp 
                            LEFT JOIN stock_move m ON (m.product_id=pp.id)
                            LEFT JOIN product_template pt ON (pp.product_tmpl_id=pt.id)
                            LEFT JOIN stock_location l ON (m.location_dest_id=l.id)    
                            LEFT JOIN stock_picking p ON (m.picking_id=p.id)
                            LEFT JOIN product_uom pu ON (pt.uom_id=pu.id)
                            LEFT JOIN product_uom u ON (m.product_uom=u.id)
                            WHERE m.date < %s AND (m.location_dest_id in %s) AND m.state='done' AND pp.active=True AND pp.id = %s 
                            GROUP BY  pp.id,pt.uom_id , m.product_uom ,pp.default_code,u.name,m.date
                            ))
                        AS foo
                        GROUP BY id
                    ''', (from_date, tuple(locations), product_data, from_date, tuple(locations), product_data))

        res = self._cr.dictfetchall()
        return res[0].get('qty', 0.00)  if res else 0.00

    def get_product_sale_qty(self, record, product=None):
        if not product:
            product = self._get_products(record)
        if isinstance(product, list):
            product_data = tuple(product)
        else:
            product_data = tuple(product.ids)

        if product_data:
            locations = self.get_parent_location(record) if record.location_id else self.get_location(record)
            # locations = [record.location_id.id] if record.location_id else self.get_location(record)
            # if record.location_id:
            #     for loc in record.location_id:
            #         locations = []
            #         for locs in loc:
            #             parents = self.env['stock.location'].search([('parent_path', '=like', locs.parent_path + '%')])
            #         locations.append(parents.id)
            # else:
            #     self.get_location(record)
            
                
            start_date = str(date.today()) if record.is_today_movement else str(record.start_date)
            end_date = str(date.today()) if record.is_today_movement else str(record.end_date)

            start_date = self.convert_withtimezone(start_date + ' 00:00:00')
            end_date = self.convert_withtimezone(end_date + ' 23:59:59')
            self._cr.execute('''
                            SELECT pp.id AS product_id,pt.categ_id,
                                sum((
                                CASE WHEN spt.code in ('outgoing') AND sp.is_pinjam = False AND sm.location_id in %s AND sourcel.usage !='inventory' AND destl.usage !='inventory'
                                THEN -(sm.product_qty * pu.factor / pu2.factor)
                                ELSE 0.0 
                                END
                                )) AS product_qty_out,
                                
                                sum((
                                CASE WHEN spt.code in ('incoming') AND sp.is_pinjam = False AND sm.location_dest_id in %s AND sourcel.usage !='inventory' AND destl.usage !='inventory' 
                                THEN (sm.product_qty * pu.factor / pu2.factor) 
                                ELSE 0.0 
                                END
                                )) AS product_qty_in,

                                sum((
                                CASE WHEN (spt.code ='internal' OR spt.code IS NULL) AND spt.is_stock = False AND sm.location_dest_id IN %s AND sourcel.usage ='internal' AND destl.usage ='internal' AND sourcel.is_wip = False AND destl.is_wip = False AND sourcel.is_stock = True
                                THEN (sm.product_qty * pu.factor / pu2.factor)  
                                WHEN (spt.code ='internal' OR spt.code IS NULL) AND spt.is_stock = False AND sm.location_id IN %s AND sourcel.usage ='internal' AND destl.usage ='internal' AND sourcel.is_wip = False AND destl.is_wip = False AND destl.is_stock = True
                                THEN -(sm.product_qty * pu.factor / pu2.factor) 
                                ELSE 0.0 
                                END
                                )) AS product_qty_internal,

                                sum((
                                CASE WHEN sm.location_dest_id IN %s AND sourcel.usage ='production' AND destl.usage ='internal'
                                THEN (sm.product_qty * pu.factor / pu2.factor)  
                                WHEN sm.location_id IN %s AND sourcel.usage ='internal' AND destl.usage ='production'
                                THEN -(sm.product_qty * pu.factor / pu2.factor) 
                                ELSE 0.0 
                                END
                                )) AS product_qty_mrp,

                                sum((
                                CASE WHEN spt.is_stock = True AND sm.location_dest_id IN %s AND sourcel.usage ='internal' AND destl.usage ='internal' AND sourcel.is_wip = False AND destl.is_wip = False 
                                THEN (sm.product_qty * pu.factor / pu2.factor)  
                                WHEN spt.is_stock = True AND sm.location_id IN %s AND sourcel.usage ='internal' AND destl.usage ='internal' AND sourcel.is_wip = False AND destl.is_wip = False 
                                THEN -(sm.product_qty * pu.factor / pu2.factor) 
                                ELSE 0.0 
                                END
                                )) AS product_qty_inspect,

                                sum((
                                CASE WHEN sourcel.usage = 'inventory' AND sm.location_dest_id in %s  
                                THEN  (sm.product_qty * pu.factor / pu2.factor)
                                WHEN destl.usage ='inventory' AND sm.location_id in %s 
                                THEN -(sm.product_qty * pu.factor / pu2.factor)
                                ELSE 0.0 
                                END
                                )) AS product_qty_adjustment
                            FROM product_product pp 
                            LEFT JOIN stock_move sm ON (sm.product_id = pp.id and sm.date >= %s and sm.date <= %s and sm.state = 'done' and sm.location_id != sm.location_dest_id)
                            LEFT JOIN stock_picking sp ON (sm.picking_id=sp.id)
                            LEFT JOIN stock_picking_type spt ON (spt.id=sp.picking_type_id)
                            LEFT JOIN stock_location sourcel ON (sm.location_id=sourcel.id)
                            LEFT JOIN stock_location destl ON (sm.location_dest_id=destl.id)
                            LEFT JOIN product_uom pu ON (sm.product_uom=pu.id)
                            LEFT JOIN product_uom pu2 ON (sm.product_uom=pu2.id)
                            LEFT JOIN product_template pt ON (pp.product_tmpl_id=pt.id)
                            WHERE pp.id in %s
                            GROUP BY pt.categ_id, pp.id order by pt.categ_id
                            ''', (tuple(locations), tuple(locations), tuple(locations), tuple(locations), tuple(locations), tuple(locations), tuple(locations), tuple(locations), tuple(locations), tuple(locations), start_date, end_date, product_data))
            values = self._cr.dictfetchall()
            if record.group_by_categ:
                sort_by_categories = sorted(values, key=itemgetter('categ_id'))
                records_by_categories = dict((k, [v for v in itr]) for k, itr in groupby(sort_by_categories, itemgetter('categ_id')))
                if not record.with_zero:
                    today_record_by_cat = {}
                    for key, value in records_by_categories.items():
                        for each in value:
                            product_beg_qty = self._get_beginning_inventory(record, each['product_id'])
                            today_movment_total = each.get('product_qty_in') + each.get('product_qty_internal') + each.get('product_qty_inspect') + each.get('product_qty_mrp') + each.get('product_qty_adjustment') + each.get('product_qty_out')
                            if record.is_today_movement:
                                if today_movment_total != 0:
                                    if key not in today_record_by_cat:
                                        today_record_by_cat.update({key:[each]})
                                    else:
                                        today_record_by_cat[key] += [each]
                            elif (product_beg_qty + today_movment_total) != 0:
                                if key not in today_record_by_cat:
                                    today_record_by_cat.update({key:[each]})
                                else:
                                    today_record_by_cat[key] += [each]
                    return today_record_by_cat
                else:
                    return records_by_categories
            else:
                return values[0]
