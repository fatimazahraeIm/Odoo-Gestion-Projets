from odoo import api, fields, models

class Produit(models.Model):
    _inherit = 'product.product'

    # Custom fields for produit
    product_code = fields.Char(string="Product Code", required=True)
    product_name = fields.Char(string="Product Name", required=True)
    product_description = fields.Text(string="Product Description")
    product_price = fields.Float(string="Product Price", required=True)
    

    # Ensure unique table names and columns for Many2many fields
    transaction_ids = fields.Many2many(
        'payment.transaction',
        'produit_payment_transaction_rel',
        'produit_id',
        'transaction_id',
        string='Transactions'
    )

    tag_ids = fields.Many2many(
        'product.tag',
        'produit_product_tag_rel',
        'produit_id',
        'tag_id',
        string='Tags'
    )
