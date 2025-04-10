from odoo import api, models, tools
from odoo.osv import expression
from odoo.tools import config


class IrRule(models.Model):
    _inherit = "ir.rule"

    # Members of the group 'group_sale_team_manager' should be able to read all partner records,
    # but must not be allowed to update records belonging to other teams.
    # The original sales_team_security module restricted access to partner records
    # to only those within the user's own team. This logic adjusts that behavior
    # to allow broader read access for team managers while maintaining write restrictions.
    @api.model
    @tools.conditional(
        "xml" not in config["dev_mode"],
        tools.ormcache(
            "self.env.uid",
            "self.env.su",
            "model_name",
            "mode",
            "tuple(self._compute_domain_context_values())",
        ),
    )
    def _compute_domain(self, model_name, mode="read"):
        user = self.env.user
        group2 = "sales_team_security.group_sale_team_manager"
        if model_name == "res.partner" and not self.env.su and user.has_group(group2):
            if mode == "read":
                return expression.normalize_domain([(1, "=", 1)])
            else:
                domain = [
                    "|",
                    ("team_id", "=", user.sale_team_id.id),
                    ("team_id", "=", False),
                ]
                return expression.normalize_domain(domain)
        return super()._compute_domain(model_name, mode=mode)
