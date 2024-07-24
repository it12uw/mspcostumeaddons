*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================================
Print Partner Outstanding Statement
====================================

The outstanding statement provides details of all outstanding partner receivables or payables
up to a particular date. This includes all unpaid invoices, unclaimed refunds and
outstanding payments. The list is displayed in chronological order and is split by currencies.

Aging details can be shown in the report, expressed in aging buckets (30 days
due, ...), so the customer or vendor can review how much is open, due or overdue.

Configuration
=============

Users willing to access to this report should have proper Accounting & Finance rights:

#. Go to *Settings / Users* and edit your user to add the corresponding access rights as follows.
#. In *Application / Accounting & Finance*, select *Billing* or *Billing Manager*
#. In *Technical Settings* mark *Show Full Accounting Features* options.

Usage
=====

To use this module, you need to:

#. Go to Invoicing > Sales > Master Data > Customers or or Invoicing > Purchases > Master Data > Vendors and select one or more
#. Press 'Action > Partner Outstanding Statement'
#. Indicate if you want to display receivables or payables, and if you want to display aging buckets


Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.png>`_.

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Miquel Raïch <miquel.raich@eficent.com>