# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad import fields, models

class FleetVehicleLogContract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'

    purchaser_employee_id = fields.Many2one(
        related='vehicle_id.driver_employee_id',
        string='Driver (Employee)',
    )
