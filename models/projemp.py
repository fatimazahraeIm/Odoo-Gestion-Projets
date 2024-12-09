from odoo import api,models, fields

class ProjEmp(models.Model):
    _description = "employees du projet"
    _name = "projemp"
    proj_id = fields.Many2one('project.project', string='Project', required=True)
    emp_id = fields.Many2one( 'hr.employee', string='Employé', required=True)
    
    #nos fields perssonalisés
    date= fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin", required=True)
    cout_total = fields.Float(string="Coût total", compute='_compute_cout_total', store=True)

    @api.depends('date', 'date_fin', 'emp_id.total_cost')
    def _compute_cout_total(self):
        for record in self:
            if record.date and record.date_fin:
                delta = record.date_fin - record.date
                jours_travailles = delta.days + 1  # Inclure le jour de début et de fin
                record.cout_total = jours_travailles * record.emp_id.total_cost
            else:
                record.cout_total = 0

    