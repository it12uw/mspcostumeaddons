
{
    "name": "Pengecekan Sample",
    "version": "1.0.1.1.0",
    "category": "Pengecekan Sample",
    "license": "AGPL-3",
    "summary": "Modul For Sample Check",
    "author": "Steven Morison, "
              "stevenmorizon123@gmail.com",
    "website": "",
    "description": """\

Pengecekan Sample Module
======================================================================

This is Sample Check module use for create new sample check based on existing sample development in 'done' state.
if the existing sample development is not in 'done' state the module system automatically show message that the choosen sample is not in 'done' state
and can't be used for.
    """,
    "depends": [
        "product",
        "marel_in_samlpe_dev_2",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/view_pengecekan_sample.xml",
    ],
    
    "installable": True,
    "auto_install": False,
    "application": True,
}
