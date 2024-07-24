# Copyright 2019 Marcelo Frare (Ass. PNLUG - Gruppo Flectra <http://flectra.pnlug.it>)
# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Flectra <http://flectra.pnlug.it>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from flectra import fields, models


class MgmtsystemMgmHR(models.Model):
    """
    Extend nonconformity adding fields for department
    """

    _inherit = ['mgmtsystem.nonconformity']

    # new fields
    # department reference
    department_id = fields.Many2one('hr.department', 'Department')
