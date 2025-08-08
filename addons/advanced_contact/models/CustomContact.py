from odoo import models, fields

class CustomContact(models.Model):
    _inherit = 'res.partner'

    #nouveau champ
    birthdate = fields.Date(string="Date de naissance")
    profession = fields.Char(string="Profession")
    importance_level = fields.Selection(
        [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string="Niveau d'importance",
        default='medium',
    )
    profile_image = fields.Binary(string="Photo de contact")
    twitter_link = fields.Char(string="Twitter")
    linkedin_link = fields.Char(string="LinkedIn")
