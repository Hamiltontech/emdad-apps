# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import models, fields


class Users(models.Model):
    _inherit = 'res.users'

    emdadbot_state = fields.Selection(selection_add=[
        ('onboarding_canned', 'Onboarding canned'),
    ], ondelete={'onboarding_canned': lambda users: users.write({'emdadbot_state': 'disabled'})})
