*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================
Report Wkhtmltopdf Param
========================

This module allows you to add new parameters for a paper format which are
then forwarded to wkhtmltopdf command as arguments. To display the arguments
that wkhtmltopdf accepts go to your command line and type 'wkhtmltopdf -H'.

A commonly used parameter in Odoo is *--disable-smart-shrinking*, that will
disable the automatic resizing of the PDF when converting. This is
important when you intend to have a layout that conforms to certain alignment.
It is very common whenever you need to conform the PDF to a predefined
layoyut (e.g. checks, official forms,...).


Usage
=====

#. Go to *Settings* and press 'Activate the developer mode (with assets)'
#. Go to *Settings - Technical - Reports - Paper Format*
#. Add additional parameters indicating the command argument name (remember to
   add prefix -- or -) and value.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Miku Laitinen <miku@avoin.systems>
* Jordi Ballester <jordi.ballester@eficent.com>