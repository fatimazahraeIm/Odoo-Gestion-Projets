from odoo import models

class ProjVehReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_projveh_details'
    _description = 'ProjVeh Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['projveh'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'projveh',
            'docs': docs,
        }