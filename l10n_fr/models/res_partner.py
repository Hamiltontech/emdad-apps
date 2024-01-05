# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.
from emdad import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    siret = fields.Char(string='SIRET', size=14)
