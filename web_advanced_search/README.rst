*This module was migrated automatically from OCA repository* 
*to flectra community repository. We do not guarantee the correctness of all information.*
*Please check https://gitlab.com/flectra-community/oca2fc/blob/master/README.md*
*fur further informations about automatic migration.*

===============
Advanced search
===============

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

 

More powerful and easy to use search, especially for related fields.

**Table of contents**

.. contents::
   :local:

Usage
=====

To use this module, you need to:

* Open *Filters* in a search view
* Select any relational field
* Select operator `is equal to` or `is not equal to`
* The text field changes to a relational selection field where you
  can search for the record in question
* Click *Apply*

To search for properties of linked records (ie invoices for customers
with a credit limit higher than X):

* Open *Filters* in a search view
* Select *Add Advanced Filter*
* Edit the advanced filter
* Click *Save*

Note that you can stack searching for properties: Simply add another
advanced search in the selection search window. You can do
this indefinetely, so it is possible to search for moves belonging
to a journal which has a user who is member of a certain group etc.

Known issues / Roadmap
======================

Improvements to the ``domain`` widget, not exclusively related to this addon:

* Use relational widgets when filtering a relational field
* Allow to filter field names

Improvements to the search view in this addon:

* Use widgets ``one2many_tags`` when searching ``one2many`` fields
* Use widgets ``many2many_tags`` when searching ``many2many`` fields
* Allow to edit current full search using the advanced domain editor
* Allow to edit individually any facet from current search using the
  advanced domain editor
* Beautiful, human-readable, domain representation when adding an
  advanced filter

Changelog
=========

11.0.1.0.2 (2018-10-31)
~~~~~~~~~~~~~~~~~~~~~~~

* Fix initialization of 1st domain node

  Sometime the dialog is not ready yet, like on EE version.
  Hence when you inject the 1st domain node
  the dialog must be already opened.

  [simahawk]


11.0.1.0.1 (2018-09-18)
~~~~~~~~~~~~~~~~~~~~~~~

* Fix `undefined` in x2m fields

  Before this patch, when searching with the "equals to" operator in any
  x2many field, the searched parameter was always `undefined`.

  The problem was that the underlying field manager implementation was
  treating those fields as x2many, while the widget used was the `one2many`
  one.

  This patch simply mocks the underlying fake record to make think that
  any relational field is always a `one2many`. This sets all pieces in
  place and makes the field manager work as expected, and thus you can
  search as expected too.

* Make linter happy

  [Yajo]


11.0.1.0.0 (2018-07-20)
~~~~~~~~~~~~~~~~~~~~~~~

* Rename, refactor, migrate to v11

  [Yajo]

Credits
=======

Authors
~~~~~~~

* Therp BV
* Tecnativa

Contributors
------------

* Flectra Community <info@flectra-community.org>
* Holger Brunn <hbrunn@therp.nl>
* Vicent Cubells <vicent.cubells@tecnativa.com>
* Jairo Llopis <jairo.llopis@tecnativa.com>
* Rami Alwafaie <rami.alwafaie@initos.com>
* Jose Mª Bernet <josemaria.bernet@guadaltech.es>
* Simone Orsi <simone.orsi@camptocamp.com>