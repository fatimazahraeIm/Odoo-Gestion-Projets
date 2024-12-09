from odoo import models

class MaintenanceReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_maintenance_details'
    _description = 'Maintenance Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['maintenance'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'maintenance',
            'docs': docs,
        }