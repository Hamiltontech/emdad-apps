# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.
from emdad import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_product_for_ui(self, pos_config):
        self.ensure_one()
        product = super()._get_product_for_ui(pos_config)
        product["optional_product_ids"] = self.optional_product_ids.product_variant_ids.ids
        return product
