*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg 
    :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
	
===========
XML Reports
===========

This module was written to extend the functionality of the reporting engine to
support XML reports and allow modules to generate them by code or by QWeb
templates.

Installation
============

To install this module, you need to:

* Install lxml_ in Odoo's ``$PYTHONPATH``.
* Install the repository `reporting-engine`_.

But this module does nothing for the end user by itself, so if you have it
installed it's probably because there is another module that depends on it.

Usage
=====

If you are a user
-----------------

You will be able to download XML reports from the *Print* menu found on form
and list views.

If you are a developer
----------------------

To learn from an example, just check the `sample module`_.

To develop with this module, you need to:

* Create a module.
* Make it depend on this one.
* Follow `instructions to create reports`_ having in mind that the
  ``report_type`` field in your ``ir.actions.report.xml`` record must be
  ``qweb-xml``.

In case you want to create a `custom report`_, the instructions remain the same
as for HTML reports, and the method that you must override is also called
``render_html``, even when this time you are creating a XML report.

You can make your custom report inherit ``report_xml.xsd_checked_report``, name
it like your XML ``<template>`` id prepended by ``report.``, add a ``xsd()``
method that returns a XSD in a string, and have XSD automatic checking for
free.

You can visit ``http://<server-address>/report/xml/<module.report_name>/<ids>``
to see your XML report online as a web page.

For further information, please visit:

* https://www.odoo.com/forum/help-1
* https://github.com/OCA/reporting-engine

Credits
=======

* Icon taken from http://commons.wikimedia.org/wiki/File:Text-xml.svg.

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Jairo Llopis <j.llopis@grupoesoc.es>
* Enric Tobella <etobella@creublanca.es>