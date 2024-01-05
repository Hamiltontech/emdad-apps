# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models


class ResumeLineType(models.Model):
    _name = 'hr.resume.line.type'
    _description = "Type of a resume line"
    _order = "sequence"

    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence', default=10)
