from odoo import models

class EmployeeReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_employee_details'
    _description = 'Employee Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['hr.employee'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.employee',
            'docs': docs,
        }