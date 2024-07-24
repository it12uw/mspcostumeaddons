{
  'name': 'Report Pembelian',
  'author': 'Hendrikus',
  'version': '0.1',
  'depends': [
      'base',
      'purchase',
      'purchase_request',
      'purchase_request_order_approved',
      'purchase_order_approved',
      'purchase_last_price_info',
  ],
  'data': [
     'views/menu.xml',
     'views/pembelian_barang.xml',
     'report/qweb_histori_pembelian_doc.xml',
     'report/qweb_histori_pembelian_template.xml',
     'report/qweb_pembelian_perbarang.xml',
     'report/qweb_pembelian_perbarang_template.xml',
  ],
  'qweb': [
    # 'static/src/xml/nama_widget.xml',
  ],
  'sequence': 1,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': '- Arkademy Part 1',
  'summary': 'Catat Penjualan Sederhana',
  'license': 'OPL-1',
  'website': 'https://www.arkana.co.id/',
  'description': '-'
}