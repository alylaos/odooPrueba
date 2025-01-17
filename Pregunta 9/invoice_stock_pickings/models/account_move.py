from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    related_pickings = fields.Many2many(
        'stock.picking',
        string='Related Transfers',
        compute='_compute_related_pickings',
        store=False
    )

    @api.depends('invoice_line_ids.sale_line_ids.order_id.picking_ids')
    def _compute_related_pickings(self):
        for record in self:
            pickings = self.env['stock.picking']
            for line in record.invoice_line_ids:
                if line.sale_line_ids:
                    for sale_line in line.sale_line_ids:
                        pickings |= sale_line.order_id.picking_ids
            record.related_pickings = pickings
