*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

=======================
Purchase Order Approved
=======================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 

This module extends the functionality of purchases adding a new state
*Approved* in purchase orders before the *Purchase Order* state. Additionally
add the possibility to set back to draft a purchase order in all the states
previous to *Purchase Order*.

In this new *Approved* state:

* You cannot modify the purchase order.
* However, you can go back to draft and pass through the workflow again.
* The incoming shipments are not created. You can create them by clicking the
  *Convert to Purchase Order* button, also moving to state *Purchase Order*.

The new state diagram is depicted below:

.. image:: https://raw.githubusercontent.com/OCA/purchase-workflow/11.0/purchase_order_approved/static/description/schema.png
   :width: 500 px
   :alt: New states diagram

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module:

#. Go to 'Purchases > Configuration > Settings'.
#. In the *Orders* section you can set the *State 'Approved' in Purchase
   Orders*.

Usage
=====

To use this module, you need to:

#. Go to a Request for Quotation.
#. Click *Confirm Order*. The state is now *Approved* (if no order approval
   is not set).
#. To move forward to the state *Purchase Order* and release the creation
   of the deliveries, click on *Convert to Purchase Order*.

Changelog
=========

11.0.1.0.0 (2018-06-06)
~~~~~~~~~~~~~~~~~~~~~~~

* [MIG] Migrated to v11.

Credits
=======

Authors
~~~~~~~

* Eficent

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Lois Rilo <lois.rilo@eficent.com>