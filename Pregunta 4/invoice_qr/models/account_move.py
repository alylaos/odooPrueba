import base64
import io
import qrcode
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_qr_invoice = fields.Binary("Código QR", compute="_compute_qr_invoice", store=True)
    x_total_quantities = fields.Float("Total Cantidades", compute="_compute_total_quantities", store=True)

    @api.depends('invoice_line_ids.quantity')
    def _compute_total_quantities(self):
        for record in self:
            record.x_total_quantities = sum(record.invoice_line_ids.mapped('quantity'))

    @api.depends('name', 'partner_id', 'invoice_date', 'x_total_quantities', 'amount_total')
    def _compute_qr_invoice(self):
        for record in self:
            qr_string = f"{record.name or ''}|{record.partner_id.name or ''}|{record.invoice_date or ''}|{record.x_total_quantities:.2f}|{record.amount_total:.2f}"
            record.x_qr_invoice = self.generate_qr_code(qr_string)

    @staticmethod
    def generate_qr_code(qr_string):
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(qr_string)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return img_str
