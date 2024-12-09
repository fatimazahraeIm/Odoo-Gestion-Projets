from odoo import models

class VilleReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_ville_details'
    _description = 'Ville Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['ville'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'ville',
            'docs': docs,
        }