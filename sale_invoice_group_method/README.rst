*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
   :alt: License LGPL-3

=========================
Sale Invoice Group Method
=========================

This module allows you to combine several Sales Orders into a single invoice,
if they meet the group criteria defined by the 'Invoice Group Method'.

The group criteria is defined in the 'Invoice Group Method' by a combination
of fields of the Sales Order. 'Invoice Address', 'Currency' and 'Payment Term'
are always included.

You can assign a default 'Invoice Group Method' to customers, so that it will
be proposed on their orders.

When no Invoice Group Method is defined in a Sales Order, the standard
approach will be used, which groups by 'Invoice Address' and 'Currency'.

Note: Existing draft invoices are not considered in the process of grouping.
However, you can find the feature implemented in ``sale_merge_draft_invoice``
from sale-workflow repository.

Configuration
=============

#. Go to 'Sales / Configuration / Invoice Group Method'
#. Create an Invoice Group Method and choose the fields of the Sales Order
   that should be equal in that particular grouping method, for their orders
   to be merged into the same invoice. For example, create the Invoice Group
   Method 'By Customer' and select the field 'Customer').

Usage
=====

Update customers
----------------

#. Go to 'Sales / Sales / Customers'
#. Choose a customer and go to 'Sales & Purchases' page.
#. Update the 'Default Invoice Group Method'

Create a Quote / Sale Order
---------------------------

#. Go to 'Sales / Sales / Quotations'.
#. Create a new Quote and inside the 'Other Information' page select an
   option from the field 'Invoice Group Method'. If the customer had a
   default, it will have been provided already.
#. Complete the Quote as usual.

Create Invoices
---------------

#. Go to 'Sales / Sales / Sales Orders'.
#. Select all the sales orders with status 'To invoice'.
#. Go to 'Action' and click 'Invoice Order'. As a result, draft invoices will be
   created for the selected Sales Orders, consolidating them according to the
   Invoice Group Method defined.

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