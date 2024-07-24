*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License LGPL-3

========================
Sale Merge Draft Invoice
========================

Odoo can merge sales orders into a single invoice, grouped by partner and
currency, when the sales orders are selected and invoiced together. This module
extends the grouping to also consider any pre-existing draft invoices and merge
them.

This feature is activated from Sales / Settings and assigned to the company
settings.

Users assigned to the group 'Change sale to invoice merge proposal'
have the possibility to activate or deactivate this option at the moment of
invoicing.

If you also need to group on fields other than partner and currency, the OCA
module sale_invoice_group_method allows you to specify alternative grouping
methods and is fully compatible with this module.

Configuration
=============

#. Go to 'Sales / Configuration / Settings'
#. In 'Quotations & Sales' go to 'Invoices' and activate the option 'Merge
   new invoices with existing draft ones'.
#. Go to 'Settings / Users / Groups' and assign to the group 'Change sale
   to invoice merge proposal' all the users that can have the possibility to
   activate/deactivate the option of merging the new invoice with existing
   draft ones.

Usage
=====

Create an Invoice from a single Sale Order
------------------------------------------

#. Go to 'Sales / Sales / Sales Orders'.
#. Select or click in a sale order.
#. Go to 'Action' and click 'Invoice Order' or press the button 'Invoice
   Order' if you are inside a sale order. The result, in case there are draft
   invoices that correspond to this one, is an existing draft invoice with
   the new lines added.
   In the wizard, if the user belongs to the group 'Change sale to invoice merge
   proposal', the option to deactivate the 'Merge with draft invoices' is
   given. In this case, the result is a new draft invoice is created
   following the usual behaviour.

Create Invoices from a group of Sales Orders
--------------------------------------------

#. Go to 'Sales / Sales / Sales Orders'.
#. Select all the sales orders with status 'To invoice'.
#. Go to 'Action' and click 'Invoice Order'. As a result, new draft invoices
   will be merged with existing ones when corresponding.
   In the wizard, if the user belongs to the group 'Change sale to invoice merge
   proposal', the option to deactivate the 'Merge with draft invoices' is
   given. In this case, the result is a new draft invoice for every sale
   order following the usual behaviour.

Credits
=======

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Roser Garcia <roser.garcia@eficent.com>
* Jordi Ballester Alomar <jordi.ballester@eficent.com>