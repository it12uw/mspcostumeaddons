from flectra import models


class MarelWipMoReportExcel(models.AbstractModel):
	_name = "report.marel_workorder_report.wip_mo_report_conti_excel"
	_description = 'Report Conti WIP XLSX'
	_inherit = 'report.report_xlsx.abstract'



	def generate_xlsx_report(self, workbook, data, lines):
		print ('lines', lines)
		format0 = workbook.add_format({'font_size': 20, 'align': 'center', 'bold': True})
		format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
		format2 = workbook.add_format({'font_size': 12, 'align': 'vcenter',})
		date = workbook.add_format({'num_format': 'mmmm d yyyy', 'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'left'})
		title_style = workbook.add_format({'font_name': 'Times', 'font_size': 14, 'bold': True, 'align': 'center'})
		header_style = workbook.add_format({'font_name': 'Times', 'bold': True, 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'center'})
		text_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'left'})
		number_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'right'})

		# sheet = workbook.add_worksheet('Resume WR XLSX')
		for dt in lines:
			sheet = workbook.add_worksheet(dt.name)
			sheet.set_landscape()
			sheet.autofilter('A2:M2')
			sheet.set_column('A:A', 5)
			sheet.set_column('B:B', 15)
			sheet.set_column('C:C', 20)
			sheet.set_column('D:D', 15)
			sheet.set_column('E:E', 15)
			sheet.set_column('F:F', 35)
			sheet.set_column('G:G', 15)
			sheet.set_column('H:H', 20)
			sheet.set_column('I:I', 10)
			sheet.set_column('J:J', 15)
			sheet.set_column('K:K', 15)
			sheet.set_column('L:L', 15)
			sheet.set_column('M:M', 15)
			sheet.merge_range('A1:M1', 'Conti Wip Production', title_style)
			sheet.write(1, 0, 'No', header_style)
			sheet.write(1, 1, 'Workcenter', header_style)
			sheet.write(1, 2, 'MO/JO', header_style)
			sheet.write(1, 3, 'Status', header_style)
			sheet.write(1, 4, 'Taggal Input', header_style)
			sheet.write(1, 5, 'Nama Prodak', header_style)
			sheet.write(1, 6, 'Order Qty', header_style)
			sheet.write(1, 7, 'Jumlah Selesai', header_style)
			sheet.write(1, 8, 'Satuan', header_style)
			sheet.write(1, 9, 'Shift', header_style)
			sheet.write(1, 10, 'Nama Operator', header_style)
			sheet.write(1, 11, 'Nama Kiusi', header_style)
			sheet.write(1, 12, 'No Mesin', header_style)
			row = 2
			number = 1

			# report = self.env[]
			for report in lines.report_ids:
				sheet.write(row, 0, number, text_style)
				sheet.write(row, 1, report.workcenter, date)
				sheet.write(row, 2, report.name, date)
				sheet.write(row, 3, report.state, date)
				sheet.write(row, 4, report.tgl_kerja, date)
				sheet.write(row, 5, report.product_id, text_style)
				sheet.write(row, 6, report.product_qty, text_style)
				sheet.write(row, 7, report.jumlah_yg_selesai, text_style)
				sheet.write(row, 8, report.uom_id, text_style)
				sheet.write(row, 9, report.shift, text_style)
				sheet.write(row, 10, report.nama_operator, text_style)
				sheet.write(row, 11, report.nama_qiusi, text_style)
				sheet.write(row, 12, report.nama_mesin_blok, number_style)
				# sheet.write(row, 8, report.qty, text_style)
				row += 1
				number += 1



		# 	sheet.write(0, 0, 'No', format0)
		# 	sheet.write(row, 1, dt.report_id.name, format1)
		# 	sheet.write(row, 4, dt.reference, format2)
		# 	row += 1
		# 	number += 1
		# 	# sheet.write(1, 5, dt.report_ids.nama_produk, format2)
		# 	# sheet.write(1, 6, dt.report_ids.qty, format2)
		# # 	sheet.write(0, 1, i.name, format1)
		# # pick = self.env['close.kiriman']._search()
		# # for i in pick:
		# # 	sheet.write(0, 0, 'No', format0)
		# # 	sheet.write(0, 1, i.name, format1)
		workbook.close()
        # output.seek(0)
        # # response.stream.write(output.read())
        # output.close()

