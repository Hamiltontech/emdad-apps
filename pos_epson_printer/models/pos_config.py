# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    epson_printer_ip = fields.Char(string='Epson Printer IP', help="Local IP address of an Epson receipt printer.")
