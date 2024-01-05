# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import models


class Website(models.Model):
    _inherit = 'website'

    def sale_product_domain(self):
        return ['&'] + super(Website, self).sale_product_domain() + [('detailed_type', '!=', 'event_booth')]
