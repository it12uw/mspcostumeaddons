===========================
MRP MTO with Stock Purchase
===========================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fmanufacture-lightgray.png?logo=github
    :target: https://github.com/OCA/manufacture/tree/11.0/mrp_mto_with_stock_purchase
    :alt: OCA/manufacture
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/manufacture-11-0/manufacture-11-0-mrp_mto_with_stock_purchase
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runbot-Try%20me-875A7B.png
    :target: https://runbot.odoo-community.org/runbot/129/11.0
    :alt: Try me on Runbot

|badge1| |badge2| |badge3| |badge4| |badge5| 

This module make compatible mrp_mto_with_stock and purchase modules.
Indeed, there is an option in mto_mto_with_stock to check the forecast stock
when checking the availibility of a Manufacture Order. But this forecast stock
does not take into account the quantities coming from draft POs. This module
adds this behavior.

**Table of contents**

.. contents::
   :local:

Configuration
=============

* This module is installed automatically when mrp_mto_with_stock and purchase module are installed

Usage
=====

When a manufacturing order is created out of a procurement evaluation
(from an orderpoint, MTO,...) the calendar is considered in the computation
of the planned start date of the manufacturing order.

For example, if it takes 1 day to manufacture a product and it is required
for Monday, the manufacturing order will be created with planned start date
on the previous Friday, if the warehouse operates under a Mo-Fri working
calendar.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/manufacture/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/OCA/manufacture/issues/new?body=module:%20mrp_mto_with_stock_purchase%0Aversion:%2011.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Akretion

Contributors
~~~~~~~~~~~~

* * Florian da Costa <florian.dacosta@akretion.com>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/manufacture <https://github.com/OCA/manufacture/tree/11.0/mrp_mto_with_stock_purchase>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.