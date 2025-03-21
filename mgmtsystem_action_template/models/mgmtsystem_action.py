# Copyright 2019 Marcelo Frare (Ass. PNLUG - Gruppo Flectra <http://flectra.pnlug.it>)
# Copyright 2019 Stefano Consolaro (Ass. PNLUG - Gruppo Flectra <http://flectra.pnlug.it>)
# Copyright 2020 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from flectra import api, fields, models, _


class MgmtsystemAction(models.Model):
    """
    Extend actions adding template reference
    """

    _inherit = 'mgmtsystem.action'

    # template reference
    template_id = fields.Many2one(
        'mgmtsystem.action.template',
        'Reference Template',
        help='Fill Action\'s fields with Template\'s values'
    )

    @api.onchange('template_id')
    def _onchange_template_id(self):
        """
        Fill some fields with template ones
        """

        if self.template_id:
            self.name = _('NEW') + ' ' + self.template_id.name
            self.type_action = self.template_id.type_action
            self.description = self.template_id.description
            self.user_id = self.template_id.user_id
            self.tag_ids = self.template_id.tag_ids
