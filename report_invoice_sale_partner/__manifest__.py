# Copyright 2025 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Report Invoice Sale Partner",
    "category": "Invoice",
    "version": "16.0.1.0.0",
    "author": "Quartile",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": ["sale"],
    "data": [
        "reports/report_invoice_document.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
}
