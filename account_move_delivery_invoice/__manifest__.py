# Copyright 2025 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Move Delivery Invoice",
    "category": "Invoice",
    "version": "16.0.1.0.0",
    "author": "Quartile",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_move_contact_attribute",  # contact_person, site_name, secondary_partner
    ],
    "data": [
        "reports/account_report.xml",
        "reports/delivery_invoice_templates.xml",
    ],
    "installable": True,
}
