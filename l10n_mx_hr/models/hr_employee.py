# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models


class Employee(models.Model):
    _inherit = 'hr.employee'

    l10n_mx_nss = fields.Char('NSS', groups="hr.group_hr_user", tracking=True)
    l10n_mx_curp = fields.Char('CURP', groups="hr.group_hr_user", tracking=True)
    l10n_mx_rfc = fields.Char('RFC', groups="hr.group_hr_user", tracking=True)
