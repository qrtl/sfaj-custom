# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def get_original_partner(self):
        if not self.company_id.partner_field_for_report_invoice:
            return False
        partner_field = self.company_id.partner_field_for_report_invoice
        sale_orders = self.invoice_line_ids.mapped("sale_line_ids.order_id")
        partners = sale_orders.mapped(partner_field.name)
        return partners[0] if partners else False
