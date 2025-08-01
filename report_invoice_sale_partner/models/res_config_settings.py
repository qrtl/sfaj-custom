# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    partner_field_for_report_invoice = fields.Many2one(
        related="company_id.partner_field_for_report_invoice",
        readonly=False,
    )
