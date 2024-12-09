from odoo import models

class EntrepotReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_entrepot_details'
    _description = 'Entrepot Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['entrepot'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'entrepot',
            'docs': docs,
        }