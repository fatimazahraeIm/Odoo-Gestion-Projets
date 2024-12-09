from odoo import models

class ProduitReport(models.AbstractModel):
    _name = 'report.gestionProjets.report_produit_details'
    _description = 'Produit Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['product.product'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'product.product',
            'docs': docs,
        }