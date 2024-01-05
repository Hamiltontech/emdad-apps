# Part of emdad. See LICENSE file for full copyright and licensing details.
from emdad import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    taxable_supply_date = fields.Date()
