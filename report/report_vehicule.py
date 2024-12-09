from odoo import models

class VehiculeReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_vehicule_details'
    _description = 'Vehicule Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['vehicule'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'vehicule',
            'docs': docs,
        }