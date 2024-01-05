# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import api, models


class AccountPaymentMethod(models.Model):
    _inherit = 'account.payment.method'

    @api.model
    def _get_payment_method_information(self):
        res = super()._get_payment_method_information()
        for code, _desc in self.env['payment.provider']._fields['code'].selection:
            if code in ('none', 'custom'):
                continue
            res[code] = {
                'mode': 'unique',
                'domain': [('type', '=', 'bank')],
            }
        return res
