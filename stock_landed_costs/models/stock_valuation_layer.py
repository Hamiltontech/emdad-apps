# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    stock_landed_cost_id = fields.Many2one('stock.landed.cost', 'Landed Cost')
