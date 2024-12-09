from odoo import api,fields,models

class Remplacement(models.Model):
    _name = "remplacement"
    _description = "remplacement en projet perssonalisé"
    #main fields static
    reference=fields.Char(string="Reference", required=True) 
    sinistre=fields.Boolean(string="Cas de sinistre", default=True)
    description=fields.Char(string="Description", required=False) 
    dateDemande=fields.Date(string="Date de la demande")
    dateLivraison=fields.Date(string="Date de livraison vehicule")
    
    ##duree= a faire apres avec computed fields
    
    vehiculePanne= fields.Many2one('vehicule', string='Vehicule à remplacer :')
    vehiculeNew= fields.Many2one('vehicule', string='Nouvelle Vehicule :')

    # Related fields pour Vehicule A remplacer infos
    immatricule = fields.Char(related='vehiculePanne.immatricule', string="Immatricule")
    photo = fields.Binary(related='vehiculePanne.photo', string="Photo")

    
    # Related fields pour Vehicule A remplacer infos
    immatriculeNew = fields.Char(related='vehiculeNew.immatricule', string="Immatricule")
    photoNew = fields.Binary(related='vehiculeNew.photo', string="Photo")
    # Related fields pour Prestataire infos

   
