*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Report QWeb Parameter
=====================

This module allows you to add new parameters on QWeb reports.
Currently, we have defined a field maximum on a report and a validation of
maximal and minimal size.
It is useful on xml reports in order to validate length.
XML are sometimes XSD dependant and we must validate its format.
For example, in spanish facturae (http://www.facturae.gob.es/Paginas/Index.aspx), where
length and format must be validated in several fields in order to send an invoice.


Usage
=====

#. Add a t-length attribute on report templates fields that will truncate the field
#. Add a t-minlength attribute on report template fields that will check the min length
#. Add a t-maxlength attribute on report template fields that will check the max length

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Enric Tobella <etobella@creublanca.es>