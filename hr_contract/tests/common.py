# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad.tests.common import TransactionCase


class TestContractCommon(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(TestContractCommon, cls).setUpClass()

        cls.employee = cls.env['hr.employee'].create({
            'name': 'Richard',
            'gender': 'male',
            'country_id': cls.env.ref('base.be').id,
        })
