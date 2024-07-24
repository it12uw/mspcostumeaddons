*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
MRP BoM Equivalences
=====================

This module allows the user to specify non-equivalent products to a part on a BOM.

Other modules can assume that products in the same category are equivalent and can be used in a Manufacturing Order if the main part is not available. Those non-equivalent products can be excluded.

Usage
=====

* Go to Manufacturing > Master Data > Bill of Materials
* Create or update a BOM to check the box "Use Equivalences"
* Set the non-equivalent products among the products of the same category

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Bhavesh Odedra <bodedra@opensourceintegrators.com>

Funders
-------

The development of this module has been financially supported by:

* Open Source Integrators <http://www.opensourceintegrators.com>