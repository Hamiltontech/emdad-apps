# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models


class MailingContact(models.Model):
    _name = 'mailing.contact'
    _inherit = ['mailing.contact', 'mail.thread.phone']

    mobile = fields.Char(string='Mobile')
