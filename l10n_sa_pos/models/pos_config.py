# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.
from emdad import models
from emdad.exceptions import UserError
from emdad.tools.translate import _


class pos_config(models.Model):
    _inherit = 'pos.config'

    def open_ui(self):
        for config in self:
            if not config.company_id.country_id:
                raise UserError(_("You have to set a country in your company setting."))
        return super(pos_config, self).open_ui()
