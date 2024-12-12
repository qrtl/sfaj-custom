# # Copyright 2022 Quartile Limited
# # License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

# # from odoo.tools import float_utils

#     # def round(self, amount):
#     #     self.ensure_one()
#     #     if "rounding_method" in self._context:
#     #         return tools.float_round(
#     #             amount,
#     #             precision_rounding=self.rounding,
#     #             rounding_method=self._context.get("rounding_method"),
#     #         )
#     #     return super().round(amount)

#     # def float_round(value, precision_digits=None, precision_rounding=None, rounding_method='HALF-UP'):
#     #     if "rounding_method" in self._context:
#     #         return float_utils.float_round(
#     #             amount,
#     #             precision_rounding=self.rounding,
#     #             rounding_method=self._context.get("rounding_method"),
#     #         )
#     #     return super().float_lound(amount)


import math
from odoo.tools.float_utils import float_round as original_float_round

# Define your custom version of the function
def float_round(value, precision_digits=None, precision_rounding=None, rounding_method='HALF-UP'):
    if "rounding_method" in self._context:
        result = original_float_round(value, precision_digits, precision_rounding, rounding_method)
        return result
# Monkey patch the original function
import odoo.tools.float_utils
odoo.tools.float_utils.float_round = float_round
