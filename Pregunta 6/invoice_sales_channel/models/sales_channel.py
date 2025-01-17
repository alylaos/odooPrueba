from odoo import models, fields

class SalesChannel(models.Model):
    _name = 'sales.channel'
    _description = 'Canal de Ventas'

    name = fields.Char("Nombre", required=True)
    description = fields.Text("Descripción")
