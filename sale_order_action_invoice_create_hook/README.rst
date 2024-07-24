*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License LGPL-3

=====================================
Sale Order Action Invoice Create Hook
=====================================

This module adds hook points in sale_order.action_invoice_create() in order
to add more flexibility in the grouping parameters for the creation of
invoices and to give the possibility to take into account draft invoices.

Although the original code has been modified a bit, the logic has been
respected and the method still does exactly the same.

Usage
=====

#. Add dependency of this module
#. Inherit from 'sale.order'
#. Change the _get_invoice_group_key function in order to return more
   grouping fields to take into account when creating a single invoice from
   various Sales Orders.
#. Change the _get_draft_invoices function in order to take into account
   existing draft invoices when creating new ones. This feature is already
   implemented in the module sale_merge_draft_invoice.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Jordi Ballester Alomar <jordi.ballester@eficent.com>
* Roser Garcia <roser.garcia@eficent.com>