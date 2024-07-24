*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=============================
Account Due List Days Overdue
=============================

This module adds to the 'Payments and due list' view the number of days that
 an open item is overdue, and classifies the amount due in separate terms
 columns  (e.g. 1-30, 31-60, +61).

The terms columns to show in the list and the number of days for within each
term can be configured.


Configuration
=============

* Go to 'Invoicing / Configuration / Overdue Terms', and add the terms,
  providing the day from, date to and a name that will be displayed in the
  Payments and due list as column.

* It is recommended to always add a last term '+ X' where the 'to days' value
  is a very big value like 99999.


Usage
=====

To use this module, you need to go to:

* Invoicing / Journal Entries / Payments and due list

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Jordi Ballester Alomar <jordi.ballester@eficent.com>
* Holger Brunn <hbrunn@therp.nl>

Do not contact contributors directly about support or help with technical issues.