# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    secondary_partner = fields.Char(tracking=True)
    contact_person = fields.Char(tracking=True)
    site_name = fields.Char(tracking=True)
