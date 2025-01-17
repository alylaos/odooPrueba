from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    sales_channel_id = fields.Many2one(
        'sales.channel', 
        string='Canal de Ventas',
        help='Selecciona el canal de ventas para esta factura.'
    )
