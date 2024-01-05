# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import models
from emdad.osv import expression


class Website(models.Model):
    _inherit = 'website'

    def sale_product_domain(self):
        return expression.AND([
            super(Website, self).sale_product_domain(),
            [('detailed_type', '!=', 'course')],
        ])
