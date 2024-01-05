# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_fr_reference_leave_type = fields.Many2one(
        'hr.leave.type',
        related='company_id.l10n_fr_reference_leave_type',
        readonly=False)
