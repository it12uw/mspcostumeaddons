/*!
 Bootstrap integration for DataTables' Buttons
 ©2016 SpryMedia Ltd - datatables.net/license
*/
function changeVisibility() {
    document.getElementById("action_nilai_inline_1_qc").style.visibility = "hidden";
  }

  // (function(c){"function"===typeof define&&define.amd?define(["jquery","datatables.net-bs","datatables.net-buttons"],function(a){return c(a,window,document)}):"object"===typeof exports?module.exports=function(a,b){a||(a=window);if(!b||!b.fn.dataTable)b=require("datatables.net-bs")(a,b).$;b.fn.dataTable.Buttons||require("datatables.net-buttons")(a,b);return c(b,a,a.document)}:c(jQuery,window,document)})