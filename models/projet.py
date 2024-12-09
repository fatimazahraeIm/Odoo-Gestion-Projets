from odoo import api, fields, models

class Projet(models.Model):
    _description = "Projet de l'entreprise"
    _inherit = 'project.project'

    # Champs personnalisés pour le projet
    date_debut_projet = fields.Date(string="Date de début du projet")
    date_fin_projet = fields.Date(string="Date de fin du projet")
    budget_projet = fields.Float(string="Budget du projet")

    
