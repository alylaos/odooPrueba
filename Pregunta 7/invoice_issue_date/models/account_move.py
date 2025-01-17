from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    issue_date = fields.Datetime(
        string="Fecha de Emisión", 
        default=fields.Datetime.now, 
        help="Fecha y hora en que se emite la factura."
    )
