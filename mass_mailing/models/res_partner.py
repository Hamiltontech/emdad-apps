# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import models


class Partner(models.Model):
    _inherit = 'res.partner'
    _mailing_enabled = True
