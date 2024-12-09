from odoo import models

class ProjProdReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_projprod_details'
    _description = 'ProjProd Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['projprod'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'projprod',
            'docs': docs,
        }