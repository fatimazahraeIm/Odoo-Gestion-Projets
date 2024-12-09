from odoo import models, fields

class Maintenance(models.Model):
    _name = "maintenance"
    _inherit = "maintenance.request"

    vehicule= fields.Many2one('vehicule', string='Vehicule')
  
    # Related fields pour Vehicule infos
    immatricule = fields.Char(related='vehicule.immatricule', string="Immatricule")
    photo = fields.Binary(related='vehicule.photo', string="Photo")
