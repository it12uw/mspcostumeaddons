{
    "name": "Snap Qc",
    "version": "1.0.1.1.0",
    "category": "Snap QC",
    "license": "AGPL-3",
    "summary": "Module For Snap QC",
    "author": "Steven Morison, "
              "stevenmorizon123@gmail.com",
    "website": "",
    "description": """\

Snap Qc Module
======================================================================

This is Snap Qc module use for create new sample check based on existing sample development in 'done' state.
if the existing sample development is not in 'done' state the module system automatically show message that the choosen sample is not in 'done' state
and can't be used for.
    """,
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/views_snap_qc.xml",
    ],
    
    "installable": True,
    "auto_install": False,
    "application": True,
}