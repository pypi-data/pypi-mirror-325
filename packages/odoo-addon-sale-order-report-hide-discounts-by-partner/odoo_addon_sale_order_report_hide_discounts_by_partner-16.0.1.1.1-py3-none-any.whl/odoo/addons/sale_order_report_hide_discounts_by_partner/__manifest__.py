# Copyright 2025 Ángel García de la Chica <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Sale Order Report Hide Discounts by Partner",
    "summary": "Sale Order Report Hide Discounts by Partner",
    "version": "16.0.1.1.1",
    "category": "Sale",
    "website": "https://github.com/sygel-technology/sy-sale-reporting",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "sale",
    ],
    "data": [
        "data/data.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "reports/sale_report_templates.xml",
    ],
}
