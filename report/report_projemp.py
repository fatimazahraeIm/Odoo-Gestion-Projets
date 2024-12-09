from odoo import models

class ProjEmpReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_projemp_details'
    _description = 'ProjEmp Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['projemp'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'projemp',
            'docs': docs,
        }