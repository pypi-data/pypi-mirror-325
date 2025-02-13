# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.float_utils import float_is_zero


class SaleOrder(models.Model):
    _inherit = "sale.order"

    show_discounts = fields.Boolean(
        compute="_compute_show_discounts",
        store=True,
        readonly=False,
        string="Show Discounts in Sale",
    )

    @api.depends("partner_id")
    def _compute_show_discounts(self):
        for sel in self:
            res = False
            if sel.partner_id:
                res = sel.partner_id.show_sale_discounts
            sel.show_discounts = res


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sale_price_unit_with_discount = fields.Float(
        compute="_compute_unit_price_with_discounts",
        digits="Sale Price Unit With Discount",
        string="Price Unit With Discount",
    )

    def _compute_unit_price_with_discounts(self):
        for sel in self:
            res = 0.0
            if not float_is_zero(
                sel.product_uom_qty,
                precision_digits=self.env["decimal.precision"].precision_get(
                    "Product Unit of Measure"
                ),
            ):
                if sel.env.user.has_group(
                    "account.group_show_line_subtotals_tax_included"
                ):
                    res = sel.price_total / sel.product_uom_qty
                elif sel.env.user.has_group(
                    "account.group_show_line_subtotals_tax_excluded"
                ):
                    res = sel.price_subtotal / sel.product_uom_qty
            sel.sale_price_unit_with_discount = res
