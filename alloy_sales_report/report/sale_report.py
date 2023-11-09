# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def invoice_name(self):
        invoice = self.env['account.invoice'].search([('origin', '=', self.name)])
        if invoice:
            return invoice.number
        else:
            return