# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    contact_person = fields.Char(tracking=True)
    site_name = fields.Char(tracking=True)

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals["contact_person"] = self.contact_person
        invoice_vals["site_name"] = self.site_name
        return invoice_vals
