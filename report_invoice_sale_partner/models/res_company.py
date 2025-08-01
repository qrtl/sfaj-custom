# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    partner_field_for_report_invoice = fields.Many2one(
        "ir.model.fields",
        domain=[
            ("model", "=", "sale.order"),
            ("ttype", "=", "many2one"),
            ("relation", "=", "res.partner"),
        ],
    )
