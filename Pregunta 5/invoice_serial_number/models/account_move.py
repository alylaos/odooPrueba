from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_serial_number = fields.Char("Número de Serie", compute="_compute_serial_and_correlative", store=True)
    x_correlative_number = fields.Char("Número Correlativo", compute="_compute_serial_and_correlative", store=True)

    @api.depends('name')
    def _compute_serial_and_correlative(self):
        for record in self:
            if record.name:
                # Parsear el número de factura
                parts = record.name.split('/')
                if len(parts) >= 3:
                    # Número de serie: Primeras dos partes concatenadas 
                    record.x_serial_number = f"{parts[0]}{parts[1]}"
                    # Número correlativo: Tercera parte rellenada a 8 dígitos
                    record.x_correlative_number = parts[2].zfill(8)
                else:
                    record.x_serial_number = ''
                    record.x_correlative_number = ''
            else:
                record.x_serial_number = ''
                record.x_correlative_number = ''
