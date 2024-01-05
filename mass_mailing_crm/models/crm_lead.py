# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _mailing_enabled = True
