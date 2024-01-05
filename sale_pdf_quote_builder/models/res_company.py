# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    sale_header = fields.Binary(string="Header pages")
    sale_header_name = fields.Char()
    sale_footer = fields.Binary(string="Footer pages")
    sale_footer_name = fields.Char()
