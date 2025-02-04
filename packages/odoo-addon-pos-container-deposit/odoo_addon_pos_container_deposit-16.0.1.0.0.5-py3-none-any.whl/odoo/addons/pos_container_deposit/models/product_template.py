# Copyright 2024 Hunki Enterprises BV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_deposit = fields.Boolean(
        help="Check this if this product is a container for which you charge deposit",
    )
    deposit_product_id = fields.Many2one(
        "product.product",
        "Deposit product",
        domain=[("is_deposit", "!=", False)],
        help="If this product is packaged in a container for which you charge deposit, "
        "add a product here that stands for the deposit",
        compute="_compute_deposit_product_id",
        inverse="_inverse_deposit_product_id",
        search="_search_deposit_product_id",
    )

    @api.depends("product_variant_ids.deposit_product_id")
    def _compute_deposit_product_id(self):
        for this in self:
            this.deposit_product_id = (
                this.product_variant_ids.deposit_product_id
                if this.product_variant_count == 1
                else False
            )

    def _inverse_deposit_product_id(self):
        for this in self:
            if this.product_variant_count > 1:
                continue
            this.product_variant_ids.write(
                {
                    "deposit_product_id": this.deposit_product_id,
                }
            )

    def _search_deposit_product_id(self, operator, value):
        return [("product_variant_ids.deposit_product_id", operator, value)]

    def copy(self, default=None):
        """
        Take care that copies include the deposit product
        """
        if default is None:
            default = {}
        default.setdefault("deposit_product_id", self.deposit_product_id.id)
        return super().copy(default=default)

    def _get_related_fields_variant_template(self):
        result = super()._get_related_fields_variant_template()
        result.append("deposit_product_id")
        return result
