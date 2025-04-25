This module adjusts security settings of stock functionality in Odoo.

* Add an ACL record for internal users to be able to read/write/create
  stock.quantity.history records, which is necessary for certain users with no stock user
  group (e.g., read-only accountants) to be able to run the inventory valuation report
  for a specific date.
