# coding: utf-8
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models


class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    def _get_payment_terminal_selection(self):
        return super(PosPaymentMethod, self)._get_payment_terminal_selection() + [('six', 'SIX')]

    six_terminal_ip = fields.Char('Six Terminal IP')
