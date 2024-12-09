from odoo import api,models, fields

class Projveh(models.Model):
    _description = "vehicules du projet"
    _name = "projveh"
    veh_id = fields.Many2one('vehicule', string='Véhicule', required=True)
    proj_id = fields.Many2one( 'project.project', string='Projet', required=True)
    
    #nos fields perssonalisés
    date= fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin", required=True)
    cout= fields.Float(string="coût", required=True)

