from odoo import models

class ProjetReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_projet_details'
    _description = 'Projet Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['project.project'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'project.project',
            'docs': docs,
        }