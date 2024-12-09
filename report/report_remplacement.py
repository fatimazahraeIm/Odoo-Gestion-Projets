from odoo import models

class RemplacementReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_remplacement_details'
    _description = 'Remplacement Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['remplacement'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'remplacement',
            'docs': docs,
        }