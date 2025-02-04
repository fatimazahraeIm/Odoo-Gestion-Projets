from odoo import api, models, fields

class Employee(models.Model):
    _description = "employée de l'entreprise"
    _inherit = ['hr.employee']
    
    # nos fields perssonalisés
    cin = fields.Char(string="CIN", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    age = fields.Integer(string="Âge", compute='_compute_age', store=True)
    photo = fields.Binary(string="Photo", attachment=True)
    etat = fields.Selection([('Disponible', 'Disponible'), ('En mission', 'En mission'), ('En congé', 'En congé')])
    typePermis = fields.Selection([('A', 'A'), ('A1', 'A1'), ('B', 'B'), ('C', 'C'), ('C1', 'C1')],
                                  string="Type de Permis")
    dateEmbauche = fields.Date(string="date d embauche", required=False)
    anciennete = fields.Integer(string="Ancienneté", compute='_compute_anciennete', store=True)

    # Champs pour le coût
    cost_type = fields.Selection([('heure', 'Heure'), ('jour', 'Jour')], string="Type de coût", required=True)
    cost = fields.Float(string="Coût", required=True)
    heures_travail = fields.Float(string="Nombre d'heures de travail par jour", default=0)
    total_cost = fields.Float(string="Coût total par jour", compute='_compute_total_cost', store=True)   

    # calculated fields automatiqumenet calculé younes_noura
    @api.depends('dateEmbauche')
    def _compute_anciennete(self):
        for record in self:
            if record.dateEmbauche:
                today = fields.Date.today()
                delta = today - record.dateEmbauche
                record.anciennete = delta.days // 365
            else:
                record.anciennete = 0

    # Calcul de l'âge via un computed field 
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                today = fields.Date.today()
                delta = today - record.birthday
                record.age = delta.days // 365
            else:
                record.age = 0

    @api.depends('cost', 'cost_type', 'heures_travail')
    def _compute_total_cost(self):
        for record in self:
            if record.cost_type == 'jour':
                record.total_cost = record.cost
            elif record.cost_type == 'heure':
                record.total_cost = record.cost * record.heures_travail

