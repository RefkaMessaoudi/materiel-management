from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('country_id')
    def _onchange_country_id(self):
        if self.country_id:
            print("self.country_id.team_id", self.country_id.team_id)
            self.team_id = self.country_id.team_id.id


