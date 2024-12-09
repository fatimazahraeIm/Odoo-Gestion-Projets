from odoo import api,models, fields

class ProjProd(models.Model):
    _description = "produits du projet"
    _name = "projprod"
    prod_id = fields.Many2one('product.product', string='Produit', required=True)
    proj_id = fields.Many2one( 'project.project', string='Projet', required=True)
    
    #nos fields perssonalisés
    date_achat= fields.Date(string="Date d achat", required=True)
    quantite= fields.Float(string="Quantité", required=True)
    prix_unit = fields.Float(string="Prix unitaire", store=True)
    total = fields.Float(string="Total", compute='_compute_total', store=True)

    @api.depends('quantite', 'prix_unit')
    def _compute_total(self):
        for record in self:
            record.total = record.quantite * record.prix_unit





