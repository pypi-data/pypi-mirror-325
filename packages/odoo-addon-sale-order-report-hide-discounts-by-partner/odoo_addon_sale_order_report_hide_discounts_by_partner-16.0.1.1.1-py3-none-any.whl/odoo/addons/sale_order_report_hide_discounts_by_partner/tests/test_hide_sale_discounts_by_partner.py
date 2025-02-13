# Copyright 2025 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.fields import Command
from odoo.tests import common, tagged
from odoo.tools.float_utils import float_is_zero


@tagged("post_install", "-at_install")
class TestHideSaleDiscountsByPartner(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestHideSaleDiscountsByPartner, cls).setUpClass()
        cls.partner1 = cls.env["res.partner"].create(
            {
                "name": "Test partner 1",
                "show_sale_discounts": False,
            }
        )
        cls.partner2 = cls.env["res.partner"].create(
            {
                "name": "Test partner 2",
                "show_sale_discounts": True,
            }
        )
        cls.product = cls.env["product.product"].create(
            {
                "name": "Product Product 4",
                "standard_price": 500.0,
            }
        )
        cls.tax = cls.env["account.tax"].create(
            {
                "name": "tax_1",
                "amount": 21.00,
            }
        )

        cls.so = cls.env["sale.order"].create(
            {
                "partner_id": cls.partner1.id,
                "order_line": [
                    Command.create(
                        {
                            "product_id": cls.product.id,
                            "product_uom_qty": 5.0,
                            "discount": 10.0,
                            "tax_id": [(6, 0, [cls.tax.id])],
                        }
                    ),
                ],
            }
        )

    def test_child_partner_show_discounts(self):
        child = self.env["res.partner"].create(
            {"name": "Test partner", "parent_id": self.partner1.id}
        )
        self.assertEqual(
            child.show_sale_discounts,
            self.partner1.show_sale_discounts,
        )

    def test_so_creation(self):
        sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner2.id,
                "order_line": [
                    Command.create(
                        {
                            "product_id": self.product.id,
                            "product_uom_qty": 5.0,
                        }
                    ),
                ],
            }
        )
        self.assertEqual(sale_order.show_discounts, self.partner2.show_sale_discounts)

    def test_so_change_partner(self):
        self.assertEqual(self.so.show_discounts, self.partner1.show_sale_discounts)
        self.so.partner_id = self.partner2
        self.assertEqual(self.so.show_discounts, self.partner2.show_sale_discounts)

    def test_user_group_show_line_subtotals_tax_excluded(self):
        """Before checks, we make sure that user belongs to the
        tax group account.group_show_line_subtotals_tax_excluded
        """
        if (
            self.env.user
            not in self.env.ref("account.group_show_line_subtotals_tax_excluded").users
        ):
            self.env.ref("account.group_show_line_subtotals_tax_included").write(
                {"users": [(3, self.env.user.id)]}
            )
            self.env.ref("account.group_show_line_subtotals_tax_excluded").write(
                {"users": [(4, self.env.user.id)]}
            )
        self.assertEqual(
            self.so.order_line[0].sale_price_unit_with_discount,
            self.so.order_line[0].price_subtotal
            / self.so.order_line[0].product_uom_qty,
        )

    def test_user_group_show_line_subtotals_tax_included(self):
        """Before checks, we make sure that user belongs to the
        tax group account.group_show_line_subtotals_tax_included
        """
        if (
            self.env.user
            not in self.env.ref("account.group_show_line_subtotals_tax_included").users
        ):
            self.env.ref("account.group_show_line_subtotals_tax_excluded").write(
                {"users": [(3, self.env.user.id)]}
            )
            self.env.ref("account.group_show_line_subtotals_tax_included").write(
                {"users": [(4, self.env.user.id)]}
            )
        self.assertEqual(
            self.so.order_line[0].sale_price_unit_with_discount,
            self.so.order_line[0].price_total / self.so.order_line[0].product_uom_qty,
        )

    def test_product_uom_qty_is_zero(self):
        self.so.order_line[0].product_uom_qty = 0.00
        self.assertTrue(
            float_is_zero(
                self.so.order_line[0].sale_price_unit_with_discount,
                precision_digits=self.env["decimal.precision"].precision_get(
                    "Product Unit of Measure"
                ),
            )
        )
