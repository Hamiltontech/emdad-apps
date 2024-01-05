# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models


class Company(models.Model):
    _inherit = "res.company"

    check_account_audit_trail = fields.Boolean(string='Audit Trail')
