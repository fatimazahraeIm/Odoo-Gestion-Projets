from odoo import api, fields, models


class vehicule(models.Model):
    _name = "vehicule"
    _inherit = ['fleet.vehicle']
    tag_ids = fields.Many2many('fleet.vehicle.tag', 'vehicule_vehicle_tag_rel', 'vehicle_tag_id', 'tag_id','Tags', copy=False)
    
    # nos fields perssonalisé
    immatricule = fields.Char('Immatricule ')
    type= fields.Selection([('Voiture','Voiture'),('Moto','Moto'),('Camion','Camion'),('Tracteur','Tracteur'),('Velo','Velo')])
    etat= fields.Selection([('Disponible','Disponible'),('En mission','En mission'),('En reparation','En reparation'),('En panne','En panne')])
    photo = fields.Binary(string="Photo", attachment=True)

    