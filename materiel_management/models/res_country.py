from odoo import models, fields, api


class ResCountry(models.Model):
    _inherit = 'res.country'

    team_id = fields.Many2one('crm.team', string='Team')

